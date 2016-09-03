# Lesson 2
import os
import os.path
import shutil

origin_path = "lesson2"
target_path = "lesson2-new"

original_files = [f for f in os.listdir(origin_path) if os.path.isfile(os.path.join(origin_path, f))]

if os.path.exists(target_path):
    os.path.rmtree()
os.makedirs(target_path)
for file in original_files:
    shutil.copyfile(origin_path+"/"+file, target_path+"/"+file)

target_files = [f for f in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, f))]
for file in target_files:
    new_name = "".join([c for c in file if not c.isdigit()])
    print("Old: {} | New: {}".format(file, new_name))
    os.rename(target_path+"/"+file, target_path+"/"+new_name)
