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

printer.PrintBitmap(BITMAP_PATH,
                    ESCPOSConst.CMP_BM_ASIS,
                    ESCPOSConst.CMP_ALIGNMENT_CENTER,
                    ESCPOSConst.CMP_BM_MODE_HT_DITHER)

printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)
printer.Disconnect()
