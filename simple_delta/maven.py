
from urllib.request import urlretrieve


class MavenDownloader:
    BASE_URL="https://repo1.maven.org/maven2"

    @staticmethod
    def maven_url(group_id: str, artifact_id: str, version: str) -> str:
        package_url = f"{group_id.replace('.','/')}/{artifact_id}/{version}"
        return f"{MavenDownloader.BASE_URL}/{package_url}"

    @staticmethod
    def download_jar(group_id: str, artifact_id: str, version: str, download_folder: str):
        jar_filename = f"{artifact_id}-{version}.jar"
        urlretrieve(
            f"{MavenDownloader.maven_url(group_id, artifact_id, version)}/{jar_filename}",
            f"{download_folder}/{jar_filename}"
        )
