
from math import floor, pi


def degree(time: float, acc: float, rad: float, vel: float = 0):
    """Count deflection angle, returns deflection angle. round by 2.

    Args:
        time (float): time
        acc (float): acceleration
        rad (float): radius
        vel (float): velocity. Defaults to 0.

    Returns:
        angle(float): deflection angle. round by 2.
    """
    round_deg = 360
    lenght = 2 * round(pi, 2) * rad
    path = vel * time + (acc * time ** 2) / 2
    turn = path / lenght
    angle = round_deg * (abs(floor(turn) - turn))

    return round(angle, 2)
