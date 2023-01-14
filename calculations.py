import math

GRAVITY = 9.8


# Calculations if h is 0
def calc_time(initial_velocity, angle_of_launch):
    if 0 < angle_of_launch < 90:
        Vy = initial_velocity * (math.sin(math.radians(angle_of_launch)))
        time_of_flight = 2 * Vy / GRAVITY
        return round(time_of_flight, 2)  # sec
    else:
        return 0


def calc_max_height(initial_velocity, angle_of_launch):
    if 0 < angle_of_launch < 90:
        Vy = initial_velocity * (math.sin(math.radians(angle_of_launch)))
        hmax = Vy ** 2 / (2 * GRAVITY)
        return round(hmax, 2)
    else:
        return 0


def calc_distance(initial_velocity, angle_of_launch):
    if 0 < angle_of_launch < 90:
        Vy = initial_velocity * (math.sin(math.radians(angle_of_launch)))
        Vx = initial_velocity * (math.cos(math.radians(angle_of_launch)))
        d = 2 * Vx * Vy / GRAVITY
        return round(d, 2)
    else:
        return 0
