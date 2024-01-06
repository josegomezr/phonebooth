from django.contrib import admin
from .models import Call

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    fields = [
        'user', 'to', 'status', 'price', 'duration'
    ]

    list_display = [
        'expanded_id', 'user', 'status', 'to', 'price', 'duration',
        'created_at', 'updated_at',
    ]

    @admin.display(description="ID")
    def expanded_id(self, obj):
        return '#{:06d}'.format(obj.id)
