#!/usr/bin/env python

"""Django command-line utility."""

import os
import sys


def main():
    """Run Django administrative commands."""

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "config.settings",
    )

    try:
        from django.core.management import (
            execute_from_command_line,
        )

    except ImportError as error:
        raise ImportError(
            "Could not import Django. Check that Django is "
            "installed and that the virtual environment is active."
        ) from error

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()