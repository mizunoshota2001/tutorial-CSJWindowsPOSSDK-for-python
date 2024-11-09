import __relimport
import time
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


def ConnectForce(printer: ESCPOSPrinter, connectType: int, addr: int, wait: int = 5, output: bool = False) -> ESCPOSPrinter:
    while printer.Connect(connectType, addr) != ESCPOSConst.CMP_SUCCESS:
        printer.Disconnect()
        time.sleep(wait)
        output and print("Reconnecting...")
    return printer


printer = ESCPOSPrinter()
printer = ConnectForce(printer, config.CONTENT_TYPE, config.ADDR)
print("Successfully connected to the printer.")
printer.Disconnect()
