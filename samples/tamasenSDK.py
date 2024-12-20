import __relimport
from datetime import datetime
import pytz
import time
import config
from csjwindowspossdk import ESCPOSConst, ESCPOSPrinter
from pathlib import Path

__assets = Path(__file__).parent.parent/"assets"
BITMAP_PATH = str(__assets/"logoimg.bmp")


class Printer:

    def __init__(self, port_type=config.CONTENT_TYPE, address=config.ADDR):
        self.port_type = port_type
        self.address = address

    def connect_force(self, printer: ESCPOSPrinter, connectType: int, addr: int, wait: int = 5, output: bool = False) -> ESCPOSPrinter:
        while printer.Connect(connectType, addr) != ESCPOSConst.CMP_SUCCESS:
            printer.Disconnect()
            time.sleep(wait)
            output and print("Reconnecting...")
        return printer

    def print_receipt(self, order_id, orderL, totalL, total, payment, note, menuL, order_date):
        self.printer = ESCPOSPrinter()
        self.printer = self.connect_force(
            self.printer, self.port_type, self.address, 5, True)
        print("Printing receipt...")
        self.printer.TransactionPrint(ESCPOSConst.CMP_TP_TRANSACTION)

        # ロゴの印刷
        self.printer.PrintBitmap(BITMAP_PATH,
                                 ESCPOSConst.CMP_ALIGNMENT_CENTER)

        # 日付と店舗名
        self.printer.PrintText(f"テスト店    {order_date.strftime('%Y/%m/%d %H:%M:%S')}\n",
                               ESCPOSConst.CMP_ALIGNMENT_LEFT,
                               ESCPOSConst.CMP_FNT_DEFAULT,
                               ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
        self.printer.PrintText("                \n",
                               ESCPOSConst.CMP_ALIGNMENT_CENTER,
                               ESCPOSConst.CMP_FNT_UNDERLINE | ESCPOSConst.CMP_FNT_BOLD,
                               ESCPOSConst.CMP_TXT_2WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)

        # 購入された商品の表示
        # 上から、名前、単価、個数、合計
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
                '''
                RIGHTにpaddingするときは、改行文字は別で入れる
                名前: 6文字, 単価: 3ｹﾀ(コンマ付けするため), 個数: 2ｹﾀ, total: 実質無制限
                たません用の設定。文字を細かくして対応しよう
                '''

        # noteの表示
        # POSでは、卵抜き、などの表示がある場合に使用
        if note:
            self.printer.PrintText(f"{note}\n",
                                   ESCPOSConst.CMP_ALIGNMENT_LEFT,
                                   ESCPOSConst.CMP_FNT_DEFAULT,
                                   ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)

        # 区切り線(アンダーバー)
        self.printer.PrintText("                \n",
                               ESCPOSConst.CMP_ALIGNMENT_CENTER,
                               ESCPOSConst.CMP_FNT_UNDERLINE | ESCPOSConst.CMP_FNT_BOLD,
                               ESCPOSConst.CMP_TXT_2WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)

        # 合計、お預り、おつりの表示
        for i in [["合  計", total], ["お預り", payment], ["おつり", payment - total]]:
            self.printer.PrintText(f"{i[0]}",
                                   ESCPOSConst.CMP_ALIGNMENT_LEFT,
                                   ESCPOSConst.CMP_FNT_DEFAULT,
                                   ESCPOSConst.CMP_TXT_2WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)
            self.printer.PrintPaddingText(f"¥{i[1]:,}\n",
                                          ESCPOSConst.CMP_FNT_DEFAULT,
                                          ESCPOSConst.CMP_TXT_2WIDTH,
                                          10, ESCPOSConst.CMP_SIDE_LEFT)
        # 合計お預かりおつりの表示。内消費税等の記入はなし

        self.printer.PrintText("\n大学HPはこちら!",
                               ESCPOSConst.CMP_ALIGNMENT_LEFT,
                               ESCPOSConst.CMP_FNT_DEFAULT,
                               ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)

        # QRコードの印刷
        self.printer.PrintQRCode("https://www.fukuchiyama.ac.jp/", 4,
                                 ESCPOSConst.CMP_QRCODE_EC_LEVEL_Q,
                                 250)

        # レシートの最後に表示する文字
        # PCフォントを使用
        self.printer.PrintTextPCFont("\nThank you!\n",
                                     ESCPOSConst.CMP_ALIGNMENT_CENTER,
                                     "Arial", 10, ESCPOSConst.CMP_FNT_ITALIC,
                                     100, 100)

        # 注文番号の表示
        self.printer.PrintText(f" {order_id} \n",
                               ESCPOSConst.CMP_ALIGNMENT_CENTER,
                               ESCPOSConst.CMP_FNT_REVERSE,
                               ESCPOSConst.CMP_TXT_6WIDTH | ESCPOSConst.CMP_TXT_7HEIGHT)

        """
        self.printer.PrintTextPCFont(f" {order_id} \n",
            ESCPOSConst.CMP_ALIGNMENT_CENTER,
            "HGSSoeiKakugothicUB", 12, ESCPOSConst.CMP_FNT_REVERSE,
            400,600)
        # TrueTypeフォントを使用。ぬるぬる
        """

        self.printer.PrintText("\n",
                               ESCPOSConst.CMP_ALIGNMENT_CENTER,
                               ESCPOSConst.CMP_FNT_DEFAULT,
                               ESCPOSConst.CMP_TXT_1WIDTH | ESCPOSConst.CMP_TXT_1HEIGHT)

        """
        self.printer.PrintBarCode(f"20{order_id:04}{order_date:%y%m%d}",
            ESCPOSConst.CMP_BCS_JAN13,
            50,3,
            ESCPOSConst.CMP_ALIGNMENT_CENTER,
            ESCPOSConst.CMP_HRI_TEXT_BELOW)
        '''
        JAN13
        20(インストアを示すらしい)
        order_id 4桁 (システム3桁なので、1桁目は0)
        order_date 6桁 (yymmdd)
        チェックデジット
        ''' 
        """

        # バーコードの印刷
        self.printer.PrintBarCode(f"{order_id:04}{order_date:%y%m%d%H}",
                                  ESCPOSConst.CMP_BCS_JAN13,
                                  50, 3,
                                  ESCPOSConst.CMP_ALIGNMENT_CENTER,
                                  ESCPOSConst.CMP_HRI_TEXT_BELOW)
        '''
        JAN13
        order_id 4桁 (システム3桁なので、1桁目は0)
        order_date 8桁 (yymmddhh)
        チェックデジット
        '''

        self.printer.CutPaper(ESCPOSConst.CMP_CUT_PARTIAL_PREFEED)

        result = self.printer.TransactionPrint(ESCPOSConst.CMP_TP_NORMAL)

        if result != ESCPOSConst.CMP_SUCCESS:
            print(f"Transaction Error : {result}")
        else:
            print("Printed receipt successfully.")

        self.printer.Disconnect()


# sample data
# 設計がばがばのPOSシステムからそのまま引っ張ってるのでごっちゃなのは許して…
order_id = 999
orderL = [{'product_id': 1, 'quantity': 10}, {
    'product_id': 3, 'quantity': 2}, {'product_id': 4, 'quantity': 1}]
totalL = [2500, 700, 0]
total = 3200
payment = 10000
note = "testだよ!"
menuL = [{'name': 'NOR', 'price': 250}, {
    'name': 'GAME', 'price': 350}, {'name': 'SMILE', 'price': 0}]
order_date = datetime.now(pytz.timezone('Asia/Tokyo'))

printer = Printer(port_type=config.CONTENT_TYPE, address=config.ADDR)
printer.print_receipt(order_id, orderL, totalL, total,
                      payment, note, menuL, order_date)
