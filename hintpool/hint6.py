from random import *


def get_hint_6(self):
    message = "agent is the nearest person to the treasure"
    return [message, None]


def verify_hint_6(self, data):
    agent_distance = abs(self.agent.current_loc[0] - self.treasure_position[0]) + abs(
        self.agent.current_loc[1] - self.treasure_position[1])
    pirate_distance = abs(self.pirate.current_loc[0] - self.treasure_position[0]) + abs(
        self.pirate.current_loc[1] - self.treasure_position[1])
    res = False
    if agent_distance < pirate_distance:
        res = True
    for row in range(self.map.H):
        for col in range(self.map.W):
            dist_from_agent = abs(
                self.agent.current_loc[0] - row) + abs(self.agent.current_loc[1] - col)
            dist_from_pirate = abs(
                self.pirate.current_loc[0] - row) + abs(self.pirate.current_loc[1] - col)
            if res and dist_from_agent >= dist_from_pirate:
                if self.map.map[row][col].is_sea() == False:
                    self.map.map[row][col].make_scan()
            elif not res and dist_from_pirate > dist_from_agent:
                if self.map.map[row][col].is_sea() == False:
                    self.map.map[row][col].make_scan()

    return res
