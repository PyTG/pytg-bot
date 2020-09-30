import telegram, yaml

from telegram.ext import Updater

from modules.pytg.Manager import Manager
from modules.pytg.load import manager

class BotManager(Manager):
    @staticmethod
    def initialize():
        BotManager.__instance = BotManager()

    @staticmethod
    def load():
        return BotManager.__instance

    def __init__(self):
        self.bot = None
        self.updater = None

    def connect(self):
        settings = manager("config").load_settings("bot", "token")

        self.bot = telegram.Bot(settings["token"])
        self.updater = Updater(settings["token"], use_context=True)