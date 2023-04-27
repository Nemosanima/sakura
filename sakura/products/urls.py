from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books/<int:book_id>/', views.BookDetail.as_view(), name='book_detail'),
    path('books/<int:book_id>/review/', views.AddReview.as_view(), name='add_review'),
    path('reviews/<int:review_id>/delete/', views.DeleteReview.as_view(), name='delete_review')
]
