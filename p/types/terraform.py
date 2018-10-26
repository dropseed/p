import os

from .base import BaseType
from ..run import run


class Terraform(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) in (".terraform", "terraform.tfstate")

    def setup(self):
        run("terraform init")

    def deploy(self):
        run("terraform apply")
