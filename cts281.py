import csjposlib
from com.citizen.sdk import ESCPOSPrinter, ESCPOSConst
__all__ = ["CTS281"]


class CTS281:
    def __init__(self, addr, test_print=False) -> None:
        self.addr = addr
        self.const = ESCPOSConst
        self.prt = ESCPOSPrinter()
        self.prt.SetCommProperties(
            self.const.CMP_COM_BAUDRATE_9600,
            self.const.CMP_COM_PARITY_NONE,
            self.const.CMP_COM_HANDSHAKE_DTRDSR
        )
        if test_print:
            self.__test_print()

    def __get_kwargs(self, locals: dict):
        return {k: v for k, v in locals.items() if k != "self" and v is not None}

    def __test_print(self):
        self.connect()
        self.prt.SetEncoding("Shift_JIS")
        self.prt.TransactionPrint(self.const.CMP_TP_TRANSACTION)
        self.prt.PrintText("CMP_E_CONNECTED",
                               self.const.CMP_ALIGNMENT_CENTER,
                               self.const.CMP_FNT_DEFAULT,
                               self.const.CMP_TXT_2WIDTH | self.const.CMP_TXT_4HEIGHT)
        self.prt.CutPaper(self.const.CMP_CUT_PARTIAL_PREFEED)
        self.prt.TransactionPrint(self.const.CMP_TP_NORMAL)
        self.disconnect()

    def is_alive(self):
        return bool(self.const.CMP_SUCCESS == self.prt.PrinterCheck())

    def connect(self):
        if self.is_alive():
            return
        print(self.prt.Connect(self.const.CMP_PORT_USB, self.addr))

    def disconnect(self):
        if not self.is_alive():
            return
        self.prt.Disconnect()


if __name__ == "__main__":
    ct = CTS281("00:01:90:DF:CD:8E", True)
