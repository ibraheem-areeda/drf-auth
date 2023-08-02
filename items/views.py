from django.shortcuts import render
from .models import Item , Feedback
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ItemSerializer , FeedbackSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class ItemListView(ListCreateAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FeedbackListView (ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsOwnerOrReadOnly]

class FeedbackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsOwnerOrReadOnly]