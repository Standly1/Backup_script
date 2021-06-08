import os #Import af "OS" libary til at tjekke og verificer stier som vi bruger til at vælge src og destination for backup.
import shutil #Import af "Shutil" libary denne bruger vi til at lave selve backup'en - det er en som indeholder copy command.
from datetime import datetime #Import af "Datetime" som vi bruger i navngivningen af backup mappen.

#Metode til backup valg - inderholder loop til valg af backup funktion.
def file_or_folder():
    while True:
        choice = input("Please chose Folder or File\n-->")
        choice = choice.lower()
        if (choice == "file") or (choice == "folder"):
            return choice


#Metode til mappe oprettelse samt navngivning.
def make_backup_dir_name(dest):
    time = datetime.now().strftime("%d-%m-%y %H;%M;%S")
    add = dest+"/backup-"+time
    return add

#Kode til valg af src & destination address for backup.
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
        #Opretter mappe ud fra vores angivende metode.
        backup_addr = make_backup_dir_name(dest_addr)
        os.mkdir(backup_addr)
        #Laver backup (copy).
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

        #Opretter mappe ud fra vores angivende metode.
        backup_addr = make_backup_dir_name(dest_addr)
        #Laver backup (copy).
        shutil.copytree(src_addr, backup_addr)


