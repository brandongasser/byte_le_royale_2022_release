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

    # def get_pathfind_list(self, x, y, shooter: Shooter, game_board, partition_grid: PartitionGrid) -> list:
    #     #temp_point = (x, y)
    #     count = 0
    #     final_path = [] #array of the final path to travel, in order
    #     #while (not (shooter.hitbox.middle in final_path)):
    #     temp = False
    #     main = []
    #     while(not(shooter.hitbox.middle in final_path)):
    #         main = [game_board.center[0], game_board.center[1],0]
    #         adjacent_cells_list = [(x-partition_grid.partition_width, y, count), (x+partition_grid.partition_width, y, count), (x, y-partition_grid.partition_width, count), (x, y+partition_grid.partition_width, count)]
    #         walls = [[(self.only_walls(list(partition_grid.get_all_objects())))[0].hitbox.top_left, (self.only_walls(list(partition_grid.get_all_objects())))[0].hitbox.top_right, (self.only_walls(list(partition_grid.get_all_objects())))[0].hitbox.bottom_left, (self.only_walls(list(partition_grid.get_all_objects())))[0].hitbox.bottom_right]]
    #         #walls is an array of arrays of top left, top right, bottom left, and bottom right coordinates of walls
    #         for i in range(1,len(self.only_walls(list(partition_grid.get_all_objects())))):
    #             walls.append([self.only_walls(list(partition_grid.get_all_objects()))[i].hitbox.top_left, self.only_walls(list(partition_grid.get_all_objects()))[i].hitbox.top_right, self.only_walls(list(partition_grid.get_all_objects()))[i].hitbox.bottom_left, self.only_walls(list(partition_grid.get_all_objects()))[i].hitbox.bottom_right])
    #         for i in range(len(adjacent_cells_list)):
    #             for m in range(len(walls)):
    #                 if ((int(adjacent_cells_list[i][0])>int(walls[m][0][0]) and int(adjacent_cells_list[i][0])<int(walls[m][1][0])) or (int(adjacent_cells_list[i][1])>int(walls[m][2][1]) and int(adjacent_cells_list[i][1])<int(walls[m][0][1]))):
    #                     adjacent_cells_list.remove(adjacent_cells_list[i])
    #                     #remove cells that are inside of walls from available adjacent cells
    #                 if(adjacent_cells_list[i] in main):
    #                     main.remove(adjacent_cells_list[i])
    #                     #remove cells that are already in main from main
    #         adjacent_cells_list = []
    #         count += 1
    #         main.append(adjacent_cells_list)

    #     current_position = shooter.hitbox.middle
    #     #final_path = [] #array of the final path to travel, in order
    #     for i in range(len(main)):
    #         adjacent_options = []
    #         #if adjacent cell is one of the ones I can move to (if it's in main) add it to a list of options
    #         if([current_position[0]-partition_grid.partition_width, current_position[1], count] == main[i]):
    #             adjacent_options.append(main[i])
    #         if([current_position[0]+partition_grid.partition_width, current_position[1], count] == main[i]):
    #             adjacent_options.append(main[i])
    #         if([current_position[0], current_position[1]-partition_grid.partition_width, count] == main[i]):
    #             adjacent_options.append(main[i])
    #         if([current_position[0], current_position[1]+partition_grid.partition_width, count] == main[i]):
    #             adjacent_options.append(main[i])
    #         next_position = adjacent_options[0] #initialize next position to the first option, then iterate through the list of options
    #         for m in range(len(adjacent_options)):
    #             if (adjacent_options[m][2]<int(next_position[2])): #if the count variable is lower, set next_position equal to that cell
    #                 next_position = adjacent_options[m]
    #         final_path[i] = next_position #add the next position to the final path array
    #         count-=1 #decrement count (because we're now working in the opposite direction, from the player to the target location)
    #     final_path.reverse()
    #     print(final_path)
    #     return final_path

    # def move(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
    #     destination = game_board.center
    #     path = self.get_pathfind_list(destination[0], destination[1], shooter, game_board, partition_grid)
    #     if(self.move_index<len(path)-2):
    #         angle = angle_to_point(shooter, path[self.move_index])
    #         #angle = angle_to_point(path[self.move_index][0], path[self.move_index+1][1])
    #     else: angle = angle_to_point(shooter, destination)
    #         #angle = angle_to_point(((path[self.move_index])[0], (path[self.move_index])[1]), destination)
    #     #angle = self.angle_to_point(path[self.move_index], path[self.move_index+1]) if (self.move_index+1<len(path)) else angle_to_point(path[self.move_index], destination)
    #     actions.set_move(int(angle), shooter.max_speed)
    #     self.move_index+=1

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
        walls_corners_list = [[walls[0].hitbox.top_left, walls[0].hitbox.top_right, walls[0].hitbox.bottom_left, walls[0].hitbox.bottom_right]] #array of arrays of duples
        for i in range(1, len(walls)):
            walls_corners_list.append([walls[i].hitbox.top_left, walls[i].hitbox.top_right, walls[i].hitbox.bottom_left, walls[i].hitbox.bottom_right])
        for i in range(len(walls)):
            if((pos[0] > int(walls_corners_list[i][0][0]) and pos[0] < int(walls_corners_list[i][1][0])) or (pos[1] > int(walls_corners_list[i][2][1]) and  pos[1] < int(walls_corners_list[i][0][1]))):
                return True
        return False            

    def find_next_move(self, target_x: int, target_y: int, me: Shooter, walls: list):
        target = (target_x, target_y)
        current_pos = me.hitbox.middle
        next_pos = me.hitbox.middle
        for i in range(-1, 1):
            for j in range(-1, 1):
                if not (i == 0 and j == 0):
                    test_pos = (current_pos[0] + (i * me.max_speed / 2), current_pos[1] + (j * me.max_speed / 2))
                    if not self.is_in_wall(*test_pos, walls) and distance(next_pos[0], next_pos[1], target[0], target[1]) > distance(test_pos[0], test_pos[1], target[0], target[1]):
                        next_pos = test_pos
        return next_pos

    def move(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter, target_x: int, target_y: int) -> None:
        target = (target_x, target_y)
        walls = self.only_walls(list(partition_grid.get_all_objects()))
        next_move = self.find_next_move(*target, shooter, walls)
        actions.set_move(int(angle_to_point(shooter, next_move)), shooter.max_speed / 2)

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
        return