import tcod as tcd

"""
Template monster for use in creating more intricate ones later
"""
class BasicMonster: #Basic smashing smacky monster (phys attacks only)
    def take_turn(self, target, fovMap, gameMap, entities):
        results = []

        monster = self.owner
        if tcd.map_is_in_fov(fovMap, monster.x, monster.y):

            if monster.distanceTo(target) >= 2:
                monster.move(target,entities,gameMap)

            elif target.fighter.cHealth > 0: #If within smacking range and has health
                attack_results = monster.fighter.attack(target)
                results.extend(attack_results)

        return results