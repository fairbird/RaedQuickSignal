#!/usr/bin/python
# -*- coding: utf-8 -*-
#RAEDQuickSignal (c) RAED 07-02-2014
#Thank's mfaraj for help

# python3
from __future__ import print_function

from Components.config import config, getConfigListEntry, ConfigText, ConfigSelection, ConfigSubsection, ConfigYesNo, configfile, NoSave
from Components.ConfigList import ConfigListScreen
from Components.ActionMap import ActionMap
from GlobalActions import globalActionMap
from enigma import eTimer, getDesktop, gFont, addFont
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from Screens.Standby import TryQuitMainloop
from Screens.ChannelSelection import ChannelSelection
from Screens.MessageBox import MessageBox
from Tools.Directories import fileExists
from Components.Sources.StaticText import StaticText
from Tools.Directories import *
from Components.config import *
from Screens.InputBox import InputBox
from Components.MenuList import MenuList
from Components.Label import Label
from datetime import datetime
import os, re, gettext
from os import environ
from Screens.ChoiceBox import ChoiceBox
from Components.Pixmap import Pixmap
from Tools.LoadPixmap import LoadPixmap
try:
        from keymapparser import readKeymap
except:
        from Components.ActionMap import loadKeymap as readKeymap
# import as python3 from plugin
from .tools.configs import *
from .tools.compat import PY3
from .tools.compat import compat_urlopen
from .tools.compat import compat_Request
from .tools.compat import compat_URLError
from .tools.Console import Console
from os import path as os_path, remove as os_remove
from six.moves.urllib.request import urlretrieve
        
#lang = language.getLanguage()
#environ["LANGUAGE"] = lang[:2]
#gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
#gettext.textdomain("enigma2")
#gettext.bindtextdomain("RaedQuickSignal", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/RaedQuickSignal/locale/"))

#def _(txt):
#       t = gettext.dgettext("RaedQuickSignal", txt)
#       if t == txt:
#               t = gettext.gettext(txt)
#       return t

### images path
BRANATV="/usr/lib/enigma2/python/boxbranding.so"
BRANDOPENPY="/usr/lib/enigma2/python/Tools/StbHardware.py"
BRANDOPENPYC="/usr/lib/enigma2/python/Tools/StbHardware.pyc"
BRANDOPENPYO="/usr/lib/enigma2/python/Tools/StbHardware.pyo"
OPENBH="/usr/lib/enigma2/python/Screens/BpBlue.py"
OPENBH2="/usr/lib/enigma2/python/Screens/BpBlue.pyc"
OPENVIX="/usr/lib/enigma2/python/Plugins/SystemPlugins/ViX"
BRANDVU="/proc/stb/info/vumodel"
### Satfinder path
Satfinderpy=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Satfinder/plugin.py")
Satfinderpyc=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Satfinder/plugin.pyc")
Satfinderpyo=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Satfinder/plugin.pyo")
### Signalfinder path
Signalfinderpy=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Signalfinder/plugin.py")
Signalfinderpyc=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Signalfinder/plugin.pyc")
Signalfinderpyo=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Signalfinder/plugin.pyo")
### PositionerSetup path
Positionerpy=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/PositionerSetup/plugin.py")
Positionerpyc=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/PositionerSetup/plugin.pyc")
Positionerpyo=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/PositionerSetup/plugin.pyo")
### Plugin path
IMAGEPLUGIN=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/images/")
PREVIEWPIC=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/images/preview/")
### picon color
COLOREPLUGIN=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/PICONS/")

try: # This is for OpenBH + OpenVIX images
        from Plugins.SystemPlugins.AutoBouquetsMaker.scanner import dvbreader
        dvbreader_available = True
except ImportError:
        print("[Satfinder] import dvbreader not available")
        dvbreader_available = False

def removeunicode(data):
        try:
            try:
                data = data.encode('utf', 'ignore')
            except:
                pass
            data = data.decode('unicode_escape').encode('ascii', 'replace').replace('?', '').strip()
        except:
            pass
        return data

def getversioninfo():
    currversion='1.0'
    version_file=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/tools/version")
    if os_path.exists(version_file):
        try:
            fp=open(version_file, 'r').readlines()
            for line in fp:
                if 'version' in line:
                    currversion=line.split('=')[1].strip()
        except:
            pass
    return (currversion)

VER = getversioninfo()

def trace_error():
    import sys
    import traceback
    try:
        traceback.print_exc(file=sys.stdout)
        traceback.print_exc(file=open('/tmp/RaedQuickSignal.log', 'a'))
    except:
        pass

def logdata(label_name = '', data = None):
    try:
        data=str(data)
        fp = open('/tmp/RaedQuickSignal.log', 'a')
        fp.write( str(label_name) + ' : ' + data+"\n")
        fp.close()
    except:
        trace_error()    
        pass

def dellog(label_name = '', data = None):
    try:
        if os_path.exists('/tmp/RaedQuickSignal.log'):
                os_remove('/tmp/RaedQuickSignal.log')
    except:
        pass

def getSatfinderinfo():
    infofile=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Satfinder/LICENSE")
    if os_path.exists(infofile):
        fp=open(infofile, 'r').readlines()
        for line in fp:
                if 'RAED' in line:
                        return getSatfinderinfo

def DreamOS():
    if os_path.exists('/var/lib/dpkg/status'):
        return DreamOS

def BHVU():
    if os_path.exists('/proc/stb/info/vumodel') and os_path.exists('/usr/lib/enigma2/python/Blackhole'):
        return BHVU

def VTI():
    VTI = resolveFilename(SCOPE_PLUGINS, "SystemPlugins/VTIPanel/plugin.pyo")
    if os_path.exists(VTI):
        return VTI

def getDesktopSize():
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1280

if isHD():
        from .screens.skinHD import *
else:
        from .screens.skinFHD import *

