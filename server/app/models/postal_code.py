from tortoise.models import Model
from tortoise import fields

class PostalCode(Model):
    cPostalCode = fields.CharField(pk=True, max_length=4)
    cTownName = fields.CharField(max_length=20, null=True)

    class Meta:
        table = "postal_code"

    def __str__(self):
        return f"{self.cPostalCode} - {self.cTownName}"