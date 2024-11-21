from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_histories', null=True)
    message = models.TextField()
    sender = models.CharField(max_length=10)  # Choices to distinguish sender
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat history for {self.user.username} at {self.timestamp}"


class CVStructure(models.Model):
    section_name = models.CharField(max_length=100)  # Education, Skills
    description = models.TextField()  # guidelines for the section
    order = models.IntegerField()  # Determines the order of sections in the CV
    is_mandatory = models.BooleanField(default=True)  # Whether this section is mandatory

    def __str__(self):
        return self.section_name


class CoverLetterStructure(models.Model):
    section_name = models.CharField(max_length=100)  # Introduction, Body, Conclusion
    description = models.TextField()  # guidelines for the section
    order = models.IntegerField()  # Determines the order of sections in the Cover Letter
    is_mandatory = models.BooleanField(default=True)  # Whether this section is mandatory

    def __str__(self):
        return self.section_name
