import __relimport
from pathlib import Path
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter, setDllPath

# 使用するSDKのライブラリを以下のURLからダウンロードしてください。
# https://www.citizen-systems.co.jp/cms/c-s/printer/download/sdk-print/CSJWindowsPOSSDK_V206J.zip
# ご自身でインストールしたライブラリのパスを指定してください。

__root = Path(__file__).parent.parent
__path = __root/"csjwindowspossdk"/"Library"/"CSJPOSLib.dll"
setDllPath(__path)
printer = ESCPOSPrinter()
print("Successfully initialized the printer.")
