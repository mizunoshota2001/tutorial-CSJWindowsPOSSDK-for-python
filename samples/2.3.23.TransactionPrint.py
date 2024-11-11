import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter
from pathlib import Path

__assets = Path(__file__).parent.parent/"assets"
BITMAP_PATH = str(__assets/"logoimg.bmp")

printer = ESCPOSPrinter()
response = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if response != ESCPOSConst.CMP_SUCCESS:
    raise Exception("Failed to connect to the printer.")
print("Successfully connected to the printer.")

#printer.SetNVBitmap(1, BITMAP_PATH, ESCPOSConst.CMP_BM_ASIS)

printer.TransactionPrint(ESCPOSConst.CMP_TP_TRANSACTION)
#printer.PrintNVBitmap(1)
printer.PrintBarCode("123456789012", ESCPOSConst.CMP_BCS_UPCA, 50, 2,
ESCPOSConst.CMP_ALIGNMENT_LEFT, ESCPOSConst.CMP_HRI_TEXT_ABOVE)
printer.PrintText("Line 1\n", ESCPOSConst.CMP_ALIGNMENT_LEFT,
ESCPOSConst.CMP_FNT_DEFAULT, ESCPOSConst.CMP_TXT_1WIDTH)
printer.PrintText("Line 2\n", ESCPOSConst.CMP_ALIGNMENT_LEFT,
ESCPOSConst.CMP_FNT_DEFAULT, ESCPOSConst.CMP_TXT_1WIDTH)
printer.PrintText("Line 3\n", ESCPOSConst.CMP_ALIGNMENT_LEFT,
ESCPOSConst.CMP_FNT_DEFAULT, ESCPOSConst.CMP_TXT_1WIDTH)
printer.PrintBarCode("123456789012", ESCPOSConst.CMP_BCS_UPCA, 50, 2,
ESCPOSConst.CMP_ALIGNMENT_LEFT, ESCPOSConst.CMP_HRI_TEXT_ABOVE)
#printer.PrintNVBitmap(1)
printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)
printer.TransactionPrint(ESCPOSConst.CMP_TP_NORMAL)

printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)
printer.Disconnect()
