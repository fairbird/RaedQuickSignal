# -*- coding: utf-8 -*-
#RAEDQuickSignal (c) RAED 07-02-2014

import os, sys, traceback
from Components.config import *
from Plugins.Extensions.RaedQuickSignal.plugin import *
from Plugins.Plugin import PluginDescriptor
from Components.config import config, configfile, ConfigSubsection, getConfigListEntry, ConfigSelection, ConfigText, ConfigYesNo
from Components.ConfigList import ConfigListScreen

logFile='/tmp/RaedQuickSignal.log'

def trace_error():
    try:
        traceback.print_exc(file=sys.stdout)
        traceback.print_exc(file=open(logFile, 'a'))
    except:
        pass

GETPath = os.path.join('/usr/share/fonts')
DEFAULTFont = '/usr/share/fonts/Default.ttf'

fonts = []
try:
    if os.path.exists(GETPath):
        for fontName in os.listdir(GETPath):
            fontNamePath = os.path.join(GETPath, fontName)
            if fontName.endswith('.ttf'):
                fontName = fontName[:-4]
                fonts.append((fontNamePath, fontName))
except Exception as error:
	trace_error()

############# plugins
config.plugins.RaedQuickSignal = ConfigSubsection()
config.plugins.RaedQuickSignal.enabledonoff = ConfigYesNo(default=True)
config.plugins.RaedQuickSignal.updateonline = ConfigYesNo(default=True)
config.plugins.RaedQuickSignal.lang = ConfigSelection(default="EN", choices = [
	("EN", "English"),
	("AR", "عربي"),
	("TR", "İngilizce"),
	("IT", "Italiano"),
	("CN", "中國人")
	])

############# language
if config.plugins.RaedQuickSignal.lang.value == "EN":
	from Plugins.Extensions.RaedQuickSignal.language.en import *
elif config.plugins.RaedQuickSignal.lang.value == "AR":
	from Plugins.Extensions.RaedQuickSignal.language.ar import *
elif config.plugins.RaedQuickSignal.lang.value == "TR":
	from Plugins.Extensions.RaedQuickSignal.language.tr import *
elif config.plugins.RaedQuickSignal.lang.value == "IT":
	from Plugins.Extensions.RaedQuickSignal.language.it import *
elif config.plugins.RaedQuickSignal.lang.value == "CN":
	from Plugins.Extensions.RaedQuickSignal.language.ch import *
else:
	from Plugins.Extensions.RaedQuickSignal.language.en import *

############# fonts
config.plugins.RaedQuickSignal.fontsenable = ConfigYesNo(default=False)
config.plugins.RaedQuickSignal.fontsStyle = ConfigSelection(default=DEFAULTFont, choices=fonts)
config.plugins.RaedQuickSignal.fontsSize = ConfigSelection(default = "Default", choices = [
	("80", _("-20")),
	("85", _("-15")),
	("90", _("-10")),
	("Default", _("Default")),
	("110", _("+10")),
	("120", _("+20")),
	("130", _("+30")),
	("140", _("+40")),
	])

############# keymap
config.plugins.RaedQuickSignal.keyname = ConfigSelection(default = "KEY_TEXT", choices = [
	("KEY_TEXT", _("TEXT")),
	("KEY_TV", _("TV")),
	("KEY_RADIO", _("RADIO")),
	("KEY_OK", _("OK")),
	("KEY_HELP", _("HELP")),
	("KEY_INFO", _("INFO")),
	("KEY_RED", _("RED")),
	("KEY_GREEN", _("GREEN")),
	("KEY_BLUE", _("BLUE")),
	("KEY_VIDEO", _("PVR")),
	("KEY_0", _("0")),
	("KEY_1", _("1")),
	("KEY_2", _("2")),
	("KEY_3", _("3")),
	("KEY_F1", _("f1")),
	("KEY_F2", _("f2")),
	("KEY_F3", _("f3"))
	])

############# style of skin
config.plugins.RaedQuickSignal.style = ConfigSelection(default = "AGC1", choices = [
	("AGC1", _("AGC Progress + Picon")),
	("AGC2", _("AGC Progress + Event Description")),
	("AGC3", _("AGC Progress + Weather")),
	("Event1", _("Event Progress + Picon")),
	("Event2", _("Event Progress + Event Description")),
	("Event3", _("Event Progress + Weather")),
	("Full1", _("Full Screen without any extra functions1")),
	("Full2", _("Full Screen without any extra functions2")),
	("Full3", _("Full Screen + Picon + Virtical")),
	("Full4", _("Full Screen + Picon + Ecm + Virtical1")),
	("Full5", _("Full Screen + Picon + Ecm + Virtical2")),
	("Full6", _("Full Screen + Picon + Ecm + Virtical3")),
	("SNR_ANALOG", _("Full Screen + Picon + Ecm + SNR-AGC_ANALOG"))
	])

############# DB Value
config.plugins.RaedQuickSignal.enabledBD = ConfigSelection(default = "Enable", choices = [
	("Enable", _("%s") % title1),
	("Disable", _("%s") % title2)
	])

############# numbers/Resolution
config.plugins.RaedQuickSignal.numbers = ConfigSelection(default = "Numbers", choices = [
	("Numbers", _("%s") % title3),
	("Resolution", _("%s") % title4)
	])

############# Piocns
config.plugins.RaedQuickSignal.piconpath = ConfigSelection(default = "PLUGIN", choices = [
	("PLUGIN", _("%s") % title5),
	("MEDIA", _("%s") % title6)
	])
	
############# Weather
config.plugins.RaedQuickSignal.Searchmethod = ConfigSelection(default = "search", choices = [
	("search", _("%s") % title90),
	("chosse", _("%s") % title91)
	])
config.plugins.RaedQuickSignal.refreshInterval = ConfigNumber(default=30) #in minutes
config.plugins.RaedQuickSignal.city = ConfigText(default="Manama", visible_width = 250, fixed_size = False)
config.plugins.RaedQuickSignal.windtype = ConfigSelection(default="ms", choices = [
	("ms", _("%s") % title7),
	("fts", _("%s") % title8),
	("kmh", _("%s") % title9),
	("mph", _("%s") % title10),
	("knots", _("%s") % title11)
	])
config.plugins.RaedQuickSignal.degreetype = ConfigSelection(default="C", choices = [
	("C", _("%s") % title12),
	("F", _("%s") % title13)
	])
config.plugins.RaedQuickSignal.weather_location= ConfigText(default="bh-BH", visible_width = 250, fixed_size = False)     
