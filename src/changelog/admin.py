from django.contrib import admin

from changelog.models.changelog import loggers_map


class ChangeLogModelAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'field', 'old_value', 'new_value', 'changed_at', )


for model in loggers_map.values():
    admin.site.register(model, ChangeLogModelAdmin)
