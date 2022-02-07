from datetime import datetime


class HumanFiendlyTextClock:
    pass


# Number converters
NUM_2_WORDS_DIC = {0: 'twelve', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                   9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                   16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'half'}

# connect word past or to
PAST = "past"
TO = "to"
CLOCK = "o'clock"
SPACE = " "


def get_human_friendly_text(time):
    """turn the time to human friendly text"""
    time, hour, min = get_hour_min(time)

    hour %= 12  # turn 13 => 1

    result = time + SPACE

    if min == 0:  # Case when time is at 1:00
        result += num_to_words(hour).capitalize() + SPACE + CLOCK
    elif min > 30:  # Case when minute is over past one
        hour += 1
        min = 60 - min
        result += num_to_words(min).capitalize() + SPACE + TO + SPACE + num_to_words(hour)
    else:
        result += num_to_words(min).capitalize() + SPACE + PAST + SPACE + num_to_words(hour)
    return result


def get_hour_min(time):
    """return the time constructed format"""
    validate(time)
    hour_min = time.split(":")
    return time, int(hour_min[0]), int(hour_min[1])


def validate(time):
    """validate the format of a input time"""
    if (not time) or (len(time) < 4) or (len(time) > 5) or (":" not in time):
        raise InvalidTimeFormatException(time, "invalid time format, please insert in format HH:MM or H:MM")
    hour_min = time.split(":")
    hour, min = hour_min[0], hour_min[1]
    if not hour or not hour.isdigit() or int(hour) > 23 or int(hour) < 0:
        raise InvalidTimeFormatException(time, "invalid hour, please insert a value between 0 to 24 for hour")
    if not min or not min.isdigit() or int(min) < 0 or int(min) > 59:
        raise InvalidTimeFormatException(time, "invalid minute, please insert a value between 0 to 59 for minute")


def num_to_words(num):
    """convert the number to words between 0 to 30"""
    if num <= 20 or num == 30:
        return NUM_2_WORDS_DIC[num]
    return NUM_2_WORDS_DIC[20] + SPACE + NUM_2_WORDS_DIC[num - 20]


class InvalidTimeFormatException(Exception):
    """Invalid error handling for time format"""
    pass
