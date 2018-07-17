from django.db import models


class BaseModel(models.Model):
    """
    All models should inherit from this model which includes basic fields.
    """

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.TextField()
    user_name = models.TextField()
