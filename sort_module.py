from pathlib import Path
from datetime import datetime
import re
import json 

default_sort_list = {

    ".rar": "Archives",
	".zip": "Archives",

    ".json": "Code/JSON",
	".py": "Code/Python",

	".js": "Code/Web/JS",
	".html": "Code/Web/HTML",
	".css": "Code/Web/CSS",

    ".txt": "Documents/Text",
	".docx": "Documents/Text",
    ".doc": "Documents/Text",
	".odp": "Documents/Text",
	".pages": "Documents/Text",
	".key": "Documents/Text",

	".xls": "Documents/Excel",
    ".xlsx": "Documents/Excel",
	".csv": "Documents/Excel",
	".numbers": "Documents/Excel",

	".pptx": "Documents/Presentation",
    ".ppt": "Documents/Presentation",

    ".exe": "Executables",

	".png": "Images",
	".jpeg": "Images",
	".jpg": "Images",
	".gif": "Images",
	".bmp": "Images",
	".tiff": "Images",

	".mp3": "Musics",
	".flac": "Musics",
	".wav": "Musics",

    ".pdf": "PDF",

	".mp4": "Videos",
	".mov": "Videos",
	".avi": "Videos",
	".webm": "Videos"
}

SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent
sort_list_path = SOURCE_DIR / "sort_list.json"
if sort_list_path.exists() == False:
    sort_list_path.touch()
    with open(sort_list_path, "w", encoding='utf-8') as f:
        json.dump(default_sort_list, f, ensure_ascii=False)


def get_the_moment():
    now = datetime.now()
    moment = now.strftime("%d/%m/%Y  %H:%M")
    return moment


def write_report(file_name, dest_folder, file_count, file_count_total, max_len):
    report_path = SOURCE_DIR / "report.txt"
    if report_path.exists() == False:
        report_path.touch()
    with open(report_path, 'a', encoding='utf-8') as report:
        now = get_the_moment()
        file_name_length = (len(file_name) + 2)
        spaces = max_len - file_name_length 
        content =f"{now}   {file_name} {' ' * spaces} ---->   {dest_folder} \n"
        report.write(content)
        if file_count == 1:
            content = f"\n{file_count_total} files were sorted"
            report.write(content)
            content = "\n_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"
            report.write(content)
        report.close()


def check_valid_folder(path_to_folder):
    if path_to_folder.exists():
        return True
    else:
        return False


