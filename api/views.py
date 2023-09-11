from ast import Name
from requests import request
from rest_framework.views import APIView
from customer.models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status #this is a file that contains status codes

class CustomerListView(APIView):
    def get(self, request):
        customers= Customer.objects.all()
        serializer= CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView): # handle single instance i.e Get
    def get(self, request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        customer.delete()
        return Response("customer deleted",status=status.HTTP_204_NO_CONTENT)