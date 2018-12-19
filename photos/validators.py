from photos.settings import BADWORDS
from django.core.exceptions import ValidationError


def badwords_detector(value):
    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError('La palabra "{0}" no esta permitida'.format(badword))
    return True
