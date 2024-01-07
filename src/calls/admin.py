from django.contrib import admin
from .models import Call
from .use_cases.perform_call import PerformCall

import logging
logger = logging.getLogger("calls")

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

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        logger.warn('Enqueuing call pk=%(pk)s', dict(pk=obj.pk))

        use_case = PerformCall()
        req = PerformCall.Request(to=obj.to)
        use_case(req)
