
import sys

from simple_delta.build import SimpleBuild
from simple_delta.config import SimpleDeltaConfig, read_config
from simple_delta.environment import SimpleEnvironment


if __name__ == "__main__":

    config_files = sys.argv[1]
    local_host = sys.argv[2]

    config = read_config(config_files)
    env = SimpleEnvironment(config, local_host)

    SimpleBuild.run(env)
