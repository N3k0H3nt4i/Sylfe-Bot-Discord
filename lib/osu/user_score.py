from .requests import get_data
from .. import UserScoreNotFound
from .beatmap import Beatmap


class UserBestScore:
    """
    Represents osu player score as class.
    """

    def __init__(
            self,
            data: dict,
            game_mode: str,
            api_key: str
    ):
        """
        :param data: JSON like object with Score data
        :param game_mode: osu! game mode
        :param api_key: osu!api key
        """
        self._data = data
        self._game_mode = game_mode
        self._api_key = api_key

    @property
    def game_mode(self) -> str:
        return self._game_mode

    @property
    def rank(self) -> str:
        x = self._data.get('rank')
        if x is None:
            return 'D'
        return x

    @property
    def beatmap_id(self) -> int:
        try:
            x = int(self._data.get('beatmap_id'))
        except TypeError:
            x = 0

        return x

    @property
    def score_id(self) -> int:
        try:
            x = int(self._data.get('score_id'))
        except TypeError:
            x = 0

        return x

    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('user_id'))
        except TypeError:
            x = 0

        return x

    @property
    def misses(self) -> int:
        try:
            x = int(self._data.get('countmiss'))
        except TypeError:
            x = 0

        return x

    @property
    def max_combo(self) -> int:
        try:
            x = int(self._data.get('maxcombo'))
        except TypeError:
            x = 0

        return x

    @property
    def pp(self) -> int:
        try:
            x = int(round(float(self._data.get('pp'))))
        except TypeError:
            x = 0

        return x

    @property
    async def map(self) -> Beatmap:
        obj = await Beatmap.form_object(beatmap_id=self.beatmap_id, mode=self._game_mode, api_key=self._api_key)
        return obj

    @classmethod
    async def form_object(cls, user_id: int, mode: str, api_key: str):
        """
        :param user_id: User id to get scores from
        :param mode: osu! game mode (osu!, Taiko etc.)
        :param api_key: osu!api key

        :return: osu.UserBestScore
        """

        modes = {
            "osu!": 0,
            "Taiko": 1,
            "CtB": 2,
            "osu!mania": 3
        }

        params = {
            'k': api_key,
            'u': user_id,
            'm': mode,
            'type': 'id',
            'limit': 1
        }
        data = await get_data(f'https://osu.ppy.sh/api/get_user_best', params=params)

        try:
            obj = cls(
                data=data[0],
                game_mode=str(modes.get(mode)),
                api_key=api_key
            )
        except IndexError:
            raise UserScoreNotFound

        return obj
