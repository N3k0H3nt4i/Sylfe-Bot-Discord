from .errors import UserNotFound
from .osu import get_data, User


class Api:
    def __init__(
            self,
            api_key: str
    ):
        """
        :type api_key: String-like api key
        """
        self._api_key = api_key

    async def get_osu_player(self, name: str, mode: str) -> User:
        """
        :type name: Player's name
        :type mode: osu! game mode e.g osu!, osu!mania etc

        :rtype: osu.User
        """

        obj = await User.form_object(username=name, mode=mode, api_key=self._api_key)

        return obj
