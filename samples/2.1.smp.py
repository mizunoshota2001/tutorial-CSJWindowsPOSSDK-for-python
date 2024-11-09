# プログラムマニュアル2.1 for python
import  config
import __relimport
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter
printer = ESCPOSPrinter()
printer.SetCommProperties(ESCPOSConst.CMP_COM_BAUDRATE_9600,
                          ESCPOSConst.CMP_COM_PARITY_NONE,
                          ESCPOSConst.CMP_COM_HANDSHAKE_DTRDSR)
result = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if (ESCPOSConst.CMP_SUCCESS == result):
    printer.SetEncoding("Shift_JIS")
    printer.TransactionPrint(ESCPOSConst.CMP_TP_TRANSACTION)
    printer.PrintText("Citizen_POS_sample1_CS\n\n",
                      ESCPOSConst.CMP_ALIGNMENT_CENTER, ESCPOSConst.CMP_FNT_DEFAULT,
                      ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
    printer.PrintText("- Sample Print 1 -\n",
                      ESCPOSConst.CMP_ALIGNMENT_CENTER, ESCPOSConst.CMP_FNT_DEFAULT,
                      ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_2HEIGHT)
    printer.PrintText("123456789012345678901234567890\n",
                      ESCPOSConst.CMP_ALIGNMENT_RIGHT, ESCPOSConst.CMP_FNT_DEFAULT,
                      ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
    printer.PrintQRCode("http://www.citizen-systems.co.jp/", 6,
                        ESCPOSConst.CMP_QRCODE_EC_LEVEL_L,
                        ESCPOSConst.CMP_ALIGNMENT_RIGHT)
    printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)
    result = printer.TransactionPrint(ESCPOSConst.CMP_TP_NORMAL)
    printer.Disconnect()
    if (ESCPOSConst.CMP_SUCCESS != result):
        print("Transaction Error :", result, "Citizen_POS_sample1")
else:
    print("Connect Error :", result, "Citizen_POS_sample1")
