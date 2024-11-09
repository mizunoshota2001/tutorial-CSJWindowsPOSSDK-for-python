import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


printer = ESCPOSPrinter()
response = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if response == ESCPOSConst.CMP_SUCCESS:
    print("Successfully connected to the printer.")
printer.Disconnect()
