# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/SIMPLEKODI
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.simplekodichristmas'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLJS-mPmTjx56KXB58hOSsF890siMODL6F"
YOUTUBE_CHANNEL_ID_2 = "PLJS-mPmTjx57nbLJ52MWpqDTKYkF8Tr7o"
YOUTUBE_CHANNEL_ID_3 = "PLJS-mPmTjx55YI36swpXv41upIzXQdsms"
YOUTUBE_CHANNEL_ID_4 = "PLJS-mPmTjx54QGvqY-5gdle_16CqnXIiS"
YOUTUBE_CHANNEL_ID_5 = "PLJS-mPmTjx55VjgzFjOzSlTRhJigRRCvI"

# Entry point
def run():
    plugintools.log("docu.run")
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Christmas Movies/TV Specials",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://i1.ytimg.com/vi/06zc5JllZC0/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christmas Music Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://i.ytimg.com/vi/QT03SvRpwWU/hqdefault.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Christmas Songs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://maryostudio.files.wordpress.com/2014/11/christmas-music.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Christmas Lights",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.ytimg.com/vi/zmZ2LZ-P830/maxresdefault.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Christmas Yule Log",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://www.goodwp.com/images/201412/goodwp.com_32133.jpg",
        folder=True )

run()