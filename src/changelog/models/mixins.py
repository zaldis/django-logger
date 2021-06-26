from crum import get_current_user
from django.forms.models import model_to_dict

from changelog.models.changelog import get_log_model


class ChangeLogMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attributes = model_to_dict(self)
        for field in attributes:
            str_field = str(field)
            setattr(self, f'old_{str_field}', attributes[field])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.handle_changelog()

    def handle_changelog(self):
        created_by = get_current_user()

        if created_by:
            attributes = model_to_dict(self)
            log_model = get_log_model(self.__class__)
            for field in attributes:
                new_value = getattr(self, field)
                old_value = getattr(self, f"old_{field}")

                if (
                    new_value 
                        and new_value != old_value 
                        and getattr(new_value, 'pk', lambda: None) != old_value
                ):
                    log_model.objects.create(
                        changed_object=self,
                        field=field,
                        old_value=old_value,
                        new_value=new_value,
                        created_by=created_by,
                    )
