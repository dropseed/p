from .scripts import Scripts
from .make import Makefile
from .js import NpmScripts


# in order of priority
known_types = [
    # manual
    Makefile,
    Scripts,
    NpmScripts,
]
