import clr
from pathlib import Path
__path = Path(__file__).parent/"Library"/"CSJPOSLib.dll"
clr.AddReference(str(__path))
if True:
    from .cts281 import CTS281
