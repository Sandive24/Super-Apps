from list_fungsi import *
import subprocess

# MAIN PROGRAM
opening()
input('\n\n\n\n\nEnter untuk lanjut.. ')
loading(5)
os.system('cls' if os.name == 'nt' else 'clear')
menu()


while True:
    clear_screen()
    menu()
    tindakan = int(input('Pilih : '))
    if tindakan == 1: 
        program1()

    # JIKA PILIH MENU 2
    elif tindakan == 2:
        program2()
    
    elif tindakan == 3:
        path = 'C:\My DATA\Gitub Project\SuperApps\main.py'
        subprocess.call(["python", path])
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        ending()
        break