import datetime

from flask_api import exceptions


def coerce_to_date(s):
    date = datetime.datetime.strptime(s, "%Y-%m-%d")
    if date < datetime.datetime.now():
        raise exceptions.APIException("Cannot bill an expired card.")
    return date


def coerce_to_integer(s):
    if len(s) != 3:
        raise exceptions.APIException("Invalid security code.")
    try:
        return int(s)
    except ValueError:
        raise exceptions.APIException("Invalid security code.")
