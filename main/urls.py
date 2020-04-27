from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from main.views.cbv import TwitList,TwitDetails,UserList,UserDetails,UserTwit,TwitUser
from main.views.fbv import twit_list,user_list

urlpatterns = [
path('login/', obtain_jwt_token),
    path('users/', user_list),
    path('users/<int:pk>/', UserDetails.as_view()),
    path('users/<int:user_id>/twit/', UserTwit.as_view()),

    path('twits/', twit_list),
    path('twits/<int:pk>/', TwitDetails.as_view()),
    path('twits/<int:twit_id>/people/', TwitUser.as_view())

]
