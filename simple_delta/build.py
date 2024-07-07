from dataclasses import dataclass
from typing import List

from simple_delta.environment import SimpleEnvironment
from simple_delta.setup import SetupJavaLib


class Build:

    @staticmethod
    def run(self, env: SimpleEnvironment):

        java_installs: List[SetupJavaLib] = [
            SetupJavaLib("java", {"JAVA_HOME": f"{env.package_home('java')}",
                                  "PATH": "PATH=$PATH:$JAVA_HOME/bin"}),
            SetupJavaLib("scala", {"SCALA_HOME": f"{env.package_home('scala')}",
                                   "PATH": "PATH=$PATH:$SCALA_HOME/bin"}),
            SetupJavaLib("spark", {"SPARK_HOME": f"{env.package_home('spark')}",
                                   "PATH": "PATH=$PATH:$SPARK_HOME/bin"}),
            SetupJavaLib("hadoop", {"SPARK_HOME": f"{env.package_home('spark')}",
                                    "PATH": "PATH=$PATH:$SPARK_HOME/bin"}),
        ]



