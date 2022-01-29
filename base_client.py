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

    
    def find_player(self, things: list, me: Shooter) -> int:
        i = 0
        for thing in things:
            if (type(thing) == Shooter and me.hitbox.middle != thing.hitbox.middle):
                return i
            i += 1
        return -1

    def shoot(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
        things = list(partition_grid.get_all_objects())
        index = self.find_player(things, shooter)
        if (index >= 0):
            opponent = things[index]
            actions.set_shoot(heading = player_utils.angle_to_point(shooter, opponent.hitbox.middle))
        print("\nturn %d:\nplayer index: %d\nopponent: %s\n\n\n" % (turn, index, things[index] if index >= 0 else "no opponent found"))

    def take_turn(self, turn, actions: Action, game_board, partition_grid: PartitionGrid, shooter: Shooter) -> None:
        shoot(turn, actions, game_board, partition_grid, shooter)