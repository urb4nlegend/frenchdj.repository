# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Portugal Media Center
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.portugal.media.center'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan01 = 'special://home/addons/plugin.video.portugal.media.center/resources/fan01.png'
icon01 = 'special://home/addons/plugin.video.portugal.media.center/resources/icon01.png'
icon02 = 'special://home/addons/plugin.video.portugal.media.center/resources/icon02.png'
icon03 = 'special://home/addons/plugin.video.portugal.media.center/resources/icon03.png'
icon04 = 'special://home/addons/plugin.video.portugal.media.center/resources/icon04.png'
icon05 = 'special://home/addons/plugin.video.portugal.media.center/resources/icon05.png'
icon06 = 'special://home/addons/plugin.video.portugal.media.center/resources/icon06.png'
icon07 = 'special://home/addons/plugin.video.portugal.media.center/resources/icon07.png'
icon08 = 'special://home/addons/plugin.video.portugal.media.center/resources/icon08.png'
icon09 = 'special://home/addons/plugin.video.portugal.media.center/resources/icon09.png'



def run():
    plugintools.log("jami.run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("jami ===> " + repr(params))
	
	plugintools.add_item(title = "BUILDS KODI PT", url = base + "playlist/PLBe2SuHqqAQVsILxuKuhU9v4WtkpcWoK2/", thumbnail = icon01, fanart = fan01, folder = True)
	plugintools.add_item(title = "BUILDS", url = base + "playlist/PLBe2SuHqqAQVGItjmqE48aKgRApJOzQYH/", thumbnail = icon02, fanart = fan01, folder = True)
	plugintools.add_item(title = "IPTV", url = base + "playlist/PLBe2SuHqqAQWQzHQPmpXUIS9YJzmUCSdu/", thumbnail = icon03, fanart = fan01, folder = True)
	plugintools.add_item(title = "RASPBERRY PI", url = base + "playlist/PLBe2SuHqqAQUQjbEzVcCNVJJqTrgbZSjA/", thumbnail = icon04, fanart = fan01, folder = True)
	plugintools.add_item(title = "FILMES E SERIES", url = base + "playlist/PLBe2SuHqqAQX9P3zvTrYSSFaRi7wWkVVC/", thumbnail = icon05, fanart = fan01, folder = True)
	plugintools.add_item(title = "CONSOLAS", url = base + "playlist/PLBe2SuHqqAQVr2QXs-hfST4si2b2TLoLI/" , thumbnail = icon06, fanart = fan01, folder = True)	
	plugintools.add_item(title = "ADD-ONS PT", url = base + "playlist/PLBe2SuHqqAQXqCB4syEjegBX1Yfev_ql7/", thumbnail = icon07, fanart = fan01, folder = True)
	plugintools.add_item(title = "DIVERSOS", url = base + "playlist/PLBe2SuHqqAQXIxfKPKNfWpiCzSGRFpHZ2/", thumbnail = icon08, fanart = fan01, folder = True)
	plugintools.add_item(title = "PT MEDIA CENTER", url = base + "channel/UCb6fo8oH9phPpNjzNjc8MOg/", thumbnail = icon09, fanart = fan01, folder = True)

	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
