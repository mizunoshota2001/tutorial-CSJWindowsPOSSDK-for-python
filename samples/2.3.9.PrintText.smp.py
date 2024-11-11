import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


printer = ESCPOSPrinter()
response = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if response != ESCPOSConst.CMP_SUCCESS:
    raise Exception("Failed to connect to the printer.")
print("Successfully connected to the printer.")

printer.PrintText("Print text data.\n",
                    ESCPOSConst.CMP_ALIGNMENT_CENTER,
                    ESCPOSConst.CMP_FNT_BOLD | ESCPOSConst.CMP_FNT_UNDERLINE,
                    ESCPOSConst.CMP_TXT_2WIDTH | ESCPOSConst.CMP_TXT_2HEIGHT)

printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)
printer.Disconnect()
