#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from the_neverending_blog.preps import set_default_env, load_sample_data


def main():
    set_default_env()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    load_sample_data()


if __name__ == '__main__':
    main()
