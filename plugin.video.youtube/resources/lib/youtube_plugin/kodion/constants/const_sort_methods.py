__author__ = 'bromix'

_xbmc = True

try:
    from xbmcplugin import *
except:
    _xbmc = False
    _count = 0


def _const(name):
    if _xbmc:
        return eval(name)
    else:
        global _count
        _count += 1
        return _count


ALBUM = _const('SORT_METHOD_ALBUM')
ALBUM_IGNORE_THE = _const('SORT_METHOD_ALBUM_IGNORE_THE')
ARTIST = _const('SORT_METHOD_ARTIST')
ARTIST_IGNORE_THE = _const('SORT_METHOD_ARTIST_IGNORE_THE')
BIT_RATE = _const('SORT_METHOD_BITRATE')
# CHANNEL = _const('SORT_METHOD_CHANNEL')
# COUNTRY = _const('SORT_METHOD_COUNTRY')
DATE = _const('SORT_METHOD_DATE')
DATE_ADDED = _const('SORT_METHOD_DATEADDED')
# DATE_TAKEN = _const('SORT_METHOD_DATE_TAKEN')
DRIVE_TYPE = _const('SORT_METHOD_DRIVE_TYPE')
DURATION = _const('SORT_METHOD_DURATION')
EPISODE = _const('SORT_METHOD_EPISODE')
FILE = _const('SORT_METHOD_FILE')
# FULL_PATH = _const('SORT_METHOD_FULLPATH')
GENRE = _const('SORT_METHOD_GENRE')
LABEL = _const('SORT_METHOD_LABEL')
# LABEL_IGNORE_FOLDERS = _const('SORT_METHOD_LABEL_IGNORE_FOLDERS')
LABEL_IGNORE_THE = _const('SORT_METHOD_LABEL_IGNORE_THE')
# LAST_PLAYED = _const('SORT_METHOD_LASTPLAYED')
LISTENERS = _const('SORT_METHOD_LISTENERS')
MPAA_RATING = _const('SORT_METHOD_MPAA_RATING')
NONE = _const('SORT_METHOD_NONE')
# PLAY_COUNT = _const('SORT_METHOD_PLAYCOUNT')
PLAYLIST_ORDER = _const('SORT_METHOD_PLAYLIST_ORDER')
PRODUCTION_CODE = _const('SORT_METHOD_PRODUCTIONCODE')
PROGRAM_COUNT = _const('SORT_METHOD_PROGRAM_COUNT')
SIZE = _const('SORT_METHOD_SIZE')
SONG_RATING = _const('SORT_METHOD_SONG_RATING')
STUDIO = _const('SORT_METHOD_STUDIO')
STUDIO_IGNORE_THE = _const('SORT_METHOD_STUDIO_IGNORE_THE')
TITLE = _const('SORT_METHOD_TITLE')
TITLE_IGNORE_THE = _const('SORT_METHOD_TITLE_IGNORE_THE')
TRACK_NUMBER = _const('SORT_METHOD_TRACKNUM')
UNSORTED = _const('SORT_METHOD_UNSORTED')
VIDEO_RATING = _const('SORT_METHOD_VIDEO_RATING')
VIDEO_RUNTIME = _const('SORT_METHOD_VIDEO_RUNTIME')
VIDEO_SORT_TITLE = _const('SORT_METHOD_VIDEO_SORT_TITLE')
VIDEO_SORT_TITLE_IGNORE_THE = _const('SORT_METHOD_VIDEO_SORT_TITLE_IGNORE_THE')
VIDEO_TITLE = _const('SORT_METHOD_VIDEO_TITLE')
VIDEO_YEAR = _const('SORT_METHOD_VIDEO_YEAR')
