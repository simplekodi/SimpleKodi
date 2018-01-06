#######################################################################
#Import Modules Section
import xbmcplugin, xbmcaddon
import sys
import urllib
import re
import backuprestore
import base_info
import glo_var
import notify
import contact
from resources.libs import wizard as wiz
global parse


#######################################################################

#######################################################################
#Global Variables
#Do Not Edit These Variables or any others in this wizard!
AddonID        = glo_var.AddonID
ADDON          = xbmcaddon.Addon(id=AddonID)
ADULT          = base_info.getS('adult')
KRYPTON        = base_info.getS('krypton')
adult          = glo_var.ADULT
krypton        = glo_var.KRYPTON
ARTA           = glo_var.ADULT_ICON
ARTK           = glo_var.KRYPTON_ICON
ARTB           = glo_var.BACKUP_ICON
ARTBL          = glo_var.BACKUPLOGIN_ICON
ARTBU          = glo_var.BUILDS_ICON
ARTCI          = glo_var.CACHE_ICON
ARTCP          = glo_var.CONVERTPATH_ICON
ARTCR          = glo_var.CHKREPO_ICON
ARTCS          = glo_var.CHKSOURCE_ICON
ARTC           = glo_var.CREDIT_ICON
ARTDA          = glo_var.DELETEALL_ICON
ARTDB          = glo_var.DELETEBACKUP_ICON
ARTD           = glo_var.DEV_ICON
ARTF           = glo_var.FRESHSTART_ICON
ARTM           = glo_var.MAINT_ICON
ARTP           = glo_var.PACKAGES_ICON
ARTR           = glo_var.REST_ICON
ARTRB          = glo_var.RESTOREBACKUP_ICON
ARTRL          = glo_var.RESTORELOGIN_ICON
ARTSA          = glo_var.SAVE_ICON
ARTS           = glo_var.SUPPORT_ICON
ARTTH          = glo_var.THUMBNAILS_ICON
ARTT           = glo_var.THEME_ICON
ARTV           = glo_var.VIEWLOG_ICON
bub            = glo_var.BACKUPBUILD
bul            = glo_var.BACKUPLOGIN
build          = glo_var.BUILD
cc             = glo_var.CLEARCACHE
chkr           = glo_var.CHKREPO
chks           = glo_var.CHKSOURCE
con            = glo_var.CONVERT
CONT_NOT       = contact.CONT_NOT
CRED_NOT       = contact.CRED_NOT
cp             = glo_var.CLEARPACK
cr             = glo_var.COLOR
cr1            = glo_var.COLOR1
cr2            = glo_var.COLOR2
cr3            = glo_var.COLOR3
cr4            = glo_var.COLOR4
ct             = glo_var.CLEARTHUMB
dab            = glo_var.DELETEBACKUP
dabs           = glo_var.DELETEALL
dev            = glo_var.DEV
DEVELOPER      = base_info.getS('developer')
FANART         = glo_var.FANART
fs             = glo_var.FRESHSTART
gn             = glo_var.GROUP_NAME
ICON           = glo_var.ICON
ICONMAINT      = glo_var.ICONMAINT if not glo_var.ICONMAINT == 'http://' else ICON
ICONSAVE       = glo_var.ICONSAVE if not glo_var.ICONSAVE == 'http://' else ICON
KEEPFAVS       = base_info.getS('keepfavourites')
KEEPSOURCES    = base_info.getS('keepsources')
KEEPPROFILES   = base_info.getS('keepprofiles')
KEEPADVANCED   = base_info.getS('keepadvanced')
maint          = glo_var.MAINT
rbb            = glo_var.RESTOREBUILDBCK
rest           = glo_var.REST
rl             = glo_var.RESTORELOGIN
save           = glo_var.SAVE
theme          = glo_var.THEME
THEME          = base_info.getS('theme')
THEME1         = glo_var.THEME1
view           = glo_var.VIEW
VERSION        = ADDON.getAddonInfo('version')
ADDF           = base_info.addFile
ANDROID        = base_info.getS('android')
APKNAME        = glo_var.APKNAME
APK            = glo_var.APKFILE
ARTAPK         = glo_var.APK_ICON
apk            = base_info.getS('apk')
####################################################################################

###################################################################################
#Categories/Default Menu
def Categories():
    base_info.addDir(cr+gn+cr2+cr1+build+cr2,'url','builds',ARTBU,FANART,'') 
    if ADULT == 'true': base_info.addDir(cr+gn+cr2+cr1+adult+cr2,'url','adult',ARTA,FANART,'')
    if KRYPTON == 'true': base_info.addDir(cr+gn+cr2+cr1+krypton+cr2,'url','krypton',ARTK,FANART,'')	
    if THEME == 'true': base_info.addDir(cr+gn+cr2+cr1+theme+cr2,'url','thememenu',ARTT,FANART,'')
    if apk == 'true' : base_info.addDir(cr+gn+cr2+cr1+APKNAME+cr2,'url','apkinstaller',ARTAPK,FANART,'')	
    base_info.addDir(cr+gn+cr2+cr1+save+cr2,'url','savedata',ARTSA,FANART,'')
    base_info.addDir(cr+gn+cr2+cr1+rest+cr2,'url','restoremenu',ARTR,FANART,'')
    base_info.addDir(cr+gn+cr2+cr1+maint+cr2,'url','maint',ARTM,FANART,'')
    if DEVELOPER == 'true': base_info.addDir(cr+gn+cr2+cr1+dev+cr2,'url','developer',ARTD,FANART,'')    
    base_info.addDir2(cr+gn+cr2+cr1+'Contact Us'+cr2,'url','contact',ARTS,FANART,'')        
    base_info.addDir2(cr+gn+cr2+cr1+'Wizard Credits'+cr2,'url','wizcreds',ARTC,FANART,'') 
    xbmc.executebuiltin('Container.SetViewMode(50)')
