'''
！学祭で実際に使用していたコードであり、SDKのサンプルコードではないです！
pip install pyserial Pillow pytz
COMは環境で書き換えてください
'''

import serial
from PIL import Image
import logging
from datetime import datetime
import pytz
from pathlib import Path

__assets = Path(__file__).parent.parent/"assets"
BITMAP_PATH = str(__assets/"logoimg.bmp")

logger = logging.getLogger(__name__)

class Printer:
    def __init__(self, port='COM4', baudrate=38400):
        self.port = port
        self.baudrate = baudrate
        self.logo = self.create_image_buffer("BITMAP_PATH")

    # 画像データをバッファに変換
    def create_image_buffer(self, image_path):
            """
            画像を1ビットモノクロに変換し、ラスタ形式のバッファを作成する。
            """
            img = Image.open(image_path).convert('1')  # モノクロ変換 (1ビット)
            width, height = img.size

            # 横幅を8で割り切れるように調整
            if width % 8 != 0:
                new_width = (width + 7) // 8 * 8
                img = img.resize((new_width, height))
                width = new_width

            # ビットマップデータの生成
            bitmap_data = bytearray()
            for y in range(height):
                for x in range(0, width, 8):
                    byte = 0
                    for bit in range(8):
                        if x + bit < width and img.getpixel((x + bit, y)) == 0:
                            byte |= (1 << (7 - bit))
                    bitmap_data.append(byte)

            # xL, xH, yL, yHを計算
            xL = width // 8 % 256
            xH = width // 8 // 256
            yL = height % 256
            yH = height // 256

            # バッファ作成 (GS v 0 コマンド)
            logo = bytearray(b'\x1D\x76\x30\x00' + bytes([xL, xH, yL, yH]))
            logo.extend(bitmap_data)
            return logo
    
    def print_receipt(self, order_id, orderL, totalL, total, payment, note, menuL, order_date):
        try:
            ser = serial.Serial(self.port, self.baudrate, timeout=0.1)
            ser.write(b'\x1B\x40')  # ESC @ (プリンタ初期化)
            ser.write(self.logo)  # 画像データの送信
            
            # 店舗名、日付
            buffer = b'\x1D\x21\x00' + "福桔祭店    {}\n".format(order_date.strftime("%Y/%m/%d %H:%M:%S")).encode("shift_jis") + b'\x1D\x21\x10'
            
            # 罫線
            buffer += b'\x1B\x2D\x01' + "                \n".encode("shift_jis") + b'\x1B\x2D\x00'
            
            # 商品名、単価、数量、合計
            # 字寄せ等を強引に行う
            for i in range(len(menuL)):
                if orderL[i]['quantity'] > 0:
                    buffer += "{0}{1}@{2} {3}ｺ\n".format(menuL[i]['name'], " " * (6 - len(menuL[i]['name'])), menuL[i]['price'], orderL[i]['quantity']).encode("shift_jis")
                    buffer += "{0}￥{1:,}\n".format(
                                    " " * (13 - (len(str(totalL[i])) if len(str(totalL[i])) < 4 else (len(str(totalL[i])) + 1))),
                                    totalL[i]).encode("shift_jis")
            if note: # 注文メモ
                buffer += b'\x1D\x21\x00' + "\n{}\n".format(note).encode("shift_jis") + b'\x1D\x21\x10'
            
            buffer += b'\x1B\x2D\x01' + "                \n".encode("shift_jis") + b'\x1B\x2D\x00'
            
            # 合計、お預り、おつり
            buffer += "合計{0}￥{1:,}\n".format(
                            " " * (9 - (len(str(total)) if len(str(total)) < 4 else (len(str(total)) + 1))),
                            total).encode("shift_jis")
            
            buffer += "お預り{0}￥{1:,}\n".format(
                            " " * (7 - (len(str(payment)) if len(str(payment)) < 4 else (len(str(payment)) + 1))),
                            payment).encode("shift_jis")
            
            buffer += "おつり{0}￥{1:,}\n".format(
                            " " * (7 - (len(str(payment - total)) if len(str(payment - total)) < 4 else (len(str(payment - total)) + 1))),
                            (payment - total)).encode("shift_jis")
            
            buffer += b'\x1D\x21\x00' + "\n          Thank you!".encode("shift_jis")
            
            # 注文番号の表示
            # フォントサイズの変更、反転などのコマンド
            buffer += b'\x1D\x21\x56' + b'\x1D\x42\x01' + "\n {} \n".format(order_id).encode("shift_jis") + b'\x1D\x42\x00'
            
            # カットコマンド
            buffer += b'\x1D\x56\x42\x2D'

            # プリンターに送信
            ser.write(buffer)
            
            ser.close()
        except Exception as e:
            logger.error(f"Error printing receipt: {e}")
            
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

# Initialize Printer instance and run the test
printer = Printer(port='COM4', baudrate=9600)
printer.print_receipt(order_id, orderL, totalL, total, payment, note, menuL, order_date)