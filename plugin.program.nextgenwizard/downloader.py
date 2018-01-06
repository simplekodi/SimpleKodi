#######################################################################
#Import Modules Section
import xbmcgui
import urllib
import time
import glo_var
class customdownload(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
#######################################################################

#######################################################################
#Global Variables
#Do Not Edit These Variables or any others in this wizard!
cr                  = glo_var.COLOR
cr1                 = glo_var.COLOR1
cr2                 = glo_var.COLOR2
cr3                 = glo_var.COLOR3
cr4                 = glo_var.COLOR4
gn                  = glo_var.GROUP_NAME
#######################################################################

#######################################################################
# Creating Functions
def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("","",' ', ' ')
    dp.update(0)
    start_time=time.time()
    customdownload().retrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb, bs, fs, dp, start_time))
     
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60)
            string = cr1+'Brought to you by KoDiY Help and '+cr2+ cr+gn+cr2
            dp.update(percent, mbs, e,string)
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
			raise Exception("Canceled")
			dp.close()
#######################################################################