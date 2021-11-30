from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from booking_app.models import Advisor,Booking

class AdvisorSerializer(ModelSerializer):
    
    class Meta:
        model = Advisor
        fields = ['id','name','photo']

class BookingSerializer(ModelSerializer):
    '''Serializes Booking model and returns advisor and booking information'''

    advisor_id = serializers.ReadOnlyField(source='advisor.id')
    advisor_name = serializers.ReadOnlyField(source='advisor.name')
    advisor_photo = serializers.ReadOnlyField(source='advisor.photo.url')
    
    class Meta:
        model= Booking
        fields = ['advisor_id','advisor_name','advisor_photo','appointment','id']
    
