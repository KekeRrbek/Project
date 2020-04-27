from rest_framework import serializers


from main.models import Twit
from main.models import User


class TwitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only='True')
    title = serializers.CharField()
    text = serializers.CharField()
    date = serializers.DateField()
    like_count = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        twit = Twit.objects.create(
            text=validated_data.get('text'),
            title=validated_data.get('title'),
            like_count=validated_data.get('like_count'),
            user_id=validated_data.get('user_id')
        )
        return twit

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.like_count = validated_data.get('like_count', instance.like_count)
        instance.user_id = validated_data.get('user_idt', instance.user_id)
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only='True')
        name = serializers.CharField()
        surname = serializers.CharField()
        nickname = serializers.DateField()
        password_for_users = serializers.IntegerField()
        last_twit_date = serializers.IntegerField()

    def create(self, validation_data):
        user = User.objects.create(
            name=validated_data.get('name'),
            surname=validated_data.get('surname'),
            nickname=validated_data.get('nickname'),
            password_for_users=validated_data.get('password_for_user')
            )
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password_for_users = validated_data.get('password_for_users', instance.password_for_users)
        instance.save()
        return instance
