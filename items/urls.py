from django.urls import path
from .views import ItemDetailView, ItemListView , FeedbackListView ,FeedbackDetailView
urlpatterns = [
   
    path('', ItemListView.as_view(), name= 'item_list'),
    path('<int:pk>',ItemDetailView.as_view(), name= 'item_detail'),
    path ('feedback/',FeedbackListView.as_view(), name= 'feedback_list'),
    path ('feedback/<int:pk>',FeedbackDetailView.as_view(), name= 'feedback_detail')
]

