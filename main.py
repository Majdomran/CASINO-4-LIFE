import subprocess
import os

def show_bank():
    subprocess.run([os.sys.executable, 'bankkonto.py'])

def show_jobb():
    subprocess.run([os.sys.executable, 'jobb.py'])

def main_menu():
    print("""
    ######      ###     ######  #### ##    ##  #######     ##         ##       #### ######## ########
    ##    ##   ## ##   ##    ##  ##  ###   ## ##     ##    ##    ##   ##        ##  ##       ##
    ##        ##   ##  ##        ##  ####  ## ##     ##    ##    ##   ##        ##  ##       ##
    ##       ##     ##  ######   ##  ## ## ## ##     ##    ##    ##   ##        ##  ######   ######
    ##       ##     ##  ######   ##  ## ## ## ##     ##    ##    ##   ##        ##  ##       ##
    ##       #########       ##  ##  ##  #### ##     ##    #########  ##        ##  ##       ##
    ##    ## ##     ## ##    ##  ##  ##   ### ##     ##          ##   ##        ##  ##       ##
     ######  ##     ##  ######  #### ##    ##  #######           ##   ######## #### ##       ######## 

    Vällkommen till CASINO 4 LIFE
    """)

    while True:
        start = input("""\nINSTRUKTIONER 
-------------------------------------------------------------------------------------------------------
|         1         |         2         |         3         |         4         |         5           |
|      AVSLUTA      |     BANK KONTO    |       WORK        |                   |                     |
|                   |                   |                   |                   |                     |
|___________________|___________________|___________________|___________________|_____________________|
|         6         |         7         |         8         |         9         |         10          |
|                   |                   |                   |                   |                     |
|                   |                   |                   |                   |                     |
|                   |                   |                   |                   |                     |
-------------------------------------------------------------------------------------------------------                                                               
SKRIV HÄR >""")
        
        if start == "1":
            break
        elif start == "2":
            show_bank()
        elif start == "3":
            show_jobb()

if __name__ == "__main__":
    main_menu()
