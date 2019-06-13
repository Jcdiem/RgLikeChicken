class Fighter: #anything that can fight (will ALWAYS have an owner)
    def __init__(self,level,vt = 0, st = 0,ag = 0,wi = 0, ac = 0):
        self.statPoints = 0
        self.armor = 0
        self.stats = [
            vt, # 0 = Vitality/Helath
            st, # 1 = Strength/Physical Dam-Def
            ag, # 2 = Agility/Ranged Damage
            wi, # 3 = Wisdom/Knowledge
            ac  # 4 = Arcane/Magic Power
        ]
        self.resetStats(vt,st,ag,wi,ac)
        self.level = level
        #Base physical is (Whatever your strength is)        
        self.basePhys = int(self.stats[1])
        #Base magic is 1 plus 2x(whatever magic stat is)
        self.baseMag = int(1+(2*self.stats[4]))
        #Your mana max is 1.5x(your base magic score)
        self.maxMana = self.baseMag*1.5
        # Base creature health is 10 (including player)
        self.baseHealth = int(self.stats[0]) #Base health (NO MODIFIERS)
        self.modBaseHealth = 1 #Percent modifier applied to basehealth
                                            #(I.E. 20% more health would go to this as +0.2)
        self.percentMax = 0.99 #limit for percent modifier stacking (to prevent 100% blocking, etc.)
        self.calcHealth()
        self.cHealth = self.totalHealth #current health (this is what we will modify for death/life)

    def calcHealth(self): #Standard for calculating health stats
        self.exHealth = self.modBaseHealth * self.baseHealth
        self.totalHealth = (self.modBaseHealth+self.exHealth)

    def resetStats(self,vt,st,ag,wi,ac): #Changes stats back to input values
        self.stats[0] = vt
        self.stats[1] = st
        self.stats[2] = ag
        self.stats[3] = wi
        self.stats[4] = ac

    def getStat(self, statNum): #Returns a stat
        #Possible stats
        #0: Vitality/Health
        #1: Strength/Phys Dam-Def
        #2: Agility/Ranged Damage
        #3: Wisdom/Knowledge
        #4: Arcane Sense/Magic Power
        return self.stats[statNum]

    def physDam(self): #TODO: Add stat modifiers to physical
        return (self.basePhys)

    def physAttack(self,target):
        results = []

        damDone = self.physDam - target.armor
        if damDone > 0:
            results.append({'message':'{0} attacks {1} for {2} health '.format(self.owner.name.capitalize(), target.name, str(damDone))})
            results.append(target.fighter.modHealth(damDone))
        else:
            results.append({'message':'{0} strikes {1} but does no damage'.format(self.owner.name.capitalize(),target.name)})

        return results

    def modHealth(self,mod):
        results = []
        self.cHealth = mod

        if self.cHealth <= 0:
            results.append({'dead': self.owner})

        return results


    #TODO: make stat spending system and leveling
    #TODO: implement magic attacks