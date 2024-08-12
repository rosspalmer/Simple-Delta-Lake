
from simple_delta.build import SimpleBuild
from simple_delta.environment import SimpleEnvironment, SimpleEnvironmentConfig


config = SimpleEnvironmentConfig("test", "/Users/rosspalmer/simple",  "/Users/rosspalmer/simple-test/.bashrc")
env = SimpleEnvironment(config)

SimpleBuild.run(env)
