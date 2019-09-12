from .scripts import Scripts
from .make import Makefile
from .js import Npm, Yarn
from .python import Pipenv
from .terraform import Terraform
from .combine import Combine
from .carthage import Carthage
from .dep import Dep


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
    Carthage,
    Dep,
]
