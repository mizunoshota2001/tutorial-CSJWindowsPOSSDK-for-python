from pathlib import Path
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter, setDllPath

# #ライブラリのパスを設定
# __path = Path(__file__).parent/"Library"/"CSJPOSLib.dll"
# setDllPath(__path)
printer = ESCPOSPrinter()
print(printer.GetVersionCode())
