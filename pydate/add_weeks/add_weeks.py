from datetime import datetime, timedelta


def add_weeks(date: datetime, amount: int) -> datetime:
    """
    Add weeks to a date.
    :param date: The date to add weeks to.
    :param weeks: The number of weeks to add.
    :return:
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(amount, int):
        raise TypeError("weeks must be of type int")

    return date + timedelta(weeks=amount)
