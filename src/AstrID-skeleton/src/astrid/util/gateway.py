import os
import socket
from pathlib import Path

import pandas as pd

from astrid.config.config import Config


def get_gateway(ygor_telescope=None, user=None, host=None):
    config = Config()
    if ygor_telescope is None:
        ygor_telescope = config.get_value("YGOR_TELESCOPE")
    gateway = Gateway(ygor_telescope)
    in_gateway, perms = gateway.inGateway(user, host)
    return in_gateway, perms


def get_gateway_msg():
    config = Config()
    in_gateway, perms = get_gateway(config.YGOR_TELESCOPE)
    msg = ""
    if perms is not None:
        if in_gateway:
            perm_keys = [pk for pk in perms.keys()]
            n_keys = len(perm_keys)
            for mi in range(n_keys):
                if mi != 0:
                    msg = msg + "\n"
                m = perm_keys[mi]
                msg = msg + f"{m}: {perms[m]}"
        else:
            raise Exception(
                f"Found these permissions for {config.USERNAME}@{config.HOSTNAME} even though they ARE NOT in the gateway: {perms}"
            )
    else:
        if in_gateway:
            raise Exception(
                f"No permissions found for {config.USERNAME}@{config.HOSTNAME} even though they ARE in the gateway"
            )
        else:
            msg = "Not in the gateway"
    return msg


class Gateway:

    def __init__(self, ygor_telescope):
        self._ygor_telescope = ygor_telescope
        self.load()

    @property
    def ygor_telescope(self):
        return self._ygor_telescope

    def load(self):
        gateway_path = Path(self.ygor_telescope) / "etc/config/securedb.txt"
        if gateway_path.exists():
            self.makeGatewayDF(gateway_path)
        else:
            raise Exception(f"Could not find gateway for YGOR_TELESCOPE={self.ygor_telescope}")

    def makeGatewayDF(self, gateway_path):
        self.db = pd.DataFrame(columns=["user", "host", "manager", "permission"])
        with open(gateway_path, "r") as file:
            for line in file:
                if not line.startswith("#"):
                    if len(line) > 1:
                        line = line.replace("\n", "")
                        info = line.split(" ")
                        perm = info[-1]
                        user_info = info[0].split("@")
                        managers = info[1:-1]
                        if len(managers) < 1:
                            row = [user_info[0], user_info[1], "All", perm]
                            self.db = pd.concat(
                                [pd.DataFrame([row], columns=self.db.columns), self.db], ignore_index=True
                            )
                        else:
                            for m in managers:
                                row = [user_info[0], user_info[1], m, perm]
                                self.db = pd.concat(
                                    [pd.DataFrame([row], columns=self.db.columns), self.db], ignore_index=True
                                )

    def inGateway(self, user=None, host=None):
        user_in_gateway, user_hosts = self.userInGateway(user)
        host_in_user_gateway = False
        if host is None:
            host = socket.getfqdn()
        if user_hosts is not None:
            host_in_user_gateway = (host in user_hosts) or ("all" in user_hosts)
        in_gateway = user_in_gateway and host_in_user_gateway
        perms = None
        if in_gateway:
            perms = {}
            user_indx = self.db["user"] == user
            host_indx = (self.db["host"] == host) | (self.db["host"] == "all")
            gateway_indx = self.db.index[user_indx & host_indx].tolist()
            for gi in gateway_indx:
                manager = self.db["manager"][gi]
                manager_perm = self.db["permission"][gi]
                perms[manager] = manager_perm
        return in_gateway, perms

    def userInGateway(self, user=None):
        user_bool = False
        user_hosts = None
        if user is None:
            user = os.getlogin()
        user_indx = self.db.index[self.db["user"] == user].tolist()
        if len(user_indx) >= 1:
            user_bool = True
            user_hosts = self.db["host"][user_indx].tolist()
        return user_bool, user_hosts
