"""Count module."""


def degree(t: float, a: float, r: float, v: float = 0):
    """Count deflection angle.

    Args:
        t (float): time
        a (float): acceleration
        r (float): radius
        v (float, optional): speed. Defaults to 0.
    Return:
        result(float): deflection angle. round by 2.
    """
    c = 2 * 3.14 * r
    s = v * t + (a * t ** 2) / 2
    turn = s / c
    result = 360 * (abs(round(turn) - turn))

    return round(result, 2)

print(degree(100, 200, 33, 15))
