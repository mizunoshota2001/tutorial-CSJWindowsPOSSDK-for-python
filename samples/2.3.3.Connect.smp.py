import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter

# たまに接続できない場合があります
# 確実に接続したい場合はConnectForce(/samples/2.3.3.ConnectForce.smp.py)を使ってください

printer = ESCPOSPrinter()
response = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if response == ESCPOSConst.CMP_SUCCESS:
    print("Successfully connected to the printer.")
printer.Disconnect()
