from typing import Iterable

from sample.models import Person


def add_person(name: str, age: int) -> bool:
    person, created = Person.objects.get_or_create(name=name, age=age)
    return created


def get_people() -> Iterable[Person]:
    return Person.objects.order_by("name", "age")
