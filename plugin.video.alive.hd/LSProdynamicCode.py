# -*- coding: utf-8 -*-
#$pyFunction
import xbmcaddon, xbmcgui
def GetLSProData(page_data,Cookie_Jar,m):
 title = "[COLOR blue][B]Electronic Must-See Sets:[/B][/COLOR]"  
 line1 = "[COLOR lime][B]. Trance [/B][COLOR white][ Ticon @ Iboga Hologram Show [COLOR lime]2017[/COLOR] ] [/COLOR]"
 line2 = "[COLOR lime][B]. Techno [/B][COLOR white][ A.Paul @ Code FABRIK Madrid [COLOR lime]2017[/COLOR] ][/COLOR]"
 line3 = "[COLOR lime][B]. Gabber [/B][COLOR white][ Partyraiser @ Masters of Hardcore [COLOR lime]2017[/COLOR] ][/COLOR]"
 xbmcgui.Dialog().yesno(title, line1, line2, line3,' See ',' Must ',4000)
 return "http://frenchdj.atspace.tv/FMC/Alive.HD/Electronik/Electronik.xml"
