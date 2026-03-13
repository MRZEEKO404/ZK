import os
import sys
import time

# Lush Colors for Termux
G = '\033[92m' ; R = '\033[91m' ; Y = '\033[93m' 
C = '\033[96m' ; W = '\033[97m' ; S = '\033[1m' ; X = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def logo():
    print(f"{C}{S}" + "━"*55 + f"{X}")
    print(f"{G}{S}  __  __  _    _  ____     _______  ____    ____   _      \n |  \/  || |  | ||  _ \   |__   __||  _ \  / __ \ | |     \n | \  / || |__| || |_) |     | |   | |_) || |  | || |     \n | |\/| ||  __  ||  _ <      | |   |  _ < | |  | || |     \n | |  | || |  | || |_) |     | |   | |_) || |__| || |____ \n |_|  |_||_|  |_||____/      |_|   |____/  \____/ |______|{X}")
    print(f"{Y}             >>> MHB OFFICIAL RUNNER v3.0 <<<{X}")
    print(f"{C}{S}" + "━"*55 + f"{X}")

def run_tool(module_name, is_paid=False):
    try:
        clear()
        logo()
        status = f"{Y}PREMIUM{X}" if is_paid else f"{G}FREE{X}"
        print(f"{W}[*] Running Module: {S}{module_name}{X}")
        print(f"{W}[*] Status: {status}")
        print(f"{G}[+] Initializing...{X}")
        time.sleep(1.2)
        
        # Importing the module (Both 'r' and 'mhb' are now small)
        mod = __import__(module_name)
        
        # Checking for entry functions (pak() for r, and others for mhb)
        if hasattr(mod, 'pak'):
            mod.pak()
        elif hasattr(mod, 'start_cracking'):
            mod.start_cracking()
        elif hasattr(mod, 'main'):
            mod.main()
        elif hasattr(mod, 'menu'):
            mod.menu()
        elif hasattr(mod, 'login'):
            mod.login()
        else:
            print(f"\n{R}[!] Error: No executable function found in {module_name}.so{X}")
            
    except ImportError:
        print(f"\n{R}[-] Error: {module_name}.so file nahi mili!{X}")
        print(f"{Y}[!] Check karein ke file ka naam '{module_name}' hi hai.{X}")
    except Exception as e:
        print(f"\n{R}[!] Crash Report: {e}{X}")
    
    input(f"\n{C}Press Enter to return to MHB Menu...{X}")

def main_menu():
    while True:
        clear()
        logo()
        # Option 1: r (Free)
        print(f"{W}[{G}01{W}] {S}RUN FREE TOOL   {C}(Module: r){X}")
        # Option 2: mhb (Paid)
        print(f"{W}[{G}02{W}] {S}{Y}RUN PAID TOOL   {G}(Module: mhb){X}")
        print(f"{W}[{R}00{W}] {S}EXIT TOOL{X}")
        print(f"{C}{S}" + "━"*55 + f"{X}")
        
        choice = input(f"{G}MHB >> {X}")

        if choice in ['1', '01']:
            run_tool("r", is_paid=False) # r is small
        elif choice in ['2', '02']:
            run_tool("mhb", is_paid=True) # mhb is small
        elif choice in ['0', '00']:
            print(f"\n{Y}[!] Closing... Allah Hafiz!{X}")
            sys.exit()
        else:
            print(f"{R}[!] Invalid selection!{X}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
