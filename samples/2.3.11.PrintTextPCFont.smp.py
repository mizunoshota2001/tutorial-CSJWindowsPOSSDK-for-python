import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


printer = ESCPOSPrinter()
response = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if response != ESCPOSConst.CMP_SUCCESS:
    raise Exception("Failed to connect to the printer.")
print("Successfully connected to the printer.")

printer.PrintTextPCFont("Print PC font data.\n",
                        ESCPOSConst.CMP_ALIGNMENT_CENTER,
                        "Arial", 30,
                        ESCPOSConst.CMP_FNT_BOLD | ESCPOSConst.CMP_FNT_ITALIC,
                        50, 50)
#テキストを画像化して印刷するよ

printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)
printer.Disconnect()
