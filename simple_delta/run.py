
import sys
from pprint import pprint
from typing import List

from simple_delta.build import SimpleBuild
from simple_delta.config import SimpleDeltaConfig
from simple_delta.environment import SimpleEnvironment


if __name__ == "__main__":

    # config_files: List[str] = sys.argv[1].split(',')
    # local_host = sys.argv[2]
    #
    # config = read_config(*config_files)
    # env = SimpleEnvironment(config, local_host)
    #
    # SimpleBuild.run(env)

    file = '/Users/rosspalmer/Desktop/sega.json'

    config = SimpleDeltaConfig.read(file)

    pprint(config)

