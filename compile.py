from posixpath import splitext
import pwd


import os

dir = os.path.abspath(os.curdir)

for item in os.listdir(dir):
    if item.endswith(".sh"):
        os.system(f'sh {item}')
    if item.endswith(".py"):
        if item == 'compile.py':
            continue
        os.system(f'python3 {item}')
    if item.endswith(".c"):
        os.system(f"gcc {item} && ./a.out")
    if item.endswith(".java"):
        os.system(f"javac {item} && java {item[:-5]}")
