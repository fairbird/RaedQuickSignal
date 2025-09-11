#!/usr/bin/python
# -*- coding: utf-8 -*-
#RAEDQuickSignal (c) RAED 2014-2025
import os, re, gettext, re, shutil, requests, sys, traceback
from datetime import datetime
from os import environ, remove
from os import system
from os.path import exists, split
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
from Components.Sources.List import List
from Components.MenuList import MenuList
from Components.Label import Label
from Screens.ChoiceBox import ChoiceBox
from Components.Pixmap import Pixmap
from Tools.LoadPixmap import LoadPixmap
from Screens.VirtualKeyBoard import VirtualKeyBoard
try:
        from keymapparser import readKeymap
except:
        from Components.ActionMap import loadKeymap as readKeymap
from twisted.web.client import downloadPage, getPage, error
from xml.etree.cElementTree import fromstring as cet_fromstring
# import as python3 from plugin
from .tools.configs import *
from .tools.compat import compat_urlopen, compat_Request, compat_URLError, compat_quote, compat_urlretrieve, PY3
from .tools.Console import Console
        
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
BLackHole="/usr/lib/enigma2/python/Blackhole"
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
    if exists(version_file):
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
        if exists('/tmp/RaedQuickSignal.log'):
                remove('/tmp/RaedQuickSignal.log')
    except:
        pass

def getSatfinderinfo():
    infofile=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Satfinder/LICENSE")
    if exists(infofile):
        fp=open(infofile, 'r').readlines()
        for line in fp:
                if 'RAED' in line:
                        return getSatfinderinfo

def DreamOS():
    if exists('/var/lib/dpkg/status'):
        return DreamOS

def BHVU():
    if exists(BRANDVU) and exists(BLackHole):
        return BHVU

def VTI():
    VTI = resolveFilename(SCOPE_PLUGINS, "SystemPlugins/VTIPanel/plugin.pyo")
    if exists(VTI):
        return VTI

def VUDevice():
    if exists(BRANDVU) and not VTI():
        if not exists(BRANDOPENPYO) or not exists(BRANDOPENPY) or not exists(BRANDOPENPYC):
                return VUDevice

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

REDC =  '\033[31m'
ENDC = '\033[m'

def cprint(text):
    print(REDC+"[RaedQuickSignal] "+text+ENDC)

