from abc import ABC, abstractmethod
from dataclasses import dataclass
import os
import tarfile
from typing import Dict, List

import urllib.request

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

        download_url = env.full_package_url(self.package)
        download_path = f"{env.config.setup_path}/{env.archive_name(self.package)}"
        lib_path = f"{env.libs_path}/{env.package_names[self.package]}"

        print(f"Downloading {self.package} binary from:")
        print(download_url)

        urllib.request.urlretrieve(download_url, download_path)

        lib_tarfile = tarfile.open(download_path, "r")
        lib_tarfile.extractall(lib_path)
        os.remove(download_path)

        # TODO add env variables to profile

