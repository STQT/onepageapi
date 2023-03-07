from django.db import models


class TgUser(models.Model):
    tg_id = models.CharField(max_length=20, db_index=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.tg_id + '-' + self.first_name


class UserForcing(models.Model):
    tg_user = models.ForeignKey(TgUser, on_delete=models.PROTECT)
    json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.tg_user.tg_id
