
from rest_framework import serializers
from .models import Item , Feedback

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields =['price','purcheser', 'name']
        # fields = '__all__'

class FeedbackSerializer (serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields =['name','purcheser', 'feedbk']