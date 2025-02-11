from django.urls import path, include
from .views import *

urlpatterns = [
    path('menu-items/', name="menu-items", view=menu_items),
    path('menu-item/<int:id>/', name="menu-items", view=menu_detail)
]