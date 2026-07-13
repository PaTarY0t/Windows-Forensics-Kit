#------------------------------------------#
#       The Code By PaTaRY0T               #
#        Since 2006 - 2026                 #
#                                          #
#------------------------------------------#


import ctypes
import winreg

ROOT = winreg.HKEY_LOCAL_MACHINE
PATH = r"SYSTEM\ControlSet001\Enum\USBSTOR"
# If Not Working
# Change this ControlSet001 to CurrentControlSet


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def print_key(key, PaTaRY0t=0):

    try:

        i= 0
        while True:
            name, value, typ = winreg.EnumValue(key, i)
            print("   " * PaTaRY0t + f"[VALUE] {name} = {value}")
            i += 1
    except OSError:
        pass



    try:
        i = 0
        while True:
            subkey_name = winreg.EnumKey(key, i)

            i += 1
            print("   " * PaTaRY0t + f"[KEY] {subkey_name}")
            
            with winreg.OpenKey(key, subkey_name) as subkey:
                print_key(subkey, PaTaRY0t + 1)


                
    except OSError:
         pass

        
try:

    if is_admin():
        print("RUN IS Administrator")
    else:
        print("RUN IS NOT Administrator")

    with winreg.OpenKey(ROOT, PATH) as key:
        print(f"Registry path: HKLM\\{PATH}\n")
        print_key(key)

except PermissionError:
    print("Access denied - Run Python as Administrator")
    

except FileNotFoundError:
    print("Registry path not found")