##############################################################################
#if isHD():
#        Space = "             "
#        SKIN_setup = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Setup.xml")
#        SKIN_WeatherLocation = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/WeatherLocation.xml")
#        SKIN_AGC_Picon = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Picon.xml")
#        SKIN_AGC_Event_Des = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Event_Des.xml")
#        SKIN_AGC_Weather = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Weather.xml")
#        SKIN_Event_Progress_Picon = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Picon.xml")
#        SKIN_Event_Progress_Event_Des = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Event_Des.xml")
#        SKIN_Event_Progress_Weather = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Weather.xml")
#        SKIN_AGC_Picon_media = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Picon_media.xml"
#        SKIN_Event_Progress_Picon_media = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Picon_media.xml")
#else:
#        Space = "                                          "
#        SKIN_setup = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Setup_FHD.xml")
#        SKIN_WeatherLocation = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/WeatherLocation.xml")
#        SKIN_AGC_Picon = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Picon_FHD.xml")
#        SKIN_AGC_Event_Des = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Event_Des_FHD.xml")
#        SKIN_AGC_Weather = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Weather_FHD.xml")
#        SKIN_Event_Progress_Picon = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Picon_FHD.xml")
#        SKIN_Event_Progress_Event_Des = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Event_Des_FHD.xml")
#        SKIN_Event_Progress_Weather = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Weather_FHD.xml")
#        SKIN_AGC_Picon_media = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Picon_media_FHD.xml")
#        SKIN_Event_Progress_Picon_media = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Picon_media_FHD.xml")
##############################################################################

import gettext
REDC =  '\033[31m'
ENDC = '\033[m'

def cprint(text):
    print(REDC+"[RaedQuickSignal] "+text+ENDC)

def downloadFile(url, filePath):
    try:
        # Download the file from `url` and save it locally under `file_name`:
        urlretrieve(url, filePath)
        return True
        req = compat_Request(url)
        response = compat_urlopen(req)         
        cprint("response.read",response.read())
        output = open(filePath, 'wb')
        output.write(response.read())
        output.close()
        response.close()
        return True
    except compat_URLError as e:
        trace_error()
        if hasattr(e, 'code'):
            cprint('We failed with error code - %s.' % e.code)
        elif hasattr(e, 'reason'):
            cprint('We failed to reach a server.')
            cprint('Reason: %s' % e.reason)
    return False

def readurl(url):
    try:
        req = compat_Request(url)
        response = compat_urlopen(req)
        data = response.read()
        response.close()
        cprint("[data %s]" % data)
        return data
    except compat_URLError as e:
        if hasattr(e, 'code'):
            cprint('We failed with error code - %s.' % e.code)
        elif hasattr(e, 'reason'):
            cprint('We failed to reach a server.')
            cprint('Reason: %s' % e.reason)

def getcities(weather_location):

    import requests,re
    S = requests.Session()
    url = (b"http://www.geonames.org/advanced-search.html?q=&country=%s&featureClass=P&startRow=".decode("utf-8")) % str(weather_location.upper())
    pages = range(0, 1501, 50) ## change 1501 as page you want
    try:
        cities=[]
        for page in pages:
                ##Change the startRow in the URL
                url_2 = url.replace("startRow=","startRow="+str(page))
                request = requests.get(url_2)
                if request.status_code == 200:
                        data = S.get(url_2, verify=False).content.decode('ascii', 'ignore')
                        blocks = str(data).split('alt="P">')
                        blocks.pop(0)
                        for block in blocks:
                                regx='''<a href="(.*?)">.*?</a>'''
                                href = re.findall(regx, block)[0]
                                cityName = os.path.split(href)[1].replace(".html","").replace("-"," ").lstrip(' ')
                                #cityName = re.findall(str(regx), str(block), re.M|re.I)[0]#.replace(".html","").split("_%", 1)[0].split("%", 1)[0]
                                cities.append(cityName)
                        cities.sort()
    except Exception as error:
                cprint('excepyion',str(error))
                trace_error()
    cities.sort()
    return cities

##### Old
        #url = (b"http://www.geonames.org/advanced-search.html?q=&country=%s&featureClass=P&continentCode=".decode("utf-8")) % str(weather_location.upper())
        #data = readurl(url)
        #if data == None:
        #        return []
        #try:
        #        regx='''<a href="(.*?)"><img src=".*?" border="0" alt=".*?"></a>'''
        #        match = re.findall(str(regx), str(data), re.M|re.I)
        #        cities = []
        #        for cityURL in match:
        #            cityName = os.path.split(cityURL)[1].replace(".html","").split("_%", 1)[0].split("%", 1)[0]    
        #            if cityName in cities:
        #                continue
        #            cities.append(cityName)
        #        cities.sort()
        #        return cities
        #except Exception as error:
        #        trace_error()

class RAED_ChannelSelection(ChannelSelection):
    def __init__(self, session):
        ChannelSelection.__init__(self, session)


