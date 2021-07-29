"""Most basic dependency injection imaginable."""

_container = {}


def register(cls, obj):
    """Register class cls with implementation obj."""
    _container[cls] = obj


def inject(cls):
    """Get implementation of class cls."""
    return _container[cls]
