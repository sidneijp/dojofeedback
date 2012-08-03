#coding=utf-8

from wtforms import Form, TextField, validators, ValidationError
from models import Dojo

class DojoForm(Form):
    name = TextField('Nome do Dojo', [ validators.Required(message="Campo obrigatorio"),
                                       validators.Length(min=1, max=100, message="Excedeu o maximo de caracteres")
                                     ])

    def validate_name(self, field):
        try:
            Dojo.objects.get(name=field.data)
            raise ValidationError('Ja existe um dojo com este nome')
        except Dojo.DoesNotExist:
            pass

