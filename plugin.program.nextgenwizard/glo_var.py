
#Import Modules 
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os

#######################################################################

# Global Variables 

AddonID             = xbmcaddon.Addon().getAddonInfo('id')
HOME                = xbmc.translatePath('special://home/')
ADDONS              = os.path.join(HOME,      'addons')
USERDATA            = os.path.join(HOME,      'userdata')
ADDON_DATA          = xbmc.translatePath(os.path.join(USERDATA,'addon_data'))
ownAddon            = xbmcaddon.Addon(id=AddonID)
URL                 = ownAddon.getSetting('URL')
ADDONTITLE          = ownAddon.getSetting('addontitle')
GROUP_NAME          = ownAddon.getSetting('groupname')
PATH                = ownAddon.getSetting('path')
EXCLUDES1           = ownAddon.getSetting('customexclude1')
EXCLUDES2           = ownAddon.getSetting('customexclude2')
EXCLUDES3           = ownAddon.getSetting('customexclude3')
EXCLUDES            = [AddonID,'script.module.requests','script.module.urllib3','script.module.chardet','script.module.idna','script.module.certifi','temp','backupdir',EXCLUDES1, EXCLUDES2, EXCLUDES3]
UPDATECHECK         = 0
AUTOUPDATE          = "Yes"
COLORA              = ownAddon.getSetting('colour1')
COLORB              = ownAddon.getSetting('colour2')
COLORC              = ownAddon.getSetting('colour3')
COLORD              = ownAddon.getSetting('colour4')
COLORE              = ownAddon.getSetting('colour5') 
COLOR               = '[COLOR '+COLORA+'][B]'
COLOR1              = '[COLOR '+COLORB+'][B]'
COLOR2              = '[/B][/COLOR]'
COLOR3              = '[COLOR '+COLORC+'][B]'
COLOR4              = '[COLOR '+COLORD+'][B]'
COLORNAME           = COLORE
ENABLE              = ownAddon.getSetting('enablenotify')

#DO NOT EDIT BASEURL, you dont need to edit the following fields if u retain file names

BASEURL             = URL + '/'
WIZVER              = BASEURL + 'wizver.txt'
ADULTFILE           = BASEURL + 'adult.txt'
KRYPTONFILE         = BASEURL + 'krypton.txt'
NOTIFICATION        = BASEURL + 'notify.txt'
SUPPORT             = BASEURL + 'support.txt'
THEMEFILE           = BASEURL + 'themes.txt'
VERSION             = BASEURL + 'version.txt'
WIZARDFILE          = BASEURL + 'wizard.txt'
APKFILE             = BASEURL + 'apk.txt'
###############################################################


#do not change the code for THEME
THEME1              = '[COLOR '+COLORNAME+'][B]%s[/B][/COLOR]'  
#Use either 'Text' or 'Image'
HEADERTYPE          = ownAddon.getSetting('header')
#Font size of header
FONTHEADER          = 'Font14'
#url to image if using Image 424x180
HEADERIMAGE         = ownAddon.getSetting('headerimage')
#Font for Notification Window
FONTSETTINGS        = 'Font12'
#Background for Notification Window
BACKGROUND          = ownAddon.getSetting('backnotify')

#######################################################################

#Menu Names are controlled here

ADULT               = ownAddon.getSetting('adultmenu')
KRYPTON             = ownAddon.getSetting('kryptonmenu')
BACKUPBUILD         = ownAddon.getSetting('backupbuild')
BACKUPLOGIN         = ownAddon.getSetting('backuplogin')
BUILD               = ownAddon.getSetting('buildmenu')
CHKREPO             = ownAddon.getSetting('checkrepo')
CHKSOURCE           = ownAddon.getSetting('checksource')
CLEARCACHE          = ownAddon.getSetting('clearcache')
CLEARPACK           = ownAddon.getSetting('clearpackages')
CLEARTHUMB          = ownAddon.getSetting('clearthumbnails')
CONVERT             = ownAddon.getSetting('convertpath')
DELETEALL           = ownAddon.getSetting('deleteall')
DELETEBACKUP        = ownAddon.getSetting('deletebackup')
DEV                 = ownAddon.getSetting('devmenu')
FRESHSTART          = ownAddon.getSetting('freshstart')
MAINT               = ownAddon.getSetting('maintmenu')
REST                = ownAddon.getSetting('restoredata')
RESTOREBUILDBCK     = ownAddon.getSetting('restorebackupdata')
RESTORELOGIN        = ownAddon.getSetting('restorelogindata')
SAVE                = ownAddon.getSetting('savemenu')
THEME               = ownAddon.getSetting('thememenu')
VIEW                = ownAddon.getSetting('viewlog')
APKNAME             = ownAddon.getSetting('apkinstal')
APK                 = ownAddon.getSetting('apk')
#######################################################################

