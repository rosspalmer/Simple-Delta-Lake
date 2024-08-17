from pathlib import Path
import shutil
from typing import List

from simple_delta.environment import SimpleEnvironment
from simple_delta.setup import SetupTask, SetupJavaLib, SetupDelta


class SimpleBuild:

    @staticmethod
    def run(env: SimpleEnvironment):

        simple_home = Path(env.config.simple_home)
        if not simple_home.exists():
            simple_home.mkdir()
        shutil.rmtree(env.libs_path, ignore_errors=True)

        setup_tasks: List[SetupTask] = [
            SetupJavaLib("java", {"JAVA_HOME": f"{env.libs_path}/jdk-{env.config.java_version}",
                                  "PATH": "$PATH:$JAVA_HOME/bin"}),
            SetupJavaLib("scala", {"SCALA_HOME": env.package_home_directory('scala'),
                                   "PATH": "$PATH:$SCALA_HOME/bin"}),
            SetupJavaLib("spark", {"SPARK_HOME": env.package_home_directory('spark'),
                                   "PATH": "$PATH:$SPARK_HOME/bin"}),
            SetupDelta()
        ]

        for task in setup_tasks:
            task.run(env)