class WeatherLocationChoiceList(Screen):
        def __init__(self, session, country):
                self.skin = SKIN_WeatherLocation
                #with open(SKIN_WeatherLocation, 'r') as f:
                #     self.skin = f.read()
                #     f.close()
                self.session = session
                self.country = country
                list = []
                Screen.__init__(self, session)
                self.title = _(country)
                self["choicelist"] = MenuList(list)
                self["key_red"] = Label(_("%s") % title14)
                self["key_green"] = Label(_("%s") % title15)
                self["myActionMap"] = ActionMap(["SetupActions", "ColorActions"],
                {
                        "ok": self.keyOk,
                        "green": self.add_city,
                        "cancel": self.keyCancel,
                        "red": self.keyCancel,
                }, -1)
                #self.iConsole = iConsole()
                self.timer = eTimer()
                try:
                        self.timer.callback.append(self.createChoiceList)
                except:
                        self.timer_conn = self.timer.timeout.connect(self.createChoiceList)
                self.timer.start(5, False)

        def createChoiceList(self):
                self.timer.stop()
                clist = []
                clist=getcities(self.country)
                self["choicelist"].l.setList(clist)

        def control_xml(self, result, retval, extra_args):
                if retval != 0:
                        self.write_none()

        def write_none(self):
                with open('/tmp/weathermsn.xml', 'w') as noneweather:
                        noneweather.write('None')
                noneweather.close()

        def get_xmlfile(self,weather_city,weather_location):
                degreetype = config.plugins.RaedQuickSignal.degreetype.value
                weather_city = removeunicode(weather_city)
                weather_city = weather_city.decode("utf-8").replace(" ","_")
                url = "http://weather.service.msn.com/data.aspx?weadegreetype=%s&culture=%s&weasearchstr=%s&src=outlook" % (degreetype, weather_location, weather_city)
                logdata('url',url)
                file_name ='/tmp/weathermsn.xml'
                # Download the file from `url` and save it locally under `file_name`:
                try:
                       ret=downloadFile(url, file_name)
                       return ret
                except Exception as error:### new
                       trace_error()
                       return False
                #self.iConsole.ePopen("wget -P /tmp -T2 "http://weather.service.msn.com/data.aspx?weadegreetype=%s&culture=%s&weasearchstr=%s&src=outlook" -O /tmp/weathermsn.xml" % (degreetype, weather_location, weather_city), self.control_xml)

        def add_city(self):
                 from Screens.VirtualKeyBoard import VirtualKeyBoard
                 self.session.openWithCallback(self.cityCallback, VirtualKeyBoard, title=_("%s") % title16, text="%s" % title17)

                 #self.session.openWithCallback(self.cityCallback, InputBox, title=_("%s") % title16, text="%s" % title17, maxSize=False, visible_width =250)

        def cityCallback(self,city=None):
                try:
                        if os_path.exists('/tmp/weathermsn.xml'):
                                os_remove('/tmp/weathermsn.xml')
                        returnValue = city
                        countryCode=self.country.lower()+"-"+self.country.upper()
                        if self.get_xmlfile(returnValue,countryCode)==False:
                                self.session.open(MessageBox, _("%s") % title18,MessageBox.TYPE_ERROR)
                                return 
                        if not fileExists('/tmp/weathermsn.xml'):
                                self.write_none()
                                self.session.open(MessageBox, _("%s") % title19,MessageBox.TYPE_ERROR)
                                return None
                        if returnValue != None:
                                self.close(returnValue)
                        else:
                                self.keyCancel()
                except Exception as error:
                        trace_error()

        def keyOk(self):
                try:
                        if os_path.exists('/tmp/weathermsn.xml'):
                                os_remove('/tmp/weathermsn.xml')
                        returnValue = self["choicelist"].l.getCurrentSelection()
                        countryCode=self.country.lower()+"-"+self.country.upper()
                        if self.get_xmlfile(returnValue,countryCode)==False:
                                self.session.open(MessageBox, _("%s") % title20,MessageBox.TYPE_ERROR)
                                return 
                        if not fileExists('/tmp/weathermsn.xml'):
                                self.write_none()
                                self.session.open(MessageBox, _("%s") % title20,MessageBox.TYPE_ERROR)
                                return None
                        if returnValue != None:
                                self.close(returnValue)
                        else:
                                self.keyCancel()
                except Exception as error:
                        trace_error()

        def keyCancel(self):
                self.close(None)

