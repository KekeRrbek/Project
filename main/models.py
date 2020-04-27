

# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    last_twit_date = models.DateField()
    nickname = models.CharField(max_length=300)
    password_for_user = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'last_twit_date': self.last_twit_date,
            'nickname': self.nickname,
            'password_for_user': self.password_for_user
        }


class Twit(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    date = models.DateField(blank=True, null=True)
    like_count = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Twit'
        verbose_name_plural = 'Twits'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'date': self.date,
            'like_count': self.like_count,
            'user_id': self.user_id
        }