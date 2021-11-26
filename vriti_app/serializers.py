from rest_framework import serializers
# from django import forms 
from .models import User

class Userserializers(serializers.HyperlinkedModelSerializer):
    #['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'category']
    # password = forms.CharField(widget=forms.PasswordInput())
    # url = serializers.HyperlinkedIdentityField(view_name = "vriti_app:user-detail")
    class Meta:
        model = User
        fields = ('id','url', 'username', 'first_name', 'last_name', 'email', 'category', 'password')      
    # username = serializers.CharField()
    # first_name = serializers.CharField(max_length = 200)
    # last_name = serializers.CharField(max_length = 200)
    # email = serializers.EmailField()
    # password = serializers.CharField()
    # password2 = serializers.CharField()
    
    # def create(self, validated_data):
    #     print(validated_data)
    #     return User.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.password = validated_data.get('password', instance.password)
#         # instance.password2 = validated_data.get('username', instance.password2)
#         instance.save()
#         return instance