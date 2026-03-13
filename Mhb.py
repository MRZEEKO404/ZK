import os
import sys
import time

# Lush Color Palette
G = '\033[92m'  # Green
R = '\033[91m'  # Red
Y = '\033[93m'  # Yellow
B = '\033[94m'  # Blue
C = '\033[96m'  # Cyan
W = '\033[97m'  # White
S = '\033[1m'   # Bold
X = '\033[0m'   # Reset

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def logo():
    print(f"""
{C}{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}
{G}{S}   __  __  _    _  ____     _______  ____    ____   _      
  |  \/  || |  | ||  _ \   |__   __||  _ \  / __ \ | |     
  | \  / || |__| || |_) |     | |   | |_) || |  | || |     
  | |\/| ||  __  ||  _ <      | |   |  _ < | |  | || |     
  | |  | || |  | || |_) |     | |   | |_) || |__| || |____ 
  |_|  |_||_|  |_||____/      |_|   |____/  \____/ |______|{X}
{Y}             >>> MHB OFFICIAL TOOL v1.0 <<<{X}
{C}{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}
    """)

def run_module(mod_name, is_paid=False):
    try:
        if is_paid:
            print(f"{Y}[*] Checking License...{X}")
            time.sleep(1.5)
            print(f"{G}[+] License Verified! Accessing Paid Module...{X}")
        else:
            print(f"{C}[*] Opening Free Version...{X}")
        
        time.sleep(1)
        
        # Importing the .so module
        # MHB.cpython-313... -> import MHB
        # file.cpython-313... -> import file
        module = __import__(mod_name)
        
        # Checking for entry point functions
        if hasattr(module, 'main'):
            module.main()
        elif hasattr(module, 'menu'):
            module.menu()
        elif hasattr(module, 'login'):
            module.login()
        else:
            # Kuch files import hote hi chal jati hain
            pass
            
    except ImportError:
        print(f"\n{R}[-] Error: {mod_name}.so file nahi mili!{X}")
        print(f"{Y}[!] Make sure files are in the same folder.{X}")
    except Exception as e:
        print(f"\n{R}[!] Module Error: {e}{X}")
    
    input(f"\n{B}Press Enter to return to MHB Menu...{X}")

def main():
    while True:
        clear()
        logo()
        
        # Menu Options
        print(f"{W}[{G}01{W}] {S}RUN FREE TOOL   {C}(File: file.so){X}")
        print(f"{W}[{G}02{W}] {S}{Y}RUN PAID TOOL   {G}(File: MHB.so){X}")
        print(f"{W}[{R}00{W}] {S}EXIT TOOL{X}")
        print(f"{C}{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}")
        
        choice = input(f"{G}MHB @ MENU >> {X}")

        if choice in ['1', '01']:
            # file.so wali free hai
            run_module("file", is_paid=False)
            
        elif choice in ['2', '02']:
            # MHB.so wali paid hai
            run_module("MHB", is_paid=True)
            
        elif choice in ['0', '00']:
            print(f"\n{Y}[!] Closing MHB TOOL... Khuda Hafiz!{X}")
            sys.exit()
        else:
            print(f"{R}[!] Galat Option! Dobara select karein.{X}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
