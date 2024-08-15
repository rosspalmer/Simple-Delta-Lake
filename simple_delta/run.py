
from simple_delta.build import SimpleBuild
from simple_delta.config import SimpleDeltaConfig
from simple_delta.environment import SimpleEnvironment


# config = SimpleEnvironmentConfig("test", "/Users/rosspalmer/simple",  "/Users/rosspalmer/simple-test/.bashrc")
config = SimpleDeltaConfig("base", "/opt/simple-lake", "/root/.bashrc")
env = SimpleEnvironment(config)

SimpleBuild.run(env)
