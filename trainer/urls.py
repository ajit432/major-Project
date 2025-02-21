from django.urls import path
from trainer.views import *
urlpatterns = [
    path('trainer_home/',trainer_home,name="trainer_home"),
    path('trainer_login/',trainer_login,name="trainer_login"),
    path('trainer_logout/',trainer_logout,name="trainer_logout"),
    path('trainer_start_mock/',trainer_start_mock,name="trainer_start_mock"),
]
