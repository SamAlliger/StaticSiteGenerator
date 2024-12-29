import os
import shutil

def main():
    source = os.path.join(".", "static")
    target = os.path.join(".", "public")
    try:
        shutil.rmtree(target)
        os.mkdir(target)
        print(f"Successfully cleared public folder at {target}")
    except:
        raise Exception(f"Couldn't clear directory {target}")
    
    copy_dir(source, target)
    

def copy_dir(source, target):
    source_items = os.listdir(source)
    print(f"Started processing on {source_items}")
    for item in source_items:
        current_path = os.path.join(source, item)
        current_target = os.path.join(target, item)
        print(f"Now processing {item} with location {current_path} and destination {current_target}")
        if os.path.isfile(current_path):
            print(f"Copied file to {shutil.copy(current_path, target)}")
        else:
            os.mkdir(current_target)
            print(f"Created directory {current_target}")
            copy_dir(current_path, current_target)
    
main()