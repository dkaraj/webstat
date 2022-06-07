from django.db import models


class Website(models.Model):
    name = models.CharField(max_length=255, default=None, null=False)
    code = models.CharField(max_length=255, default=None, unique=True, null=False)
    development_mode = models.BooleanField(default=False)
    support_email = models.EmailField(default=None, null=True)
    no_reply_email = models.EmailField(default=None, null=True)
    developer_email = models.EmailField(default=None, null=True)
    timezone = models.CharField(max_length=32,
                                default='UTC')

    class Meta:
        db_table = 'website'
