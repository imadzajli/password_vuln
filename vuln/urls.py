from django.urls import path
from .views import *

urlpatterns =[
    path('login/',login),
    path('comments/', comment_view, name='comment_view'),
    path('del/',delete),
    path('cookie/',set_test_cookie),
]