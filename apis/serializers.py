from rest_framework import serializers
from .models import users

class usersSerializer(serializers.ModelSerializer):
      class Meta:
        model =users
        fields =  (
                "user_id",
                "fname",
                "lname",
                "email", 
                "phone",
                "password",
                "age",
                "gender", 
                # "fire_id",
                "created_on"
        
        
        )


    
    # fname = serializers.CharField(max_length=200,required = True)
    # lname = serializers.CharField(max_length=200,required = True)
    # email = serializers.CharField(max_length=200,required = True)
    # phone = serializers.CharField(max_length=200,required = True)
    # password = serializers.CharField(
    #     write_only = True,
    #     required = True,
    #     help_text  ='leave empty is no changes needed',
    #     style = {'input_type':'password','placeholder':'password'}
    # )
    # age = serializers.IntegerField()
    # gender = serializers.CharField(max_length=100,required=True)
    # Firebase_id = serializers.CharField(max_length=200,required=True)

    # class Meta:
    #     model = users