###################################################################################

###################################################################################
#Adult Menu
def Adult_Menu():  
    link = base_info.OPEN_URL(glo_var.ADULTFILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,description in match:
        base_info.addDir2(name,url,'adultwiz',image,fanart,description)
        xbmc.executebuiltin('Container.SetViewMode(50)')
####################################################################################   

###################################################################################
#Krypton Build Menu
def Krypton_Menu():  
    link = base_info.OPEN_URL(glo_var.KRYPTONFILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,image,fanart,description in match:
        base_info.addDir2(name,url,'kryptonwiz',image,fanart,description)
        xbmc.executebuiltin('Container.SetViewMode(50)')
####################################################################################   

###################################################################################
#Backup Menu
def Backup_Menu():
    on = '[COLOR green]ON[/COLOR]'; off = '[COLOR red]OFF[/COLOR]'    
    sources    = 'true' if KEEPSOURCES   == 'true' else 'false'
    advanced   = 'true' if KEEPADVANCED  == 'true' else 'false'
    profiles   = 'true' if KEEPPROFILES  == 'true' else 'false'
    favourites = 'true' if KEEPFAVS      == 'true' else 'false'    
    base_info.addFile(cr+gn+cr2+cr1+'Keep \'Sources\': %s' % sources.replace('true',on).replace('false',off)           ,'togglesetting', 'keepsources',    icon=ICONSAVE,  themeit=THEME1)
    base_info.addFile(cr+gn+cr2+cr1+'Keep \'Profiles\': %s' % profiles.replace('true',on).replace('false',off)         ,'togglesetting', 'keepprofiles',   icon=ICONSAVE,  themeit=THEME1)
    base_info.addFile(cr+gn+cr2+cr1+'Keep \'Advancedsettings\': %s' % advanced.replace('true',on).replace('false',off) ,'togglesetting', 'keepadvanced',   icon=ICONSAVE,  themeit=THEME1)
    base_info.addFile(cr+gn+cr2+cr1+'Keep \'Favourites\': %s' % favourites.replace('true',on).replace('false',off)     ,'togglesetting', 'keepfavourites', icon=ICONSAVE,  themeit=THEME1)        
    base_info.addDir2(cr+gn+cr2+cr1+bul+cr2,'url','backupdata',ARTBL,FANART,'')	
    base_info.addDir2(cr+gn+cr2+cr1+bub+cr2,'url','backup',ARTB,FANART,'')
    base_info.addDir(cr+gn+cr2+cr1+dab+cr2,'url','deletesingle',ARTDB,FANART,'')
    base_info.addDir2(cr+gn+cr2+cr1+dabs+cr2,'url','deleteall',ARTDA,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')
####################################################################################	
		
###################################################################################
#Builds Menu
def Builds_Menu():
    #if ADULT == 'true': base_info.addDir(cr+gn+cr2+cr1+adult+cr2,'url','adult',ARTA,FANART,'')
    #if KRYPTON == 'true': base_info.addDir(cr+gn+cr2+cr1+krypton+cr2,'url','krypton',ARTK,FANART,'')
    link = base_info.OPEN_URL(glo_var.BASEURL + 'wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        base_info.addDir2(name,url,'install',iconimage,fanart,description)
        xbmc.executebuiltin('Container.SetViewMode(50)')        
####################################################################################    

###################################################################################
#Developer Menu
def Developer_Menu():
    base_info.addDir2(cr+gn+cr2+cr1+chkr+cr2,'url','checkrepos',ARTCR,FANART,'')         
    base_info.addDir2(cr+gn+cr2+cr1+chks+cr2,'url','checksources',ARTCS,FANART,'')  
    base_info.addDir2(cr+gn+cr2+cr1+con+cr2,'url','convertpath',ARTCP,FANART,'')
    base_info.addDir2(cr+gn+cr2+cr1+view+cr2,'url','viewlog',ARTV,FANART,'')
    ADDF('Advanced Settings',      'autoadvanced',      icon=ICONMAINT, themeit=THEME1)
    xbmc.executebuiltin('Container.SetViewMode(50)')
###################################################################################

###################################################################################
#Maintenance Menu
def Maintenance():
    base_info.addDir2(cr+gn+cr2+cr1+cc+cr2,'url','clearcache',ARTCI,FANART,'')
    base_info.addDir2(cr+gn+cr2+cr1+cp+cr2,'url','clearpackages',ARTP,FANART,'')     
    base_info.addDir2(cr+gn+cr2+cr1+ct+cr2,'url','clearthumb',ARTTH,FANART,'')	            
    base_info.addDir2(cr+gn+cr2+cr1+fs+cr2,'url','freshstart',ARTF,FANART,'')     
    xbmc.executebuiltin('Container.SetViewMode(50)')
####################################################################################

###################################################################################
#Restore Menu
def Restore_Menu():
    base_info.addDir(cr+gn+cr2+cr1+rbb+cr2,'url','restore',ARTRB,FANART,'')
    base_info.addDir(cr+gn+cr2+cr1+rl+cr2,'url','restoredata',ARTRL,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')
####################################################################################

###################################################################################
#Theme Menu
def Theme_Menu():
    link = base_info.OPEN_URL(glo_var.THEMEFILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        base_info.addDir2(name,url,'theme',iconimage,fanart,description)
    xbmc.executebuiltin('Container.SetViewMode(50)')
####################################################################################

####################################################################################
#apk menu
def apkMenu():
    link = base_info.OPEN_URL(APK).replace('\n','').replace('\r','').replace('\t','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"').findall(link)
    if len(match) > 0:
        for name, url, icon, fanart, adult, description in match:
            base_info.addFile(name, 'apkinstall', name, url, description=description, icon=icon, fanart=fanart, themeit=THEME1)
        else: base_info.loga("[APK Menu] ERROR: Invalid Format.")
    base_info.setView('files', 'viewType')
####################################################################################
	
####################################################################################
#Define Paramaters
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

params=get_params()
url         = None
name        = None
mode        = None
iconimage   = None
fanart      = None
description = None
try:     mode=urllib.unquote_plus(params["mode"])
except:  pass
try:     name=urllib.unquote_plus(params["name"])
except:  pass
try:     url=urllib.unquote_plus(params["url"])
except:  pass
try:     iconimage=urllib.unquote_plus(params["iconimage"])
except:  pass
try:     fanart=urllib.unquote_plus(params["fanart"])
except:  pass
try:     description=urllib.unquote_plus(params["description"])
except:  pass

base_info.loga('[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % (VERSION, mode if not mode == '' else None, name, url))

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if base_info.getS('auto-view')=='true':
        base_info.ebi("Container.SetViewMode(%s)" % base_info.getS(viewType) )
#######################################################################

#######################################################################
# Below we are creating the different modes
if mode==None               : Categories()
elif mode=='adult'          : Adult_Menu()
elif mode=='krypton'        : Krypton_Menu()
elif mode=='adultwiz'       : base_info.Wizard_Adult(name,url,description)
elif mode=='kryptonwiz'     : base_info.Wizard_Krypton(name,url,description)
elif mode=='backup'         : backuprestore.Backup()
elif mode=='backupdata'     : backuprestore.Backup_Login()
elif mode=='builds'         : Builds_Menu()
elif mode=='checkrepos'     : base_info.Broken_Repos()
elif mode=='checksources'   : base_info.Broken_Sources()
elif mode=='clearcache'     : base_info.Delete_Cache(url)
elif mode=='clearpackages'  : base_info.Delete_Packages(url)
elif mode=='clearthumb'     : base_info.Clear_Thumb()       
elif mode=='contact'        : contact.contact(CONT_NOT)
elif mode=='convertpath'    : backuprestore.Convert_Special(url)
elif mode=='delete'         : backuprestore.Delete_Backup(url)
elif mode=='deleteall'      : backuprestore.Delete_All_Backups()
elif mode=='deletesingle'   : backuprestore.ListBackDel()
elif mode=='developer'      : Developer_Menu()
elif mode=='forceclose'     : base_info.killxbmc()
elif mode=='freshstart'     : base_info.Fresh_Start()
elif mode=='install'        : base_info.Wizard(name,url,description)
elif mode=='maint'          : Maintenance()
elif mode=='restore'        : backuprestore.Restore()
elif mode=='restoredata'    : backuprestore.Restore_Login()
elif mode=='restorezip'     : backuprestore.Read_Zip(url)
elif mode=='restorelog'     : backuprestore.Read_Login_Data_Zip(url)
elif mode=='restoremenu'    : Restore_Menu()
elif mode=='savedata'       : Backup_Menu()
elif mode=='theme'          : base_info.Wizard_Theme(name,url,description)
elif mode=='thememenu'      : Theme_Menu()
elif mode=='togglesetting'  : base_info.setS(name, 'false' if base_info.getS(name) == 'true' else 'true'); base_info.ebi('Container.Refresh')
elif mode=='viewlog'        : base_info.viewLogFile()
elif mode=='wizcreds'       : contact.credits(CRED_NOT)
elif mode=='wizardupdate'   : base_info.wizardUpdate()
elif mode=='apkinstaller'   : apkMenu()
elif mode=='apkinstall'     : base_info.apkInstaller(name, url)
#######################################################################

#######################################################################
#End of Directory
xbmcplugin.endOfDirectory(int(sys.argv[1]))
#######################################################################