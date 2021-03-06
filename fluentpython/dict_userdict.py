# UserDict subclasses MutableMapping
import collections


class StrKeyDict(collections.UserDict):
    def __missing_(self, key):
        if isinstance(self, key):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item
