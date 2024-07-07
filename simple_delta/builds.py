from dataclasses import dataclass

from simple_delta.environment import SimpleEnvironment


@dataclass
class Builder:
    environment_name: str
    setup_path: str


def default(environment_name: str):
    env = SimpleEnvironment(environment_name)

    return
