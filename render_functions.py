import tcod


def render_all(con, entities, game_map, screen_width, screen_height, colors):
    """
    Handle blitting everything to the console

    :param con: tcod console
    :param entities: list of Entity
    :param game_map: GameMap of tiles
    :param screen_width: int
    :param screen_height: int
    :param colors: dict of colors
    """

    # game map
    # Draw all the tiles in the game map
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = not game_map.tiles.transparent[y, x]
            visible = game_map.tiles.fov[y, x]  # to the player, only

            if visible:
                if wall:
                    tcod.console_set_char_background(con, x, y, colors.get('light_wall'), tcod.BKGND_SET)
                else:
                    tcod.console_set_char_background(con, x, y, colors.get('light_ground'), tcod.BKGND_SET)

            else:
                if wall:
                    tcod.console_set_char_background(con, x, y, colors.get('dark_wall'), tcod.BKGND_SET)
                else:
                    tcod.console_set_char_background(con, x, y, colors.get('dark_ground'), tcod.BKGND_SET)

    # entities
    for entity in entities:
        draw_entity(con, entity, game_map.tiles.fov)

    tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    """
    go through all entities and call clear_entity on them

    :param con: tcod console
    :param entities: list of Entity
    """
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov_map):
    """
    put entity on con
    :param con: tcod console
    :param entity: Entity
    """

    entity_is_in_fov = fov_map[entity.y, entity.x]
    if entity_is_in_fov:
        tcod.console_set_default_foreground(con, entity.color)
        tcod.console_put_char(con, entity.x, entity.y, entity.char, tcod.BKGND_NONE)


def clear_entity(con, entity):
    """
    put ' ' where entity was on con
    :param con: tcod console
    :param entity: Entity
    """

    tcod.console_put_char(con, entity.x, entity.y, ' ', tcod.BKGND_NONE)
