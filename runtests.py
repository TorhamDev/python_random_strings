'''
Use this program to run tests manually.
'''
import subprocess
import time
subprocess.run('pytest -vv --capture=no --log-cli-level=DEBUG',check=True)
time.sleep(86400) # I mean... a day is enought right?