from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('new_order/', views.NewOrder.as_view(), name='new_order'),
    path('made_order/', views.MadeOrder.as_view(), name='made_order')
]
