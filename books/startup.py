import sys  
from importlib import reload
from pprint import pp #allows you to print pretty-formatted data structures, such as lists and dictionaries.

try:
    from rich import pretty, traceback
except ModuleNotFoundError:
    pass
else:
    pretty.install()
    traceback.install(show_locals=False)

sys.ps1 = "py$ "
sys.ps2 = "py> "
