import os
import socket
from pathlib import Path

import toml
from dotenv import dotenv_values

from astrid import get_path_root


class Config:

    def __init__(self):
        self.ROOT_PATH = get_path_root()
        self.ENV_PATH = self.ROOT_PATH / ".env"
        self.TOML_PATH = self.ROOT_PATH / "pyproject.toml"
        self.load_user()
        self.load_env()
        self.parse_toml()

    def load_user(self):
        self.USERNAME = os.getlogin()
        self.HOSTNAME = socket.getfqdn()

    def load_env(self):
        self.env_all = dotenv_values(self.ENV_PATH)
        self.YGOR_TELESCOPE = self.env_all["YGOR_TELESCOPE"]
        self.YGOR_ROOT = self.env_all["YGOR_ROOT"]
        self.YGOR_INSTALL = self.env_all["YGOR_INSTALL"]
        self.GB_ROOT = self.env_all["GB_ROOT"]

    def parse_toml(self):
        with open(self.TOML_PATH, "r") as f:
            toml_str = f.read()
            toml_all = toml.loads(toml_str)
        for k in toml_all.keys():
            if k not in self.env_all.keys():
                self.env_all[k] = toml_all[k]
            else:
                raise KeyError(f"Key {k} exists in both .env and pyproject.toml")
        self.PROJECT_NAME = self.env_all["project"]["name"]

    def get_value(self, key1, key2=None):
        if key2 is None:
            config_value = self.env_all[key1]
        else:
            config_value = self.env_all[key1][key2]
        return config_value


if __name__ == "__main__":
    config = Config()
    ygor_telescope = config.get_value("YGOR_TELESCOPE")
    project_name = config.get_value("project", "name")
    print(ygor_telescope)
    print(project_name)
