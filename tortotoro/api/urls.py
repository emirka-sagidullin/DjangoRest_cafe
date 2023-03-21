from django.urls import path, include
from . import views


urlpatterns = [
    path('order/', views.order_list),
    path('order/<int:pk>/', views.order_detail),
    path('status/', views.status_list),
    path('status/<int:pk>', views.status_detail),
    path('employee/', views.employee_list),
    path('employee/<int:pk>', views.employee_detail),
    path('post/', views.post_list),
    path('post/<int:pk>', views.post_detail),
]