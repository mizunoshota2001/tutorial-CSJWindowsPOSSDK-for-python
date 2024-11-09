import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


printer = ESCPOSPrinter()

print("Searching the printer...")
searchTime = 10  # 推奨値
responce, status = printer.SearchESCPOSPrinter(config.CONTENT_TYPE, searchTime)
if status != ESCPOSConst.CMP_SUCCESS:
    raise Exception("Failed to search the printer.")
print("Successfully searched the printer.")
print("Printer's address:", responce)
