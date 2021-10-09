from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "age"], name="unique_person")
        ]

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"
