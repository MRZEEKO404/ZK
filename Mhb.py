import os
import sys
import time

# Colors
G = '\033[92m' ; R = '\033[91m' ; Y = '\033[93m' 
C = '\033[96m' ; W = '\033[97m' ; S = '\033[1m' ; X = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def logo():
    print(f"{C}{S}" + "━"*50 + f"{X}")
    print(f"{G}{S}  __  __  _    _  ____     _______  ____    ____   _      \n |  \/  || |  | ||  _ \   |__   __||  _ \  / __ \ | |     \n | \  / || |__| || |_) |     | |   | |_) || |  | || |     \n | |\/| ||  __  ||  _ <      | |   |  _ < | |  | || |     \n | |  | || |  | || |_) |     | |   | |_) || |__| || |____ \n |_|  |_||_|  |_||____/      |_|   |____/  \____/ |______|{X}")
    print(f"{Y}             >>> MHB OFFICIAL TOOL v1.0 <<<{X}")
    print(f"{C}{S}" + "━"*50 + f"{X}")

def run_free():
    try:
        print(f"{G}[+] Loading FREE Tool (file.so)...{X}")
        import file # Aapki free file
        
        # Jo list aapne bheji uske mutabiq ye functions hain
        if hasattr(file, 'start_cracking'):
            file.start_cracking()
        elif hasattr(file, 'show_logo'):
            file.show_logo()
        elif hasattr(file, 'main'):
            file.main()
        else:
            print(f"{R}[-] Entry point nahi mila!{X}")
    except ImportError:
        print(f"{R}[-] Error: file.so nahi mili!{X}")
    except Exception as e:
        print(f"{R}[-] Error: {e}{X}")
    input(f"\n{C}Press Enter to return...{X}")

def run_paid():
    try:
        print(f"{Y}[*] Accessing PAID Tool (MHB.so)...{X}")
        import MHB # Aapki paid file
        
        # Paid file ke liye common functions
        if hasattr(MHB, 'main'):
            MHB.main()
        elif hasattr(MHB, 'login'):
            MHB.login()
        elif hasattr(MHB, 'menu'):
            MHB.menu()
        elif hasattr(MHB, 'start_cracking'):
            MHB.start_cracking()
        else:
            print(f"{Y}[!] Module loaded, but no main() found.{X}")
    except ImportError:
        print(f"{R}[-] Error: MHB.so nahi mili!{X}")
    except Exception as e:
        print(f"{R}[-] Error: {e}{X}")
    input(f"\n{C}Press Enter to return...{X}")

def main():
    while True:
        clear()
        logo()
        print(f"{W}[{G}01{W}] {S}RUN FREE TOOL{X}")
        print(f"{W}[{G}02{W}] {S}RUN PAID TOOL{X}")
        print(f"{W}[{R}00{W}] {S}EXIT{X}")
        print(f"{C}{S}" + "━"*50 + f"{X}")
        
        choice = input(f"{G}MHB >> {X}")

        if choice in ['1', '01']:
            run_free()
        elif choice in ['2', '02']:
            run_paid()
        elif choice in ['0', '00']:
            print(f"{Y}Khuda Hafiz!{X}")
            sys.exit()
        else:
            print(f"{R}Invalid Choice!{X}")
            time.sleep(1)

if __name__ == "__main__":
    main()
