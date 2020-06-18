from collections import UserDict


class NeverNoneDict(UserDict):
    """
    Dictionary with no None entries.
    Deletes keys that get updated to None and works recursively.

    >>> NeverNoneDict({"a": 2, "b": None, "c": {"d": None}})
    {'a': 2, 'c': {}}
    >>> dict_ = NeverNoneDict({"a": 2})
    >>> dict_["a"] = None
    >>> dict_
    {}
    """
    def __setitem__(self, key, value):
        if value is not None:
            if isinstance(value, dict):
                value = NeverNoneDict(value)
            return super().__setitem__(key, value)
        elif super().__contains__(key):
            return super().__delitem__(key)
