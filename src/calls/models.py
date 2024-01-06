from django.utils.functional import cached_property
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Call(models.Model):
    class Status(models.TextChoices):
        # The call is freshly created in the system
        CREATED = "created", _('Created')
        # The call is ready and waiting in line before dialing.
        QUEUED = "queued", _('Enqueued')
        # The call is currently ringing.
        RINGING = "ringing", _('Ringing')
        # The call was answered and is currently in progress.
        IN_PROGRESS = "in-progress", _('In Progress')
        # The call was hung up while it was queued or ringing.
        CANCELED = "canceled", _('Canceled')
        # The call was answered and has ended normally.
        COMPLETED = "completed", _('Completed')
        # The caller received a busy signal.
        BUSY = "busy", _('Busy')
        # There was no answer or the call was rejected.
        NO_ANSWER = "no-answer", _('No Answer')
        # The call could not be completed as dialed, most likely because the
        # phone number was non-existent.
        FAILED = "failed", _('Failed')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.DO_NOTHING,
        related_name='calls'
    )

    status = models.CharField(
        max_length=16,
        null=False,
        choices=Status,
        default=Status.CREATED,
    )

    to = models.CharField(
        max_length=32,
        null=False,
        blank=False
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        null=True
    )

    duration = models.SmallIntegerField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = _("call")
        verbose_name_plural = _("calls")
