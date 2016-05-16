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

fan1 = 'special://home/addons/plugin.video.jami/resources/fan1.jpg'
icon1 = 'special://home/addons/plugin.video.jami/resources/icon1.png'
icon2 = 'special://home/addons/plugin.video.jami/resources/icon2.png'
icon3 = 'special://home/addons/plugin.video.jami/resources/icon3.png'
icon4 = 'special://home/addons/plugin.video.jami/resources/icon4.png'
icon5 = 'special://home/addons/plugin.video.jami/resources/icon5.png'
icon6 = 'special://home/addons/plugin.video.jami/resources/icon6.png'
icon7 = 'special://home/addons/plugin.video.jami/resources/icon7.png'
icon8 = 'special://home/addons/plugin.video.jami/resources/icon8.png'
icon9 = 'special://home/addons/plugin.video.jami/resources/icon9.png'
icon10 = 'special://home/addons/plugin.video.jami/resources/icon10.png'
icon11 = 'special://home/addons/plugin.video.jami/resources/icon11.png'
icon12 = 'special://home/addons/plugin.video.jami/resources/icon12.png'
icon13 = 'special://home/addons/plugin.video.jami/resources/icon13.png'
icon14 = 'special://home/addons/plugin.video.jami/resources/icon14.png'
icon15 = 'special://home/addons/plugin.video.jami/resources/icon15.png'
icon16 = 'special://home/addons/plugin.video.jami/resources/icon16.png'
icon17 = 'special://home/addons/plugin.video.jami/resources/icon17.png'
icon18 = 'special://home/addons/plugin.video.jami/resources/icon18.png'
icon19 = 'special://home/addons/plugin.video.jami/resources/icon19.png'
icon20 = 'special://home/addons/plugin.video.jami/resources/icon20.png'
icon21 = 'special://home/addons/plugin.video.jami/resources/icon21.png'
icon22 = 'special://home/addons/plugin.video.jami/resources/icon22.png'
icon22a = 'special://home/addons/plugin.video.jami/resources/icon22a.png'
icon23 = 'special://home/addons/plugin.video.jami/resources/icon23.png'
icon23a = 'special://home/addons/plugin.video.jami/resources/icon23a.png'
icon24 = 'special://home/addons/plugin.video.jami/resources/icon24.png'
icon25 = 'special://home/addons/plugin.video.jami/resources/icon25.png'
icon26 = 'special://home/addons/plugin.video.jami/resources/icon26.png'


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
	plugintools.add_item(title = "Angry Birds", url = base + "playlist/PLVZggjiHl7zWTZDWcXNok7JFZUlb8vdHZ/", thumbnail = icon1, fanart = fan1, folder = True)
	plugintools.add_item(title = "Ruca - T01 a T24 [PT]", url = base + "playlist/PLsWbExGo1KPaYUuRSfzyF1X11Czip4259/", thumbnail = icon2, fanart = fan1, folder = True)
	plugintools.add_item(title = "Max - T01 a T05 [PT]", url = base + "playlist/PLsWbExGo1KPbil5fBWgJlv2gQPTcABI7x/", thumbnail = icon3, fanart = fan1, folder = True)
	plugintools.add_item(title = "Octonautas [PT]", url = base + "playlist/PLjRUOcyjSeAxv2ITxi2CVbNKUz-cK9YfA/", thumbnail = icon4, fanart = fan1, folder = True)
	plugintools.add_item(title = "Noddy [PT]", url = base + "playlist/PLrH5HKiu5jUeEVAVEctaHl1qud4zbYg5O/" , thumbnail = icon5, fanart = fan1, folder = True)	
	plugintools.add_item(title = "Pocoyo [PT]", url = base + "user/childrenvideos/", thumbnail = icon6, fanart = fan1, folder = True)
	plugintools.add_item(title = "Heidi 3D [PT]", url = base + "playlist/PLnp6B7ujCv2A8aaaa-6niKGW-SoChr88d/", thumbnail = icon7, fanart = fan1, folder = True)	
	plugintools.add_item(title = "Abelha Maia 3D [PT]", url = base + "playlist/PLTf5zA07OijMLjuAJGYQ_dT7s8fgo7kpN/", thumbnail = icon8, fanart = fan1, folder = True)
	plugintools.add_item(title = "Herois da Cidade [PT]", url = base + "playlist/PLFepGKlvmn74D95OwZkSSQR3uk4T2ReHD/", thumbnail = icon9, fanart = fan1, folder = True)
	plugintools.add_item(title = "Bob o Construtor [PT]", url = base + "playlist/PLrH5HKiu5jUd7KNHHylSmu_WvFZ1pyURq/", thumbnail = icon10, fanart = fan1, folder = True)
	plugintools.add_item(title = "Thomas e Amigos [PT]", url = base + "playlist/PLZ-7k3FZDGmm5XODLaqSXX98OME6gk6Um/", thumbnail = icon11, fanart = fan1, folder = True)
	plugintools.add_item(title = "Ovelha Choné - T01/T02", url = base + "playlist/PLsWbExGo1KParAPrKtn8aQfLnEFepaajb/", thumbnail = icon12, fanart = fan1, folder = True)
	plugintools.add_item(title = "Vila Moleza [PT]", url = base + "playlist/PLrH5HKiu5jUeWGDGh3EYBvMQ-eU1CSy4J/", thumbnail = icon13, fanart = fan1, folder = True)
	plugintools.add_item(title = "Panda e os Caricas [PT]", url = base + "channel/UCvw-R-r3p6Hc-yj1qyoPslQ/", thumbnail = icon14, fanart = fan1, folder = True)
	plugintools.add_item(title = "Xana Toc Toc [PT]", url = base + "user/XanaTocTocVEVO/", thumbnail = icon15, fanart = fan1, folder = True)
	plugintools.add_item(title = "Violeta [Musicais]", url = base + "playlist/PLE308E8FD36F34EAC/", thumbnail = icon16, fanart = fan1, folder = True)
	plugintools.add_item(title = "Turma da Mónica [BR]", url = base + "playlist/PLWduEF1R_tVZYNTH8ajFOEDkDT_hfIQL9/", thumbnail = icon17, fanart = fan1, folder = True)
	plugintools.add_item(title = "Charlie Brown [BR]", url = base + "playlist/PLolevrZYo2eGlwPrvK1Nr_rwUGSpbJMYK/", thumbnail = icon18, fanart = fan1, folder = True)
	plugintools.add_item(title = "Daniel Tigre [BR]", url = base + "playlist/PLoaBAxtZve6nmFuNHCmIRLz_bo2aCD4wX/", thumbnail = icon19, fanart = fan1, folder = True)
	plugintools.add_item(title = "Masha e o Urso [BR]", url = base + "playlist/PLsWbExGo1KPYsGKNTnOemWCEdxRNHJyRm/", thumbnail = icon20, fanart = fan1, folder = True)
	plugintools.add_item(title = "Jelly Jamm [BR]"  , url = base + "playlist/PL-CfLd2XMlrw7Cq-LT4UMNJrzLr9OjMpk/", thumbnail = icon21, fanart = fan1, folder = True)
	plugintools.add_item(title = "Sonic X [BR]", url = base + "playlist/PLj0Fsa9q1GRCKN_i_-1zRTM0m9m-GW6E1/", thumbnail = icon22, fanart = fan1, folder = True)
	plugintools.add_item(title = "Team Hot Wheels [BR]", url = base + "playlist/PLsWbExGo1KPb-TTwpvyEDIZa51JUYLr9l/", thumbnail = icon22a, fanart = fan1, folder = True)
	plugintools.add_item(title = "Tartarugas Ninja [PT]", url = base + "playlist/PL12TUMahWFQR6XqoHTKm5-RvCSYy1EPg1/", thumbnail = icon23, fanart = fan1, folder = True)
	plugintools.add_item(title = "Irmãos Grimm [PT]", url = base + "playlist/PLaerdHbAdrDIIi3LuIIdCRGdFoHe3lS_D/", thumbnail = icon23a, fanart = fan1, folder = True)
	plugintools.add_item(title = "Dartacão [PT]", url = base + "playlist/PLrH5HKiu5jUe8ZF8jwdtprpucMVEjRON5/", thumbnail = icon24, fanart = fan1, folder = True)
	plugintools.add_item(title = "Era uma vez - 4 Temporadas [PT]", url = base + "playlist/PLsWbExGo1KPZRlqvLY2Ja_SAJZMgBcdxD/", thumbnail = icon25, fanart = fan1, folder = True)
	plugintools.add_item(title = "Contos Infantis [PT]", url = base + "channel/UCOre4lsfRMaC62bOHUjPp2Q/", thumbnail = icon26, fanart = fan1, folder = True)
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
