from rest_framework import serializers
from .utils import validarRut
from . import models

class DebtSerializer(serializers.ModelSerializer):
  
  client = serializers.PrimaryKeyRelatedField(queryset=models.Client.objects.all())

  def validate_institution(self, value):
    if value == '':
      raise serializers.ValidationError('Campo obligatorio')
    return value
  
  def validate_amount(self, value):
    if value == '':
      raise serializers.ValidationError('Campo rut obligatorio')
    return value
  
  class Meta:
      model = models.Debt
      fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
  client = serializers.PrimaryKeyRelatedField(queryset=models.Client.objects.all())
  def validate_text(self, value):
    if value == '':
      raise serializers.ValidationError('Campo obligatorio')
    return value
  
  def validate_role(self, value):
    if value == '':
      raise serializers.ValidationError('Campo obligatorio')
    return value
  
  class Meta:
      model = models.Message
      fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
  def validate_rut(self, value):
    if value == '':
      raise serializers.ValidationError('Campo rut obligatorio')
    
    if(validarRut(value)==False):
      raise serializers.ValidationError('Rut no es valido')
    
    return value
  
  def validate_name(self, value):
    if value == '':
      raise serializers.ValidationError('Campo nombre obligatorio')
    return value

  class Meta:
    model = models.Client
    fields = '__all__' 

class ClientAllSerializer(serializers.ModelSerializer):
  debts = DebtSerializer(many=True, read_only=True)
  messages = DebtSerializer(many=True, read_only=True)

  def validate_rut(self, value):
    if value == '':
      raise serializers.ValidationError('Campo rut obligatorio')
    
    if(validarRut(value)==False):
      raise serializers.ValidationError('Rut no es valido')
    
    return value
  
  def validate_name(self, value):
    if value == '':
      raise serializers.ValidationError('Campo nombre obligatorio')
    return value

  class Meta:
    model = models.Client
    fields = '__all__' 



