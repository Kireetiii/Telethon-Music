import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6016282205:AAFKN2xip5xArBZ6ioGG3Xb9FyYbwssfUhA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOMgBu3C3s1D0eIUr6gZ926vuiW-5fMfe6YnKGSPa6GkRXnrhRsx62FS3Q_4gszIkJf3cWKLmkSci5Vn4qa2YR7KCOoBg9eNkF5z1t7-YUcDLBbDQ9yMAM43dMz535a1Xg6_nXSmVljFFeInaE8aFHOwVVpOzhLG40gNpjhKvVF75MjEShq5EqDuX6DhCCgMCLe87LnbUeyM1XVJwgMBxRJlhMoBkqNTYfJz5PCloTcXHbQhmm5e7y_PRyxnrIi5e9-5NoPe3-SEl-poIdeZe0S7dmljttTNMgvaaMt6NtPwuCav64Kgmh78EZdbDgxxaSs4iEcfhxKL9HD8UdaDOs_376vo= ")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
