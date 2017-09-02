# -*- coding: utf-8 -*-
#$pyFunction
import xbmcaddon, xbmcgui
def GetLSProData(page_data,Cookie_Jar,m):
 title = "[COLOR blue][B]Portuguese Festivals Must-See Concerts:[/B][/COLOR]"  
 line1 = "[COLOR lime][B]. Primavera Sound [/B][COLOR white][ Arab Strap - Primavera Sound [COLOR lime]2017[/COLOR] ][/COLOR]"
 line2 = "[COLOR lime][B]. NOS Alive [/B][COLOR white][ Depeche Mode - NOS Alive [COLOR lime]2017[/COLOR] ][/COLOR]"
 line3 = "[COLOR lime][B]. SB/SR [/B][COLOR white][ Foals - Super Bock Super Rock [COLOR lime]2014[/COLOR] ][/COLOR]"
 xbmcgui.Dialog().ok(title, line1, line2, line3)
 return "http://frenchdj.atspace.tv/FMC/Alive.HD/Portuguese_Festivals/Portuguese_Festivals.xml"
