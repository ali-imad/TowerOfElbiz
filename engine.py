import tcod
from input_handlers import handle_keys
from entity import Entity
from render_functions import render_all, clear_all
from map_objects.game_map import GameMap

FONT = "fonts/arial12x12.png"
COLORS = {
    'dark_wall': tcod.Color(13, 27, 42),
    'dark_ground': tcod.Color(66, 76, 85),
    'light_wall': tcod.Color(190, 188, 0),
    'light_ground': tcod.Color(139, 145, 59)
}


def main():
    # TODO: refactor this stuff around. make certain variables global, etc.
    screen_width = 80
    screen_height = 50

    # map settings
    map_width = 80
    map_height = 40

    room_max_size = 11
    room_min_size = 6
    max_rooms = 50

    # fov settings
    fov_algo = tcod.FOV_PERMISSIVE_2
    fov_light_walls = True
    fov_radius = 7

    tcod.console_set_custom_font(FONT, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(screen_width, screen_height, 'nRogue', False, tcod.RENDERER_OPENGL2, vsync=False)

    game_map = GameMap(map_width, map_height)

    con = tcod.console_new(screen_width, screen_height)

    key = tcod.Key()
    mouse = tcod.Mouse()

    player = Entity(0, 0, '@', tcod.white, 'Player')
    entities = [player]

    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)

    fov_recompute = True
    fov_map = game_map.tiles.fov  # stores the fov map in a variable. type: np.ndarray[y, x]

    game_map.populate_map(entities)

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        if fov_recompute:
            game_map.tiles.compute_fov(player.x, player.y, fov_radius, fov_light_walls, fov_algo)

        render_all(con, entities, game_map, screen_width, screen_height, COLORS)
        tcod.console_flush()
        clear_all(con, entities)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if game_map.tiles.walkable[player.y + dy, player.x + dx]:
                player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

        if key.vk == tcod.KEY_ESCAPE:
            return True


if __name__ == '__main__':
    main()
