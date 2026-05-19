from django.db import models

# Create your models here.
class EmergencyRequest(models.Model):

    token = models.OneToOneField(Token, on_delete=models.CASCADE, related_name='emergency_request', null=True, blank=True)
    emergency_type = models.CharField(max_length=100)
    document = models.FileField(upload_to='emergency_docs/', null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Emergency ({self.emergency_type}) for Token {self.token.serial_number} - {self.status}"
