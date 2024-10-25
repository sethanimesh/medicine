from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    side_effect = models.TextField(blank=True, null=True)
    containdications = models.TextField(blank=True, null=True)
    dosage = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class UserMedication(models.Model):
    users = models.ForeignKey('auth.User', on_delete=models.CASCADE) #link to the user
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCASE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    dosage_taken = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__self(self):
        return f"{self.user.username}-{self.medicine.name}"