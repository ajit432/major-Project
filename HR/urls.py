from django.urls import path
from HR.views import *
urlpatterns = [
    path('hr_home/',hr_home,name="hr_home"),
    path('hr_login/',hr_login,name="hr_login"),
    path('hr_logout/',hr_logout,name="hr_logout"),
    path('hr_set_mock/',hr_set_mock,name="hr_set_mock"),
    path('hr_show_student_ratings/',hr_show_student_ratings,name="hr_show_student_ratings"),
    path('hr_show_student_ratings_indi<pk>/',hr_show_student_ratings_indi,name="hr_show_student_ratings_indi"),
]
