import random
import tcod.map
import numpy as np
from map_objects.tile import Tile
from map_objects.rectangle import Rect


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = tcod.map.Map(self.width, self.height)  # tiles are addressed in [y, x]
        self.rooms = None

    def create_room(self, room):
        """
        go through the tiles in a rectangle and chisel out the rectangle
        :param room: rect
        """
        # '+ 1' ensures a 1 tile wall around the room
        self.tiles.walkable[room.y1 + 1:room.y2-1, room.x1+1:room.x2-1] = True
        self.tiles.transparent[room.y1 + 1:room.y2-1, room.x1+1:room.x2-1] = True

    def create_h_tunnel(self, x1, x2, y):
        self.tiles.walkable[y, min(x1, x2):max(x1, x2)] = True
        self.tiles.transparent[y, min(x1, x2):max(x1, x2) + 1] = True

    def create_v_tunnel(self, y1, y2, x):
        self.tiles.walkable[min(y1, y2):max(y1, y2) + 1, x] = True
        self.tiles.transparent[min(y1, y2):max(y1, y2) + 1, x] = True

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        """
        :param max_rooms:
        :param room_min_size:
        :param room_max_size:
        :param map_width:
        :param map_height:
        :param player:
        """
        rooms = []
        num_rooms = 0

        # room scatter randomly method
        for i in range(max_rooms):
            w = random.randint(room_min_size, room_max_size)
            h = random.randint(room_min_size, room_max_size)
            x = random.randint(0, map_width - w - 1)
            y = random.randint(0, map_height - h - 1)

            # establish a potential new room 'r'
            r = Rect(x, y, w, h)

            # add the first room if rooms is empty
            if num_rooms == 0:
                rooms.append(r)
                num_rooms += 1

            else:
                for room in rooms:
                    # if any room is contained within the new room, or vice versa, break out of the loop
                    if room.intersect(r) or r.intersect(room):
                        break
                # if the room does not encapsulate or is not encapsulated in another room
                else:
                    rooms.append(r)
                    num_rooms += 1

        """
        now that the room list has been established, lets parse through it and 
        make tunnels to neighbouring (by index) rooms
        """

        for i in range(num_rooms - 1):
            room = rooms[i]
            other_room = rooms[i + 1]

            # get the centers of each room
            room_x, room_y = room.center()
            other_room_x, other_room_y = other_room.center()

            # store the y1's, y2's, x1's, x2's in a default assuming room is relative top left to other room
            x1, x2 = min(room_x, other_room_x), max(room_x, other_room_x)
            y1, y2 = min(room_y, other_room_y), max(room_y, other_room_y)
            rela_pos = (room_x > other_room_x, room_y > other_room_y)

            # start checking relative locations
            # if the room centers are vertically aligned
            if room_x == other_room_x:
                self.create_v_tunnel(y1, y2, x1)

            # if the room centers are horizontally aligned
            elif room_y == other_room_y:
                self.create_h_tunnel(x1, x2, y1)
            # no alignment, start using rela pos
            else:
                # if the room is to the right of the other room
                if rela_pos[0]:
                    self.create_v_tunnel(y1, y2, room_x)
                    self.create_h_tunnel(x1, x2, other_room_y)
                # else, the room is to the left of the other room
                else:
                    self.create_h_tunnel(x1, x2, room_y)
                    self.create_v_tunnel(y1, y2, other_room_x)

        # now that we've carved tunnels, run through rooms once more and carve the rooms themselves
        for room in rooms:
            self.create_room(room)

        # store the rooms in the level
        self.rooms = rooms

        # finally, set player x and y to the first rooms center
        player.x, player.y = rooms[0].center()

    def populate_map(self, entity_list):
        pass

    def compute_fov(self, x, y, radius, algo, light_walls=True):
        """
        Returns 2d boolean mask of the area covered by transparent tiles based on radius at [y, x].
        :param x:
        :param y:
        :return:
        """
        self.tiles.compute_fov(x, y, radius, light_walls, algo)
