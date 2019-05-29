import tcod as tcd
from input_handling import handle_keys
from entity import Entity
from render_functions import clear_all, render_all

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 50

    ply = Entity(int(screen_width / 2), int(screen_height / 2), '@', tcd.red)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', tcd.yellow)
    entities = [npc, ply]

    tcd.console_set_custom_font('font.png', tcd.FONT_TYPE_GREYSCALE | tcd.FONT_LAYOUT_TCOD)

    tcd.console_init_root(screen_width, screen_height, 'Rougelike Chicken', False)
    con = tcd.console_new(screen_width, screen_height)

    key = tcd.Key()
    mouse = tcd.Mouse()

    while not tcd.console_is_window_closed():
        tcd.sys_check_for_event(tcd.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, screen_width, screen_height)#TODO: constuff
        tcd.console_flush()

        clear_all(con, entities)


        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            ply.move(dx,dy)

        if exit:
            return True

        if fullscreen:
            tcd.console_set_fullscreen(not tcd.console_is_fullscreen())


if __name__ == '__main__':
    main()
