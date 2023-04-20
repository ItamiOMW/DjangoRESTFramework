from rest_framework import serializers

from .models import Woman


class WomanSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Woman
        fields = "__all__"
