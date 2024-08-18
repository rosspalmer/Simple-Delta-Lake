
import sys

from simple_delta.build import SimpleBuild
from simple_delta.config import SimpleDeltaConfig, read_config
from simple_delta.environment import SimpleEnvironment


if __name__ == "__main__":

    config_file = sys.argv[1]
    config = read_config(config_file)

    env = SimpleEnvironment(config)

    SimpleBuild.run(env)
