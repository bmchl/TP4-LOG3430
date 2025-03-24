import os
import sys

result = os.system("git bisect start $badhash $goodhash")
if result != 0:
    sys.exit(result)

result = os.system("git bisect run python manage.py test")
test_failed = result != 0

os.system("git bisect reset")

if test_failed:
    sys.exit(1)