import tcod as tcd
class KeybindingSystem:
    def __init__(self):
        self.keys=[ #For characters only!
            'w', # 0 = Up
            's', # 1 = Down
            'a', # 2 = Left
            'd', # 3 = Right
            'q', # 4 = Up and left
            'e', # 5 = Up and right
            'z', # 6 = Down and left
            'c'  # 7 = Down and right
        ]
        # self.upKey = 'w'
        # self.downKey = 's'
        # self.leftKey = 'a'
        # self.rightKey = 'd'
        # self.leftUp = 'q'
        # self.rightUp = 'e'
        # self.downLeft = 'z'
        # self.downRight = 'c'

    def handleKeys(self,key):
        keyChar = chr(key.c)

        # Movement keys
        if key.vk == tcd.KEY_UP or keyChar == self.keys[0]: #move up
            return {'move': (0, -1)}
        elif key.vk == tcd.KEY_DOWN or keyChar == self.keys[1]: #move down
            return {'move': (0, 1)}
        elif key.vk == tcd.KEY_LEFT or keyChar == self.keys[2]: #move left
            return {'move': (-1, 0)}
        elif key.vk == tcd.KEY_RIGHT or keyChar == self.keys[3]: #move right
            return {'move': (1, 0)}
        elif keyChar == self.keys[4]: #Move diagonally up and left
            return {'move': (-1, -1)} 
        elif keyChar == self.keys[5]: #Move diagonally up and right
            return {'move': (1, -1)}
        elif keyChar == self.keys[6]: #Move diagonally down and left
            return {'move': (-1, 1)}
        elif keyChar == self.keys[7]: #Move diagonally down and right
            return {'move': (1, 1)}

        if key.vk == tcd.KEY_ENTER and key.lalt:
            # Alt+Enter: toggle full screen
            return {'fullscreen': True}

        elif key.vk == tcd.KEY_ESCAPE:
            # Exit the game
            return {'exit': True}

        # No key was pressed
        return {}
    
    def changeKey(self,key,change):
        self.keys[key] = change