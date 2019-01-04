import os

from .base import BaseType


class Terraform(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) in (".terraform", "terraform.tfstate")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.install = "terraform init"
        self.deploy = "terraform apply"
