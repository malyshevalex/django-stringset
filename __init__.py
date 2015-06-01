__author__ = 'Alex Malyshev <malyshevalex@gmail.com>'
from collections import MutableSet

from .serializers import JsonSerializer

DEFAULT_SERIALIZER = JsonSerializer()


class StringSet(MutableSet):

    def __init__(self, *args):
        self.data = set()
        for arg in args:
            self.add(arg)

    def add(self, value):
        if value:
            if isinstance(value, (StringSet, list, tuple)):
                for i in value:
                    self.add(i)
            elif isinstance(value, str):
                self.data.add(value)
            else:
                raise TypeError('Arguments should be string, StringSet, list or tuple rather than %s' % type(value))
        return self

    def discard(self, value):
        self.data.discard(value)
        return self

    def __contains__(self, x):
        return x in self.data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for r in self.data:
            yield r
        return

    def serialize(self, serializer=DEFAULT_SERIALIZER):
        return serializer.from_python(list(self))

    @classmethod
    def deserialize(cls, data, serializer=DEFAULT_SERIALIZER):
        return cls(serializer.to_python(data))
