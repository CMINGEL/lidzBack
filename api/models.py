from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=25)
    rut = models.CharField(max_length=10, unique=True)
    salary = models.IntegerField(null=True, blank=True)
    savings = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.rut
    
class Message(models.Model):
    """Modelo que almacena los mensajes intercambiados con cada cliente. """
    ROLE_CHOICES = [('client', 'client'), ('agent', 'agent')]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField( )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name="Rol",)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sent_at']

class Debt(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='debts')
    institution = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    due_date = models.DateField()
    class Meta:
        ordering = ['client', 'due_date']
