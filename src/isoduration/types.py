from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from isoduration.operations import add


@dataclass
class DateDuration:
    years: Decimal = Decimal(0)
    months: Decimal = Decimal(0)
    days: Decimal = Decimal(0)
    weeks: Decimal = Decimal(0)

    def __neg__(self) -> DateDuration:
        return DateDuration(
            years=-self.years, months=-self.months, days=-self.days, weeks=-self.weeks,
        )


@dataclass
class TimeDuration:
    hours: Decimal = Decimal(0)
    minutes: Decimal = Decimal(0)
    seconds: Decimal = Decimal(0)

    def __neg__(self) -> TimeDuration:
        return TimeDuration(
            hours=-self.hours, minutes=-self.minutes, seconds=-self.seconds,
        )


class Duration:
    def __init__(self, date_duration: DateDuration, time_duration: TimeDuration):
        self.date = date_duration
        self.time = time_duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.date}, {self.time})"

    def __str__(self) -> str:
        return ""

    def __hash__(self) -> int:
        return 0

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Duration):
            return self.date == other.date and self.time == other.time

        return NotImplemented

    def __neg__(self) -> Duration:
        return Duration(-self.date, -self.time)

    def __add__(self, other: datetime) -> datetime:
        if isinstance(other, datetime):
            return add(other, self)

        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other: object) -> NotImplemented:
        return NotImplemented

    def __rsub__(self, other: datetime) -> datetime:
        if isinstance(other, datetime):
            return -self + other

        return NotImplemented
