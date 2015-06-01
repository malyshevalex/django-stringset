__author__ = 'Alex Malyshev <malyshevalex@gmail.com>'

import json
from abc import ABCMeta, abstractmethod


class AbstractSerializer(metaclass=ABCMeta):

    @abstractmethod
    def to_python(self, s):
        pass

    @abstractmethod
    def from_python(self, obj):
        pass


class JsonSerializer(AbstractSerializer):

    def to_python(self, s):
        return json.loads(s)

    def from_python(self, obj):
        return json.dumps(obj)
