import __relimport
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter

printer = ESCPOSPrinter()
res, status = printer.SearchESCPOSPrinter(ESCPOSConst.CMP_PORT_COM, 10)
print(list(res), status)