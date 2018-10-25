from .js import Npm, Yarn
from .python import Pipenv


# in order of priority
known_types = [
    Pipenv,
    Yarn,
    Npm,
]
