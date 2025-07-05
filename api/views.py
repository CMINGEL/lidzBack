from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models
from . import utils

class ClientView(APIView):
    def get(self, request, pk=None):
        try:
            if pk:
                queryset = models.Client.objects.get(pk=pk)
                serializer = serializers.ClientAllSerializer(queryset, many=False) 
            else:    
                queryset = models.Client.objects.all()
                serializer = serializers.ClientSerializer(queryset, many=True) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        data = request.data
        serializer = serializers.ClientAllSerializer(data=data)
        serializer.is_valid(raise_exception=True)
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
        queryset = models.Message.objects.filter(pk=pk)
        serializer = serializers.MessageSerializer(queryset, many=True) 
        return Response(serializer.data)
        
    def post(self, request):
        data = request.data
        serializer = serializers.MessageSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response(status=status.HTTP_201_CREATED)

class FollowView(APIView):
    def get(self, request, pk):
        try:
            queryset = models.Client.objects.get(pk=pk)
            serializer = serializers.ClientAllSerializer(queryset, many=False)
            filtro = utils.mensajeHoy(serializer.data["messages"])
            respuesta = utils.chatBox(serializer.data, filtro)
            guardaMensaje = utils.guardarMensaje(respuesta, pk, 'agent')
            return Response({respuesta}, status=status.HTTP_200_OK)
        except models.Client.DoesNotExist:
            return Response({},status=status.HTTP_404_NOT_FOUND)


 