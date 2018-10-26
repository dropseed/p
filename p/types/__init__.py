from .scripts import Scripts
from .make import Makefile
from .js import Npm, Yarn
from .python import Pipenv
from .terraform import Terraform
from .combine import Combine
from .subdir import Subdirectory


# in order of priority
known_types = [
    # universal
    Makefile,
    Scripts,
    # specific tools/languages
    Pipenv,
    Yarn,
    Npm,
    Terraform,
    Combine,
    # last, so overriden by direct directory
    Subdirectory,
]
