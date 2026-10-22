from expApp.models import Expense,User
from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=["id","username","email"]

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields="__all__"
        read_only_fields=["id","created_at","owner"]