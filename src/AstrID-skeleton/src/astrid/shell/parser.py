from argparse import ArgumentParser
from pathlib import Path

from astrid.config.config import Config


class Parser(ArgumentParser):
    """Parse the command-line arguments"""

    def __init__(self):
        self.config = Config()
        description = f"""
            {self.config.PROJECT_NAME} Launcher
            All CLI arguments other than those defined below are passed through to iPython.
            See $ ipython --help for more details
            """
        super(Parser, self).__init__(description=description)

        self.add_args()

    def add_args(self):
        self.add_argument("-v", "--verbosity", help="Set logging verbosity", type=int, default=2, choices=[0, 1, 2, 3])
        self.add_argument("--log", help="Specify log path", type=Path)
        self.add_argument("-q", "--quiet", help="Silence DEBUG- and INFO-level logs to stderr", action="store_true")
        # return parser.parse_known_args()
