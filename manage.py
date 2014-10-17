#!/usr/bin/env python

import os
import sys


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geode_geonode.settings")
    execute_from_command_line(sys.argv)

