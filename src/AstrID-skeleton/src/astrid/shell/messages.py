from rich.console import Console
from rich.table import Table

from astrid import __version__
from astrid.config.config import Config
from astrid.util.gateway import get_gateway_msg

config = Config()


def newlines(n=1):
    for i in range(n):
        print("\n")


def welcome_banner():
    newlines(2)
    table = banner_table()
    console = Console()
    console.print(table)
    newlines(2)


def banner_table():
    table = Table(title=f"{config.PROJECT_NAME} {__version__} Session Configuration")

    table.add_column("Key", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    table.add_row("Username", config.USERNAME)
    table.add_row("Host", config.HOSTNAME)
    table.add_row("YGOR_TELESCOPE", config.YGOR_TELESCOPE)

    gateway_msg = get_gateway_msg()
    table.add_row("Gateway", gateway_msg)
    return table