class RaedQuickSignalScreen(Screen):
        def __init__(self, session):
                Screen.__init__(self, session)
                dellog()

                ## Add Fonts codes
                if config.plugins.RaedQuickSignal.fontsSize.value == "Default":
                        fontSize = 100
                else:
                        fontSize = config.plugins.RaedQuickSignal.fontsSize.value
                #try:
                #        fontfile = config.plugins.RaedQuickSignal.fontsStyle.value
                #except:
                #        fontfile = IMAGEPLUGIN + 'nmsbd.ttf'
                #addFont(fontfile, 'RSQFont', int(fontSize), 1)
                ## End Add Fonts codes

                if config.plugins.RaedQuickSignal.style.value == "AGC1":
                        if config.plugins.RaedQuickSignal.piconpath.value == "PLUGIN":
                             if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                                   self.skin = SKIN_AGC_Picon_SNRdB
                             else:
                                   self.skin = SKIN_AGC_Picon_NOSNRdB
                        elif config.plugins.RaedQuickSignal.piconpath.value == "MEDIA":
                             if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                                   self.skin = SKIN_AGC_Picon_media_SNRdB
                             else:
                                   self.skin = SKIN_AGC_Picon_media_NOSNRdB
                elif config.plugins.RaedQuickSignal.style.value == "AGC2":
                        if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                             self.skin = SKIN_AGC_Event_Des_SNRdB
                        else:
                             self.skin = SKIN_AGC_Event_Des_NOSNRdB
                elif config.plugins.RaedQuickSignal.style.value == "AGC3":
                        if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                             self.skin = SKIN_AGC_Weather_SNRdB
                        else:
                             self.skin = SKIN_AGC_Weather_NOSNRdB
                elif config.plugins.RaedQuickSignal.style.value == "Event1":
                        if config.plugins.RaedQuickSignal.piconpath.value == "PLUGIN":
                             if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                                   self.skin = SKIN_Event_Progress_Picon_SNRdB
                             else:
                                   self.skin = SKIN_Event_Progress_Picon_NOSNRdB
                        elif config.plugins.RaedQuickSignal.piconpath.value == "MEDIA":
                             if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                                   self.skin = SKIN_Event_Progress_Picon_media_SNRdB
                             else:
                                   self.skin = SKIN_Event_Progress_Picon_media_NOSNRdB
                elif config.plugins.RaedQuickSignal.style.value == "Event2":
                        if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                             self.skin = SKIN_Event_Progress_Event_Des_SNRdB
                        else:
                             self.skin = SKIN_Event_Progress_Event_Des_NOSNRdB
                elif config.plugins.RaedQuickSignal.style.value == "Event3":
                        if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                             self.skin = SKIN_Event_Progress_Weather_SNRdB
                        else:
                             self.skin = SKIN_Event_Progress_Weather_NOSNRdB
                elif config.plugins.RaedQuickSignal.style.value == "Full1":
                        self.skin = SKIN_Full_Screen1
                elif config.plugins.RaedQuickSignal.style.value == "Full2":
                        if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                             self.skin = SKIN_Full_Screen2_SNRdB
                        else:
                             self.skin = SKIN_Full_Screen2_NOSNRdB
                elif config.plugins.RaedQuickSignal.style.value == "Full3":
                        if config.plugins.RaedQuickSignal.piconpath.value == "PLUGIN":
                                self.skin = SKIN_Full_Screen_Picon_Vertical
                        elif config.plugins.RaedQuickSignal.piconpath.value == "MEDIA":
                                self.skin = SKIN_Full_Screen_Picon_media_Vertical
                elif config.plugins.RaedQuickSignal.style.value == "Full4":
                        if config.plugins.RaedQuickSignal.piconpath.value == "PLUGIN":
                                self.skin = SKIN_Full_Screen_Picon_Ecm1_Vertical
                        elif config.plugins.RaedQuickSignal.piconpath.value == "MEDIA":
                                self.skin = SKIN_Full_Screen_Picon_media_Ecm1_Vertical
                elif config.plugins.RaedQuickSignal.style.value == "Full5":
                        if config.plugins.RaedQuickSignal.piconpath.value == "PLUGIN":
                                self.skin = SKIN_Full_Screen_Picon_Ecm2_Vertical
                        elif config.plugins.RaedQuickSignal.piconpath.value == "MEDIA":
                                self.skin = SKIN_Full_Screen_Picon_media_Ecm2_Vertical
                elif config.plugins.RaedQuickSignal.style.value == "Full6":
                        if config.plugins.RaedQuickSignal.piconpath.value == "PLUGIN":
                                self.skin = SKIN_Full_Screen_Picon_Ecm3_Vertical
                        elif config.plugins.RaedQuickSignal.piconpath.value == "MEDIA":
                                self.skin = SKIN_Full_Screen_Picon_media_Ecm3_Vertical
                elif config.plugins.RaedQuickSignal.style.value == "SNR_ANALOG":
                        if config.plugins.RaedQuickSignal.piconpath.value == "PLUGIN":
                                self.skin = SKIN_Full_Screen_Picon_Ecm3_SNR_ANALOG
                        elif config.plugins.RaedQuickSignal.piconpath.value == "MEDIA":
                                self.skin = SKIN_Full_Screen_Picon_media_Ecm3_SNR_ANALOG
                self.session = session
                if not DreamOS() and not BHVU():
                        self.startupservice = config.servicelist.startupservice.value
                        sref = self.session.nav.getCurrentService()
                        from ServiceReference import ServiceReference
                        p = ServiceReference(str(sref))
                        servicename = str(p.getServiceName())
                        serviceurl = p.getPath()
                        config.servicelist.startupservice.value = serviceurl
                        config.servicelist.startupservice.save()
                if fileExists(OPENBH) or fileExists(OPENBH2) or fileExists(OPENVIX):
                        self.servicelist = self.session.instantiateDialog(RAED_ChannelSelection)
                else:
                        self.servicelist = self.session.instantiateDialog(ChannelSelection)
                self["setupActions"] = ActionMap(["WizardActions", "SetupActions", "MenuActions", "ColorActions"],
                    {
                         "cancel": self.exit,
                         "menu":self.showsetup,
                         "up": self.keyUp,
                         "down": self.keyDown,
                         "left": self.keyLeft,
                         "right": self.keyRight,
                         "yellow": self.keyyellow,
                         "blue": self.keyblue,
                    })
                shown=True
                #self.onLayoutFinish.append(self.layoutFinished)
                # open source and DreamOS
                if os.path.exists(Satfinderpy) or os.path.exists(Satfinderpyo) or os.path.exists(Satfinderpyc):
                        if BHVU() or VTI():
                                self["Satfinder"] = Label(_(" "))
                                logdata("Label Key_blue: SatFinder does not support Scan feature (VU+ BH/VTI)\n")
                        elif getSatfinderinfo() or os.path.exists(BRANDOPENPYO) or os.path.exists(BRANDOPENPY) or os.path.exists(BRANDOPENPYC):
                                self["Satfinder"] = Label("%s" % title77)
                        else:
                                self["Satfinder"] = Label(_(" "))
                                logdata("Label Key_blue: SatFinder does not support Scan feature\n")
                # VU+ (BH & VTI)
                elif os.path.exists(Signalfinderpy) or os.path.exists(Signalfinderpyo) or os.path.exists(Signalfinderpyc):
                        if BHVU() or VTI():
                                self["Satfinder"] = Label("%s" % title78)
                        else:
                                self["Satfinder"] = Label(_(" "))
                                logdata("Label Key_blue: Signalfinder does not support Scan feature\n")
                else:
                        self["Satfinder"] = Label(_(" "))
                        logdata("Label Key_blue: Satfinder Not Installed\n")

                if os.path.exists(Positionerpy) or os.path.exists(Positionerpyo) or os.path.exists(Positionerpyc):
                        self["Positioner"] = Label("%s" % title79)
                else:
                        self["Positioner"] = Label(_(" "))
                        logdata("Label Key_yellow: PositionerSetup Not Installed\n")
                self.onShown.append(self.onWindowShow)

        def onWindowShow(self):
                self.onShown.remove(self.onWindowShow)
                self.instance.show()
                #self.setTitle("QuickSignal by RAED V" + str(VER + Space + datetime_now))
                self.setTitle("%s%s" % (title21, VER))
                self.new_version = VER
                updateOnline = config.plugins.RaedQuickSignal.updateonline.value
                if updateOnline:
                         self.checkupdates()
                cfile = open("/tmp/.RaedQuickSignal","w")
                cfile.close()

        #def layoutFinished(self):
        #        self.instance.show()
                #self.setTitle("QuickSignal by RAED V" + str(VER + Space + datetime_now))
        #        self.setTitle(_("RaedQuickSignal V %s") % VER)
        #        self.new_version = VER
        #        if config.plugins.RaedQuickSignal.updateonline.value:
        #                 self.checkupdates()
        #        cfile = open("/tmp/.RaedQuickSignal","w")
        #        cfile.close()

        def keyyellow(self):
                try:
                        if os.path.exists(Positionerpy) or os.path.exists(Positionerpyo) or os.path.exists(Positionerpyc):
                                try:
                                        from Plugins.SystemPlugins.PositionerSetup.ui import PositionerSetup
                                except:
                                        from Plugins.SystemPlugins.PositionerSetup.plugin import PositionerSetup
                                from Components.NimManager import nimmanager
                                nimList = nimmanager.getNimListOfType('DVB-S')
                                if len(nimList) == 0:
                                        self.session.open(MessageBox, _('%s') % title22, MessageBox.TYPE_ERROR)
                                else:
                                        usableNims = []
                                        for x in nimList:
                                                configured_rotor_sats = nimmanager.getRotorSatListForNim(x)
                                                if len(configured_rotor_sats) != 0:
                                                        usableNims.append(x)

                                        if len(usableNims) == 1:
                                                self.session.open(PositionerSetup, usableNims[0])
                                        else:
                                                self.session.open(MessageBox, _('%s') % title23, MessageBox.TYPE_ERROR)
                        else:
                                logdata("keyyellow: positioner Not Installed\n")
                except Exception as error:
                       trace_error()

        def keyblue(self):
                try:
                        if os.path.exists(Satfinderpy) or os.path.exists(Satfinderpyo) or os.path.exists(Satfinderpyc) or os.path.exists(Signalfinderpy) or os.path.exists(Signalfinderpyo) or os.path.exists(Signalfinderpyc): # Satfinder
                                from Components.NimManager import nimmanager
                                if not BHVU() and (getSatfinderinfo() or os.path.exists(BRANDOPENPYO) or os.path.exists(BRANDOPENPY) or os.path.exists(BRANDOPENPYC)):
                                        from Plugins.SystemPlugins.Satfinder.plugin import Satfinder
                                        nimList = []
                                        if DreamOS(): # DreamOS
                                                logdata("keyblue: Open Satfinder DreamOS\n")
                                                nims = nimmanager.getNimListOfType("DVB-S")
                                                for x in nims:
                                                        nim = nimmanager.getNimConfig(x)
                                                        if not nim.sat.configMode.value in ("loopthrough", "satposdepends", "nothing"):
                                                                nimList.append(x)

                                                if len(nimList) == 0:
                                                        self.session.open(MessageBox, _("%s") % title24, MessageBox.TYPE_ERROR)
                                                else:
                                                        if len(nimList) == 1:
                                                                self.session.open(Satfinder, nimList[0])
                                                        else:
                                                                self.session.open(Satfinder)
                                        else:
                                                nims = nimmanager.nim_slots
                                                try: # OpenATV
                                                        logdata("keyblue: Open Satfinder OpenATV\n")
                                                        for n in nims:
                                                                if not (n.isCompatible("DVB-S") or n.isCompatible("DVB-T") or n.isCompatible("DVB-C") or n.isCompatible("ATSC")):
                                                                        continue
                                                                if n.isCompatible("DVB-S") and n.config.dvbs.configMode.value  in ("loopthrough", "satposdepends", "nothing"):
                                                                        continue
                                                                if n.isCompatible("DVB-S") and n.config.dvbs.configMode.value == "advanced" and len(nimmanager.getSatListForNim(n.slot)) < 1:
                                                                        continue
                                                                nimList.append(n)
                                                except: # Other Open source
                                                        for n in nims:
                                                                logdata("keyblue: Open Satfinder Opensource\n")
                                                                #if not any([n.isCompatible(x) for x in "DVB-S", "DVB-T", "DVB-C", "ATSC"]):
                                                                if not (n.isCompatible("DVB-S") or n.isCompatible("DVB-T") or n.isCompatible("DVB-C") or n.isCompatible("ATSC")):
                                                                        continue
                                                                if n.config_mode in ("loopthrough", "satposdepends", "nothing"):
                                                                        continue
                                                                if n.isCompatible("DVB-S") and n.config_mode in ("advanced", "simple") and len(nimmanager.getSatListForNim(n.slot)) < 1 and len(n.getTunerTypesEnabled()) < 2:
                                                                        continue
                                                                nimList.append(n)
                                                if len(nimList) == 0:
                                                        self.session.open(MessageBox, _("%s") % title25, MessageBox.TYPE_ERROR)
                                                else:
                                                        try:
                                                                        if dvbreader_available:
                                                                                logdata("keyblue: Open Satfinder Vix/BH\n")
                                                                                from Plugins.SystemPlugins.Satfinder.plugin import SatfinderExtra
                                                                                self.session.open(SatfinderExtra)
                                                                        else:
                                                                                logdata("keyblue: Open Satfinder Opensource\n")
                                                                                self.session.open(Satfinder)
                                                        except Exception:
                                                                logdata("keyblue: Open Satfinder Opensource\n")
                                                                self.session.open(Satfinder)
                                                        

                                elif BHVU() or VTI(): # VU+ (BH and VTI)
                                        if os.path.exists(Satfinderpyo) or os.path.exists(Satfinderpyc) or os.path.exists(Signalfinderpy) or os.path.exists(Signalfinderpyc):
                                                logdata("keyblue: Open Signalfinder BH or VTI\n")
                                                from enigma import eDVBFrontendParametersSatellite
                                                from Plugins.SystemPlugins.Signalfinder.plugin import SignalFinderMultistreamT2MI, SignalFinderMultistream, SignalFinder
                                                multistream = hasattr(eDVBFrontendParametersSatellite, "PLS_Root")
                                                t2mi = hasattr(eDVBFrontendParametersSatellite, "No_T2MI_PLP_Id") and hasattr(eDVBFrontendParametersSatellite, "T2MI_Default_Pid")
                                                nims = nimmanager.nim_slots
                                                sat_nimList = []
                                                for x in nims:
                                                        if not x.isCompatible("DVB-S"):
                                                                continue
                                                        try:
                                                                nimConfig = nimmanager.getNimConfig(x.slot).dvbs
                                                        except:
                                                                nimConfig = nimmanager.getNimConfig(x.slot)
                                                        if not hasattr(nimConfig, 'configMode'):
                                                                continue
                                                        if nimConfig.configMode.value in ("loopthrough", "satposdepends", "nothing"):
                                                                continue
                                                        if nimConfig.configMode.value in ("simple" ,"advanced") and len(nimmanager.getSatListForNim(x.slot)) < 1:
                                                                nimConfig.configMode.value = "nothing"
                                                                nimConfig.configMode.save()
                                                                continue
                                                        sat_nimList.append(x)
                                                sat = len(sat_nimList)
                                                if sat == 0:
                                                        self.session.open(MessageBox, _("%s") % title26, MessageBox.TYPE_ERROR)
                                                        return
                                                if t2mi and multistream:
                                                        self.session.open(SignalFinderMultistreamT2MI)
                                                elif multistream:
                                                        self.session.open(SignalFinderMultistream)
                                                else:
                                                        self.session.open(SignalFinder)
                                        else:
                                                logdata("keyblue: SignalFinder not inistalled\n")
                                else:
                                        logdata("keyblue: SatFinder/SignalFinder does not support Scan feature\n")
                        else:
                               logdata("keyblue: Satfinder/Signalfinder Not Installed\n")
                except Exception as error:
                       trace_error()

        def keyLeft(self):
                self.servicelist.moveUp()
                self.servicelist.zap()

        def keyRight(self):
                self.servicelist.moveDown()
                self.servicelist.zap()

        def keyUp(self):
                self.session.execDialog(self.servicelist)

        def keyDown(self):
                self.session.execDialog(self.servicelist)

        def exit(self):
                if os_path.exists("/tmp/.RaedQuickSignal"):
                        os_remove("/tmp/.RaedQuickSignal")
                if not DreamOS() and not BHVU():
                        config.servicelist.startupservice.value = self.startupservice
                        config.servicelist.startupservice.save()
                self.close()

        def setupback(self,answer=False):
                if answer:
                        self.exit()
                        
        def showsetup(self):
                self.session.openWithCallback(self.setupback,RaedQuickSignal_setup)

        def checkupdates(self):
               try:
                       from twisted.web.client import getPage, error
                       url = b"https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/installer.sh"
                       getPage(url,timeout=10).addCallback(self.parseData).addErrback(self.errBack)
               except Exception as error:
                       trace_error()

        def errBack(self,error=None):
               logdata("errBack-error",error)

        def parseData(self, data):
               if PY3:
                   data = data.decode("utf-8")
               else:
                   data = data.encode("utf-8")
               if data:
                   lines = data.split("\n")
                   for line in lines:
                       if line.startswith("version"):
                          self.new_version = line.split("=")[1]
                          #break #if enabled the for loop will exit before reading description line
                       if line.startswith("description"):
                          self.new_description = line.split("=")[1]
                          break
               logdata("Current VER",VER)
               logdata('New VER',self.new_version)
               if float(VER) == float(self.new_version) or float(VER)>float(self.new_version):
                   logdata("Updates","No new version available")
               else :
                   new_version = self.new_version
                   new_description = self.new_description
                   self.session.openWithCallback(self.install, MessageBox, _('%s %s %s.\n\n%s.\n\n%s.' % (title27, new_version, title28, new_description, title29)), MessageBox.TYPE_YESNO)

        def install(self,answer=False):
                try:
                     if answer:
                           cmdlist = []
                           cmd="wget https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/installer.sh -O - | /bin/sh"
                           cmdlist.append(cmd)
                           self.session.open(Console, title='%s' % title30, cmdlist=cmdlist, finishedCallback=self.myCallback, closeOnSuccess=False)
                except:
                           trace_error()
        
        def myCallback(self,result):
                return

