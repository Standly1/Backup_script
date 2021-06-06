import os
import shutil
from datetime import datetime

def file_or_folder():
    while True:
        choice = input("Please chose Folder or File\n-->")
        choice = choice.lower()
        if (choice == "file") or (choice == "folder"):
            return choice


#Method for make the backup folder name
def make_backup_dir_name(dest):
    time = datetime.now().strftime("%H%M%S-%d-%m-%y")
    add = dest+"/backup-"+time
    return add


if __name__ == '__main__':
    src_addr = ""
    dest_addr = ""
    backup_type = file_or_folder()
    if backup_type == "file":
        file_exists = False
        while not file_exists:
            src_addr = input("Please insert src for file\n-->")
            file_exists = os.path.isfile(src_addr)
            if not file_exists:
                print("Please write a real path")
        file_exists = False
        while not file_exists:
            dest_addr = input("Please insert dest for file\n-->")
            file_exists = os.path.exists(dest_addr)
            if not file_exists:
                print("Please write a real path")
        #Now we can make a dir for the backup
        backup_addr = make_backup_dir_name(dest_addr)
        os.mkdir(backup_addr)
        #Do the backup
        shutil.copy(src_addr, backup_addr)

    elif backup_type == "folder":
        file_exists = False
        while not file_exists:
            src_addr = input("Please insert src for folder\n-->")
            file_exists = os.path.exists(src_addr)
            if not file_exists:
                print("Please write a real path")
        file_exists = False
        while not file_exists:
            dest_addr = input("Please insert dest for folder\n-->")
            file_exists = os.path.exists(dest_addr)
            if not file_exists:
                print("Please write a real path")

        # Now we can make a dir for the backup
        backup_addr = make_backup_dir_name(dest_addr)
        # Do the backup
        shutil.copytree(src_addr, backup_addr)


