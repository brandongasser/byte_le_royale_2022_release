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

    
    def find_opponent(self, things: list, me: Shooter) -> int:
        i = 0
        for thing in things:
            if (type(thing) == Shooter and me.hitbox.middle != thing.hitbox.middle):
                return i
            i += 1
        return -1

    def movement(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
        # This is the list that contains all the objects on the map your player can see
        map_objects = partition_grid.get_all_objects()
        # This is a tuple that represents the position 1 unit in front of where the player
        forward_position = (shooter.hitbox.middle[0] + shooter.hitbox.width + math.cos(math.radians(shooter.heading)),
                            shooter.hitbox.middle[1] + shooter.hitbox.height + math.sin(math.radians(shooter.heading)))
        object_in_front = None
        if forward_position[0] < game_board.width and forward_position[1] < game_board.height:
            object_in_front = partition_grid.find_object_coordinates(forward_position[0], forward_position[1])
        if self.prev_location != shooter.hitbox.middle:
            angle = angle_to_point(shooter, game_board.center)
            actions.set_move(int(angle), shooter.max_speed)
            self.prev_location = shooter.hitbox.middle
        elif object_in_front or 0 <= forward_position[0] <= 500 or 0 <= forward_position[1] <= 500 \
                and self.prev_location != game_board.center:
            #shooter.heading = 0
            actions.set_move((shooter.heading + 90) % 360, 10)

    def shoot(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
        things = list(partition_grid.get_all_objects())
        index = self.find_opponent(things, shooter)
        if (index >= 0):
            opponent = things[index]
            if (distance(opponent.hitbox.middle[0], opponent.hitbox.middle[1], shooter.hitbox.middle[0], shooter.hitbox.middle[1]) <= 30):
                actions.set_shoot(heading = angle_to_point(shooter, opponent.hitbox.middle))

    def take_turn(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
        self.shoot(turn, actions, game_board, partition_grid, shooter)
        self.movement(turn, actions, game_board, partition_grid, shooter)