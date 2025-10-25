from tortoise.models import Model
from tortoise import fields
from tortoise.validators import Validator
from typing import Any


class PostalCodeValidator(Validator):
    def __call__(self, value: Any):
        if not value.isdigit():
            raise ValueError('postal code must contain only numbers')
        if len(value) != 4:
            raise ValueError('postal code must be exactly 4 digits')


class TownNameValidator(Validator):
    def __call__(self, value: Any):
        if not value.strip():
            raise ValueError('town name cannot be empty')
        if not all(char.isalpha() or char.isspace() or char in "-'." for char in value):
            raise ValueError('town name can only contain letters, spaces, hyphens, apostrophes, and dots')
        if len(value) < 3 or len(value) > 25:
            raise ValueError('town name must be between 3 - 25 chars')


class PostalCode(Model):
    postal_code = fields.CharField(pk=True, max_length=4, source_field='cPostalCode',
                                   validators=[PostalCodeValidator()])

    # From Reddit: Længste bynavn: 'Vester Torsted Udflyttere', 25 tegn, den ligger i nærheden af Vejen. - https://www.reddit.com/r/Denmark/comments/3o50mv/hvad_er_danmarks_l%C3%A6ngste_bynavn/
    town_name = fields.CharField(max_length=25, source_field='cTownName', validators=[TownNameValidator()])

    class Meta:
        table = 'postal_code'
