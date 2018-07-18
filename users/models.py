from django.db import models


class BaseModel(models.Model):
    """
    All models should inherit from this model which includes basic fields.
    """

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Configuration(BaseModel):
    key = models.TextField()
    value = models.TextField()

    def __str__(self):
        return f"{self.key} = {self.value}"
