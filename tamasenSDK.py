from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter
from datetime import datetime
import pytz
import logging
import time

logger = logging.getLogger(__name__)

def connectForce(connectType: int, addr: str, wait: int = 5) -> ESCPOSPrinter:
    printer = ESCPOSPrinter()
    while printer.Connect(connectType, addr) != ESCPOSConst.CMP_SUCCESS:
        printer.Disconnect()
        time.sleep(wait)
        print("Reconnecting...")
    return printer

class Printer:
    def __init__(self, port_type=ESCPOSConst.CMP_PORT_Bluetooth, address="00:01:90:df:cd:aa"):
        self.port_type = port_type
        self.address = address
        self.printer = connectForce(self.port_type, self.address)
        self.printer.SetEncoding("Shift_JIS")

    def print_receipt(self, order_id, orderL, totalL, total, payment, note, menuL, order_date):
        try:
            self.printer.TransactionPrint(ESCPOSConst.CMP_TP_TRANSACTION)

            # Print logo image
            self.printer.PrintBitmap("logoimg.bmp",
                ESCPOSConst.CMP_ALIGNMENT_CENTER)
            
            self.printer.PrintText(f"テスト店    {order_date.strftime('%Y/%m/%d %H:%M:%S')}\n",
                ESCPOSConst.CMP_ALIGNMENT_LEFT,
                ESCPOSConst.CMP_FNT_DEFAULT,
                ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            self.printer.PrintText("                \n",
                ESCPOSConst.CMP_ALIGNMENT_CENTER,
                ESCPOSConst.CMP_FNT_UNDERLINE | ESCPOSConst.CMP_FNT_BOLD,
                ESCPOSConst.CMP_TXT_2WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            
            for i in range(len(menuL)):
                if orderL[i]['quantity'] > 0:
                    self.printer.PrintPaddingText(f"{menuL[i]['name']}",
                        ESCPOSConst.CMP_FNT_DEFAULT,
                        ESCPOSConst.CMP_TXT_2WIDTH,
                        6, ESCPOSConst.CMP_SIDE_RIGHT)
                    self.printer.PrintPaddingText(f"@{menuL[i]['price']:,}",
                        ESCPOSConst.CMP_FNT_DEFAULT,
                        ESCPOSConst.CMP_TXT_2WIDTH,
                        5, ESCPOSConst.CMP_SIDE_RIGHT)
                    self.printer.PrintPaddingText(f"{orderL[i]['quantity']}ｺ\n",
                        ESCPOSConst.CMP_FNT_DEFAULT,
                        ESCPOSConst.CMP_TXT_2WIDTH,
                        4, ESCPOSConst.CMP_SIDE_LEFT)
                    self.printer.PrintPaddingText(f"¥{totalL[i]:,}\n",
                        ESCPOSConst.CMP_FNT_DEFAULT,
                        ESCPOSConst.CMP_TXT_2WIDTH,
                        16, ESCPOSConst.CMP_SIDE_LEFT)
                    #RIGHTにpaddingするときは、改行文字は別で入れる
                    #名前: 6文字, 単価: 3ｹﾀ(コンマ付けするため), 個数: 2ｹﾀ, total: 実質無制限
                    #たません用の設定。文字を細かくして対応しよう
            
            if note:
                self.printer.PrintText(f"{note}\n",
                    ESCPOSConst.CMP_ALIGNMENT_LEFT,
                    ESCPOSConst.CMP_FNT_DEFAULT,
                    ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            
            self.printer.PrintText("                \n",
                ESCPOSConst.CMP_ALIGNMENT_CENTER,
                ESCPOSConst.CMP_FNT_UNDERLINE | ESCPOSConst.CMP_FNT_BOLD,
                ESCPOSConst.CMP_TXT_2WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            
            self.printer.PrintText(f"合  計",
                ESCPOSConst.CMP_ALIGNMENT_LEFT,
                ESCPOSConst.CMP_FNT_DEFAULT,
                ESCPOSConst.CMP_TXT_2WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            self.printer.PrintPaddingText(f"¥{total:,}\n",
                ESCPOSConst.CMP_FNT_DEFAULT,
                ESCPOSConst.CMP_TXT_2WIDTH,
                10, ESCPOSConst.CMP_SIDE_LEFT)
            
            self.printer.PrintText(f"お預り",
                ESCPOSConst.CMP_ALIGNMENT_LEFT,
                ESCPOSConst.CMP_FNT_DEFAULT,
                ESCPOSConst.CMP_TXT_2WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            self.printer.PrintPaddingText(f"¥{payment:,}\n",
                ESCPOSConst.CMP_FNT_DEFAULT,
                ESCPOSConst.CMP_TXT_2WIDTH,
                10, ESCPOSConst.CMP_SIDE_LEFT)
            
            self.printer.PrintText(f"おつり",
                ESCPOSConst.CMP_ALIGNMENT_LEFT,
                ESCPOSConst.CMP_FNT_DEFAULT,
                ESCPOSConst.CMP_TXT_2WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            self.printer.PrintPaddingText(f"¥{payment - total:,}\n",
                ESCPOSConst.CMP_FNT_DEFAULT,
                ESCPOSConst.CMP_TXT_2WIDTH,
                10, ESCPOSConst.CMP_SIDE_LEFT)
            
            self.printer.PrintText("\nアンケートはこちら!",
                ESCPOSConst.CMP_ALIGNMENT_LEFT,
                ESCPOSConst.CMP_FNT_DEFAULT,
                ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            
            self.printer.PrintQRCode("https://www.fukuchiyama.ac.jp/", 4,
                        ESCPOSConst.CMP_QRCODE_EC_LEVEL_Q,
                        250)
            
            self.printer.PrintTextPCFont("\nThank you!\n",
                ESCPOSConst.CMP_ALIGNMENT_CENTER,
                "Arial", 10, ESCPOSConst.CMP_FNT_ITALIC,
                100, 100)
            
            self.printer.PrintText(f" {order_id} \n",
                ESCPOSConst.CMP_ALIGNMENT_CENTER,
                ESCPOSConst.CMP_FNT_REVERSE,
                ESCPOSConst.CMP_TXT_6WIDTH | ESCPOSConst.CMP_TXT_7HEIGHT)
            
            """ self.printer.PrintTextPCFont(f" {order_id} \n",
                ESCPOSConst.CMP_ALIGNMENT_CENTER,
                "HGSSoeiKakugothicUB", 12, ESCPOSConst.CMP_FNT_REVERSE,
                400,600) """
            
            self.printer.PrintText("\n",
                ESCPOSConst.CMP_ALIGNMENT_CENTER,
                ESCPOSConst.CMP_FNT_DEFAULT,
                ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            
            self.printer.PrintBarCode("123456789012",
                ESCPOSConst.CMP_BCS_EAN13,
                50,3,
                ESCPOSConst.CMP_ALIGNMENT_CENTER,
                ESCPOSConst.CMP_HRI_TEXT_BELOW)
            
            # Cut the paper
            self.printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)

            # Finalize transaction
            result = self.printer.TransactionPrint(ESCPOSConst.CMP_TP_NORMAL)
            if result != ESCPOSConst.CMP_SUCCESS:
                logger.error(f"Transaction Error : {result}")
                self.printer.Disconnect()

        except Exception as e:
            logger.error(f"Error printing receipt: {e}")
            self.printer.Disconnect()
        finally:
            # Disconnect the printer
            self.printer.Disconnect()

# Example usage
order_id = 999
orderL = [{'product_id': 1, 'quantity': 10}, {'product_id': 2, 'quantity': 2}, {'product_id': 3, 'quantity': 1}]
totalL = [2500, 700, 0]
total = 3200
payment = 10000
note = "testだよ!"
menuL = [{'name': 'NOR', 'price': 250}, {'name': 'GAME', 'price': 350}, {'name': 'SMILE', 'price': 0}]
order_date = datetime.now(pytz.timezone('Asia/Tokyo'))

# Initialize Printer instance and run the test
printer = Printer(port_type=ESCPOSConst.CMP_PORT_Bluetooth, address="00:01:90:df:cd:aa")
printer.print_receipt(order_id, orderL, totalL, total, payment, note, menuL, order_date)
