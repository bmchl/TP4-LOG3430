import os
import sys

bad_hash = sys.argv[1]  
good_hash = sys.argv[2] 

os.system("git bisect start $badhash $goodhash")

os.system("git bisect run python manage.py test")

os.system("git bisect reset")