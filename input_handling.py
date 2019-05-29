import tcod as tcd


def handle_keys(key):
    # Movement keys
    if key.vk == tcd.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == tcd.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == tcd.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == tcd.KEY_RIGHT:
        return {'move': (1, 0)}

    if key.vk == tcd.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    elif key.vk == tcd.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}