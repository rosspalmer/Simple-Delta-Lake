from pathlib import Path
import shutil
from typing import Dict, List

from simple_delta.setup import SetupTask
from simple_delta.setup import InstallJavaLib, SetupDelta, SetupMasterConfig, SetupEnvsScript
from simple_delta.environment import SimpleEnvironment


class SimpleBuild:

    @staticmethod
    def run(env: SimpleEnvironment):

        simple_home = Path(env.config.simple_home)
        if not simple_home.exists():
            simple_home.mkdir()
        shutil.rmtree(env.libs_path, ignore_errors=True)

        setup_tasks: Dict[str, SetupTask] = {
            "install_java": InstallJavaLib("java", {"JAVA_HOME": f"{env.libs_path}/jdk-{env.config.get_version('java')}",
                                           "PATH": "$PATH:$JAVA_HOME/bin"}),
            "install_scala": InstallJavaLib("scala", {"SCALA_HOME": env.package_home_directory('scala'),
                                            "PATH": "$PATH:$SCALA_HOME/bin"}),
            "install_spark": InstallJavaLib("spark", {"SPARK_HOME": env.package_home_directory('spark'),
                                            "PATH": "$PATH:$SPARK_HOME/bin"}),
            "install_delta": SetupDelta(),
            "setup_master": SetupMasterConfig(),
            "setup_envs": SetupEnvsScript()
        }

        for task_name, task in setup_tasks.items():
            task.run(env)
