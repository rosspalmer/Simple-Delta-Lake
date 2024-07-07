from dataclasses import dataclass


@dataclass
class SimpleEnvironment:
    name: str
    setup_path: str
    profile_path: str = "~/.bashrc"
    java_version: str = "11.0.21+9"
    hadoop_version: str = "3.2.4"
    scala_version: str = "2.12.18"
    spark_version: str = "3.5.1"

    def package_name(self, package: str) -> str:
        match package:
            case "java":
                return f"OpenJDK11U-jdk_x64_linux_hotspot_${self.java_version.replace()}"
            case "scala":
                return f"scala-{self.scala_version}"
            case "spark":
                return f"spark-{self.spark_version}-bin-hadoop3"

    def package_archive_name(self, package: str) -> str:

        package_name = self.package_name(package)

        archive_extension = ""
        match package:
            case "java":
                archive_extension = "tar.gz"
            case "scala":
                archive_extension = "tgz"
            case "spark":
                archive_extension = "tgz"

        return f"{package_name}.{archive_extension}"

    def package_url(self, package: str) -> str:
        package_archive = self.package_archive_name(package)
        url_prefix = "TODO"
        return f"{url_prefix}/{package_archive}"

    def package_home(self, package: str) -> str:
        return f"{self.setup_path}/{package}"
