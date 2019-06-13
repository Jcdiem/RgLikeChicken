import tcod as tcd

from components.fighter import Fighter
from input_handling import handle_keys
from entity import Entity, get_blocking_entities_at_location
from game_states import GameStates
from fov_functions import initialize_fov, recompute_fov
from render_functions import clear_all, render_all
from map_objects.game_map import GameMap

def main():
    #Screen stuff
    screen_width = 80
    screen_height = 50

    #Map genration stuff
    map_width = 80
    map_height = 50
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    maxMonPerRoom = 3

    #FOV stuff
    fov_radius_base = 5
    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = fov_radius_base #Set to base so it can be modified by the game for torches etc

    colors = {
        'player': tcd.Color(50,255,50),
        'enemy': tcd.Color(255,50,255),
        'friendly': tcd.Color(75,255,75),
        'dark_wall': tcd.Color(0, 0, 100),
        'dark_ground': tcd.Color(50, 50, 150),
        'light_wall': tcd.Color(130,110,50),
        'light_ground': tcd.Color(200,100,50)
    }

    ply = Entity(0, 0, '@', colors.get('player'), 'Player', blocks=True)
    entities = [ply]

    tcd.console_set_custom_font('font.png', tcd.FONT_TYPE_GREYSCALE | tcd.FONT_LAYOUT_TCOD)

    tcd.console_init_root(screen_width, screen_height, 'Rougelike Chicken', False)
    con = tcd.console_new(screen_width, screen_height)

    #Map stuff
    game_map = GameMap(map_width, map_height)
    game_map.make_map(max_rooms,room_min_size,room_max_size,map_width,map_height, ply, entities, maxMonPerRoom)

    #FOV Stuff
    fov_recompute = True
    fov_map = initialize_fov(game_map)

    #Input Shnizzle 
    key = tcd.Key()
    mouse = tcd.Mouse()

    #Game state stuff
    game_state = GameStates.PLAYERS_TURN

    while not tcd.console_is_window_closed():
        tcd.sys_check_for_event(tcd.EVENT_KEY_PRESS, key, mouse)

        if fov_recompute:
            recompute_fov(fov_map, ply.x, ply.y, fov_radius, fov_light_walls, fov_algorithm)

        render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors)

        fov_recompute = False 

        tcd.console_flush()

        clear_all(con, entities)


        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move and game_state == GameStates.PLAYERS_TURN:
            dx, dy = move
            xDest = ply.x + dx #Where we are going to bes X
            yDest = ply.y + dy #Where we are going to be Y
            if not game_map.is_blocked(xDest, yDest):
                target = get_blocking_entities_at_location(entities, xDest, yDest)

                if target:
                    print('You kick the '+target.name+' in the shins, much to its annoyance')
                else:
                    ply.move(dx,dy)

                    fov_recompute = True

                game_state = GameStates.ENEMY_TURN

        if exit:
            return True

        if fullscreen:
            tcd.console_set_fullscreen(not tcd.console_is_fullscreen())

        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity != ply:
                    print('The '+ entity.name+' stands completely still.')

            game_state = GameStates.PLAYERS_TURN


if __name__ == '__main__':
    main()
