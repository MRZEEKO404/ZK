mport os
import sys
import time

# Colors (Lush Theme)
G = '\033[92m' ; R = '\033[91m' ; Y = '\033[93m' 
C = '\033[96m' ; W = '\033[97m' ; S = '\033[1m' ; X = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def logo():
    print(f"{C}{S}" + "━"*55 + f"{X}")
    print(f"{G}{S}  __  __  _    _  ____     _______  ____    ____   _      \n |  \/  || |  | ||  _ \   |__   __||  _ \  / __ \ | |     \n | \  / || |__| || |_) |     | |   | |_) || |  | || |     \n | |\/| ||  __  ||  _ <      | |   |  _ < | |  | || |     \n | |  | || |  | || |_) |     | |   | |_) || |__| || |____ \n |_|  |_||_|  |_||____/      |_|   |____/  \____/ |______|{X}")
    print(f"{Y}             >>> MHB OFFICIAL TOOL v1.0 <<<{X}")
    print(f"{C}{S}" + "━"*55 + f"{X}")

def execute_module(module_name):
    try:
        print(f"{G}[+] Loading {module_name}...{X}")
        # Module import kar rahe hain (.so extension ke baghair)
        mod = __import__(module_name)
        
        # Aapki list ke mutabiq functions check kar rahe hain
        if hasattr(mod, 'start_cracking'):
            mod.start_cracking()
        elif hasattr(mod, 'main'):
            mod.main()
        elif hasattr(mod, 'menu'):
            mod.menu()
        elif hasattr(mod, 'show_logo'):
            mod.show_logo()
        else:
            print(f"{R}[-] Entry function (start_cracking/main) nahi mila!{X}")
            
    except ImportError as e:
        print(f"\n{R}[-] Error: {module_name}.so r nahi mili!{X}")
        print(f"{Y}[!] Check karein ke r isi folder mein hai.{X}")
    except Exception as e:
        print(f"\n{R}[!] Error: {e}{X}")
    
    input(f"\n{C}Press Enter to return to MHB Menu...{X}")

def main_menu():
    while True:
        clear()
        logo()
        print(f"{W}[{G}01{W}] {S}RUN FREE TOOL   {C}(r: r){X}")
        print(f"{W}[{G}02{W}] {S}{Y}RUN PAID TOOL   {G}(r: MHB){X}")
        print(f"{W}[{R}00{W}] {S}EXIT{X}")
        print(f"{C}{S}" + "━"*55 + f"{X}")
        
        cmd = input(f"{G}MHB >> {X}")

        if cmd in ['1', '01']:
            execute_module("r")
        elif cmd in ['2', '02']:
            execute_module("MHB")
        elif cmd in ['0', '00']:
            print(f"{Y}Allah Hafiz!{X}")
            sys.exit()
        else:
            print(f"{R}Invalid Option!{X}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
