import os
import shutil

TARGET = r"C:\Users\chaoa\Pictures\.thumbnails"

if not os.path.isdir(TARGET):
    raise SystemExit(1)

for entry in os.listdir(TARGET):
    path = os.path.join(TARGET, entry)
    try:
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    except OSError:
        pass

raise SystemExit(0)

