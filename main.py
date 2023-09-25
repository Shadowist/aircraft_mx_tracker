import argparse
from os import path
from source import mx_utils


def new(filename: str):
    mx_utils.create_plane_database(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Aircraft MX Logs",
        description="""
        This programs manages aircraft logbooks!
        """
    )

    parser.add_argument(
        '-n',
        '--new',
        help="Creates a new aircraft database.",
        action='store_true'
    )

    parser.add_argument(
        '-o',
        '--open',
        help="Opens the aircraft database.",
        action='store_true'
    )

    parser.add_argument(
        '-f',
        '--filename',
        help="The database file to open.",
        required=True
    )

    args = parser.parse_args()

    # Path Handling
    if args.open and not path.exists(args.filename):
        parser.print_help()
        msg = "\n=================================\n"
        msg += f"filename: {args.filename} is not a valid path!\n"
        msg += "Please select an existing path.\n"
        msg += "================================="
        print(msg)

    if args.new:
        new(args.filename)
