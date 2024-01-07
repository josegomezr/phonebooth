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

        req = PerformCall.Request(
            to=obj.to,
            callback_url=reverse('calls:twilio_voice-xml',
                kwargs=dict(
                    id=obj.id
                )
            )
        )

        use_case = PerformCall()
        req = PerformCall.Request(to=obj.to)
        response = use_case(req)
        
        logger.info('Twilio call pk=%(pk)s to=%(to)s sid=%(sid)s',
            dict(
                pk=obj.pk,
                to=req.to,
                sid=response.call_sid
            )
        )
