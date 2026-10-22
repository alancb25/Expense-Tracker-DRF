# from django.shortcuts import render
from expApp.models import Expense 
from expApp.serializers import ExpenseSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
# from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


# from rest_framework import viewsets

# Create your views here.

class ExpenseCreateListView(CreateAPIView,ListAPIView):
    # queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
        ]
    filterset_fields=["category","payment"]
    search_fields=["title"]
    ordering_fields=["amount","created_at"]

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ExpenseRetrieveUpdateDeleteView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = ExpenseSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)
    # queryset=Expense.objects.all()
