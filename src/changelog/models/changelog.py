from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


loggers_map = {}

def create_log_model(model: models.Model) -> None:

    class Meta:
        ordering = ('-changed_at', )

    attributes = {
        'changed_object': models.ForeignKey(model, on_delete=models.DO_NOTHING),
        'created_by': models.ForeignKey(User, on_delete=models.DO_NOTHING),
        'changed_at': models.DateTimeField(auto_now_add=True),
        'field': models.CharField(max_length=255),
        'old_value': models.CharField(max_length=255, null=True, blank=True),
        'new_value': models.CharField(max_length=255),

        'Meta': Meta,
        '__module__': __name__,
    }
    loggers_map[model] = type(
        f'{model._meta.label}.Logger',
        (models.Model, ),
        attributes
    )


def get_log_model(model: models.Model) -> models.Model:
    log_model = loggers_map.get(model)
    if log_model is None:
        raise ValueError(f'Model <{log_model.__name__}> is not logged')
    return log_model