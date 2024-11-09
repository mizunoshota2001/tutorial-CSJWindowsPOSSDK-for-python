import __relimport
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter


printer = ESCPOSPrinter()
response = printer.Connect(config.CONTENT_TYPE, config.ADDR)
if response != ESCPOSConst.CMP_SUCCESS:
    raise Exception("Failed to connect to the printer.")
print("Successfully connected to the printer.")

name_size = 24  # 商品名サイズ
price_size = 7  # 価格サイズ

# １行目
printer.PrintPaddingText("Sandwich",
                         ESCPOSConst.CMP_FNT_DEFAULT,
                         ESCPOSConst.CMP_TXT_1WIDTH,
                         name_size,
                         ESCPOSConst.CMP_SIDE_RIGHT)
printer.PrintPaddingText("5.00",
                         ESCPOSConst.CMP_FNT_DEFAULT,
                         ESCPOSConst.CMP_TXT_1WIDTH,
                         price_size,
                         ESCPOSConst.CMP_SIDE_LEFT)
printer.PrintNormal("\n")

# ２行目
printer.PrintPaddingText("Hamburg steak",
                         ESCPOSConst.CMP_FNT_DEFAULT,
                         ESCPOSConst.CMP_TXT_1WIDTH,
                         name_size,
                         ESCPOSConst.CMP_SIDE_RIGHT)
printer.PrintPaddingText("12.00",
                         ESCPOSConst.CMP_FNT_DEFAULT,
                         ESCPOSConst.CMP_TXT_1WIDTH,
                         price_size,
                         ESCPOSConst.CMP_SIDE_LEFT)
printer.PrintNormal("\n")

# ３行目
printer.PrintPaddingText("Coffee",
                         ESCPOSConst.CMP_FNT_DEFAULT,
                         ESCPOSConst.CMP_TXT_1WIDTH,
                         name_size,
                         ESCPOSConst.CMP_SIDE_RIGHT)
printer.PrintPaddingText("2.00",
                         ESCPOSConst.CMP_FNT_DEFAULT,
                         ESCPOSConst.CMP_TXT_1WIDTH,
                         price_size,
                         ESCPOSConst.CMP_SIDE_LEFT)
printer.PrintNormal("\n")

printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)
printer.Disconnect()
