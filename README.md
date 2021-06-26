# Basic logger for django models

## HOW TO USE

```
from changelog.models import ChangeLogMixin, track_model_changes

@track_model_changes
class UserModel(models.Model):
    pass
```

Then run:
```
python manage.py makemigrations
```
to create new migrations to make appropriate Log models (from marked by you).

And finally sync migrations:
```
python manage.py migrate
```


## HOW IT WORKS

You should mark all necessary models with `track_model_changes` decorator. It saves all models, that will be prepared to track.

Next you also have to add mixin: `ChangeLogMixin`. It adds some changes to `__save__` method of the model. when the model will be changed the method will be triggered and appropriate ChangeLog model will be updated with new row about this change.