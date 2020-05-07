



class Variable():

    _name: str = None
    _value = None

    _isAutoIncrement: str = None

    def __init__(self, name, value):
        self._name = name
        self._value = value
        self._isAutoIncrement = False
        pass

    def __call__(self):

        if (self._isAutoIncrement):
            oldValue = self._value

            if (self._value is float or self._value is int):
                self._value += 1
            else:
                pass
        else:
            return self._value

    def __repr__(self):

        return self()
