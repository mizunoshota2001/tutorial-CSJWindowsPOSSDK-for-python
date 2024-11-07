import clr
from pathlib import Path
__path = Path(__file__).parent/"Library"/"CSJPOSLib.dll"
clr.AddReference(str(__path))
import com.citizen.sdk
tmp=com.citizen.sdk.ESCPOSConst
print({k:getattr(tmp, k) for k in dir(tmp)})