def downloadFile(url, filePath):
    try:
        # Download the file from `url` and save it locally under `file_name`:
        compat_urlretrieve(url, filePath)
        return True
        req = compat_Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # add [headers={'User-Agent': 'Mozilla/5.0'}] to fix HTTP Error 403: Forbidden
        response = compat_urlopen(req,timeout=5)
        cprint("response.read: %s" % response.read())
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
        req = compat_Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # add [headers={'User-Agent': 'Mozilla/5.0'}] to fix HTTP Error 403: Forbidden
        response = compat_urlopen(req,timeout=5)
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
                                cityName = split(href)[1].replace(".html","").replace("-"," ").lstrip(' ')
                                #cityName = re.findall(str(regx), str(block), re.M|re.I)[0]#.replace(".html","").split("_%", 1)[0].split("%", 1)[0]
                                cities.append(cityName)
                        cities.sort()
    except Exception as error:
                cprint('excepyion: %s' % str(error))
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
        #            cityName = split(cityURL)[1].replace(".html","").split("_%", 1)[0].split("%", 1)[0]    
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
                with open('/tmp/RaedQSweathermsn.xml', 'w') as noneweather:
                        noneweather.write('None')
                noneweather.close()

        def get_xmlfile(self,weather_city,weather_location):
                degreetype = config.plugins.RaedQuickSignal.degreetype.value
                weather_city = removeunicode(weather_city)
                weather_city = weather_city.decode("utf-8").replace(" ","_")
                url = "http://weather.service.msn.com/data.aspx?weadegreetype=%s&culture=%s&weasearchstr=%s&src=outlook" % (degreetype, weather_location, weather_city)
                logdata('url',url)
                file_name ='/tmp/RaedQSweathermsn.xml'
                # Download the file from `url` and save it locally under `file_name`:
                try:
                       ret=downloadFile(url, file_name)
                       return ret
                except Exception as error:### new
                       trace_error()
                       return False
                #self.iConsole.ePopen("wget -P /tmp -T2 "http://weather.service.msn.com/data.aspx?weadegreetype=%s&culture=%s&weasearchstr=%s&src=outlook" -O /tmp/RaedQSweathermsn.xml" % (degreetype, weather_location, weather_city), self.control_xml)

        def add_city(self):
                 self.session.openWithCallback(self.cityCallback, VirtualKeyBoard, title=_("%s") % title16, text="%s" % title17)
                 #self.session.openWithCallback(self.cityCallback, InputBox, title=_("%s") % title16, text="%s" % title17, maxSize=False, visible_width =250)

        def cityCallback(self,city=None):
                try:
                        if exists('/tmp/RaedQSweathermsn.xml'):
                                remove('/tmp/RaedQSweathermsn.xml')
                        returnValue = city
                        countryCode=self.country.lower()+"-"+self.country.upper()
                        if self.get_xmlfile(returnValue,countryCode)==False:
                                self.session.open(MessageBox, _("%s") % title18,MessageBox.TYPE_ERROR)
                                return 
                        if not fileExists('/tmp/RaedQSweathermsn.xml'):
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
                        if exists('/tmp/RaedQSweathermsn.xml'):
                                remove('/tmp/RaedQSweathermsn.xml')
                        returnValue = self["choicelist"].l.getCurrentSelection()
                        countryCode=self.country.lower()+"-"+self.country.upper()
                        if self.get_xmlfile(returnValue,countryCode)==False:
                                self.session.open(MessageBox, _("%s") % title20,MessageBox.TYPE_ERROR)
                                return 
                        if not fileExists('/tmp/RaedQSweathermsn.xml'):
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

                system("rm -f /tmp/RaedQSweathermsn.xml")
                self.degreetype = config.plugins.RaedQuickSignal.degreetype.value
                self.weather_city = config.plugins.RaedQuickSignal.city.value
                self.language = config.osd.language.value.replace('_', '-')
                if self.language == 'en-EN':
                        self.language = 'en-US'

                ## Add Fonts codes
                #if config.plugins.RaedQuickSignal.fontsSize.value == "Default":
                #        fontSize = 100
                #else:
                #        fontSize = config.plugins.RaedQuickSignal.fontsSize.value
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
                try:
                        self.startupservice = config.servicelist.startupservice.value
                        sref = self.session.nav.getCurrentService()
                        from ServiceReference import ServiceReference
                        p = ServiceReference(str(sref))
                        servicename = str(p.getServiceName())
                        serviceurl = p.getPath()
                        config.servicelist.startupservice.value = serviceurl
                        config.servicelist.startupservice.save()
                except:
                        pass
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
                if exists(Satfinderpy) or exists(Satfinderpyo) or exists(Satfinderpyc):
                        if BHVU() or VTI():
                                self["Satfinder"] = Label(_(" "))
                                logdata("Label Key_blue: SatFinder does not support Scan feature (VU+ BH/VTI)\n")
                        elif getSatfinderinfo() or exists(BRANDOPENPYO) or exists(BRANDOPENPY) or exists(BRANDOPENPYC):
                                self["Satfinder"] = Label("%s" % title77)
                        else:
                                self["Satfinder"] = Label(_(" "))
                                logdata("Label Key_blue: SatFinder does not support Scan feature\n")
                # VU+ (BH & VTI)
                elif exists(Signalfinderpy) or exists(Signalfinderpyo) or exists(Signalfinderpyc):
                        if BHVU() or VTI():
                                self["Satfinder"] = Label("%s" % title78)
                        else:
                                self["Satfinder"] = Label(_(" "))
                                logdata("Label Key_blue: Signalfinder does not support Scan feature\n")
                else:
                        self["Satfinder"] = Label(_(" "))
                        logdata("Label Key_blue: Satfinder Not Installed\n")

                if exists(Positionerpy) or exists(Positionerpyo) or exists(Positionerpyc):
                        self["Positioner"] = Label("%s" % title79)
                else:
                        self["Positioner"] = Label(_(" "))
                        logdata("Label Key_yellow: PositionerSetup Not Installed\n")
                self.onShown.append(self.onWindowShow)

        def get_xmlfile(self):
                xmlfile = "http://weather.service.msn.com/data.aspx?weadegreetype=%s&culture=%s&weasearchstr=%s&src=outlook" % (self.degreetype, self.language, compat_quote(self.weather_city))
                if PY3:
                        import six
                        downloadPage(six.ensure_binary(xmlfile), "/tmp/RaedQSweathermsn.xml").addCallback(self.downloadFinished).addErrback(self.downloadFailed)
                else:
                        downloadPage(xmlfile, "/tmp/RaedQSweathermsn.xml").addCallback(self.downloadFinished).addErrback(self.downloadFailed)

        def downloadFinished(self, result):
                print("[WeatherMSN] Download finished")

        def downloadFailed(self, result):
                print("[WeatherMSN] Download failed!")

        def onWindowShow(self):
                self.onShown.remove(self.onWindowShow)
                self.instance.show()
                self.get_xmlfile()
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
                        if exists(Positionerpy) or exists(Positionerpyo) or exists(Positionerpyc):
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
                        if exists(Satfinderpy) or exists(Satfinderpyo) or exists(Satfinderpyc) or exists(Signalfinderpy) or exists(Signalfinderpyo) or exists(Signalfinderpyc): # Satfinder
                                from Components.NimManager import nimmanager
                                if not BHVU() and (getSatfinderinfo() or exists(BRANDOPENPYO) or exists(BRANDOPENPY) or exists(BRANDOPENPYC)):
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
                                        if exists(Satfinderpyo) or exists(Satfinderpyc) or exists(Signalfinderpy) or exists(Signalfinderpyc):
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
                if exists("/tmp/.RaedQuickSignal"):
                        remove("/tmp/.RaedQuickSignal")
                try:
                        config.servicelist.startupservice.value = self.startupservice
                        config.servicelist.startupservice.save()
                except:
                        pass
                self.close()

        def setupback(self,answer=False):
                if answer:
                        self.exit()
                        
        def showsetup(self):
                self.session.openWithCallback(self.setupback,RaedQuickSignal_setup)

        def checkupdates(self):
               try:    
                       url = b"https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/installer.sh"
                       getPage(url,timeout=10).addCallback(self.parseData).addErrback(self.errBack)
               except Exception as error:
                       trace_error()

        def errBack(self,error=None):
                logdata("errBack-error",error)

        def errBack(self,error=None):
                logdata("errBack-error",error)

        def parseData(self, data):
                if PY3:
                       data = data.decode("utf-8")
                else:
                       data = data.encode("utf-8")

                if data:
                       lines = data.split("\n")
                       desc_started = False
                       desc_lines = []
                       for line in lines:
                                line = line.strip()
                                if line.startswith("version"):
                                        self.new_version = line.split("=")[1].strip('"').strip().strip('"').strip("'")
                                elif line.startswith("description="):
                                        desc_started = True
                                        first_part = line.split("=", 1)[1].lstrip('"').strip().strip('"').strip("'")
                                        if first_part.endswith('"'):
                                                # description is in one line only
                                                self.new_description = first_part.rstrip('"')
                                                desc_started = False
                                        else:
                                                desc_lines.append(first_part)
                                elif desc_started:
                                        if line.endswith('"'):
                                                desc_lines.append(line.rstrip('"'))
                                                desc_started = False
                                                self.new_description = "\n".join(desc_lines)
                                        else:
                                                desc_lines.append(line)
                if float(VER) >= float(self.new_version):
                                logdata("Updates", "No new version available")
                else:
                                new_description = self.new_description
                                self.session.openWithCallback(self.install, MessageBox, _('%s %s %s.\n\n%s.\n\n%s.' % (title27, self.new_version, title28, new_description, title29)), MessageBox.TYPE_YESNO)

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
                if exists("/tmp/.RaedQuickSignal"):
                        remove("/tmp/.RaedQuickSignal")
                keymap = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/tools/keymap.xml")
                global globalActionMap
                readKeymap(keymap)
                if 'displayHelp' in globalActionMap.actions:
                        del globalActionMap.actions['displayHelp']
                elif 'showSherlock' in globalActionMap.actions:
                        del globalActionMap.actions['showSherlock']
                globalActionMap.actions['showRaedQuickSignal'] = self.ShowHide

        def ShowHide(self):
                if exists("/tmp/.RaedQuickSignal") == False:
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

                if (exists(BRANDOPENPYO) or exists(BRANDOPENPY) or exists(BRANDOPENPYC)) and ((exists(Satfinderpy) or exists(Satfinderpyo) or exists(Satfinderpyc))):
                        self["key_blue"] = StaticText(_(" "))
                        logdata('key_blue: You have open source image')
                elif getSatfinderinfo() and not (BHVU() or VTI()):
                        self["key_blue"] = StaticText(_(" "))
                        logdata('key_blue: You already install my mod plugin')
                else:
                        self["key_blue"] = StaticText(_("Download SatFinder"))

                if exists(Signalfinderpy) or exists(Signalfinderpyo) or exists(Signalfinderpyc):
                        self["key_blue"] = StaticText(_(" "))
                        logdata('key_blue: You already installed Signalfinder')
                elif BHVU() or VTI():
                        self["key_blue"] = StaticText(_("%s") % title34)

                self["Picture"] = Pixmap()
                self["help"] = StaticText()

                self.currkeyname_value = config.plugins.RaedQuickSignal.keyname.value
                self.fontsStyle_value = config.plugins.RaedQuickSignal.fontsStyle.value
                self.fontssize_value = config.plugins.RaedQuickSignal.fontsSize.value
                #self.fontsenabled_value = config.plugins.RaedQuickSignal.fontsenable.value
                self.numbers_value = config.plugins.RaedQuickSignal.numbers.value
                self.lang_value = config.plugins.RaedQuickSignal.lang.value
                self.Searchmethod = config.plugins.RaedQuickSignal.Searchmethod.value

                self.createConfigList()
                self.onLayoutFinish.append(self.setWindowTitle)

        #def run(self):
        #          self.session.open(RaedQuickSignalScreen)

        def createConfigList(self):
                self.configChanged = True

                self.set_enabledonoff = getConfigListEntry(_("%s") % title35, config.plugins.RaedQuickSignal.enabledonoff, _("%s") % title36)
                self.set_showplugin = getConfigListEntry(_("%s") % title95, config.plugins.RaedQuickSignal.showplugin, _("%s") % title96)
                self.set_updateonline = getConfigListEntry(_("%s") % title37, config.plugins.RaedQuickSignal.updateonline, _("%s") % title38)
                self.set_keyname = getConfigListEntry(_("%s") % title39, config.plugins.RaedQuickSignal.keyname, _("%s") % title40)
                self.set_enabledBD = getConfigListEntry(_("%s") % title41, config.plugins.RaedQuickSignal.enabledBD, _("%s") % title42)
                self.set_numbers = getConfigListEntry(_("%s") % title43, config.plugins.RaedQuickSignal.numbers, _("%s") % title44)
                self.set_piconpath = getConfigListEntry(_("%s") % title45, config.plugins.RaedQuickSignal.piconpath, _("%s") % title46)
                self.set_style = getConfigListEntry(_("%s") % title47, config.plugins.RaedQuickSignal.style, _("%s") % title48)
                self.set_fontsenable = getConfigListEntry(_("%s") % title49, config.plugins.RaedQuickSignal.fontsenable, _("%s")% title50)
                self.set_fontsStyle = getConfigListEntry(_("%s") % title51, config.plugins.RaedQuickSignal.fontsStyle, _("%s") % title52)
                self.set_fontssize = getConfigListEntry(_("%s") % title88, config.plugins.RaedQuickSignal.fontsSize, _("%s") % title89)
                self.set_refreshInterval = getConfigListEntry(_("%s") % title53, config.plugins.RaedQuickSignal.refreshInterval, _("%s") % title54)
                self.set_Searchmethod = getConfigListEntry(_("%s")  % title92, config.plugins.RaedQuickSignal.Searchmethod, _("%s")  % title93)
                self.set_degreetype = getConfigListEntry(_("%s") % title55, config.plugins.RaedQuickSignal.degreetype, _("%s") % title56)
                self.set_city = getConfigListEntry(_("%s") % title57, config.plugins.RaedQuickSignal.city, _("%s") % title58)
                self.language = getConfigListEntry(_("%s") % title59, config.plugins.RaedQuickSignal.lang, _("%s") % title60)

                self.list = []
                self.list.append(getConfigListEntry("%s" % title61))
                self.list.append(self.set_enabledonoff)
                if config.plugins.RaedQuickSignal.enabledonoff.value:
                        self.list.append(self.set_showplugin)
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
                        #self.list.append(self.set_Searchmethod)
                        self.list.append(self.set_city)

                self["config"].list = self.list
                self["config"].l.setList(self.list)
                self["config"].onSelectionChanged.append(self.updateHelp)
                self["config"].onSelectionChanged.append(self.Picture)

                # DreamOS Config/menu fonts
                #if DreamOS():
                        #if config.plugins.RaedQuickSignal.fontsenable.value and isHD():
                #        if isHD():
                #                self["config"].l.setValueFont(gFont("RSQFont", 24)) ## set font to config menu
                #                self["config"].l.setDescriptionFont(gFont("RSQFont", 24)) ## set font to DescriptionFont
                #                self["config"].l.setItemHeight(26) ## set ItemHeight to config menu
                        #elif config.plugins.RaedQuickSignal.fontsenable.value and not isHD():
                #        elif not isHD():
                #                self["config"].l.setValueFont(gFont("RSQFont", 28)) ## set font to config menu
                #                self["config"].l.setDescriptionFont(gFont("RSQFont", 28)) ## set font to DescriptionFont
                #                self["config"].l.setItemHeight(38) ## set ItemHeight to config menu

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
                                if exists(preview):
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
                if (exists(BRANDOPENPYO) or exists(BRANDOPENPY) or exists(BRANDOPENPYC)) and (exists(Satfinderpy) or exists(Satfinderpyo) or exists(Satfinderpyc)):
                        logdata('keyBlue: You have open source')
                elif not getSatfinderinfo() or not exists(Satfinderpy) or not exists(Satfinderpyo) or not exists(Satfinderpyc) or not exists(Signalfinderpy) or not exists(Signalfinderpyc) or not exists(Signalfinderpyo):
                        if exists(BRANDOPENPYO) or exists(BRANDOPENPY) or exists(BRANDOPENPYC):
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

        def ShowsearchBarracuda(self, name):
                if name is not None:
                        self.session.open(SearchLocationMSN, name)
                return

        def keyOk(self):
                cur = self["config"].getCurrent()
                if cur == self.set_city:
                        config.plugins.RaedQuickSignal.Searchmethod.save()
                        self.session.openWithCallback(self.ShowsearchBarracuda, VirtualKeyBoard, title=_('%s') % title16)
                        #if config.plugins.RaedQuickSignal.Searchmethod.value == "search":
                        #        config.plugins.RaedQuickSignal.Searchmethod.save()
                        #        self.session.openWithCallback(self.ShowsearchBarracuda, VirtualKeyBoard, title=_('%s') % title16)
                        #elif config.plugins.RaedQuickSignal.Searchmethod.value == "chosse":
                        #        config.plugins.RaedQuickSignal.Searchmethod.save()
                        #        countriesFile = resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/tools/countries')
                        #        countries=open(countriesFile).readlines()
                        #        clist=[]
                        #        for country in countries:
                        #                countryCode,countryName=country.split(",")
                        #                clist.append((countryName,countryCode))
                        #        self.session.openWithCallback(self.choicesback, ChoiceBox, _('%s') % title67, clist)
                if cur == self.set_showplugin:
                        self.session.open(SelectionScreen)

        def choicesback(self, select):
                if select:
                    self.country = select[1]
                    #config.plugins.RaedQuickSignal.weather_location.value = self.country.lower()+"-"+self.country.upper()
                    #config.plugins.RaedQuickSignal.weather_location.save()
                    self.language = config.osd.language.value.replace('_', '-')
                    if self.language == 'en-EN':
                        self.language = 'en-US'
                    self.language = self.country
                    self.session.openWithCallback(self.citiesback, WeatherLocationChoiceList, self.country)
                    
        def citiesback(self,select):
                if select:
                  weather_city = select
                  weather_city.capitalize() 
                  config.plugins.RaedQuickSignal.city.setValue(weather_city)
                  self.createConfigList()

        def save(self):
                #if self["config"].isChanged():
                system("rm -f /tmp/RaedQSweathermsn.xml")
                if self.configChanged:
                        for x in self["config"].list:
                                if len(x)>1:
                                        x[1].save()
                        configfile.save()
                        # we can not use resolveFilename(SCOPE_PLUGINS) here the keymap.xml will be not writable 
                        if exists('/usr/lib64/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml'):
                            keyfile = open("/usr/lib64/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml", "w")
                        else:
                            keyfile = open("/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml", "w")
                        keyfile.write('<keymap>\n\t<map context="GlobalActions">\n\t\t<key id="%s" mapto="showRaedQuickSignal" flags="m" />\n\t</map>\n</keymap>' % config.plugins.RaedQuickSignal.keyname.value)
                        keyfile.close()
                        if not self.currkeyname_value == config.plugins.RaedQuickSignal.keyname.value \
                        or not self.fontsStyle_value == config.plugins.RaedQuickSignal.fontsStyle.value \
                        or not self.fontssize_value == config.plugins.RaedQuickSignal.fontsSize.value \
                        or not self.numbers_value == config.plugins.RaedQuickSignal.numbers.value \
                        or not self.lang_value == config.plugins.RaedQuickSignal.lang.value \
                        or not self.Searchmethod == config.plugins.RaedQuickSignal.Searchmethod.value:
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


