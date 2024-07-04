from rest_framework import serializers
from .models import Specialization, Designation ,Doctor, AvailableTime , Review


class SpecializationSerailizers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta :
        model = Specialization 
        fields = '__all__'
        
        
class DesignationSerailizers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta :
        model = Designation 
        fields = '__all__'
        
class DoctorSerailizers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta :
        model = Doctor 
        fields = '__all__'
        
        
class AvailableTimeSerailizers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta :
        model = AvailableTime 
        fields = '__all__'
        
class ReviewSerailizers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta :
        model = Review 
        fields = '__all__'