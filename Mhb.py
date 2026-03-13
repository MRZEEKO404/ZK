import os
import sys
import time

# Colors
G = '\033[92m' ; R = '\033[91m' ; Y = '\033[93m' 
C = '\033[96m' ; W = '\033[97m' ; S = '\033[1m' ; X = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def show_logo():
    print(f"{C}{S}" + "━"*55 + f"{X}")
    print(f"{G}{S}  __  __  _    _  ____     _______  ____    ____   _      \n |  \/  || |  | ||  _ \   |__   __||  _ \  / __ \ | |     \n | \  / || |__| || |_) |     | |   | |_) || |  | || |     \n | |\/| ||  __  ||  _ <      | |   |  _ < | |  | || |     \n | |  | || |  | || |_) |     | |   | |_) || |__| || |____ \n |_|  |_||_|  |_||____/      |_|   |____/  \____/ |______|{X}")
    print(f"{Y}             >>> MHB OFFICIAL RUNNER v6.0 <<<{X}")
    print(f"{C}{S}" + "━"*55 + f"{X}")

def join_groups_once():
    # Hidden file path (SDCard storage permission honi chahiye)
    check_path = "/sdcard/.mhb_joined.txt"
    
    if not os.path.exists(check_path):
        group1 = "https://chat.whatsapp.com/HdppaiQyFtZ1AwiOzc5iEe?mode=gi_t"
        group2 = "https://chat.whatsapp.com/FtIOPca2aXt43eHIUnTRtv?mode=hqctcla"
        
        clear()
        show_logo()
        print(f'{Y} [!] First Time User Detected...{X}')
        print(f'{G} [➔] Joining Group 1...{X}')
        os.system(f'termux-open-url "{group1}"')
        time.sleep(4)
        
        print(f'{G} [➔] Joining Group 2...{X}')
        os.system(f'termux-open-url "{group2}"')
        time.sleep(2)
        
        # Ek nishani bana di ke join ho gaya
        try:
            with open(check_path, "w") as f:
                f.write("done")
            print(f"\n{G} [✔] Thanks For Joining! Opening Menu...{X}")
        except:
            # Agar storage permission na ho to current folder mein file bana do
            with open("/sdcard/Android/.mhb_joined.txt", "w") as f:
                f.write("done")
        
        time.sleep(2)

def run_tool(module_name, is_paid=False):
    try:
        clear()
        show_logo()
        status = f"{Y}PREMIUM{X}" if is_paid else f"{G}FREE{X}"
        print(f"{W}[*] Loading: {S}{module_name}{X} | Status: {status}")
        time.sleep(1.2)
        
        # Importing compiled .so module
        mod = __import__(module_name)
        
        # Function Calls
        if hasattr(mod, 'pak'): mod.pak()
        elif hasattr(mod, 'start_cracking'): mod.start_cracking()
        elif hasattr(mod, 'main'): mod.main()
        elif hasattr(mod, 'menu'): mod.menu()
        else:
            print(f"\n{R}[!] Entry point not found!{X}")
            
    except ImportError:
        print(f"\n{R}[-] Error: {module_name}.so not found!{X}")
    except Exception as e:
        print(f"\n{R}[!] Crash: {e}{X}")
    
    input(f"\n{C}Press Enter to return...{X}")

def main_menu():
    while True:
        clear()
        show_logo()
        print(f"{W}[{G}01{W}] {S}RUN FREE TOOL   {C}(Module: Random){X}")
        print(f"{W}[{G}02{W}] {S}{Y}RUN PAID TOOL   {G}(Module: OLD){X}")
        print(f"{W}[{R}00{W}] {S}EXIT TOOL{X}")
        print(f"{C}{S}" + "━"*55 + f"{X}")
        
        choice = input(f"{G}MHB >> {X}")

        if choice in ['1', '01']:
            run_tool("r", is_paid=False)
        elif choice in ['2', '02']:
            run_tool("mhb", is_paid=True)
        elif choice in ['0', '00']:
            print(f"\n{Y}[!] Khuda Hafiz!{X}")
            sys.exit()

if __name__ == "__main__":
    # Pehle check karega ke user ne group join kiya hai ya nahi
    join_groups_once()
    # Phir menu khulega
    main_menu()
