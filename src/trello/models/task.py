from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db import models

from changelog.models import ChangeLogMixin, track_model_changes
from trello.models.column import Column
from trello.models.mixins import BaseModelMixin, CreatedAtMixin, CreatedByMixin


User = get_user_model()


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=False)


class ArchivedTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=True)


class AllTaskManager(models.Manager):
    use_in_migrations = True


@track_model_changes
class Task(ChangeLogMixin, BaseModelMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField(default=0)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    estimated_time = models.FloatField(help_text="in minutes", blank=True, null=True)
    is_archived = models.BooleanField(default=False)

    objects = TaskManager()
    archived_objects = ArchivedTaskManager()
    all_objects = AllTaskManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["position"]
