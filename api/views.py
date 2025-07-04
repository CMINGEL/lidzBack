from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models

class ClientView(APIView):
    def get(self, request, pk=None):
        try:
            if pk:
                queryset = models.Client.objects.get(pk=pk)
                serializer = serializers.ClientAllSerializer(queryset, many=False) 
            else:    
                queryset = models.Client.objects.all()
                serializer = serializers.ClientSerializer(queryset, many=True) 
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        data = request.data
        serializer = serializers.ClientAllSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        print("es valid?")
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class DebtView(APIView):
    def post(self, request):
        data = request.data
        serializer = serializers.DebtSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class MessaggeView(APIView):
    def get(self, request, pk):
        # try:
            queryset = models.Message.objects.filter(pk=pk)
            serializer = serializers.MessageSerializer(queryset, many=True) 
            return Response(serializer.data)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        # try:
            data = request.data
            serializer = serializers.MessageSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            return Response(status=status.HTTP_201_CREATED)
        # except Exception as e:
        #     return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)