class RaedQuickSignal():
        def __init__(self):
                self.dialog = None

        def gotSession(self, session):
                self.session = session
                self.RaedQuickSignal = None
                if os_path.exists("/tmp/.RaedQuickSignal"):
                        os_remove("/tmp/.RaedQuickSignal")
                keymap = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/tools/keymap.xml")
                global globalActionMap
                readKeymap(keymap)
                if 'displayHelp' in globalActionMap.actions:
                        del globalActionMap.actions['displayHelp']
                elif 'showSherlock' in globalActionMap.actions:
                        del globalActionMap.actions['showSherlock']
                globalActionMap.actions['showRaedQuickSignal'] = self.ShowHide

        def ShowHide(self):
                if os_path.exists("/tmp/.RaedQuickSignal") == False:
                        if config.plugins.RaedQuickSignal.enabledonoff.value:
                                self.session.open(RaedQuickSignalScreen)

#################################
pSignal = RaedQuickSignal()
#################################

class RaedQuickSignal_setup(ConfigListScreen, Screen):
        def __init__(self, session):
                self.session = session

                Screen.__init__(self, session)
                self.skin = SKIN_setup
                self.RaedQuickSignal_fake_entry = NoSave(ConfigNothing())
                self.list = []
                ConfigListScreen.__init__(self, self.list)
                self.configChanged = False

                self["setupActions"] = ActionMap(["SetupActions", "ColorActions", "EPGSelectActions"],
                {
                        "red": self.cancel,
                        "cancel": self.cancel,
                        "green": self.save,
                        "yellow": self.keyYellow,
                        "blue": self.keyBlue,
                        "ok": self.keyOk
                }, -2)

                self["key_red"] = StaticText(_("%s") % title31)
                self["key_green"] = StaticText(_("%s") % title32)
                self["key_yellow"] = StaticText(_("%s") % title33)

                if (os.path.exists(BRANDOPENPYO) or os.path.exists(BRANDOPENPY) or os.path.exists(BRANDOPENPYC)) and ((os.path.exists(Satfinderpy) or os.path.exists(Satfinderpyo) or os.path.exists(Satfinderpyc))):
                        self["key_blue"] = StaticText(_(" "))
                        logdata('key_blue: You have open source image')
                elif getSatfinderinfo() and not (BHVU() or VTI()):
                        self["key_blue"] = StaticText(_(" "))
                        logdata('key_blue: You already install my mod plugin')
                else:
                        self["key_blue"] = StaticText(_("Download SatFinder"))

                if os.path.exists(Signalfinderpy) or os.path.exists(Signalfinderpyo) or os.path.exists(Signalfinderpyc):
                        self["key_blue"] = StaticText(_(" "))
                        logdata('key_blue: You already installed Signalfinder')
                elif BHVU() or VTI():
                        self["key_blue"] = StaticText(_("%s") % title34)

                self["Picture"] = Pixmap()
                self["help"] = StaticText()

                self.currkeyname_value = config.plugins.RaedQuickSignal.keyname.value
                self.fontsStyle_value = config.plugins.RaedQuickSignal.fontsStyle.value
                #self.fontsenabled_value = config.plugins.RaedQuickSignal.fontsenable.value
                self.numbers_value = config.plugins.RaedQuickSignal.numbers.value
                self.lang_value = config.plugins.RaedQuickSignal.lang.value

                self.createConfigList()
                self.onLayoutFinish.append(self.setWindowTitle)

        #def run(self):
        #          self.session.open(RaedQuickSignalScreen)

        def createConfigList(self):
                self.configChanged = True

                self.set_enabledonoff = getConfigListEntry(_("%s") % title35, config.plugins.RaedQuickSignal.enabledonoff, _("%s") % title36)
                self.set_updateonline = getConfigListEntry(_("%s") % title37, config.plugins.RaedQuickSignal.updateonline, _("%s") % title38)
                self.set_keyname = getConfigListEntry(_("%s") % title39, config.plugins.RaedQuickSignal.keyname, _("%s") % title40)
                self.set_enabledBD = getConfigListEntry(_("%s") % title41, config.plugins.RaedQuickSignal.enabledBD, _("%s") % title42)
                self.set_numbers = getConfigListEntry(_("%s") % title43, config.plugins.RaedQuickSignal.numbers, _("%s") % title44)
                self.set_piconpath = getConfigListEntry(_("%s") % title45, config.plugins.RaedQuickSignal.piconpath, _("%s") % title46)
                self.set_style = getConfigListEntry(_("%s") % title47, config.plugins.RaedQuickSignal.style, _("%s") % title48)
                #self.set_fontsenable = getConfigListEntry(_("%s") % title49, config.plugins.RaedQuickSignal.fontsenable, _("%s")% title50)
                self.set_fontsStyle = getConfigListEntry(_("%s") % title51, config.plugins.RaedQuickSignal.fontsStyle, _("%s") % title52)
                self.set_fontssize = getConfigListEntry(_("%s") % title88, config.plugins.RaedQuickSignal.fontsSize, _("%s") % title89)
                self.set_refreshInterval = getConfigListEntry(_("%s") % title53, config.plugins.RaedQuickSignal.refreshInterval, _("%s") % title54)
                self.set_degreetype = getConfigListEntry(_("%s") % title55, config.plugins.RaedQuickSignal.degreetype, _("%s") % title56)
                self.set_city = getConfigListEntry(_("%s") % title57, config.plugins.RaedQuickSignal.city, _("%s") % title58)
                self.language = getConfigListEntry(_("%s") % title59, config.plugins.RaedQuickSignal.lang, _("%s") % title60)

                self.list = []
                self.list.append(getConfigListEntry("%s" % title61))
                self.list.append(self.set_enabledonoff)
                if config.plugins.RaedQuickSignal.enabledonoff.value:
                        self.list.append(self.set_updateonline)
                        self.list.append(self.set_keyname)
                        self.list.append(self.language)
                        self.list.append(getConfigListEntry("%s" % title62))
                        self.list.append(self.set_enabledBD)
                        self.list.append(self.set_numbers)
                        self.list.append(self.set_piconpath)
                        self.list.append(self.set_style)
                        #self.list.append(self.set_fontsenable)
                        #if config.plugins.RaedQuickSignal.fontsenable.value:
                        self.list.append(self.set_fontsStyle)
                        self.list.append(self.set_fontssize)
                        self.list.append(getConfigListEntry("%s" % title63))
                        self.list.append(self.set_refreshInterval)
                        self.list.append(self.set_degreetype)
                        self.list.append(self.set_city)

                self["config"].list = self.list
                self["config"].l.setList(self.list)
                self["config"].onSelectionChanged.append(self.updateHelp)
                self["config"].onSelectionChanged.append(self.Picture)

                # DreamOS Config/menu fonts
                if DreamOS():
                        #if config.plugins.RaedQuickSignal.fontsenable.value and isHD():
                        if isHD():
                                self["config"].l.setValueFont(gFont("RSQFont", 24)) ## set font to config menu
                                self["config"].l.setDescriptionFont(gFont("RSQFont", 24)) ## set font to DescriptionFont
                                self["config"].l.setItemHeight(26) ## set ItemHeight to config menu
                        #elif config.plugins.RaedQuickSignal.fontsenable.value and not isHD():
                        elif not isHD():
                                self["config"].l.setValueFont(gFont("RSQFont", 28)) ## set font to config menu
                                self["config"].l.setDescriptionFont(gFont("RSQFont", 28)) ## set font to DescriptionFont
                                self["config"].l.setItemHeight(38) ## set ItemHeight to config menu

        def setWindowTitle(self):
                self.setTitle("%s%s" % (title21, VER))

        def updateHelp(self):
                cur = self["config"].getCurrent()
                if cur:
                        self["help"].text = cur[2]

        def Picture(self):
                try:
                        cur = self["config"].getCurrent()
                        if cur == self.set_style:
                                preview = PREVIEWPIC + "%s.png" % config.plugins.RaedQuickSignal.style.value
                                if os.path.exists(preview):
                                        self['Picture'].instance.setPixmapFromFile(preview)
                                        self["Picture"].show()
                                else:
                                        logdata('Picture preview: No preview image')
                        else:
                                self["Picture"].hide()
                except Exception as error:
                        logdata("Picture preview:", error)

        def keyLeft(self):
                ConfigListScreen.keyLeft(self)
                self.Picture()
                self.createConfigList()

        def keyRight(self):
                ConfigListScreen.keyRight(self)
                self.Picture()
                self.createConfigList()

        def keyYellow(self):
                self.session.open(PiconsScreen)

        def keyBlue(self):
                if (os.path.exists(BRANDOPENPYO) or os.path.exists(BRANDOPENPY) or os.path.exists(BRANDOPENPYC)) and (os.path.exists(Satfinderpy) or os.path.exists(Satfinderpyo) or os.path.exists(Satfinderpyc)):
                        logdata('keyBlue: You have open source')
                elif not getSatfinderinfo() or not os.path.exists(Satfinderpy) or not os.path.exists(Satfinderpyo) or not os.path.exists(Satfinderpyc) or not os.path.exists(Signalfinderpy) or not os.path.exists(Signalfinderpyc) or not os.path.exists(Signalfinderpyo):
                        if os.path.exists(BRANDOPENPYO) or os.path.exists(BRANDOPENPY) or os.path.exists(BRANDOPENPYC):
                                self.session.openWithCallback(self.installsat, MessageBox, _('%s') % title64, MessageBox.TYPE_YESNO)
                        else:
                                self.session.openWithCallback(self.installsat, MessageBox, _('%s') % title65, MessageBox.TYPE_YESNO)

        def installsat(self,answer=False):
                try:
                     if answer:
                           cmdlist = []
                           cmd="wget https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/installerSat.sh -O - | /bin/sh"
                           cmdlist.append(cmd)
                           self.session.open(Console, title='%s' % title66, cmdlist=cmdlist, finishedCallback=self.myCallback, closeOnSuccess=False)
                except:
                           trace_error()

        def myCallback(self,result):
                return

        def keyOk(self):
                cur = self["config"].getCurrent()
                if cur == self.set_city:
                        countriesFile = resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/tools/countries')
                        countries=open(countriesFile).readlines()
                        clist=[]
                        for country in countries:
                                countryCode,countryName=country.split(",")
                                clist.append((countryName,countryCode))
                        self.session.openWithCallback(self.choicesback, ChoiceBox, _('%s') % title67, clist)

        def choicesback(self, select):
                if select:
                    self.country=select[1]
                    config.plugins.RaedQuickSignal.weather_location.value=self.country.lower()+"-"+self.country.upper()
                    config.plugins.RaedQuickSignal.weather_location.save()
                    self.session.openWithCallback(self.citiesback, WeatherLocationChoiceList, self.country)
                    
        def citiesback(self,select):
                if select:
                  weather_city = select
                  weather_city.capitalize() 
                  config.plugins.RaedQuickSignal.city.setValue(weather_city)
                  self.createConfigList()

        def save(self):
                #if self["config"].isChanged():
                if self.configChanged:
                        for x in self["config"].list:
                                if len(x)>1:
                                        x[1].save()
                        configfile.save()
                        # we can not use resolveFilename(SCOPE_PLUGINS) here the keymap.xml will be not writable 
                        if os_path.exists('/usr/lib64/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml'):
                            keyfile = open("/usr/lib64/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml", "w")
                        else:
                            keyfile = open("/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml", "w")
                        keyfile.write('<keymap>\n\t<map context="GlobalActions">\n\t\t<key id="%s" mapto="showRaedQuickSignal" flags="m" />\n\t</map>\n</keymap>' % config.plugins.RaedQuickSignal.keyname.value)
                        keyfile.close()
                        if not self.currkeyname_value == config.plugins.RaedQuickSignal.keyname.value or \
                        not self.fontsStyle_value == config.plugins.RaedQuickSignal.fontsStyle.value or \
                        not self.numbers_value == config.plugins.RaedQuickSignal.numbers.value or \
                        not self.lang_value == config.plugins.RaedQuickSignal.lang.value:
                                self.session.openWithCallback(self.restart, MessageBox, _("%s") % title68)
                        else:
                                self.close(True)
                else:
                        self.close(False)

        def cancel(self):
                for i in self["config"].list:
                        if len(i)>1:
                                i[1].cancel()
                self.close(False)

        def restart(self,answer=None):
                if answer:
                   self.session.open(TryQuitMainloop, 3)
                   return
                self.close(True)

