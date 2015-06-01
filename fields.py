__author__ = 'Alex Malyshev <malyshevalex@gmail.com>'


from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import StringSet, DEFAULT_SERIALIZER


class StringSetField(models.Field, metaclass=models.SubfieldBase):
    description = _('StringSet Field')
    serializer = DEFAULT_SERIALIZER

    def __init__(self, *args, **kwargs):
        try:
            self.serializer = kwargs.pop('serializer')
        except KeyError:
            pass
        super(StringSetField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'TextField'

    def to_python(self, value):
        if isinstance(value, StringSet):
            return value
        return StringSet.deserialize(value, serializer=self.serializer)

    def get_prep_value(self, value):
        value = self.to_python(value)
        return value.serialize(self.serializer)
