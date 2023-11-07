from django.urls import path
from .views import UserProfileList, UserProfileDetail, RegisterUser,ListCreateMembers,MembersDetail

urlpatterns = [
    path("profiles/", UserProfileList.as_view()),
    path("profiles/<int:pk>/", UserProfileDetail.as_view()),
    path("signup/", RegisterUser.as_view()),
    path('members/',ListCreateMembers.as_view()),
    path('member/<int:pk>/',MembersDetail.as_view())
]
