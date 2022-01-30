from game.client.user_client import UserClient
from game.common.enums import *

######################################################
# imports for type hints
from game.common.action import Action
from game.common.moving.shooter import Shooter
from game.utils.partition_grid import PartitionGrid
######################################################

from game.utils.player_utils import *


class Client(UserClient):
    def __init__(self):
        super().__init__()
        self.prev_location = (0, 0)

    def team_name(self):
        return 'Java'


    # def movement(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
    #     # This is the list that contains all the objects on the map your player can see
    #     map_objects = partition_grid.get_all_objects()
    #     # This is a tuple that represents the position 1 unit in front of where the player
    #     forward_position = (shooter.hitbox.middle[0] + shooter.hitbox.width + math.cos(math.radians(shooter.heading)),
    #                         shooter.hitbox.middle[1] + shooter.hitbox.height + math.sin(math.radians(shooter.heading)))
    #     object_in_front = None
    #     if forward_position[0] < game_board.width and forward_position[1] < game_board.height:
    #         object_in_front = partition_grid.find_object_coordinates(forward_position[0], forward_position[1])
    #     if self.prev_location != shooter.hitbox.middle:
    #         angle = angle_to_point(shooter, game_board.center)
    #         actions.set_move(int(angle), shooter.max_speed)
    #         self.prev_location = shooter.hitbox.middle
    #     elif object_in_front or 0 <= forward_position[0] <= 500 or 0 <= forward_position[1] <= 500 \
    #             and self.prev_location != game_board.center:
    #         #shooter.heading = 0
    #         actions.set_move((shooter.heading + 90) % 360, 10)

    def find_opponent(self, things: list, me: Shooter) -> int:
        i = 0
        for thing in things:
            if thing.object_type == ObjectType.shooter and me.hitbox.middle != thing.hitbox.middle:
                return i
            i += 1
        return -1

    def only_walls(self, things: list) -> list:
        walls = []
        for thing in things:
            if thing.object_type == ObjectType.wall:
                walls.append(thing)
        return walls

    def only_guns(self, things: list) -> list:
        guns = []
        for thing in things:
            if thing.object_type == ObjectType.gun:
                guns.append(thing)
        return guns

    def find_nearest_gun(self, guns: list, type: GunType, me: Shooter) -> int:
        nearest = -1
        i = 0
        for gun in guns:
            if gun.gun_type == type and (nearest == -1 or distance(me.hitbox.middle[0], me.hitbox.middle[1], gun.hitbox.middle[0], gun.hitbox.middle[1]) < distance(me.hitbox.middle[0], me.hitbox.middle[1], guns[i].hitbox.middle[0], guns[i].hitbox.middle[1])):
                nearest = i
            i += 1
        return nearest

    def is_in_wall(self, pos_x: int, pos_y: int, walls: list) -> bool:
        pos = (pos_x, pos_y)
        walls_corners_list = [] #array of arrays [left, right, top, bottom]
        for i in range(len(walls)):
            walls_corners_list.append([walls[i].hitbox.top_left[0], walls[i].hitbox.top_right[0], walls[i].hitbox.top_right[1], walls[i].hitbox.bottom_left[1]])
        for i in range(len(walls)):
            if((pos[0] > int(walls_corners_list[i][1]) and pos[0] < int(walls_corners_list[i][0])) or (pos[1] < int(walls_corners_list[i][2]) and pos[1] > int(walls_corners_list[i][3]))):
                return True
        return False

    def find_next_move(self, target_x: int, target_y: int, me: Shooter, walls: list):
        target = (target_x, target_y)
        current_pos = me.hitbox.middle
        next_pos = (0, 0)
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    test_pos = (int(current_pos[0] - (i * me.max_speed / 1.5)), int(current_pos[1] - (j * me.max_speed / 1.5)))
                    if (not self.is_in_wall(*test_pos, walls)) and distance(*test_pos, *target) < distance(*next_pos, *target):
                        next_pos = test_pos
        return next_pos

    def move(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter, target_x: int, target_y: int) -> None:
        target = (target_x, target_y)
        walls = self.only_walls(list(partition_grid.get_all_objects()))
        next_move = self.find_next_move(*target, shooter, walls)
        actions.set_move(int(angle_to_point(shooter, next_move)), int(shooter.max_speed))

    def shoot(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
        things = list(partition_grid.get_all_objects())
        index = self.find_opponent(things, shooter)
        if (index >= 0):
            opponent = things[index]
            if (distance(opponent.hitbox.middle[0], opponent.hitbox.middle[1], shooter.hitbox.middle[0], shooter.hitbox.middle[1]) <= shooter.primary_gun.range):
                actions.set_shoot(angle_to_point(shooter, opponent.hitbox.middle))

    def reload(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
        if shooter.primary_gun.mag_ammo == 0:
            actions.set_action(ActionType.reload)

    def take_turn(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
        self.move(turn, actions, game_board, partition_grid, shooter, *game_board.center)
        self.shoot(turn, actions, game_board, partition_grid, shooter)
        self.reload(turn, actions, game_board, partition_grid, shooter)