
from typing import Dict

from simple_delta.config import SimpleDeltaConfig


class SimpleEnvironment:

    def __init__(self, config: SimpleDeltaConfig):
        self.config = config
        self.libs_path = f"{config.simple_home}/libs"

        self.package_urls: Dict[str, str] = {
            "java": "https://github.com/adoptium/temurin11-binaries/releases/download"
                    f"/jdk-{self.config.java_version.replace('+', '%2B')}",
            "scala": f"https://downloads.lightbend.com/scala/{self.config.scala_version}",
            # FIXME use spark url which has older versions
            "spark": f"https://dlcdn.apache.org/spark/spark-{self.config.spark_version}",
        }

        self.package_names: Dict[str, str] = {
            "java": f"OpenJDK11U-jdk_x64_linux_hotspot_{self.config.java_version.replace('+', '_')}",
            "scala": f"scala-{self.config.scala_version}",
            "spark": f"spark-{self.config.spark_version}-bin-hadoop3"
        }

        self.package_extensions: Dict[str, str] = {
            "java": "tar.gz",
            "scala": "tgz",
            "spark": "tgz"
        }

    def archive_name(self, package: str) -> str:
        return f"{self.package_names[package]}.{self.package_extensions[package]}"

    def full_package_url(self, package: str) -> str:
        return f"{self.package_urls[package]}/{self.archive_name(package)}"

    def libs_directory(self) -> str:
        return f"{self.config.simple_home}/libs"

    def package_home_directory(self, package: str) -> str:
        return f"{self.libs_directory()}/{self.package_names[package]}"
