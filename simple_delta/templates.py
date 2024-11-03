from typing import Any, Callable, Dict

from simple_delta.config import SimpleDeltaConfig


DEFAULT_VERSIONS = {
    "java": "11.0.21+9",
    "scala": "2.12.18",
    "spark": "3.5.2",
    "delta": "3.2.0",
    "hadoop": "3.3.1",
    "hive": "3.1.2"
}


DEFAULT_JDBC = {

}


class Templates:

    @staticmethod
    def generate(template_name: str, **kwargs):
        match template_name:
            case "standalone_delta_master":
                return Templates._generate_standalone_delta_master(kwargs)

    @staticmethod
    def _generate_standalone_delta_master(kwargs: Dict[str, Any]) -> SimpleDeltaConfig:

        name = kwargs['name']
        simple_home = kwargs['simple_home']
        profile_path = kwargs['profile_path']

        packages = DEFAULT_VERSIONS.copy()
        del packages['hadoop']

        env = SimpleDeltaConfig(
            name, simple_home, profile_path,
            packages, **kwargs
        )

        return env


