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
    lib_tar_url: str
    output_home: str
    home_variable: str

    def run(self, env: SimpleEnvironment):

        lib_tar_name = wget.download(self.lib_tar_url)

        output_lib_tar = f"{self.output_home}/{lib_tar_name}"
        output_lib_dir = output_lib_tar.split(".")[1]

        os.rename(f"{os.getcwd()}/{lib_tar_name}", output_lib_tar)
        lib_tarfile = tarfile.open(output_lib_tar, "r")
        lib_tarfile.extractall(output_lib_dir)
        os.remove(output_lib_tar)

