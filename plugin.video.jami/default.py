# -*- coding: utf-8 -*-
#------------------------------------------------------------
# jami
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.jami'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan001 = 'special://home/addons/plugin.video.jami/resources/fan001.jpg'
icon001 = 'special://home/addons/plugin.video.jami/resources/icon001.png'
icon002 = 'special://home/addons/plugin.video.jami/resources/icon002.png'
icon003 = 'special://home/addons/plugin.video.jami/resources/icon003.png'
icon004 = 'special://home/addons/plugin.video.jami/resources/icon004.png'
icon005 = 'special://home/addons/plugin.video.jami/resources/icon005.png'
icon006 = 'special://home/addons/plugin.video.jami/resources/icon006.png'
icon007 = 'special://home/addons/plugin.video.jami/resources/icon007.png'
icon008 = 'special://home/addons/plugin.video.jami/resources/icon008.png'
icon009 = 'special://home/addons/plugin.video.jami/resources/icon009.png'
icon010 = 'special://home/addons/plugin.video.jami/resources/icon010.png'
icon011 = 'special://home/addons/plugin.video.jami/resources/icon011.png'
icon012 = 'special://home/addons/plugin.video.jami/resources/icon012.png'
icon013 = 'special://home/addons/plugin.video.jami/resources/icon013.png'
icon014 = 'special://home/addons/plugin.video.jami/resources/icon014.png'
icon015 = 'special://home/addons/plugin.video.jami/resources/icon015.png'
icon016 = 'special://home/addons/plugin.video.jami/resources/icon016.png'
icon017 = 'special://home/addons/plugin.video.jami/resources/icon017.png'
icon018 = 'special://home/addons/plugin.video.jami/resources/icon018.png'
icon019 = 'special://home/addons/plugin.video.jami/resources/icon019.png'
icon020 = 'special://home/addons/plugin.video.jami/resources/icon020.png'
icon021 = 'special://home/addons/plugin.video.jami/resources/icon021.png'
icon022 = 'special://home/addons/plugin.video.jami/resources/icon022.png'
icon023 = 'special://home/addons/plugin.video.jami/resources/icon023.png'
icon024 = 'special://home/addons/plugin.video.jami/resources/icon024.png'
icon025 = 'special://home/addons/plugin.video.jami/resources/icon025.png'
icon026 = 'special://home/addons/plugin.video.jami/resources/icon026.png'
icon027 = 'special://home/addons/plugin.video.jami/resources/icon027.png'
icon028 = 'special://home/addons/plugin.video.jami/resources/icon028.png'


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
	plugintools.add_item(title = "Angry Birds", url = base + "playlist/PLVZggjiHl7zWTZDWcXNok7JFZUlb8vdHZ/", thumbnail = icon001, fanart = fan001, folder = True)
	plugintools.add_item(title = "Ruca - T01 a T24 [PT]", url = base + "playlist/PLsWbExGo1KPaYUuRSfzyF1X11Czip4259/", thumbnail = icon002, fanart = fan001, folder = True)
	plugintools.add_item(title = "Max - T01 a T05 [PT]", url = base + "playlist/PLsWbExGo1KPbil5fBWgJlv2gQPTcABI7x/", thumbnail = icon003, fanart = fan001, folder = True)
	plugintools.add_item(title = "Octonautas [PT]", url = base + "playlist/PLjRUOcyjSeAxv2ITxi2CVbNKUz-cK9YfA/", thumbnail = icon004, fanart = fan001, folder = True)
	plugintools.add_item(title = "Noddy [PT]", url = base + "playlist/PLrH5HKiu5jUeEVAVEctaHl1qud4zbYg5O/" , thumbnail = icon005, fanart = fan001, folder = True)	
	plugintools.add_item(title = "Pocoyo [PT]", url = base + "user/childrenvideos/", thumbnail = icon006, fanart = fan001, folder = True)
	plugintools.add_item(title = "Heidi 3D [PT]", url = base + "playlist/PLnp6B7ujCv2A8aaaa-6niKGW-SoChr88d/", thumbnail = icon007, fanart = fan001, folder = True)	
	plugintools.add_item(title = "Abelha Maia 3D [PT]", url = base + "playlist/PLTf5zA07OijMLjuAJGYQ_dT7s8fgo7kpN/", thumbnail = icon008, fanart = fan001, folder = True)
	plugintools.add_item(title = "Herois da Cidade [PT]", url = base + "playlist/PLFepGKlvmn74D95OwZkSSQR3uk4T2ReHD/", thumbnail = icon009, fanart = fan001, folder = True)
	plugintools.add_item(title = "Bob o Construtor [PT]", url = base + "playlist/PLrH5HKiu5jUd7KNHHylSmu_WvFZ1pyURq/", thumbnail = icon010, fanart = fan001, folder = True)
	plugintools.add_item(title = "Thomas e Amigos [PT]", url = base + "playlist/PLZ-7k3FZDGmm5XODLaqSXX98OME6gk6Um/", thumbnail = icon011, fanart = fan001, folder = True)
	plugintools.add_item(title = "Ovelha Choné - T01/T02", url = base + "playlist/PLsWbExGo1KParAPrKtn8aQfLnEFepaajb/", thumbnail = icon012, fanart = fan001, folder = True)
	plugintools.add_item(title = "Vila Moleza [PT]", url = base + "playlist/PLrH5HKiu5jUeWGDGh3EYBvMQ-eU1CSy4J/", thumbnail = icon013, fanart = fan001, folder = True)
	plugintools.add_item(title = "Panda e os Caricas [PT]", url = base + "channel/UCvw-R-r3p6Hc-yj1qyoPslQ/", thumbnail = icon014, fanart = fan001, folder = True)
	plugintools.add_item(title = "Xana Toc Toc [PT]", url = base + "user/XanaTocTocVEVO/", thumbnail = icon015, fanart = fan001, folder = True)
	plugintools.add_item(title = "Violeta [Musicais]", url = base + "playlist/PLE308E8FD36F34EAC/", thumbnail = icon016, fanart = fan001, folder = True)
	plugintools.add_item(title = "Turma da Mónica [BR]", url = base + "playlist/PLWduEF1R_tVZYNTH8ajFOEDkDT_hfIQL9/", thumbnail = icon017, fanart = fan001, folder = True)
	plugintools.add_item(title = "Charlie Brown [BR]", url = base + "playlist/PLolevrZYo2eGlwPrvK1Nr_rwUGSpbJMYK/", thumbnail = icon018, fanart = fan001, folder = True)
	plugintools.add_item(title = "Daniel Tigre [BR]", url = base + "playlist/PLoaBAxtZve6nmFuNHCmIRLz_bo2aCD4wX/", thumbnail = icon019, fanart = fan001, folder = True)
	plugintools.add_item(title = "Masha e o Urso [BR]", url = base + "playlist/PLsWbExGo1KPYsGKNTnOemWCEdxRNHJyRm/", thumbnail = icon020, fanart = fan001, folder = True)
	plugintools.add_item(title = "Jelly Jamm [BR]"  , url = base + "playlist/PL-CfLd2XMlrw7Cq-LT4UMNJrzLr9OjMpk/", thumbnail = icon021, fanart = fan001, folder = True)
	plugintools.add_item(title = "Sonic X [BR]", url = base + "playlist/PLj0Fsa9q1GRCKN_i_-1zRTM0m9m-GW6E1/", thumbnail = icon022, fanart = fan001, folder = True)
	plugintools.add_item(title = "Team Hot Wheels [BR]", url = base + "playlist/PLsWbExGo1KPb-TTwpvyEDIZa51JUYLr9l/", thumbnail = icon023, fanart = fan001, folder = True)
	plugintools.add_item(title = "Tartarugas Ninja [PT]", url = base + "playlist/PL12TUMahWFQR6XqoHTKm5-RvCSYy1EPg1/", thumbnail = icon024, fanart = fan001, folder = True)
	plugintools.add_item(title = "Irmãos Grimm [PT]", url = base + "playlist/PLaerdHbAdrDIIi3LuIIdCRGdFoHe3lS_D/", thumbnail = icon025, fanart = fan001, folder = True)
	plugintools.add_item(title = "Dartacão [PT]", url = base + "playlist/PLrH5HKiu5jUe8ZF8jwdtprpucMVEjRON5/", thumbnail = icon026, fanart = fan001, folder = True)
	plugintools.add_item(title = "Era uma vez - 4 Temporadas [PT]", url = base + "playlist/PLsWbExGo1KPZRlqvLY2Ja_SAJZMgBcdxD/", thumbnail = icon027, fanart = fan001, folder = True)
	plugintools.add_item(title = "Contos Infantis [PT]", url = base + "channel/UCOre4lsfRMaC62bOHUjPp2Q/", thumbnail = icon028, fanart = fan001, folder = True)
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
