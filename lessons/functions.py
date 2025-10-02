"""
functions
"""


def abc(a, b, c):
    print(a, b, c)


abc(1, c=2, b=3)


def weekly_shower_water_consumption(
    showers_per_week, shower_length_in_minutes, AVERAGE_GALLONS_PER_MINUTE=2
):
    return showers_per_week * shower_length_in_minutes * AVERAGE_GALLONS_PER_MINUTE
