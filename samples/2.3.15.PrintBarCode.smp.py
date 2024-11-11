import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


printer = ESCPOSPrinter()
response = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if response != ESCPOSConst.CMP_SUCCESS:
    raise Exception("Failed to connect to the printer.")
print("Successfully connected to the printer.")

printer.PrintBarCode("123456789012",
                      ESCPOSConst.CMP_BCS_UPCA,
                      50, 2,
                      ESCPOSConst.CMP_ALIGNMENT_LEFT,
                      ESCPOSConst.CMP_HRI_TEXT_ABOVE
                      )

printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)
printer.Disconnect()
