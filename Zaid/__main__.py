import sys
from pytgcalls import idle
from Zaid import telethon, call_py
path = "Zaid/plugins/*.py"
idle()
telethon.run_until_disconnected()