#do not change ART as this will affect all images!
ART                 = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'resources/art/'))
#ART                 = xbmc.translatePath(os.path.join('profile://xbmc/addons/' + AddonID, 'resources/art/'))

#######################################################################

#Image ICON's are set below
ADULT_ICON          = ART + 'adult.png'
KRYPTON_ICON        = ART + 'krypton.png'
BACKUP_ICON         = ART + 'backupbuild.png'
BACKUPLOGIN_ICON    = ART + 'backuplogin.png'
BUILDS_ICON			= ART + 'builds.png'
CACHE_ICON          = ART + 'cache.png'
CHKREPO_ICON        = ART + 'repo.png'
CHKSOURCE_ICON      = ART + 'source.png'
CONVERTPATH_ICON    = ART + 'convert.png'
CREDIT_ICON         = ART + 'credits.png'
DELETEALL_ICON      = ART + 'deleteallbackups.png'
DELETEBACKUP_ICON   = ART + 'deletebackup.png'
DEV_ICON            = ART + 'developer.png'
FANART              = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID , 'fanart.jpg'))
FRESHSTART_ICON     = ART + 'freshstart.png'
ICON                = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
ICONSAVE            = ART + 'iconsave.png'
MAINT_ICON          = ART + 'maintenance.png'
PACKAGES_ICON       = ART + 'packages.png'
REST_ICON           = ART + 'restoredata.png'
RESTOREBACKUP_ICON  = ART + 'restorebackup.png'
RESTORELOGIN_ICON   = ART + 'restorelogin.png'
SAVE_ICON           = ART + 'save.png'
SUPPORT_ICON        = ART + 'contact.png'
THEME_ICON          = ART + 'themes.png'
THUMBNAILS_ICON     = ART + 'thumbnails.png'
VIEWLOG_ICON        = ART + 'viewlog.png'
ICONMAINT           = ART + 'maintenance.png'
APK_ICON            = ART + 'apk.png'
#######################################################################
#Global Variables, Do Not Edit These Variables

ADDON               = xbmcaddon.Addon(id=AddonID)
HOME                = xbmc.translatePath('special://home/')
ADDONS              = os.path.join(HOME,      'addons')
USERDATA            = os.path.join(HOME,      'userdata')
ADDON_DATA          = xbmc.translatePath(os.path.join(USERDATA,'addon_data'))
ADDON_ID            = xbmcaddon.Addon().getAddonInfo('id')
ADDONDATA           = os.path.join(USERDATA,  'addon_data', ADDON_ID)
DATABASE            = os.path.join(USERDATA,  'Database') 
DATABASES           = xbmc.translatePath(os.path.join(USERDATA,'Database'))
dialog              = xbmcgui.Dialog()
DIALOG              = xbmcgui.Dialog()
dp                  = xbmcgui.DialogProgress()
DP                  = xbmcgui.DialogProgress()
EXCLUDES_FOLDER     = xbmc.translatePath(os.path.join(USERDATA,'BACKUP'))
HEADERMESSAGE       = GROUP_NAME
LOG                 = xbmc.translatePath('special://logpath/')
NAVI                = xbmc.translatePath(os.path.join(ADDONS,'script.navi-x'))
PACKAGES            = xbmc.translatePath(os.path.join('special://home/addons/' + 'packages'))
PLUGIN              = os.path.join(ADDONS,    ADDON_ID)
selfAddon           = xbmcaddon.Addon(id=AddonID)
skin                = xbmc.getSkinDir()
THUMBS              = os.path.join(USERDATA,  'Thumbnails')
USER_AGENT          = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
USB                 = xbmc.translatePath(os.path.join(HOME,'backupdir'))
ADVANCEDFILE        = 'http://'
#######################################################################