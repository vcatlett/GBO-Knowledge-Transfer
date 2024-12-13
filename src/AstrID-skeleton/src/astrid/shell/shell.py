from astrid import __version__
from astrid.config.config import Config
from astrid.gui import app
from astrid.log import init_logging
from astrid.shell.messages import welcome_banner
from astrid.shell.parser import Parser

config = Config()


def main():
    # args, remaining_args = parse_args()
    # init_logging(verbosity=args.verbosity, path=args.log, quiet=args.quiet)
    welcome_banner()
    app.launch()


if __name__ == "__main__":
    main()
