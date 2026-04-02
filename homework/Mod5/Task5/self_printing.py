import os
import subprocess

result = 0
for n in range(1, 11):
    result += n ** 2

BASE_DIR = os.path.abspath(__file__)
command = ['cat', BASE_DIR]
print(subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout)