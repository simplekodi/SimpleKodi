#######################################################################
#Import Modules Section
import xbmcgui
import os 
import re
import glo_var
import base_info
#######################################################################

#######################################################################
#Global Variables
#Do Not Edit These Variables or any others in this wizard!
ART            = glo_var.ART
FANART         = glo_var.FANART
BACKGROUND     = glo_var.BACKGROUND if not glo_var.BACKGROUND == '' or not base_info.workingURL(glo_var.BACKGROUND) else FANART
CONTNOT        = base_info.getS('contnot')
CONT_NOT       = glo_var.SUPPORT
CONTNOTEDISMISS= base_info.getS('contnotedismiss')
CONTNOTEID     = base_info.getS('contnoteid')
cr             = glo_var.COLOR
cr1            = glo_var.COLOR1
cr2            = glo_var.COLOR2
cr3            = glo_var.COLOR3
cr4            = glo_var.COLOR4
CREDNOT        = base_info.getS('crednot')
CREDNOTEDISMISS= base_info.getS('crednotedismiss')
CREDNOTEID     = base_info.getS('crednoteid')
FONTHEADER     = glo_var.FONTHEADER if not glo_var.FONTHEADER == '' else "Font16"
FONTSETTINGS   = glo_var.FONTSETTINGS if not glo_var.FONTSETTINGS == '' else "Font14"
HEADERTYPE     = glo_var.HEADERTYPE if glo_var.HEADERTYPE == 'Image' else 'Text'
HEADERMESSAGE  = glo_var.HEADERMESSAGE
HEADERIMAGE    = glo_var.HEADERIMAGE
THEME          = glo_var.THEME1
#######################################################################

#######################################################################
#NOTIFICATIONS
ACTION_PREVIOUS_MENU 			=  10	## ESC action
ACTION_NAV_BACK 				=  92	## Backspace action
ACTION_MOVE_LEFT				=   1	## Left arrow key
ACTION_MOVE_RIGHT 				=   2	## Right arrow key
ACTION_MOVE_UP 					=   3	## Up arrow key
ACTION_MOVE_DOWN 				=   4	## Down arrow key
ACTION_MOUSE_WHEEL_UP 			= 104	## Mouse wheel up
ACTION_MOUSE_WHEEL_DOWN			= 105	## Mouse wheel down
ACTION_MOVE_MOUSE 				= 107	## Down arrow key
ACTION_SELECT_ITEM				=   7	## Number Pad Enter
ACTION_BACKSPACE				= 110	## ?
ACTION_MOUSE_LEFT_CLICK 		= 100
ACTION_MOUSE_LONG_CLICK 		= 108
#######################################################################
#Contact Code
def Contact_Notification(msg='', resize=False, L=0 ,T=0 ,W=1280 ,H=720 , TxtColor='0xFFFFFFFF', Font=FONTSETTINGS, BorderWidth=15):
	class MyWindow(xbmcgui.WindowDialog):
		scr={};
		def __init__(self,msg='',L=0,T=0,W=1280,H=720,TxtColor='0xFFFFFFFF',Font='font14',BorderWidth=10):
			image_path = os.path.join(ART, 'ContentPanel.png')
			self.border = xbmcgui.ControlImage(L,T,W,H, image_path)
			self.addControl(self.border)
			self.BG=xbmcgui.ControlImage(L+BorderWidth,T+BorderWidth,W-(BorderWidth*2),H-(BorderWidth*2), BACKGROUND, aspectRatio=0, colorDiffuse='0x9FFFFFFF')
			self.addControl(self.BG)
			#title
			if HEADERTYPE == 'Image':
				iLogoW=144; iLogoH=68
				self.iLogo=xbmcgui.ControlImage((L+(W/2))-(iLogoW/2),T+10,iLogoW,iLogoH,HEADERIMAGE,aspectRatio=0)
				self.addControl(self.iLogo); 
			else:
				title = HEADERMESSAGE
				times = int(float(FONTHEADER[-2:]))
				temp = title.replace('[', '<').replace(']', '>')
				temp = re.sub('<[^<]+?>', '', temp)
				title_width = len(str(temp))*(times - 1)
				title = THEME % title
				self.title=xbmcgui.ControlTextBox(L+(W-title_width)/2,T+BorderWidth,title_width,30,font=FONTHEADER,textColor='0xFF1E90FF')
				self.addControl(self.title)
				self.title.setText(title)
			#body
			msg = THEME % msg
			self.TxtMessage=xbmcgui.ControlTextBox(L+BorderWidth+10,T+30+BorderWidth,W-(BorderWidth*2)-20,H-(BorderWidth*2)-75,font=Font,textColor=TxtColor)
			self.addControl(self.TxtMessage)
			self.TxtMessage.setText(msg)
			#buttons
			focus=os.path.join(ART, 'button-focus_lightblue.png'); nofocus=os.path.join(ART, 'button-focus_grey.png')
			w1      = int((W-(BorderWidth*5))/3); h1 = 35
			t       = int(T+H-h1-(BorderWidth*1.5))
			space   = int(L+(BorderWidth*1.5))
			dismiss = int(space+w1+BorderWidth)
			later   = int(dismiss+w1+BorderWidth)
			
			self.buttonDismiss=xbmcgui.ControlButton(dismiss,t,w1,h1,cr+"Thank"+cr2,textColor="0xFF000000",focusedColor="0xFF000000",alignment=2,focusTexture=focus,noFocusTexture=nofocus)
			self.buttonRemindMe=xbmcgui.ControlButton(later,t,w1,h1,cr1+"You"+cr2,textColor="0xFF000000",focusedColor="0xFF000000",alignment=2,focusTexture=focus,noFocusTexture=nofocus)
			self.addControl(self.buttonDismiss); self.addControl(self.buttonRemindMe)
			self.buttonRemindMe.controlLeft(self.buttonDismiss); self.buttonRemindMe.controlRight(self.buttonDismiss)
			self.buttonDismiss.controlLeft(self.buttonRemindMe); self.buttonDismiss.controlRight(self.buttonRemindMe)
			self.setFocus(self.buttonRemindMe)

		def doRemindMeLater(self):
			base_info.loga("[Contact Notification] Remind Me Later")
			self.CloseWindow()

		def doDismiss(self):
			base_info.loga("[Contact Notification] Dismiss")
			self.CloseWindow()

		def onAction(self,action):
			try: F=self.getFocus()
			except: F=False
			if   action == ACTION_PREVIOUS_MENU: self.doRemindMeLater()
			elif action == ACTION_NAV_BACK: self.doRemindMeLater()

		def onControl(self,control):
			if   control==self.buttonRemindMe: self.doRemindMeLater()
			elif control== self.buttonDismiss: self.doDismiss()
			else:
				try:    self.setFocus(self.buttonRemindMe)
				except: pass

		def CloseWindow(self): self.close()
	if resize==False: maxW=1280; maxH=720; W=int(maxW/1.5); H=int(maxH/1.5); L=int((maxW-W)/2); T=int((maxH-H)/2); 
	TempWindow=MyWindow(msg=msg,L=L,T=T,W=W,H=H,TxtColor=TxtColor,Font=Font,BorderWidth=BorderWidth); 
	TempWindow.doModal()
	del TempWindow
def contact(msg='', TxtColor='0xFFFFFFFF', Font='font12', BorderWidth=10):
    base_info.loga("[Contact Notification] Started")
    url = base_info.workingURL(CONT_NOT)
    if url == True:
			link  = base_info.OPEN_URL(CONT_NOT).replace('\r','').replace('\t','')
			id, msg = link.split('|||')
			base_info.loga("[Contact Notification] id: %s" % str(int(id)))
			base_info.setS('contnoteid', str(int(id)))
			base_info.setS('contnotedismiss', 'false')
			Contact_Notification(msg=msg)
			base_info.loga("[Contact Notification] Complete")
    else: base_info.loga("[Contact Notification] URL(%s): %s" % (CONT_NOT, url))   
#######################################################################

#######################################################################
#Credits Code
def Credits_Notification(msg='', resize=False, L=0 ,T=0 ,W=1280 ,H=720 , TxtColor='0xFFFFFFFF', Font=FONTSETTINGS, BorderWidth=15):
	class MyWindow(xbmcgui.WindowDialog):
		scr={};
		def __init__(self,msg='',L=0,T=0,W=1280,H=720,TxtColor='0xFFFFFFFF',Font='font14',BorderWidth=10):
			image_path = os.path.join(ART, 'ContentPanel.png')
			self.border = xbmcgui.ControlImage(L,T,W,H, image_path)
			self.addControl(self.border)
			self.BG=xbmcgui.ControlImage(L+BorderWidth,T+BorderWidth,W-(BorderWidth*2),H-(BorderWidth*2), BACKGROUND, aspectRatio=0, colorDiffuse='0x9FFFFFFF')
			self.addControl(self.BG)
			#title
			if HEADERTYPE == 'Image':
				iLogoW=144; iLogoH=68
				self.iLogo=xbmcgui.ControlImage((L+(W/2))-(iLogoW/2),T+10,iLogoW,iLogoH,HEADERIMAGE,aspectRatio=0)
				self.addControl(self.iLogo); 
			else:
				title = HEADERMESSAGE
				times = int(float(FONTHEADER[-2:]))
				temp = title.replace('[', '<').replace(']', '>')
				temp = re.sub('<[^<]+?>', '', temp)
				title_width = len(str(temp))*(times - 1)
				title = THEME % title
				self.title=xbmcgui.ControlTextBox(L+(W-title_width)/2,T+BorderWidth,title_width,30,font=FONTHEADER,textColor='0xFF1E90FF')
				self.addControl(self.title)
				self.title.setText(title)
			#body
			msg = THEME % msg
			self.TxtMessage=xbmcgui.ControlTextBox(L+BorderWidth+10,T+30+BorderWidth,W-(BorderWidth*2)-20,H-(BorderWidth*2)-75,font=Font,textColor=TxtColor)
			self.addControl(self.TxtMessage)
			self.TxtMessage.setText(msg)
			#buttons
			focus=os.path.join(ART, 'button-focus_lightblue.png'); nofocus=os.path.join(ART, 'button-focus_grey.png')
			w1      = int((W-(BorderWidth*5))/3); h1 = 35
			t       = int(T+H-h1-(BorderWidth*1.5))
			space   = int(L+(BorderWidth*1.5))
			dismiss = int(space+w1+BorderWidth)
			later   = int(dismiss+w1+BorderWidth)
			
			self.buttonDismiss=xbmcgui.ControlButton(dismiss,t,w1,h1,cr+"Thank"+cr2,textColor="0xFF000000",focusedColor="0xFF000000",alignment=2,focusTexture=focus,noFocusTexture=nofocus)
			self.buttonRemindMe=xbmcgui.ControlButton(later,t,w1,h1,cr1+"You"+cr2,textColor="0xFF000000",focusedColor="0xFF000000",alignment=2,focusTexture=focus,noFocusTexture=nofocus)
			self.addControl(self.buttonDismiss); self.addControl(self.buttonRemindMe)
			self.buttonRemindMe.controlLeft(self.buttonDismiss); self.buttonRemindMe.controlRight(self.buttonDismiss)
			self.buttonDismiss.controlLeft(self.buttonRemindMe); self.buttonDismiss.controlRight(self.buttonRemindMe)
			self.setFocus(self.buttonRemindMe)

		def doRemindMeLater(self):
			base_info.loga("[Contact Notification] Remind Me Later")
			self.CloseWindow()

		def doDismiss(self):
			base_info.loga("[Contact Notification] Dismiss")
			self.CloseWindow()

		def onAction(self,action):
			try: F=self.getFocus()
			except: F=False
			if   action == ACTION_PREVIOUS_MENU: self.doRemindMeLater()
			elif action == ACTION_NAV_BACK: self.doRemindMeLater()

		def onControl(self,control):
			if   control==self.buttonRemindMe: self.doRemindMeLater()
			elif control== self.buttonDismiss: self.doDismiss()
			else:
				try:    self.setFocus(self.buttonRemindMe)
				except: pass

		def CloseWindow(self): self.close()
	if resize==False: maxW=1280; maxH=720; W=int(maxW/1.5); H=int(maxH/1.5); L=int((maxW-W)/2); T=int((maxH-H)/2); 
	TempWindow=MyWindow(msg=msg,L=L,T=T,W=W,H=H,TxtColor=TxtColor,Font=Font,BorderWidth=BorderWidth); 
	TempWindow.doModal()
	del TempWindow
CRED_NOT = ('http://lesismor.co.uk/version/credits.txt')
def credits(msg='', TxtColor='0xFFFFFFFF', Font='font12', BorderWidth=10):
    base_info.loga("[Credit Notification] Started")
    url = base_info.workingURL(CRED_NOT)
    if url == True:
			link  = base_info.OPEN_URL(CRED_NOT).replace('\r','').replace('\t','')
			id, msg = link.split('|||')
			base_info.loga("[Credit Notification] id: %s" % str(int(id)))
			base_info.setS('crednoteid', str(int(id)))
			base_info.setS('crednotedismiss', 'false')
			Credits_Notification(msg=msg)
			base_info.loga("[Credits Notification] Complete")
    else: base_info.loga("[Credits Notification] URL(%s): %s" % (CRED_NOT, url))
####################################################################### 