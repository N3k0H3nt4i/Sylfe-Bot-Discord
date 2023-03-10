from .requests import get_data
from .. import UserScoreNotFound
from .beatmap import Beatmap


class UserRecentScore:
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
    def title(self) -> str:
        x = self._data.get('title')
        if x is None:
            return 'aq'
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


    '''
    @property
    async def image(self) -> str:
       await UserRecentScore.form_object(beatmapset_id=self.beatmapset_id)
       return await f"https://b.ppy.sh/beatmaps/{self.beatmapset_id}l.jpg"

       '''
 

    @property
    async def map(self) -> Beatmap:
        obj = await Beatmap.form_object(beatmap_id=self.beatmap_id, mode=self._game_mode, api_key=self._api_key, title=self.title)
        return obj

    @classmethod
    async def form_object(cls, user_id: int, mode: str, api_key: str):
        """
        :param user_id: User id to get scores from
        :param mode: osu! game mode (osu!, Taiko etc.)
        :param api_key: osu!api key

        :return: osu.UserRecentScore
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
        data = await get_data(f'https://osu.ppy.sh/api/get_user_recent', params=params)

        try:
            obj = cls(
                data=data[0],
                game_mode=str(modes.get(mode)),
                api_key=api_key
            )
        except IndexError:
            raise UserScoreNotFound

        return obj


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



    
class TopScores:
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
    def score_id(self) -> int:
        try:
            x = int(self._data.get('score'))
        except TypeError:
            x = 0

        return x


    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('count50'))
        except TypeError:
            x = 0

        return x

    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('count100'))
        except TypeError:
            x = 0

        return x


    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('count300'))
        except TypeError:
            x = 0

        return x

    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('countmiss'))
        except TypeError:
            x = 0

        return x

    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('countkatu'))
        except TypeError:
            x = 0

        return x


    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('countgeki'))
        except TypeError:
            x = 0

        return x

    
    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('perfect'))
        except TypeError:
            x = 0

        return x
    
    
    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('enabled_mods'))
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
    def user_id(self) -> int:
        try:
            x = int(self._data.get('date'))
        except TypeError:
            x = 0

        return x
    
    @property
    def user_id(self) -> int:
        try:
            x = int(self._data.get('rank'))
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
    def beatmapset_id(self) -> int:
        try:
            x = int(round(float(self._data.get('beatmapset_id'))))
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

        :return: osu.TopScores
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
        data = await get_data(f'https://osu.ppy.sh/api/get_scores', params=params)

        try:
            obj = cls(
                data=data[0],
                game_mode=str(modes.get(mode)),
                api_key=api_key
            )
        except IndexError:
            raise UserScoreNotFound

        return obj

















''' 
class UserReceScore:
    # ...

    @property
    async def map(self) -> Beatmap:
        obj = await Beatmap.form_object(beatmap_id=self.beatmap_id, mode=self._game_mode, api_key=self._api_key)
        return obj

    @property
    async def recent_play(self) -> Beatmap:
        obj = await Beatmap.form_object(beatmap_id=self.beatmap_id, mode=self._game_mode, api_key=self._api_key)
        return obj
'''



class TopPlay:
  

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
        ob = await Beatmap.form_object(beatmap_id=self.beatmap_id, mode=self._game_mode, api_key=self._api_key)
        return ob

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
        data = await get_data(f'https://osu.ppy.sh/api/get_beatmaps?limit=100&k=api&username&mode', params=params)

        try:
            ob = cls(
                data=data[0],
                game_mode=str(modes.get(mode)),
                api_key=api_key
            )
        except IndexError:
            raise UserScoreNotFound

        return ob
