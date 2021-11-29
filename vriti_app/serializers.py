from rest_framework import serializers
# from django import forms 
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style = {'input_type': 'password'}, write_only = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

        def save(self):
            account = User(
                email = self.validated_data['email'],
                username = self.validated_data['username'],
                firstname = self.validated_data['first_name'],
                lastname = self.validated_data['last_name'],
                category = self.validated_data['category'],
                is_superuser = self.validated_data['is_superuser'],
            )
            password = self.validated_data['password']
            password2 = self.validated_data['password2']

            if password != password2:
                raise serializers.validationError({'Password must match'})

            print(account)
            account.set_password(password)
            account.save()
            return account


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