class SelectionScreen(Screen, ConfigListScreen):

        def __init__(self, session):
                Screen.__init__(self, session)
                self.skin = SKIN_SelectionScreen
                ConfigListScreen.__init__(self, [], session=session)
                self.session = session
                self.setup_title = _("Select your choose")
                self.setTitle(self.setup_title)

                # Load pixmaps for checkboxes
                sz_w = getDesktop(0).size().width()
                if sz_w == 1280 :
                        self.empty_box = LoadPixmap(resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/images/checkbox_empty.png'))
                        self.checked_box = LoadPixmap(resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/images/checkbox_checked.png'))
                else:
                        self.empty_box = LoadPixmap(resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/images/checkbox_empty2.png'))
                        self.checked_box = LoadPixmap(resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/images/checkbox_checked2.png'))

                # Initialize selection states
                self.selection_states = {
                        "Menu": False,
                        "Channellist": False,
                        "Extensions": False
                }

                # Get current config value and update selection states
                self.current_value = config.plugins.RaedQuickSignal.showplugin.value
                if self.current_value:
                        selected_items = self.current_value.split(',')
                        for item in selected_items:
                                if item in self.selection_states:
                                        self.selection_states[item] = True

                # Create list of options with their checkbox states
                self.list = []

                # Set up the list component
                self["list"] = List(self.list)

                # Now update the list
                self.updateList()

                # Set up labels
                self["key_green"] = Label(_("Save"))
                self["key_red"] = Label(_("Cancel"))

                # Set up actions
                self["actions"] = ActionMap(["WizardActions", "ColorActions", "MenuActions"], {
                        "ok": self.select_option,
                        "cancel": self.close,
                        "back": self.close,
                        "green": self.save
                }, -2)  # Higher priority to ensure OK is captured (DreamOS images need it)

                self.onLayoutFinish.append(self.layoutFinished)

        def layoutFinished(self):
                self.setTitle(self.setup_title)

        def updateList(self):
                # Store the current index before updating the list
                current_index = self["list"].getIndex() or 0
                self.list = []
                choices = [
                        ("Menu", _("Menu")),
                        ("Channellist", _("Channellist")),
                        ("Extensions", _("Extensions"))
                ]

                for key, text in choices:
                        pixmap = self.checked_box if self.selection_states[key] else self.empty_box
                        self.list.append((text, pixmap, key))

                self["list"].setList(self.list)
                # Restore the previous index, ensuring it's within bounds
                if current_index < len(self.list):
                        self["list"].setIndex(current_index)
                else:
                        self["list"].setIndex(0)  # Fallback to first item if index is out of range

        def select_option(self):
                current = self["list"].getCurrent()
                if current:
                        key = current[2]
                        self.selection_states[key] = not self.selection_states[key]
                        self.updateList()

        def save(self):
                # Save all selected options as comma-separated string
                selected_options = [key for key, state in self.selection_states.items() if state]
                new_value = ','.join(selected_options)
                config.plugins.RaedQuickSignal.showplugin.value = new_value
                config.plugins.RaedQuickSignal.showplugin.save()

                if self.current_value != new_value:
                        self.session.openWithCallback(self.restart, MessageBox, _("You need to restart GUI\nDo you want to do it now ?!"))
                else:
                        self.close(True)

        def restart(self,answer=None):
                if answer:
                        self.session.open(TryQuitMainloop, 3)
                else:
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
                list.append(getConfigListEntry("%s" % title98))
                list.append((_("%s") % title69, "Black"))
                list.append((_("%s") % title70, "White"))
                list.append((_("%s") % title71, "Transparent"))
                list.append((_("%s") % title94, "Transparent2"))
                if not (BHVU() or VTI() or DreamOS()):
                	list.append(getConfigListEntry("%s" % title99))
                	list.append((_("%s") % title97, "BO-HLALA-Style"))
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
                        elif index == "Transparent2":
                                pic = resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/images/preview/TransparentPicon2.png')
                        elif index == "BO-HLALA-Style":
                                pic = resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/images/preview/BO-HLALA-Style.png')
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
                                elif index == "Transparent2":
                                        cmd='wget https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/picons/installerTransparentPicons2.sh -O - | /bin/sh'
                                        cmdlist.append(cmd)
                                elif index == "BO-HLALA-Style":
                                        cmd='wget -O - https://github.com/fairbird/RaedQuickSignal/raw/refs/heads/main/Style/BO-HLALA-Style.tar.gz | tar -xz -C /'
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


class SearchLocationMSN(Screen):
        def __init__(self, session, name):
                Screen.__init__(self, session)
                self.skin = SKIN_SearchLocationMSN
                self.session = session
                self.eventname = name
                self.resultlist = []
                self.setTitle(_("Search Location Weather MSN"))
                self["menu"] = MenuList(self.resultlist)

                self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"], 
                        {
                                "ok": self.okClicked,
                                "cancel": self.close,
                                "up": self.pageUp,
                                "down": self.pageDown
                        }, -1)

                self.showMenu()

        def pageUp(self):
                self['menu'].instance.moveSelection(self['menu'].instance.moveUp)

        def pageDown(self):
                self['menu'].instance.moveSelection(self['menu'].instance.moveDown)

        def showMenu(self):
                try:
                        results = search_title(self.eventname)
                except:
                        results = []
                if len(results) == 0:
                        return False
                self.resultlist = []
                for searchResult in results:
                        try:
                                self.resultlist.append(searchResult)
                        except:
                                pass
                self['menu'].l.setList(self.resultlist)

        def okClicked(self):
                id = self['menu'].getCurrent()
                if id:
                        config.plugins.RaedQuickSignal.city.value = id.replace(", ", ",")
                        config.plugins.RaedQuickSignal.city.save()
                        self.close()
        
def search_title(id):
        url = "http://weather.service.msn.com/find.aspx?outputview=search&weasearchstr=%s&culture=en-US&src=outlook" % id
        msnrequest = compat_Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # add [headers={'User-Agent': 'Mozilla/5.0'}] to fix HTTP Error 403: Forbidden
        try:
                msnpage = compat_urlopen(msnrequest,timeout=5)
        except (compat_URLError, HTTPException, socket.error) as err:
                print("[Location] Error: Unable to retrieve page - Error code: ", str(err))
        content = msnpage.read() if PY3 else msnpage.read().encode("UTF-8", "ignore")
        msnpage.close()
        root = cet_fromstring(content)
        search_results = []
        if content:
                for childs in root:
                        if childs.tag == 'weather':
                                locationcode = "%s" % (childs.attrib.get('weatherlocationname') if PY3 else childs.attrib.get('weatherlocationname').encode("UTF-8", "ignore"))
                                search_results.append(locationcode)
        return search_results


def sessionstart(reason, session=None, **kwargs):
        if reason == 0:
                pSignal.gotSession(session)

def main_menu(menuid, **kwargs):
        if menuid == "mainmenu" and config.plugins.RaedQuickSignal.showplugin.value:
                return [(_("RaedQuickSignal"), main, "RaedQuickSignal", 45)]
        else:
                return []

def run(session, *args, **kwargs):
        session.open(RaedQuickSignalScreen)

def main(session, *args, **kwargs):
        session.open(RaedQuickSignal_setup)


description = _("RaedQuickSignal")

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

        show = config.plugins.RaedQuickSignal.showplugin.value
        selected_options = show.split(",") if show else []

        menulist = PluginDescriptor(
                name=_("RaedQuickSignal"),
                description=description,
                where=PluginDescriptor.WHERE_MENU,
                fnc=main_menu
        )

        extDescriptor = PluginDescriptor(
                name=_("RAED's RaedQuickSignal [RaedQuickSignal]"),
                description=description,
                where=PluginDescriptor.WHERE_EXTENSIONSMENU,
                fnc=run
        )

        if hasattr(PluginDescriptor, "WHERE_CHANNEL_CONTEXT_MENU"):
		contextlist = PluginDescriptor(
			name=_("RAED's RaedQuickSignal [RaedQuickSignal]"),
			description=description,
			where=PluginDescriptor.WHERE_CHANNEL_CONTEXT_MENU,
			fnc=run
		)

        if "Menu" in selected_options:
                result.append(menulist)
        if "Extensions" in selected_options:
                result.append(extDescriptor)
        if "Channellist" in selected_options:
                result.append(contextlist)
                if DreamOS():
                        result.append(
                                PluginDescriptor(
                                        name=_("RAED's RaedQuickSignal [RaedQuickSignal]"),
                                        description=description,
                                        where=PluginDescriptor.WHERE_CHANNEL_SELECTION_RED,
                                        fnc=run
                                )
                        )
        return result
