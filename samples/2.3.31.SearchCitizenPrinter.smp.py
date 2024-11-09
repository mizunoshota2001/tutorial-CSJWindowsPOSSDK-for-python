import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


printer = ESCPOSPrinter()
print("Searching the printer...")
searchTime = 10  # 推奨値
responce, status = printer.SearchCitizenPrinter(
    config.CONTENT_TYPE, searchTime)
if status != ESCPOSConst.CMP_SUCCESS:
    raise Exception("Failed to search the printer.")
print("Successfully searched the printer.")
for item in responce:
    print("|----------------")
    print("|     IP Address: " + item.ipAddress)
    print("|    MAC Address: " + item.macAddress)
    print("| Device Address: " + item.bdAddress)
    print("|    Device Name: " + item.deviceName)
    print("|  Printer Model: " + item.printerModel)
