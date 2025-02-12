from django.urls import path, include
from .views import *

urlpatterns = [
    path('menu-items/', name="menu-items", view=menu_items),
    path('menu-item/<int:id>/', name="menu-items", view=menu_detail),
    path('category/', name="category-list", view=category_items),
    path('category/<int:id>/', name="category-detail", view=category_detail)
]