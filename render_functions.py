import tcod as tcd


def render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors):
    if fov_recompute:
            # Draw all the tiles in the game map
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = tcd.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight
                if visible:
                    if wall:
                        tcd.console_set_char_background(con, x, y, colors.get('light_wall'), tcd.BKGND_SET)
                    else:
                        tcd.console_set_char_background(con, x, y, colors.get('light_ground'), tcd.BKGND_SET)
                    
                    game_map.tiles[x][y].explored = True
                elif game_map.tiles[x][y].explored:
                    if wall:
                        tcd.console_set_char_background(con, x, y, colors.get('dark_wall'), tcd.BKGND_SET)
                    else:
                        tcd.console_set_char_background(con, x, y, colors.get('dark_ground'), tcd.BKGND_SET)
    # Draw all entities in the list
    for entity in entities:
        draw_entity(con, entity, fov_map)

    tcd.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov_map):
    if tcd.map_is_in_fov(fov_map, entity.x, entity.y):
        tcd.console_set_default_foreground(con, entity.color)
        tcd.console_put_char(con, entity.x, entity.y, entity.char, tcd.BKGND_NONE)


def clear_entity(con, entity):
    # erase the character that represents this object
    tcd.console_put_char(con, entity.x, entity.y, ' ', tcd.BKGND_NONE)