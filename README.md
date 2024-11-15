# Windows POS Print SDK サンプル集

## 注意事項

**本プロジェクトは、Citizen 公式のものではなく、個人的に作成したラッパーライブラリです。**

Citizen Systems 株式会社の Windows POS Print SDK を利用していますが、本ライブラリおよび本サンプル集は非公式のものであり、公式サポートは提供しておりません。ご使用に際しては、自己責任で行ってください。

## 目次

<!-- 1. [SDK のダウンロード](#sdk のダウンロード) -->
aaaaaaa
2. [不具合調査](#不具合調査)
3. [接続失敗の原因](#接続失敗の原因)

## SDK のダウンロード

本サンプル集では、Windows POS Print SDK を使用してプリンタとの接続および通信を行う方法を紹介しています。

標準の設定では、`/csjwindowspossdk/Library` に DLL ファイルが配置されていることを想定しています。

使用する SDK のライブラリを以下の URL からダウンロードしてください：

[CSJWindowsPOSSDK_V206J.zip](https://www.citizen-systems.co.jp/cms/c-s/printer/download/sdk-print/CSJWindowsPOSSDK_V206J.zip)

DLL ファイルを別の場所に配置したい場合は、[`/samples/setDllPath.smp.py`](samples/setDllPath.smp.py) の設定用サンプルをご参照ください。

ダウンロード後、ご自身でインストールしたライブラリのパスを指定してください。

## 不具合調査

### Bluetooth の接続状況監視における問題

- 使用していないにもかかわらず、一瞬だけ接続中になる。
- このタイミングでプログラムを実行すると、接続できない可能性がある。
- 接続が可能になるまでループを続けると、実際には接続済み状態を一度解除する必要があるようです。
- そのため、すぐに再接続を試みると、ドライバーは前回の接続を継続しており、再接続に失敗します。
- **解決策:** 再接続を試みる際に待機時間を設ける必要があります。

### シリアル通信のバッファを使用する方法

- バッファを COM ポートに送信しておくことで、ドライバーが一瞬接続されたときにデータが送信されているはずです。

## 接続失敗の原因

1. **接続済み状態が解除されていない場合**

   - **対策:** `Disconnect` メソッドを実行して接続を解除します。

2. **一定秒数ごとの自動 Bluetooth 接続のタイミングと重なっている場合**
   - **原因:** Bluetooth 設定を確認すると、一定時間ごとにプリンタと自動接続が行われているようです。このタイミングでは SDK の `Connect` を実行できません。

# git clone

```bash
git clone https://github.com/mizunoshota2001/tutorial-CSJWindowsPOSSDK-for-python.git
```

# Project Structure

```bash
tutorial-CSJWindowsPOSSDK-for-python/
    ├── .gitattributes
    ├── .gitignore
    ├── assets/
    ├── csjwindowspossdk/
      ├── Library/
      │   ├── CSJPOSLib.dll
      │   ├── CSJPOSLibW32.dll
      │   └── CSJPOSLibW64.dll
    │   ├── __init__.py
    │   ├── ESCPOSConst.py
    │   └── ESCPOSPrinter.py
    ├── docs/
    │   └── 講座用.pptx
    ├── README.md
    ├── requirements.txt
    └── samples/
        ├── __relimport.py
        ├── 2.1.smp.py
        ├── ...
```

# Python3.11
```bash
pip install –r requirememts.txt
```



# セキュリティーがひっかる場合
```bash
System.NotSupportedException: ネットワーク上の場所からアセンブリを読み込もうとしました。これにより、以前のバージョンの .NET Framework で、アセンブリがサンドボックス化された可能性があります。このリリースの .NET Framework では、CAS ポリシーが既定で有効になっていないため、この読み込みは危険な場合があります。この読み込みがアセンブリのサンドボックス化を目的としない場合は、loadFromRemoteSources スイッチを有効にしてください。詳細については、http://go.microsoft.com/fwlink/?LinkId=155569 を参照してください。
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "c:\...\tutorial-CSJWindowsPOSSDK-for-python\samples\2.1.smp.py", line 6, in <module>
    printer = ESCPOSPrinter()
              ^^^^^^^^^^^^^^^
  File "c:\...\tutorial-CSJWindowsPOSSDK-for-python\csjwindowspossdk\ESCPOSPrinter.py", line 24, in __init__
    clr.AddReference(str(dllPath))
System.IO.FileLoadException: ファイルまたはアセンブリ 'file:///c:\...\tutorial-CSJWindowsPOSSDK-for-python\csjwindowspossdk\Library\CSJPOSLib.dll'、またはその依存関係の 1 つが読み込めませんでした。操作はサポートされません。 (HRESULT からの例外:0x80131515)
ファイル名 'file:///c:\...\tutorial-CSJWindowsPOSSDK-for-python\csjwindowspossdk\Library\CSJPOSLib.dll' です。'file:///c:\...\tutorial-CSJWindowsPOSSDK-for-python\csjwindowspossdk\Library\CSJPOSLib.dll' ---> System.NotSupportedException: ネットワーク上の場所からアセンブリを読み込もうとしました。これにより、以前のバージョンの .NET Framework で、アセンブリがサンドボックス化された可能性があります。このリリースの .NET Framework では、CAS ポリシーが既定で有効になっていないため、この読み込みは危険な場合があります。この読み込みがアセンブリのサンドボックス化を目的としない場合は、loadFromRemoteSources スイッチを有効にしてください。詳細については、http://go.microsoft.com/fwlink/?LinkId=155569 を参照してください。
   場所 System.Reflection.RuntimeAssembly._nLoad(AssemblyName fileName, String codeBase, Evidence assemblySecurity, RuntimeAssembly locationHint, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)
   場所 System.Reflection.RuntimeAssembly.InternalLoadAssemblyName(AssemblyName assemblyRef, Evidence assemblySecurity, RuntimeAssembly reqAssembly, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)
   場所 System.Reflection.RuntimeAssembly.InternalLoadFrom(String assemblyFile, Evidence securityEvidence, Byte[] hashValue, AssemblyHashAlgorithm hashAlgorithm, Boolean forIntrospection, Boolean suppressSecurityChecks, StackCrawlMark& stackMark)
   場所 System.Reflection.Assembly.LoadFrom(String assemblyFile)
   場所 Python.Runtime.AssemblyManager.LoadAssemblyFullPath(String name)
   場所 Python.Runtime.CLRModule.AddReference(String name)
```
- プロパティからセキュリティを許可してください。