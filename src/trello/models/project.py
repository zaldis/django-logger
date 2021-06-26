from django.db import models

from changelog.models import ChangeLogMixin, track_model_changes
from trello.models.mixins import BaseModelMixin


@track_model_changes
class Project(ChangeLogMixin, BaseModelMixin):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
