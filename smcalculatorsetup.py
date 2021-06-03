import sys
from cx_Freeze import *

includefiles=['cal.ico','logo.ico']
base = None
if sys.platform == "win32":
    base = "Win32GUI"


shortcut_table = [
    ("DesktopShortcut",   #Shortcut
    "DesktopFolder",   #Directory
    "My Calculator",  #Name
    "TARGETDIR",  #Component
    "[TARGETDIR]\smcalculator.exe",  #Target
    None,  #Argument
    None,  #Description
    None,  #Hotkey
    None,  #Icon
    None,  #IconIndex
    None,  #ShowCmd
    "TARGETDIR",  #wkDir

    )
]
msi_data ={"Shortcut": shortcut_table}


#Change some Default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="My Calculator",
    author="Pushpendra Gaur",
    name="My Calculator",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="smcalculator.py",
            base=base,
            icon='logo.ico',
        )
    ]
)