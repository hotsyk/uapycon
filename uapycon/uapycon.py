# -*- coding: utf-8 -*-

import datetime


def days_till_pycon():
    today = datetime.date.today()
    pycon_start = datetime.date(2016, 4, 23)
    if pycon_start > today:
        return "PyCon Ukraine starts in {0} days".format(
            (pycon_start - today).days)
    elif pycon_start == today:
        return "Hurry up, PyCon Ukraine is today!"
    else:
        return "Looks, like you are missing it :("
