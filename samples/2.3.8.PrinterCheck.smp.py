import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


printer = ESCPOSPrinter()
response = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if response != ESCPOSConst.CMP_SUCCESS:
    raise Exception("Failed to connect to the printer.")
print("Successfully connected to the printer.")

status = printer.Status()

if ESCPOSConst.CMP_STS_NORMAL == status:
    print("Normal status")
    status2 = printer.Status(ESCPOSConst.CMP_STS_PAPER_EMPTY)
    if ESCPOSConst.CMP_STS_PAPER_NEAREMPTY & status2 > 0:
        print("Paper is near empty")
else:
    if printer.ESCPOSConst.CMP_STS_COVER_OPEN & status > 0:
        print("Cover is open")
    if printer.ESCPOSConst.CMP_STS_PAPER_EMPTY & status > 0:
        print("Paper is empty")
    if printer.SearchESCPOSConst.CMP_STS_PRINTEROFF & status > 0:
        print("Printer is off")

status3 = printer.Status(ESCPOSConst.CMP_STS_DRAWER_LEVEL_H | ESCPOSConst.CMP_STS_PAPER_ONPRESENTER)
if ESCPOSConst.CMP_STS_DRAWER_LEVEL_H & status3 > 0:
    print("Status of pin 3 of drawer kick-out connector = H")
if ESCPOSConst.CMP_STS_PAPER_ONPRESENTER & status3 > 0:
    print("Paper is hold on presenter or paper exit sensor")


printer.Disconnect()