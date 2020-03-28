import uuid

from django.db import models


class Profile(models.Model):
    pid = models.CharField(primary_key=True, default=uuid.uuid4)
    preferred_name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)  # Renamed from `name`
    last_name = models.CharField(max_length=256, null=True)  # New, nullable column

    @property
    def name(self):
        return self.first_name

    @name.setter
    def name(self, value):
        self.first_name = value
