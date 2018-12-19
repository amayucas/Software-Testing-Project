from django.conf import settings

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'
DEFAULT_LICENSES = {
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative commons')
}

LICENSES = getattr(settings, 'LICENSES', DEFAULT_LICENSES)


BADWORDS = getattr(settings, 'LIST_OF_BADWORDS', [])