from dataclasses import dataclass
from pathlib import Path
import shutil
from typing import List

from simple_delta.environment import SimpleEnvironment
from simple_delta.setup import SetupJavaLib


class SimpleBuild:

    @staticmethod
    def run(env: SimpleEnvironment):

        # Delete SIMPLE_HOME directory if it exists and create empty directory
        simple_home = Path(env.config.simple_home)
        if simple_home.exists():
            shutil.rmtree(simple_home)
        simple_home.mkdir()

        required_installs: List[SetupJavaLib] = [
            SetupJavaLib("java", {"JAVA_HOME": env.package_home_directory('java'),
                                  "PATH": "$PATH:$JAVA_HOME/bin"}),
            SetupJavaLib("scala", {"SCALA_HOME": env.package_home_directory('scala'),
                                   "PATH": "$PATH:$SCALA_HOME/bin"}),
            SetupJavaLib("spark", {"SPARK_HOME": env.package_home_directory('spark'),
                                   "PATH": "$PATH:$SPARK_HOME/bin"}),
            # SetupJavaLib("hadoop", {"SPARK_HOME": f"{env.package_home('spark')}",
            #                         "PATH": "PATH=$PATH:$SPARK_HOME/bin"}),
        ]

        for install in required_installs:
            install.run(env)
