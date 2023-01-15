class OsuBotError(Exception):
    pass


class UserNotFound(OsuBotError):
    pass


class UserScoreNotFound(OsuBotError):
    pass


class BeatmapNotFound(OsuBotError):
    pass
