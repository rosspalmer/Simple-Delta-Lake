
import sys
from pprint import pprint
from typing import List

from simple_delta.config import SimpleDeltaConfig
from simple_delta.environment import SimpleEnvironment


if __name__ == "__main__":

    config_files: List[str] = sys.argv[1].split(',')
    if len(sys.argv) > 1:
        local_host = sys.argv[2]
    else:
        local_host = ''

    config = SimpleDeltaConfig.read(*config_files)
    env = SimpleEnvironment(config, local_host)

    env.sync()

