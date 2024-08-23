from abc import ABC, abstractmethod
import os
import tarfile
from typing import Dict, List

import urllib.request

from simple_delta.config import ResourceConfig
from simple_delta.environment import SimpleEnvironment


class SetupTask(ABC):

    @abstractmethod
    def run(self, env: SimpleEnvironment):
        pass


class InstallJavaLib(SetupTask):

    def __init__(self, package: str,  env_variables: Dict[str, str]):
        self.package = package
        self.env_variables = env_variables

    def run(self, env: SimpleEnvironment):

        download_url = env.full_package_url(self.package)
        download_path = f"{env.config.simple_home}/{env.archive_name(self.package)}"
        lib_path = f"{env.libs_path}/{env.package_names[self.package]}"

        print(f"Downloading {self.package} binary from:")
        print(download_url)

        urllib.request.urlretrieve(download_url, download_path)

        lib_tarfile = tarfile.open(download_path, "r")
        lib_tarfile.extractall(env.libs_path)
        lib_tarfile.close()
        os.remove(download_path)

        print(f"Updating profile script at: {env.config.profile_path}")
        if not os.path.isfile(env.config.profile_path):
            raise FileNotFoundError(f"Profile script not found: {env.config.profile_path}")

        # TODO overwrite if exports already existing in file
        with open(env.config.profile_path, 'a') as file:
            for variable_name, variable_value in self.env_variables.items():
                file.writelines(f'export {variable_name}={variable_value}\n')


class SetupDelta(SetupTask):

    def run(self, env: SimpleEnvironment):

        print("Adding Delta libraries to spark_defaults.conf file")

        # TODO overwrite delta configs instead of appending
        with open(env.spark_config_path(), 'a') as spark_config_file:
            spark_config_file.write(f"spark.jars.packages io.delta:delta-spark_2.12:{env.config.delta_version}\n")
            spark_config_file.write("spark.sql.extensions io.delta.sql.DeltaSparkSessionExtension\n")
            spark_config_file.write("spark.sql.catalog.spark_catalog org.apache.spark.sql.delta.catalog.DeltaCatalog\n")


class SetupMasterConfig(SetupTask):

    def run(self, env: SimpleEnvironment):

        print(f"Setup master config at {env.spark_config_path()}")

        # TODO overwrite delta configs instead of appending
        with open(env.spark_config_path(), 'a') as spark_config_file:

            if env.config.master_cores:
                spark_config_file.write(f"spark.driver.cores {env.config.master_cores}\n")

            if env.config.master_memory:
                spark_config_file.write(f"spark.driver.memory {env.config.master_memory}\n")

            if env.config.worker_memory:
                spark_config_file.write(f"spark.executor.memory {env.config.worker_memory}\n")

            if env.config.warehouse_path:
                spark_config_file.write(f"spark.sql.warehouse.dir {env.config.warehouse_path}\n")


class SetupEnvsScript(SetupTask):

    def run(self, env: SimpleEnvironment):

        print(f"Setup spark-env.sh bash script at {env.spark_env_sh_path()}")

        worker_info: ResourceConfig | None = None
        for worker_config in env.config.workers:
            if worker_config.host == env.local_host:
                worker_info = worker_config
                break

        with open(env.spark_env_sh_path(), 'a') as env_sh_file:

            env_sh_file.write(f'export SPARK_LOCAL_IP="{env.local_host}"')
            env_sh_file.write(f'export SPARK_HOST_IP="{env.config.master.host}"')
            env_sh_file.write(f'export SPARK_WORKER_CORES={env.config.worker_cores}')
            env_sh_file.write(f'export SPARK_WORKER_MEMORY={env.config.worker_memory}')
            if worker_info:
                env_sh_file.write(f'export SPARK_WORKER_INSTANCES={worker_info.instances}')
