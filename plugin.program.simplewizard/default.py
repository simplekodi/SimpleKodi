#######################################################################
#Import Modules and or Scripts
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys
import shutil
import urllib2,urllib
import re
import extract
import time
import downloader
import plugintools
import zipfile
import ntpath
#######################################################################

#######################################################################
#Editable Global Variables
#######################################################################
#AddonID = This name MUST match your folder name and the addon id inside
#your addon.xml file. If it does not match it will not work.
AddonID      = 'plugin.program.simplewizard'
#######################################################################
#Version = This is the version you used inside your addon.xml file
VERSION      = "1.0.1"
#######################################################################
#EXAMPLE     = https://simplewizard.000webhostapp.com/Wizard/wizard.html
#BASEURL     = https://simplewizard.000webhostapp.com
#PATH        =                           			 /Wizard
#FILE        =                                              /wizard.html
PATH         = "Wizard"
#######################################################################
#ADDONTITLE = Title of your Addon goes here
ADDONTITLE   = 'Simple Wizard'
#######################################################################
#WIZARDFILE = This is a DIRECT link to your Wizard.txt file
WIZARDFILE   = 'https://simplewizard.000webhostapp.com/Wizard/wizard.html'
#######################################################################

#######################################################################
#Global Variables
#Do Not Edit These Variables
USER_AGENT   = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
dp           = xbmcgui.DialogProgress()
dialog       = xbmcgui.Dialog()
HOME         = xbmc.translatePath('special://home/')
USERDATA     = os.path.join(HOME,      'userdata')
ADDON        = xbmcaddon.Addon(id=AddonID)
ADDON_ID     = xbmcaddon.Addon().getAddonInfo('id')
ADDONDATA    = os.path.join(USERDATA,  'addon_data', ADDON_ID)
EXCLUDES     = [AddonID]
#######################################################################

#######################################################################
#Functions
def CATEGORIES():
    link = OPEN_URL('https://simplewizard.000webhostapp.com/Wizard/wizard.html').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')
    addDir('FRESH START','url',6,'','','')
        
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    
def wizard(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=aqua]Simple Wizard[/COLOR]","[COLOR=red]DOWNLOADING[/COLOR]",'', '[COLOR=orange]Please Wait[/COLOR]')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "Extracting Simple Kodi, Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    dialog = xbmcgui.Dialog()
    dialog.ok("DOWNLOAD COMPLETE! ", 'To ensure all changes are saved you must now close Kodi', 'Unplug your device  or switch off from the power outlet NOW and leave for 5 seconds before switching back on.')
    killxbmc()
        
def log(log):
    xbmc.log("[%s]: %s" % (ADDONTITLE, log))
    if not os.path.exists(ADDONDATA): os.makedirs(ADDONDATA)      
        
def killxbmc(over=None):
    if over: choice = 1
    else: choice = dialog.yesno('Force Close Kodi', 'You should Force Close Kodi for your changes to take effect.', 'Would you like to continue?', nolabel='Cancel',yeslabel='Force Close Kodi')
    if choice == 1:
        log("Force Closing Kodi: Platform[%s]" % str(platform()))
        os._exit(1)

def platform():
    if xbmc.getCondVisibility('system.platform.android'):   return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):   return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'): return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):     return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):    return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):     return 'ios'


def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="https://simplewizard.000webhostapp.com/pics/freshstart.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
             
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]    
        return param

def FRESHSTART(params):
    choice2 = xbmcgui.Dialog().yesno("Are you sure?", 'Are you sure you want to wipe this install?', '', 'All addons EXCLUDING SIMPLE WIZARD will be completely wiped!', yeslabel='Yes',nolabel='No')
    if choice2 == 0:
        return
    elif choice2 == 1:
        dp.create("Please Wait","FRESHSTART IN PROGRESS",'', 'Please Wait')
        try:
            for root, dirs, files in os.walk(HOME,topdown=True):
                dirs[:] = [d for d in dirs if d not in EXCLUDES]
                for name in files:
                    try:
                        os.remove(os.path.join(root,name))
                        os.rmdir(os.path.join(root,name))
                    except: pass
                        
                for name in dirs:
                    try: os.rmdir(os.path.join(root,name)); os.rmdir(root)
                    except: pass
        except: pass
    dialog.ok('Completed','FreashStart Successful, please restart Kodi for changes to take effect.','','')
    killxbmc()					  
			  
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None

try        : url=urllib.unquote_plus(params["url"])
except     : pass
try        : name=urllib.unquote_plus(params["name"])
except     : pass
try        : iconimage=urllib.unquote_plus(params["iconimage"])
except     : pass
try        : mode=int(params["mode"])
except     : pass
try        : fanart=urllib.unquote_plus(params["fanart"])
except     : pass
try        : description=urllib.unquote_plus(params["description"])
except     : pass
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )

if mode==None or url==None or len(url)<1     : CATEGORIES()
elif mode==1                                 : wizard(name,url,description)
elif mode==6                                 : FRESHSTART(params)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))