from jsonschema._validators import required
from rest_framework import serializers

from onepageapi.stats.models import TgUser, UserForcing


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = "__all__"


class UserForcingSerializer(serializers.ModelSerializer):
    tg_user_id = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = UserForcing
        exclude = "tg_user",
