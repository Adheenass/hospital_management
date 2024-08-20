from rest_framework import serializers
from .models import person



class peopleserializer(serializers.ModelSerializer):
     class Meta :
        model = person
        # fields = ['name' , 'age']
        # exclude = ['name']
        fields = '__all__'