import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


printer = ESCPOSPrinter()
response = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if response != ESCPOSConst.CMP_SUCCESS:
    raise Exception("Failed to connect to the printer.")
print("Successfully connected to the printer.")
printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)
printer.Disconnect()
