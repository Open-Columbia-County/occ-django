from django.db import models
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TheStatus(models.Model):
    status = models.OneToOneField(Status, unique=True, on_delete=CASCADE)
    img = models.ImageField(upload_to='statusImgs', default='coveredbridge04.jpg')
    def __str__(self):
        return f'{self.status.name} TheStatus'
    
def create_status_theStatus(sender, instance, created, **kwargs):
    if created:
        Status.objects.create(status=instance)
        post_save.connect(create_status_theStatus, sender=Status)

class Projects(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    liveLink = models.CharField(max_length=255, blank=True)
    sourceCode = models.CharField(max_length=255, blank=True)
    status = models.ForeignKey(Status, related_name='projStatus', on_delete=CASCADE)

class Role(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class TheRole(models.Model):
    role = models.OneToOneField(Role, unique=True, on_delete=CASCADE)
    img = models.ImageField(upload_to='roleImgs', default='coveredbridge04.jpg')
    def __str__(self):
        return f'{self.role.name} TheRole'

def create_role_theRole(sender, instance, created, **kwargs):
    if created:
        Role.objects.create(role=instance)
        post_save.connect(create_role_theRole, sender=Role)

class Members(models.Model):
    firstName = models.CharField(max_length=255, blank=True)
    lastName = models.CharField(max_length=255, blank=True)
    brigadeEmail = models.CharField(max_length=255, blank=True)
    personalEmail = models.CharField(max_length=255, blank=True)
    linkedIn = models.CharField(max_length=255, blank=True)
    role = models.ForeignKey(Role, related_name='memberRole', on_delete=CASCADE)

    def fullName(self):
        return f'{self.firstName} {self.lastName}'