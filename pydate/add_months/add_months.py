from datetime import datetime


def add_months(date: datetime, amount: int) -> datetime:
    """
    Add months to a date.
    :param date: The date to add months to.
    :param months: The number of months to add.
    :return:
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(amount, int):
        raise TypeError("months must be of type int")

    _months = date.month + amount
    _years = date.year + _months // 12
    _months = _months % 12
    return date.replace(year=_years, month=_months)
