import numpy as np
from pprint import pprint


def asteroid_search(ast_map):
    seeing_map = np.zeros_like(ast_map)

    x_locs, y_locs = np.where(ast_map == 1)
    for x, y in zip(x_locs, y_locs):
        # list of angles which I can see astroids along
        visible = []
        # Loop through other asteroids
        for x_i, y_i in zip(x_locs, y_locs):
            if x_i == x and y_i == y:
                continue
            dx = x - x_i
            dy = y - y_i
            angle = np.arctan2(dy,dx).round(6)
            if angle not in visible:
                visible.append(angle)
        seeing_map[x,y] = len(visible)

    return seeing_map

def destroy_asteroids(ast_map):
    remenants = np.asarray(ast_map)
    laser_x, laser_y = np.where(remenants == 2)

    N_clear = 200
    current_angle = 1e-10
    N_dest = 0
    while N_dest < N_clear:
        x_locs, y_locs = np.where(remenants == 1)

        visible = {}
        for x_i, y_i in zip(x_locs, y_locs):
            if x_i == laser_x and y_i == laser_y:
                continue
            dx = laser_x - x_i
            dy = laser_y - y_i
            angle = np.arctan2(dy,dx).round(6)[0]
            angle = float(angle)

            if angle > 0:
                angle -= 2*np.pi

            if angle not in visible:
                visible[angle] = (x_i, y_i)
            else:
                x_p, y_p = visible[angle]
                dist_p = (laser_x - x_p)**2 + (laser_y - y_p)**2
                dist_i = (laser_x - x_i)**2 + (laser_y - y_i)**2
                if dist_p > dist_i:
                    visible[angle] = (x_i, y_i)

        angles = sorted(visible.keys())[::-1]
        i = 0
        angle = angles[i]
        while angle >= current_angle:
            i += 1
            angle = angles[i]

        next_asteroid = visible[angle]

        remenants[next_asteroid] = 0
        N_dest += 1
        current_angle = angle
    print("The {}th asteroid to be destroyed is {}".format(N_clear, next_asteroid))




key = {
    '.': 0,
    '#': 1,
    'X': 2,
}
with open('day10.txt', 'r') as map_file:
    ast_map = []
    for line in map_file:
        line = [key[i] for i in line.strip()]
        ast_map.append(line)
ast_map = np.asarray(ast_map)

visible_asteroids = asteroid_search(ast_map)
best_loc = np.where(visible_asteroids == visible_asteroids.max())

print("The best location to build a station is {}, {}, from where we can see {} asteroids".format(*best_loc, visible_asteroids.max()))

ast_map[best_loc] = 2
destroy_asteroids(ast_map)

