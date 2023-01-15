from abc import ABC

from discord.ext import bridge


class OsuBot(bridge.Bot, ABC):

    """
        Here we can put custom bot methods and properties.
    """

    def __init__(self, *args, **options):
        super().__init__(*args, **options)
