'''
Compile c code using makefile.
Help: https://stackoverflow.com/questions/3121555/invoke-make-from-different-directory-with-python-script
'''
import subprocess,time
import os

current_path = os.getcwd() # finding working or current directory path
process = subprocess.Popen(["make"], cwd=current_path)
time.sleep(2)
process.terminate()

