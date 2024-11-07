from pathlib import Path
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter, setDllPath
__path = Path(__file__).parent/"Library"/"CSJPOSLib.dll"
setDllPath(__path)
printer = ESCPOSPrinter()
print(printer.GetVersionCode())
