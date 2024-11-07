import clr
from pathlib import Path
dllPath = Path(__file__).parent/"Library"/"CSJPOSLib.dll"


def setDllPath(path: str):
    global dllPath
    dllPath = path


class ESCPOSPrinter:
    def __init__(self):
        clr.AddReference(str(dllPath))
        import com.citizen.sdk
        self.__printer = com.citizen.sdk.ESCPOSPrinter()

    def Connect(self, connectType: int, addr: int, Port: int = None, Timeout: int = None):
        args = [connectType, addr]
        Port and args.append(Port)
        Timeout and args.append(Timeout)
        return self.__printer.Connect(*args)

    def Disconnect(self):
        return self.__printer.Disconnect()

    def SetCommProperties(self, baudRate: int, parity: int, handShake: int):
        return self.__printer.SetCommProperties(baudRate, parity, handShake)

    def SetEncoding(self, charset: str):
        return self.__printer.SetEncoding(charset)

    def PrinterCheck(self):
        return self.__printer.PrinterCheck()

    def Status(self, type: int = None):
        args = [type] if type else []
        return self.__printer.Status(*args)

    def PrintText(self, data: str, alignment: int, attribute: int, textSize: int):
        return self.__printer.PrintText(data, alignment, attribute, textSize)

    def PrintPaddingText(self, data: str, attribute: int, textSize: int, length: int, side: int):
        return self.__printer.PrintPaddingText(data, attribute, textSize, length, side)

    def PrintTextPCFont(self, data: str, alignment: int, fntName: str, point: int, style: int, hRatio: int, vRatio: int):
        return self.__printer.PrintTextPCFont(data, alignment, fntName, point, style, hRatio, vRatio)

    def PrintBitmap(self, filePath, alignment):
        raise Exception("Not implemented")

    def SetNVBitmap(self, filePath):
        raise Exception("Not implemented")

    def PrintNVBitmap(self, alignment):
        raise Exception("Not implemented")

    def PrintBarCode(self, data: str, symbology: int, height: int, width: int, alignment: int, textPosition: int):
        return self.__printer.PrintBarCode(data, symbology, height, width, alignment, textPosition)

    def PrintPDF417(self, data, columns, rows, width, height, errorCorrectionLevel, alignment):
        raise Exception("Not implemented")

    def PrintQRCode(self, data: str, moduleSize: int, ECLevel: int, alignment: int):
        return self.__printer.PrintQRCode(data, moduleSize, ECLevel, alignment)

    def PrintGS1DataBarStacked():
        raise Exception("Not implemented")

    def CutPaper(self, type: int):
        return self.__printer.CutPaper(type)

    def UnitFeed(self, ufCount: int) -> int:
        return self.__printer.UnitFeed(ufCount)

    def MarkFeed(self, markType: int) -> int:
        return self.__printer.MarkFeed(markType)

    def OpenDrawer(self, drawer: int, pulseLen: int) -> int:
        return self.__printer.OpenDrawer(drawer, pulseLen)

    def TransactionPrint(self, control: int) -> int:
        return self.__printer.TransactionPrint(control)

    def RotatePrint(self, rotation: int) -> int:
        return self.__printer.RotatePrint(rotation)

    def PageModePrint(self, control: int) -> int:
        return self.__printer.PageModePrint(control)

    def ClearPrintArea(self) -> int:
        return self.__printer.ClearPrintArea()

    def ClearOutput(self) -> int:
        return self.__printer.ClearOutput()

    def PrintData(self, data: bytes) -> int:
        return self.__printer.PrintData(data)

    def PrintNormal(self, data: str) -> int:
        return self.__printer.PrintNormal(data.encode('utf-8'))

    def WatermarkPrint(self, start: int, nvImageNumber: int, pass_num: int, feed: int, repeat: int) -> int:
        return self.__printer.WatermarkPrint(start, nvImageNumber, pass_num, feed, repeat)

    def SearchCitizenPrinter(self, connectType: int, searchTime: int) -> list:
        return self.__printer.SearchCitizenPrinter(connectType, searchTime)

    def SearchESCPOSPrinter(self, connectType: int, searchTime: int) -> list[str]:
        return self.__printer.SearchESCPOSPrinter(connectType, searchTime)

    def SetIPSettings(self, macAddress: str, enableDHCP: bool, ipAddress: str, subnetMask: str, defaultGateway: str) -> int:
        return self.__printer.SetIPSettings(macAddress, enableDHCP, ipAddress, subnetMask, defaultGateway)

    def PrinterCheckEx(self, connectType, addr, port=None, timeout=None):
        raise Exception("Not implemented")

    def OpenDrawerEx(self, connectType, addr, port=None, timeout=None):
        raise Exception("Not implemented")

    def SetPrintCompletedTimeout(self, timeout: int) -> int:
        return self.__printer.SetPrintCompletedTimeout(timeout)

    def SetLog(self, mode: int, path: str, maxSize: int) -> None:
        self.__printer.SetLog(mode, path, maxSize)

    def GetVersionCode(self) -> int:
        return self.__printer.GetVersionCode()

    def GetVersionName(self) -> str:
        return self.__printer.GetVersionName()
