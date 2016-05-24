# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Alive HD
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.alive.hd'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan01 = 'special://home/addons/plugin.video.alive.hd/resources/fan01.png'
iconAA = 'special://home/addons/plugin.video.alive.hd/resources/iconAA.png'
iconAB = 'special://home/addons/plugin.video.alive.hd/resources/iconAB.png'
iconAC = 'special://home/addons/plugin.video.alive.hd/resources/iconAC.png'
iconAD = 'special://home/addons/plugin.video.alive.hd/resources/iconAD.png'
icon01 = 'special://home/addons/plugin.video.alive.hd/resources/icon01.png'
icon02 = 'special://home/addons/plugin.video.alive.hd/resources/icon02.png'
icon03 = 'special://home/addons/plugin.video.alive.hd/resources/icon03.png'
icon04 = 'special://home/addons/plugin.video.alive.hd/resources/icon04.png'
icon05 = 'special://home/addons/plugin.video.alive.hd/resources/icon05.png'
icon06 = 'special://home/addons/plugin.video.alive.hd/resources/icon06.png'
iconBA = 'special://home/addons/plugin.video.alive.hd/resources/iconBA.png'
iconBB = 'special://home/addons/plugin.video.alive.hd/resources/iconBB.png'
iconBC = 'special://home/addons/plugin.video.alive.hd/resources/iconBC.png'
iconBD = 'special://home/addons/plugin.video.alive.hd/resources/iconBD.png'







def run():
    plugintools.log("alive.hd.run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("alive.hd ===> " + repr(params))
	plugintools.add_item(title = "Wacken Open Air", url = base + "playlist/PLqIQyrHgoWoKI8z1ODSIMFW103sIhXDJ5/", thumbnail = iconAA, fanart = fan01, folder = True)
	plugintools.add_item(title = "Rock AM Ring", url = base + "playlist/PLqIQyrHgoWoICwYBKfnmuJRCIOB3U43Mb/", thumbnail = iconAB, fanart = fan01, folder = True)
	plugintools.add_item(title = "Reading Festival", url = base + "playlist/PLqIQyrHgoWoIKuMCz7611QuRg2HpJDRan/", thumbnail = iconAC, fanart = fan01, folder = True)
	plugintools.add_item(title = "Glastonbury Festival", url = base + "playlist/PLqIQyrHgoWoKIc6yJ6aDegiEfiXa_ELT3/", thumbnail = iconAD, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Jurassic Rock ]", url = base + "playlist/PLqIQyrHgoWoJ8e5adzV6VwgW-v9vg-Zc8/", thumbnail = icon01, fanart = fan01, folder = True)	
	plugintools.add_item(title = "[ Rock & Blues ]", url = base + "playlist/PLqIQyrHgoWoIPZ4jKiDyJ6Sl2sCkIW0HU/", thumbnail = icon02, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Hard & Heavy ]", url = base + "playlist/PLqIQyrHgoWoLIi9gYTzSXCVz7ng-5I-s2/", thumbnail = icon03, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Fusion Metal ]", url = base + "playlist/PLqIQyrHgoWoL5xlRnsrBGfqymXtyQzFQy/", thumbnail = icon04, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Indie Rock ]", url = base + "playlist/PLqIQyrHgoWoKx_I2ZI76N9mbTkQh9rp8Z/", thumbnail = icon05, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Electronic Music ]", url = base + "playlist/PLqIQyrHgoWoLd9UevjdOPw7X-DywtMHl3/" , thumbnail = icon06, fanart = fan01, folder = True)	
	plugintools.add_item(title = "Sónar Barcelona ", url = base + "playlist/PLqIQyrHgoWoKKQ6hMB7MS_I_zNkfppS5C/", thumbnail = iconBA, fanart = fan01, folder = True)
	plugintools.add_item(title = "Boiler Room", url = base + "playlist/PLqIQyrHgoWoKZ5l0puIUoPIY4j809zPf2/", thumbnail = iconBB, fanart = fan01, folder = True)
	plugintools.add_item(title = "Space Ibiza", url = base + "playlist/PLqIQyrHgoWoJWjpjC5yXNpbWBrhYrw-9m/", thumbnail = iconBC, fanart = fan01, folder = True)
	plugintools.add_item(title = "Dance Trippin TV", url = base + "playlist/PLqIQyrHgoWoLppvZwVuUl51rOVlaP_XW3/", thumbnail = iconBD, fanart = fan01, folder = True)
	
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