def check_folder_name_validity(new_folder):
    invalid_chars = r'[<>:"\\|?*\x00-\x1F]'
    reserved_names = ["CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]

    if re.search(invalid_chars, new_folder):
        print("\nSome invalids chars are in the name ")
        return False
    
    if new_folder.upper() in reserved_names:
        print("\nYou used a reserved name ")
        return False
    
    if new_folder.startswith(" "):  
        print("\nDon't use a space at the starts of a folder name ")
        return False 
    
    if len(new_folder) > 30:
        print("\nIt's supposed to be a folder name, not a novel ")
        return False
    
    else:
        return True
    
  
def choice_menu(choice, path_to_folder, report):
    print(f"""
_______________________________________________________________________________
                    WELCOME TO THE S.O.R.T.E.D
      
      1: Add a path 
      2: Activate / Desactivate report 
      3: Display the sort list 
      4: Add an extension to the sort list 
      5: Remove an extension from the sort list 
      6: Change the destination folder of an extension
      7: Sort
      8: Infos
      9: Quit

      The actual path is : {path_to_folder}                                                                                                
      Report is {report}
______________________________________________________________________________               
""")
    
    choice = input("Faites votre choix : ")

    return choice


def add_folder_to_sort(path_to_folder):
    print("""
_______________________________________________________________________________
TIP : You can paste a copied path by right clicking with your mouse    
               
""")
    path_to_folder = input("Enter the path of your folder : ")
    path_to_folder = Path(path_to_folder)
    if check_valid_folder(path_to_folder): 
        return path_to_folder 
    else:
        print("""
The given path doesn't exists\n
Would you like to retry ?                             --> Press r
Would you like to quit to main menu ?                 --> Press q
             """)
        choice = input("Make your choice : ")
        if choice == "r":
            return add_folder_to_sort(path_to_folder="")
        elif choice == "q":
            return 
        else:
            return


def report_on_off(state_report):
    if state_report == "activated":
        state_report = "desactivated"
        return state_report
    else: 
        state_report = "activated"
        return state_report


def display_sort_list():
    with open(sort_list_path, "r", encoding='utf-8') as f: 
        sort_list = json.load(f)
        print("\n")
        max_len = 0
        for key, value in sort_list.items():
            ext_len = (len(key) + 4)
            if ext_len > max_len:
                max_len = ext_len 
        for key, value in sort_list.items():
            ext_len = (len(key) + 2)
            spaces = max_len - ext_len
            print("Extensions ", key, spaces * " ", "goes to the folder   -->   ", value)
        input("\nPress enter to leave  . . .") 


def add_extension():
    print("""
_______________________________________________________________________________
TIP : Don't forget the dot before your extension type   
               
""")
    with open(sort_list_path, "r", encoding='utf-8') as f: 
        sort_list = json.load(f)

    new_ext = input("Enter a new extension type : ")

    if new_ext.startswith(".") == False:
        print("""
It didn't start with a dot\n
Would you like to retry ?                             --> Press r
Would you like to quit to main menu ?                 --> Press q
             """)
        choice = input("Make your choice : ")
        if choice == "r":
            add_extension()
        if choice == "q":
            return
        else:
            return
       
    if new_ext in sort_list:
        print("""
This extension is already in the list \n
Would you like to retry ?                             --> Press r
Would you like to change its destination folder ?     --> Press c
Would you like to quit to main menu ?                 --> Press q
              """)
        choice = input("Make your choice : ")
        if choice == "r":
            add_extension()
        if choice == "c":
            pass
        elif choice == "q":
            return
        else:
            return
    new_folder = input("\nEnter the folder you want this type of file to be sorted in : ")
    is_folder_name_valid = check_folder_name_validity(new_folder)
    if is_folder_name_valid == True: 
        sort_list[new_ext] = new_folder
        sort_list = dict(sorted(sort_list.items(), key=lambda item: item[1].lower()))
        with open(sort_list_path, "w", encoding='utf-8') as f:
            json.dump(sort_list, f, ensure_ascii=False, indent=4)
        print(f"\nThe extension {new_ext} has been added to the list and will go to the folder {new_folder}")
        input("\nPress enter to leave  . . .") 
    else:
        print("""
Would you like to retry ?               --> Press r
Would you like to quit to main menu ?   --> Press q
              """)
        choice = input("Make your choice : ")
        if choice == "r":
            add_extension()
        if choice == "q":
            return
        else:
            return


def remove_extension():
    print("""
_______________________________________________________________________________
TIP : Don't forget the dot before your extension type   
               
""")
    ext_to_rm = input("Enter extension you'd like to remove : ")
    with open(sort_list_path, "r", encoding='utf-8') as f: 
        sort_list = json.load(f)
    if ext_to_rm in sort_list:
        del sort_list[ext_to_rm]
        print(f"\nThe extension {ext_to_rm} has been removed from the list")
        input("\nPress enter to leave  . . .") 
        sort_list = dict(sorted(sort_list.items(), key=lambda item: item[1].lower()))
        with open(sort_list_path, "w", encoding='utf-8') as f:
            json.dump(sort_list, f, ensure_ascii=False, indent=4)
    else: 
        print("""
The extension you typped doesn't exist in the list\n
Would you like to add it ?              --> Press a
Would uoi like to retry ?               --> Press r
Would you like to quit to main menu ?   --> Press q
              """)
        choice = input("Make your choice : ")
        if choice == "a":   
            add_extension()
        if choice == "r":
            remove_extension()
        if choice == "q":
            return
        else:
            return


def change_dest_folder():
    print("""
_______________________________________________________________________________
TIP : Don't forget the dot before your extension type   
               
""")
    ext = input("Enter the extension you want to change the sorted folder : ")
    with open(sort_list_path, "r", encoding='utf-8') as f: 
        sort_list = json.load(f)
    if ext in sort_list:
        print(f"\nThe current sorted destination folder of {ext} files is {sort_list[ext]}")
        new_folder = input("\nEnter the new name of the folder : ")
        is_folder_name_valid = check_folder_name_validity(new_folder)
        if is_folder_name_valid == True:
            sort_list[ext] = new_folder
            sort_list = dict(sorted(sort_list.items(), key=lambda item: item[1].lower()))
            with open(sort_list_path, "w", encoding='utf-8') as f:
                json.dump(sort_list, f, ensure_ascii=False, indent=4)
            print(f"\nThe destination folder of {ext} has been changed to {new_folder}")
            input("\nPress enter to leave  . . .") 

        else:
            print("""
Would you like to retry ?               --> Press r
Would you like to quit to main menu ?   --> Press q
              """)
            choice = input("Make your choice : ")
            if choice == "r":
                change_dest_folder()
            if choice == "q":
                return
            else:
                return
    else:
        print("""
The extension you typped doesn't exist in the list\n
Would you like to add it ?              --> Press a
Would you like to retry ?               --> Press r
Would you like to quit to main menu ?   --> Press q
              """)
        choice = input("Make your choice : ")
        if choice == "a":   
            add_extension()
        if choice == "r":
            change_dest_folder()
        if choice == "q":
            return
        else:
            return


def apply_sort(path_to_folder, state_report):
    if path_to_folder == "None":
        print("\nThere's no valid directory ")
        return
    else:
        path_to_folder = Path(path_to_folder)
        path_to_folder = list(path_to_folder.iterdir())
        file_count_total = sum(1 for item in path_to_folder if item.is_file())
        max_len = 0
        with open(sort_list_path, "r", encoding='utf-8') as f: 
            sort_list = json.load(f)

        for f in path_to_folder:
            if f.is_file():
                len_file = (len(f.name) + 4)
                if len_file > max_len:
                    max_len = len_file
        for f in path_to_folder:
            try:
                if f.is_file():
                    file_sorted = False
                    file_count = sum(1 for item in path_to_folder if item.is_file())
                    for key, value in sort_list.items():
                        if f.suffix == key:
                            new_path = Path(f.parent / value / f.name)
                            new_folder_path = Path(f.parent / value)
                            if  not new_folder_path.exists():
                                new_folder_path.mkdir(parents = True)
                            f.rename(new_path)
                            file_sorted = True                    
                            if state_report == "activated":
                                write_report(f.name, new_folder_path.name, file_count, file_count_total, max_len)
                            break
                    if not file_sorted:
                        new_path = Path(f.parent / "Others" / f.name)
                        new_folder_path = Path(f.parent / "Others") 
                        if  not new_folder_path.exists():
                            new_folder_path.mkdir(parents = True)
                        f.rename(new_path)
                        file_sorted = True                    
                        if state_report == "activated":
                            write_report(f.name, new_folder_path.name, file_count, file_count_total, max_len)
            except:
                print("\nAn error has occurred. Please make sure you have the necessary permissions for the folder you want to sort")
                input("\nPress enter to continue ...")
        
        print("\nFolder successfully sorted")
        input("\nPress enter to continue ...")


def display_infos():
    print("""
_______________________________________________________________________________
The Super Organizer Review Through Existing Directories goes through a given
folder and puts each files inside into an organized folder with explicit name
based on their extension types
          
1: Add the path of the folder you want to sort
2: Activate or deactivate the creation of a .txt file with every file sorted
inside. It goes where the python script is 
3: Display all extensions that will be sorted and their destination folder
4: Add a nex extnesion and its destination folder to the list 
5: Remove an extension and its destination folder to the list
6: Choose an extension and change its destination folder
7: Lanch the S.O.R.T.E.D program 
8: Well, you're actually inside this option, you should understand what it does
9: Quit the program 
_______________________________________________________________________________
""")
    
    input("Press enter to leave infos  . . .")   
