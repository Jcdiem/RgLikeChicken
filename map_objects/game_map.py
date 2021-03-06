import tcod as tcd
from components.ai import BasicMonster
from components.fighter import Fighter
from map_objects.tile import Tile
from map_objects.rectangle import Rect
from random import randint
from entity import Entity

class GameMap:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities, max_monsters_per_room):
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            #randm width and height
            w = randint(room_min_size, room_max_size) 
            h = randint(room_min_size, room_max_size)
            #Random pos (inside map boundries)
            x = randint(0,map_width - w - 1)
            y = randint(0,map_height - h - 1)

            new_room = Rect(x,y,w,h)

            for other_room in rooms:
                if new_room.intersect(other_room): #room invald
                    break
            else: #room valid
                self.create_room(new_room)
                (new_x, new_y) = new_room.center()

                if num_rooms == 0: # if starting room
                    player.x = new_x
                    player.y = new_y
                else: #If not first, connect to past room
                    (prev_x, prev_y) = rooms[num_rooms-1].center()

                    #50/50
                    if randint(0, 1) == 1:
                        #horiz then vert
                        self.create_h_tunnel(prev_x,new_x,prev_y)
                        self.create_v_tunnel(prev_y,new_y,prev_x)
                    else:
                        #vert then horiz
                        self.create_v_tunnel(prev_y,new_y,prev_x)
                        self.create_h_tunnel(prev_x,new_x,prev_y)

                self.place_entities(new_room, entities, max_monsters_per_room)

                rooms.append(new_room)
                num_rooms += 1

    def create_room(self, room):
        # go through the tiles in the room design and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2): #Appearnlty no end value given when using range
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def place_entities(self, room, entities, max_monsters_per_room):
        #Choose random number of monsters
        numMonsters = randint(0, max_monsters_per_room)

        for i in range(numMonsters):
            #Random location
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                if randint(0, 100) < 80: #Make orc
                    fightComp = Fighter(1,-7,0)
                    aiComp = BasicMonster()
                    monster = Entity(x, y, 'o', tcd.desaturated_green, 'Orc', blocks=True, fighter=fightComp, ai=aiComp)
                else: #Make troll
                    fightComp = Fighter(1,-4,1)
                    aiComp = BasicMonster()
                    monster = Entity(x, y, 'T', tcd.darker_green, 'Troll', blocks=True, fighter=fightComp, ai=aiComp)

                entities.append(monster)

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False