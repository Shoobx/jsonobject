import inspect
from jsonobject.base import AssertTypeProperty, JsonProperty, JsonArray, JsonObject


class StringProperty(AssertTypeProperty):
    _type = basestring


class IntegerProperty(AssertTypeProperty):
    _type = int


class ObjectProperty(JsonProperty):
    def __init__(self, obj_type, default=Ellipsis, **kwargs):
        self._obj_type = obj_type
        if default is Ellipsis:
            default = self.obj_type
        super(ObjectProperty, self).__init__(default=default, **kwargs)


    @property
    def obj_type(self):
        if inspect.isfunction(self._obj_type):
            return self._obj_type()
        else:
            return self._obj_type

    def wrap(self, obj):
        return self.obj_type.wrap(obj)

    def unwrap(self, obj):
        assert isinstance(obj, self.obj_type), \
            '{} is not an instance of {}'.format(obj, self.obj_type)
        return obj, obj._obj


class ListProperty(ObjectProperty):

    def __init__(self, obj_type, default=Ellipsis, **kwargs):
        if default is Ellipsis:
            default = list
        super(ListProperty, self).__init__(obj_type, default=default, **kwargs)

    def wrap(self, obj):
        return JsonArray(obj, wrapper=type_to_property(self.obj_type))

    def unwrap(self, obj):
        assert isinstance(obj, list), \
            '{} is not an instance of list'.format(obj)

        if isinstance(obj, JsonArray):
            return obj, obj._obj
        else:
            wrapped = self.wrap([])
            wrapped.extend(obj)
            return self.unwrap(wrapped)

TYPE_TO_PROPERTY = {
    int: IntegerProperty,
    basestring: StringProperty,
}


def type_to_property(obj_type):
    if issubclass(obj_type, JsonObject):
        return ObjectProperty(obj_type)
    elif obj_type in TYPE_TO_PROPERTY:
        return TYPE_TO_PROPERTY[obj_type]()
    else:
        for key, value in TYPE_TO_PROPERTY.items():
            if issubclass(obj_type, key):
                return value()
        raise TypeError('Type {} not recognized'.format(obj_type))