class PiconsScreen(Screen):
        def __init__(self, session):
                self.session = session

                Screen.__init__(self, session)
                self.skin = SKIN_Picons
                self.RaedQuickSignal_fake_entry = NoSave(ConfigNothing())

                self["setupActions"] = ActionMap(["SetupActions"],
                {
                        "cancel": self.cancel,
                        "ok": self.DownloadPicons
                }, -1)

                self["Picture"] = Pixmap()

                list = []
                list.append((_("%s") % title69, "Black"))
                list.append((_("%s") % title70, "White"))
                list.append((_("%s") % title71, "Black"))
                self["menu"] = MenuList(list)
                self["menu"].onSelectionChanged.append(self.Picture)
                self.onShow.append(self.Picture)
                self.onLayoutFinish.append(self.setWindowTitle)

        def setWindowTitle(self):
                self.setTitle(_("RaedQuickSignal V %s") % VER)

        def Picture(self):
                try:
                        index = self["menu"].l.getCurrentSelection()[1]
                        if index == "Black":
                                pic = resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/images/preview/BlackPicon.png')
                        elif index == "White":
                                pic = resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/images/preview/WhitePicon.png')
                        elif index == "Transparent":
                                pic = resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/images/preview/TransparentPicon.png')
                        self['Picture'].instance.setPixmapFromFile(pic)
                except Exception as error:
                        logdata("Picture preview:", error)

        def DownloadPicons(self):
                self.session.openWithCallback(self.installPicon, MessageBox, _('%s') % title72, MessageBox.TYPE_YESNO)

        def installPicon(self, answer=False):
                try:
                        if answer:
                                cmdlist = []
                                index = self["menu"].l.getCurrentSelection()[1]
                                if index == "Black":
                                        cmd='wget https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/picons/installerBlackPicons.sh -O - | /bin/sh'
                                        cmdlist.append(cmd)
                                elif index == "White":
                                        cmd='wget https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/picons/installerWhitePicons.sh -O - | /bin/sh'
                                        cmdlist.append(cmd)
                                elif index == "Transparent":
                                        cmd='wget https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/picons/installerTransparentPicons.sh -O - | /bin/sh'
                                        cmdlist.append(cmd)
                                self.session.open(Console, title='%s' % title73, cmdlist=cmdlist, finishedCallback=self.Finished, closeOnSuccess=True)
                        else:
                                self.close()
                except:
                    trace_error()

        def Finished(self):
                self.session.open(MessageBox, _('%s') % title74, MessageBox.TYPE_INFO,timeout=4)

        def cancel(self):
                self.close()

##############################################################################
def sessionstart(reason, session = None, **kwargs):
        if reason == 0:
                pSignal.gotSession(session)
##############################################################################
def main(session, **kwargs):
        session.open(RaedQuickSignal_setup)
##############################################################################
def Plugins(**kwargs):
        result = [
                PluginDescriptor(
                        where = [PluginDescriptor.WHERE_SESSIONSTART],
                        fnc = sessionstart
                ),
                PluginDescriptor(
                        name=_("RaedQuickSignal Setup"),
                        description = _("RAED's RaedQuickSignal setup"),
                        where = PluginDescriptor.WHERE_PLUGINMENU,
                        icon = 'images/RaedQuickSignal.png',
                        fnc = main
                ),
        ]
        return result
