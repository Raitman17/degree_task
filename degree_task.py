"""Count module."""


def degree(time: float, acc: float, rad: float, vel: float = 0):
    """Count deflection angle.

    Args:
        time (float): time
        acc (float): acceleration
        rad (float): radius
        vel (float, optional): velocity. Defaults to 0.
    Return:
        result(float): deflection angle. round by 2.
    """
    lenght = 2 * 3.14 * rad
    path = vel * time + (acc * time ** 2) / 2
    turn = path / lenght
    result = 360 * (abs(round(turn) - turn))

    return round(result, 2)

print(degree(100, 200, 33, 15))
