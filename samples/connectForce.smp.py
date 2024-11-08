import __relimport
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter
import time


def connectForce(connectType: int, addr: int, wait: int = 5) -> ESCPOSPrinter:
    printer = ESCPOSPrinter()
    while printer.Connect(connectType, addr) != ESCPOSConst.CMP_SUCCESS:
        printer.Disconnect()
        time.sleep(wait)
        print("Reconnecting...")
    return printer


printer: ESCPOSPrinter
printer = connectForce(
    ESCPOSConst.CMP_PORT_Bluetooth, "00:01:90:DF:C9:11")
print(printer.PrinterCheck())
printer.Disconnect()
