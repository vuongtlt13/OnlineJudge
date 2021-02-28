#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oj.settings")

    print(os.getenv("JUDGE_SERVER_TOKEN"))
    from django.core.management import execute_from_command_line
    import django
    sys.stdout.write("Django VERSION " + str(django.VERSION) + "\n")

    execute_from_command_line(sys.argv)
