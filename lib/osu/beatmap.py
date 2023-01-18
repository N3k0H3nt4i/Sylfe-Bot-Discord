from .requests import get_data
from .. import UserScoreNotFound
from ..errors import BeatmapNotFound


class Beatmap:
    """
    Represents osu beatmap as class.
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
    def title(self) -> str:
        x = self._data.get('title')
        if x is None:
            return 'No Title'
        return x

    @property
    def creator(self) -> str:
        x = self._data.get('creator')
        if x is None:
            return 'Undefined'
        return x

    @property
    def beatmap_id(self) -> int:
        try:
            x = int(self._data.get('beatmap_id'))
        except TypeError:
            x = 0

        return x
    
    
    @property
    def beatmapset_id(self) -> int:
        try:
            x = int(round(float(self._data.get('beatmapset_id'))))
        except TypeError:
            x = 0

        return x
    
    @property
    def type(self) -> str:
        types = {
            "-2": "Graveyarded",
            "-1": "WIP",
            "0": "Pending",
            "1": "Ranked",
            "2": "Approved",
            "3": "Qualified",
            "4": "Loved",
            "None": "Undefined"
        }

        try:
            x = types.get(str(self._data.get('approved')))
        except TypeError:
            x = "Bruh"

        return x

    @property
    def difficulty(self) -> int:
        try:
            x = int(round(float(self._data.get('difficultyrating'))))
        except TypeError:
            x = 0

        return x

    @classmethod
    async def form_object(cls, beatmapset_id, beatmap_id: int, mode: str, api_key: str):
        """
        :param beatmap_id: Betmap id to get data from
        :param mode: osu! game mode (osu!, Taiko etc.)
        :param api_key: osu!api key

        :return: osu.Beatmap
        """

        modes = {
            "osu!": 0,
            "Taiko": 1,
            "CtB": 2,
            "osu!mania": 3
        }

        params = {
            'k': api_key,
            's': beatmapset_id,
            'b': beatmap_id,
            'm': mode,
            'type': 'id',
        }
        data = await get_data(f'https://osu.ppy.sh/api/get_beatmaps', params=params)

        try:
            obj = cls(
                data=data[0],
                game_mode=str(modes.get(mode)),
                api_key=api_key
            )
        except IndexError:
            raise BeatmapNotFound

        return obj
