import __relimport
import time
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter

printer = ESCPOSPrinter()
printer.Connect(ESCPOSConst.CMP_PORT_Bluetooth, "00:01:90:DF:C9:11")
time.sleep(3)
printer.Disconnect()
