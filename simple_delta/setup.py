from abc import ABC, abstractmethod
from dataclasses import dataclass
import os
import tarfile
from typing import Dict, List

import wget

from simple_delta.environment import SimpleEnvironment


class SetupTask(ABC):

    @abstractmethod
    def run(self, env: SimpleEnvironment):
        pass


class SetupJob:

    def __init__(self, tasks: List[SetupTask]):
        self.tasks = tasks

    def run(self, env: SimpleEnvironment):

        for task in self.tasks:
            task.run(env)


@dataclass
class SetupJavaLib(SetupTask):
    package: str
    env_variables: Dict[str, str]

    def run(self, env: SimpleEnvironment):

        download_path = f"{env.setup_path}/{env.package_archive_name(self.package)}"
        wget.download(env.package_url(self.package), download_path)

        lib_tarfile = tarfile.open(download_path, "r")
        lib_tarfile.extractall(env.package_home(self.package))
        os.remove(download_path)

        # TODO add env variables to profile

