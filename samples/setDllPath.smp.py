import __relimport
from pathlib import Path
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter, setDllPath

__root = Path(__file__).parent.parent
__path = __root/"csjwindowspossdk"/"Library"/"CSJPOSLib.dll"
setDllPath(__path)
printer = ESCPOSPrinter()
print(printer.GetVersionCode())
