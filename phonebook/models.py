from django.db import models


class Persone(models.Model):
    name = models.CharField('Contact name', max_length=100)

    def __str__(self):
        return self.name
    
    def all_phones_to_string(self):
        return ", ".join([phone.phone for phone in self.phones.all()])
    

class Phone(models.Model):
    phone = models.CharField('Phone', max_length=11)
    contact = models.ForeignKey(Persone, on_delete=models.CASCADE, related_name='phones')

    def __str__(self):
        return self.phone
