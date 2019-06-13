import tcod as tcd

"""
Template monster for use in creating more intricate ones later
"""
class BasicMonster:
    def take_turn(self, target, fovMap, gameMap, entities):
        monster = self.owner
        if tcd.map_is_in_fov(fovMap, monster.x, monster.y):

            if monster.distanceTo(target) >= 2 and monster.distanceTo(target) <= 10:
                monster.moveTo(target.x, target.y, gameMap, entities)

            #elif (CONDITION):
            #   stuff here you want to happen if the player is within distance of the enemy