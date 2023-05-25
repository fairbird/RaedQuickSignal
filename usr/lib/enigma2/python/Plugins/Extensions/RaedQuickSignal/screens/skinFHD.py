#RAEDQuickSignal (c) RAED 07-02-2014

import os
from enigma import addFont
from Screens.Screen import Screen
from Components.Pixmap import Pixmap
from Components.config import config
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Plugins.Extensions.RaedQuickSignal.tools.configs import *

## Add Fonts codes
IMAGEPLUGIN=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/images/")

if config.plugins.RaedQuickSignal.fontsStyle.value == "Default":
	FontName='Regular'
else:
	fontfile = config.plugins.RaedQuickSignal.fontsStyle.value
	FontName='RSQFont'
	addFont(fontfile, 'RSQFont', 100, 1)

## End Add Fonts codes

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

if config.plugins.RaedQuickSignal.numbers.value == "Numbers":
	NUMBERS = '''
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="{0}; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>'''.format(FontName)
elif config.plugins.RaedQuickSignal.numbers.value == "Resolution":
	NUMBERS = '''
  <widget source="session.CurrentService" render="Label" font="{0};30" position="80,617" size="87,40" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};30" position="171,617" size="19,40" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};30" position="195,617" size="80,40" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>'''.format(FontName)

### SKIN_setup
if DreamOS():
      SKIN_setup = """
<screen name="RaedQuickSignal_setup" position="0,0" size="1920,1080" title="RAED's RaedQuickSignal setup" flags="wfNoBorder" backgroundColor="#16000000">
  <widget source="Title" position="269,40" size="1210,65" render="Label" font="{0};50" foregroundColor="#00ffa500" backgroundColor="#16000000" transparent="1" halign="center"/>
  <widget source="session.VideoPicture" render="Pig" position="1017,168" size="827,437" backgroundColor="#ff000000" zPosition="1"/>
  <eLabel text="Background of VideoPicture" foregroundColor="#00ffffff" backgroundColor="#00ffffff" size="842,452" position="1010,160" zPosition="-10"/>
  <widget source="global.CurrentTime" font="{0};55" foregroundColor="#00ffffff" backgroundColor="#16000000" halign="center" position="1565,3" render="Label" size="353,84"  transparent="1" valign="center" zPosition="5">
    <convert type="ClockToText">Default</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1565,78" size="353,65" font="{0};50" halign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" zPosition="6">
    <convert type="ClockToText">Format:%d.%m.%Y</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1010,611" zPosition="1" size="842,68" font="{0};34" halign="center" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="ServiceName">Name</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="1010,671" zPosition="2" size="842,68" font="{0};32" halign="center" foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="EventName">Name</convert>
  </widget>
  <widget name="config" position="15,140" size="981,690" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" />
  <widget source="key_red" render="Label" position="1,1035" zPosition="2" size="381,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_green" render="Label" position="544,1035" zPosition="2" size="381,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_yellow" render="Label" position="1074,1035" zPosition="2" size="381,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_blue" render="Label" position="1534,1035" zPosition="2" size="381,32" font="{0};25" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <ePixmap position="68,1070" zPosition="1" size="250,4" pixmap="{1}/images/red.png" alphatest="blend"/>
  <ePixmap position="605,1070" zPosition="1" size="250,4" pixmap="{1}/images/green.png" alphatest="blend"/>
  <ePixmap position="1137,1070" zPosition="1" size="250,4" pixmap="{1}/images/yellow.png" alphatest="blend"/>
  <ePixmap position="1599,1070" zPosition="1" size="250,4" pixmap="{1}/images/blue.png" alphatest="blend"/>
  <widget source="help" render="Label" position="15,826" size="1187,199" font="{0};32" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="1229,773" size="400,225" zPosition="5" alphatest="blend"/>
  <ePixmap position="1326,785" zPosition="3" size="200,200" pixmap="{1}/images/fairbirdfhd.png" alphatest="blend"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
else:
      SKIN_setup = """
<screen name="RaedQuickSignal_setup" position="0,0" size="1920,1080" title="RAED's RaedQuickSignal setup" flags="wfNoBorder" backgroundColor="#16000000">
  <widget source="Title" position="269,40" size="1210,65" render="Label" font="{0};50" foregroundColor="#00ffa500" backgroundColor="#16000000" transparent="1" halign="center"/>
  <widget source="session.VideoPicture" render="Pig" position="1017,168" size="827,437" backgroundColor="#ff000000" zPosition="1"/>
  <eLabel text="Background of VideoPicture" foregroundColor="#00ffffff" backgroundColor="#00ffffff" size="842,452" position="1010,160" zPosition="-10"/>
  <widget source="global.CurrentTime" font="{0};55" foregroundColor="#00ffffff" backgroundColor="#16000000" halign="center" position="1565,3" render="Label" size="353,84" transparent="1" valign="center" zPosition="5">
    <convert type="ClockToText">Default</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1565,78" size="353,65" font="{0};50" halign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" zPosition="6">
    <convert type="ClockToText">Format:%d.%m.%Y</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1010,611" zPosition="1" size="842,68" font="{0};34" halign="center" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="ServiceName">Name</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="1010,671" zPosition="2" size="842,68" font="{0};32" halign="center" foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="EventName">Name</convert>
  </widget>
  <widget name="config" position="15,140" size="981,690" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="2" font="{0};30" secondFont="{0};28" itemHeight="40" />
  <widget source="key_red" render="Label" position="1,1035" zPosition="2" size="381,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_green" render="Label" position="544,1035" zPosition="2" size="381,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_yellow" render="Label" position="1074,1035" zPosition="2" size="381,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_blue" render="Label" position="1534,1035" zPosition="2" size="381,32" font="{0};25" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <ePixmap position="68,1070" zPosition="1" size="250,4" pixmap="{1}/images/red.png" alphatest="blend"/>
  <ePixmap position="605,1070" zPosition="1" size="250,4" pixmap="{1}/images/green.png" alphatest="blend"/>
  <ePixmap position="1137,1070" zPosition="1" size="250,4" pixmap="{1}/images/yellow.png" alphatest="blend"/>
  <ePixmap position="1599,1070" zPosition="1" size="250,4" pixmap="{1}/images/blue.png" alphatest="blend"/>
  <widget source="help" render="Label" position="15,826" size="1187,199" font="{0};32" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="1229,773" size="400,225" zPosition="5" alphatest="blend"/>
  <ePixmap position="1326,785" zPosition="3" size="200,200" pixmap="{1}/images/fairbirdfhd.png" alphatest="blend"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_setup2
if DreamOS():
      SKIN_setup2 = """
<screen backgroundColor="#16000000" name="RaedQuickSignal_setup" position="center,center" size="1050,935" title="RAED's RaedQuickSignal setup" flags="wfNoBorder">
  <eLabel position="0,53" size="1050,1" zPosition="10" backgroundColor="#00ffffff" transparent="0"/>
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bab329" position="30,5" size="981,45" transparent="1" />
  <widget name="config" position="15,60" size="1015,600" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" />
  <widget source="key_red" render="Label" position="45,896" zPosition="2" size="165,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_green" render="Label" position="265,896" zPosition="2" size="165,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <!--widget source="key_yellow" render="Label" position="480,896" zPosition="2" size="200,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" /-->
  <widget source="key_blue" render="Label" position="600,896" zPosition="2" size="284,32" font="{0};25" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <ePixmap position="45,928" zPosition="1" size="165,2" pixmap="{1}/images/red.png" alphatest="blend" />
  <ePixmap position="265,928" zPosition="1" size="165,2" pixmap="{1}/images/green.png" alphatest="blend" />
  <!--ePixmap position="480,928" zPosition="1" size="200,2" pixmap="{1}/images/yellow.png" alphatest="blend" /-->
  <ePixmap position="640,928" zPosition="1" size="200,2" pixmap="{1}/images/blue.png" alphatest="blend" />
  <widget source="help" render="Label" position="45,667" size="554,225" font="{0};28" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="613,667" size="400,225" zPosition="5" alphatest="blend"/>
  <ePixmap position="712,680" size="200,200" zPosition="3" pixmap="{1}/images/fairbirdfhd.png" alphatest="blend" />
 </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
else:
      SKIN_setup2 = """
<screen backgroundColor="#16000000" name="RaedQuickSignal_setup" position="center,center" size="1050,935" title="RAED's RaedQuickSignal setup" flags="wfNoBorder">
  <eLabel position="0,53" size="1050,1" zPosition="10" backgroundColor="#00ffffff" transparent="0"/>
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bab329" position="30,5" size="981,45" transparent="1" />
  <widget name="config" position="15,60" size="1015,600" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" font="{0};30" secondFont="{0};28" itemHeight="40" />
  <widget source="key_red" render="Label" position="45,896" zPosition="2" size="165,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_green" render="Label" position="265,896" zPosition="2" size="165,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <!--widget source="key_yellow" render="Label" position="480,896" zPosition="2" size="200,32" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" /-->
  <widget source="key_blue" render="Label" position="600,896" zPosition="2" size="284,32" font="{0};25" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <ePixmap position="45,928" zPosition="1" size="165,2" pixmap="{1}/images/red.png" alphatest="blend" />
  <ePixmap position="265,928" zPosition="1" size="165,2" pixmap="{1}/images/green.png" alphatest="blend" />
  <!--ePixmap position="480,928" zPosition="1" size="200,2" pixmap="{1}/images/yellow.png" alphatest="blend" /-->
  <ePixmap position="640,928" zPosition="1" size="200,2" pixmap="{1}/images/blue.png" alphatest="blend" />
  <widget source="help" render="Label" position="45,667" size="554,225" font="{0};28" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="613,667" size="400,225" zPosition="5" alphatest="blend"/>
  <ePixmap position="712,680" zPosition="3" size="200,200" pixmap="{1}/images/fairbirdfhd.png" alphatest="blend" />
 </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Picons
if DreamOS():
      SKIN_Picons = """
<screen name="PiconsScreen" backgroundColor="#16000000" position="center,center" size="1050,365" title="RAED's RaedQuickSignal Picons setup" flags="wfNoBorder">
  <eLabel position="0,53" size="1050,1" zPosition="10" backgroundColor="#00ffffff"/>
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bab329" position="30,5" size="981,45" transparent="1"/>
  <widget name="menu" position="15,60" size="615,229" foregroundColor="#00ffffff" backgroundColor="#16000000" foregroundColorSelected="#00000000" backgroundColorSelected="#00ffffff" scrollbarMode="showOnDemand" transparent="1" zPosition="1"/>
  <eLabel text="{1}" position="16,295" size="1015,32" font="{0};32" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <eLabel text="{2}" position="16,330" size="1015,32" font="{0};32" foregroundColor="#00bab329" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="638,62" size="400,225" zPosition="5" alphatest="blend"/>
</screen>
""".format(FontName, title75, title76)
else:
      SKIN_Picons = """
<screen name="PiconsScreen" backgroundColor="#16000000" position="center,center" size="1050,365" title="RAED's RaedQuickSignal Picons setup" flags="wfNoBorder">
  <eLabel position="0,53" size="1050,1" zPosition="10" backgroundColor="#00ffffff"/>
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bab329" position="30,5" size="981,45" transparent="1"/>
  <widget name="menu" position="15,60" size="615,229" font="{0};35" itemHeight="45" foregroundColor="#00ffffff" backgroundColor="#16000000" foregroundColorSelected="#00000000" backgroundColorSelected="#00ffffff" scrollbarMode="showOnDemand" transparent="1" zPosition="1"/>
  <eLabel text="{1}" position="16,295" size="1015,32" font="{0};32" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <eLabel text="{2}" position="16,330" size="1015,32" font="{0};32" foregroundColor="#00bab329" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="638,62" size="400,225" zPosition="5" alphatest="blend"/>
</screen>
""".format(FontName, title75, title76)

### SKIN_WeatherLocation
if DreamOS():
	SKIN_WeatherLocation = """
<screen backgroundColor="#16000000" name="WeatherLocationChoiceList" position="0,0" size="767,1080" title="Location list" flags="wfNoBorder">
  <widget source="Title" render="Label" position="30,11" size="701,74" font="{0};45" transparent="1"/>
  <widget name="choicelist" position="30,95" size="701,890" scrollbarMode="showOnDemand" scrollbarWidth="6" transparent="1"/>
  <eLabel position="75,1065" size="290,5" zPosition="-10" backgroundColor="#00ff2525"/>
  <eLabel position="380,1065" size="290,5" zPosition="-10" backgroundColor="#00389416"/>
  <widget name="key_red" position="75,1018" size="290,45" halign="center" valign="center" zPosition="1" font="{0};35" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget name="key_green" position="380,1018" size="290,45" halign="center" valign="center" zPosition="1" font="{0};35" foregroundColor="#00f0f0f0" transparent="1"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
else:
	SKIN_WeatherLocation = """
<screen backgroundColor="#16000000" name="WeatherLocationChoiceList" position="0,0" size="767,1080" title="Location list" flags="wfNoBorder">
  <widget source="Title" render="Label" position="30,11" size="701,74" font="{0};45" transparent="1"/>
  <widget name="choicelist" font="{0};35" itemHeight="40" position="30,95" size="701,890" scrollbarMode="showOnDemand" scrollbarWidth="6" transparent="1"/>
  <eLabel position="75,1065" size="290,5" zPosition="-10" backgroundColor="#00ff2525"/>
  <eLabel position="380,1065" size="290,5" zPosition="-10" backgroundColor="#00389416"/>
  <widget name="key_red" position="75,1018" size="290,45" halign="center" valign="center" zPosition="1" font="{0};35" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget name="key_green" position="380,1018" size="290,45" halign="center" valign="center" zPosition="1" font="{0};35" foregroundColor="#00f0f0f0" transparent="1"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
### SKIN_SearchLocationMSN
if DreamOS():
	SKIN_SearchLocationMSN = """
		<!-- Search LocationMSN -->
		<screen name="SearchLocationMSN" position="center,center" size="1212,673" title="SearchLocationMSN">
		<widget name="menu" position="20,20" size="1182,640" scrollbarMode="showOnDemand" transparent="1" />
		</screen>
"""
else:
	SKIN_SearchLocationMSN = """
		<!-- Search LocationMSN -->
		<screen name="SearchLocationMSN" position="center,center" size="1212,673" title="SearchLocationMSN">
		<widget name="menu" position="20,20" size="1182,640" font="{0};36" itemHeight="50" scrollbarMode="showOnDemand" transparent="1" />
		</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
##different way ...
#SKIN_WeatherLocation = """
#<screen backgroundColor="#16000000" name="WeatherLocationChoiceList" position="center,center" size="1280,720" title="Location list" flags="wfNoBorder">
#			<widget source="Title" render="Label" position="70,47" size="950,43" font="%(key)s;35" transparent="1" />
#			<widget name="choicelist" position="70,115" size="700,480" scrollbarMode="showOnDemand" scrollbarWidth="6" transparent="1" />
#			<eLabel position=" 55,675" size="290, 5" zPosition="-10" backgroundColor="#00ff2525" />
#			<eLabel position="350,675" size="290, 5" zPosition="-10" backgroundColor="#00389416" />
#			<eLabel position="645,675" size="290, 5" zPosition="-10" backgroundColor="#00bab329" />
#			<eLabel position="940,675" size="290, 5" zPosition="-10" backgroundColor="#000080ff" />
#			<widget name="key_red" position="70,635" size="260,25" zPosition="1" font="%(key)s;20" halign="left" foregroundColor="#00f0f0f0" transparent="1" />
#			<widget name="key_green" position="365,635" size="260,25" zPosition="1" font="%(key)s;20" halign="left" foregroundColor="#00f0f0f0" transparent="1" />
#		</screen>
#""" % {'key': FontName,}

### SKIN_AGC_Picon
SKIN_AGC_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="753,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
    <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="753,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Event_Des
SKIN_AGC_Event_Des_SNRdB = """
 <screen backgroundColor="#16000000" name="AGC_Event_Des" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="{0}; 28" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Event_Des_NOSNRdB = """
 <screen backgroundColor="#16000000" name="AGC_Event_Des" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="{0}; 28" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Weather
SKIN_AGC_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="332,613" size="241,32" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,691" size="400,40" font="{0}; 30" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,636" size="150,60" font="{0}; 45" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="775,694" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,693" size="147,50" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="760,625" size="60,60" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,631" size="147,50" font="{0}; 35" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/risefhd.png" position="850,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="850,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setfhd.png" position="1000,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1000,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
      <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="332,613" size="241,32" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,691" size="400,40" font="{0}; 30" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,636" size="150,60" font="{0}; 45" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="775,694" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,693" size="147,50" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="760,625" size="60,60" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,631" size="147,50" font="{0}; 35" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/risefhd.png" position="850,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="850,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setfhd.png" position="1000,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1000,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Picon
SKIN_Event_Progress_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="753,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="753,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Event_Des
SKIN_Event_Progress_Event_Des_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="{0}; 28" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Event_Des_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="{0}; 28" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Weather
SKIN_Event_Progress_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="332,613" size="241,32" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,691" size="400,40" font="{0}; 30" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,636" size="150,60" font="{0}; 45" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="775,694" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,693" size="147,50" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="760,625" size="60,60" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,631" size="147,50" font="{0}; 35" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/risefhd.png" position="850,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="850,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setfhd.png" position="1000,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1000,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="332,613" size="241,32" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,691" size="400,40" font="{0}; 30" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,636" size="150,60" font="{0}; 45" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="775,694" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,693" size="147,50" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="760,625" size="60,60" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,631" size="147,50" font="{0}; 35" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/risefhd.png" position="850,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="850,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setfhd.png" position="1000,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1000,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Picon_media
SKIN_AGC_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="753,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="753,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Picon_media
SKIN_Event_Progress_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="753,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="753,624" size="190,110" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="30,615" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="995,479" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="5,479" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Full_Screen
SKIN_Full_Screen1 = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,7" size="1860,75" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};45" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="1665,22" size="225,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="1440,52" size="450,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="541,532" size="1319,131" font="{0}; 60" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="794,422" size="315,97" font="{0}; 55" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="1081,422" size="488,97" font="{0}; 55" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="541,716" size="1319,131" font="{0}; 55" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="541,839" size="1319,131" font="{0}; 50" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,150" size="1860,75" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="37,150" size="150,75" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="{0};52"/>
	<widget source="session.FrontendStatus" render="Label" position="1552,150" size="330,75" halign="right" valign="center" transparent="1" font="{0};52">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,240" size="1860,75" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="37,240" size="150,75" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="{0};52"/>
	<widget source="session.FrontendStatus" render="Label" position="1552,240" size="330,75" halign="right" valign="center" transparent="1" font="{0};52">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="SNR:" position="30,360" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,390" size="450,112" font="{0};108" halign="left" backgroundColor="#16000000" transparent="1">
		<convert type="FrontendInfo">SNRdB</convert>
	</widget>
	<eLabel text="AGC:" position="30,540" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,570" size="450,112" backgroundColor="#16000000" transparent="1" font="{0};108" halign="left">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="BER:" position="30,720" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,750" size="450,112" font="{0};108" halign="left" backgroundColor="#16000000" transparent="1">
		<convert type="FrontendInfo">BER</convert>
	</widget>
	<widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="30,900" size="465,135" font="{0};108" halign="left" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" >
		<convert type="FrontendInfo">LOCK</convert>
		<convert type="ConditionalShowHide"/>
	</widget>
	<widget name="Positioner" position="32,92" size="800,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
	<widget name="Satfinder" position="1087,92" size="800,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1006,488" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1006,488" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1006,488" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};45" position="1065,482" size="143,50" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};45" position="1215,482" size="19,50" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};45" position="1239,482" size="143,50" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

SKIN_Full_Screen2_SNRdB = """
<screen backgroundColor="#ccffffff" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,7" size="1860,75" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};45" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="1665,22" size="225,37" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="1440,52" size="450,37" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
	<!-- Tuner Info  -->
	<widget source="session.CurrentService" render="Label" position="19,922" size="1880,65" font="{0}; 50" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="10">
		<convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="19,1006" size="1880,65" font="{0}; 50" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="10">
		<convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,915" size="1860,75" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="37,915" size="150,75" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};52"/>
	<widget source="session.FrontendStatus" render="Label" position="1552,915" size="330,75" halign="right" valign="center" transparent="1" font="{0};52">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,1000" size="1860,75" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="37,1000" size="150,75" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};52"/>
	<widget source="session.FrontendStatus" render="Label" position="1552,1000" size="330,75" halign="right" valign="center" transparent="1" font="{0};52">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Label" position="1552,840" size="330,80" font="{0};70" halign="right" foregroundColor="#00ff2525" backgroundColor="#00ff2525" transparent="1">
		<convert type="FrontendInfo">SNRdB</convert>
	</widget>
	<widget name="Positioner" position="677,12" size="400,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#ccffffff" foregroundColor="#00ff2525" transparent="1"/>
	<widget name="Satfinder" position="1123,12" size="400,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#ccffffff" foregroundColor="#000080ff" transparent="1"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

SKIN_Full_Screen2_NOSNRdB = """
<screen backgroundColor="#ccffffff" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,7" size="1860,75" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};45" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="1665,22" size="225,37" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="1440,52" size="450,37" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
	<!-- Tuner Info  -->
	<widget source="session.CurrentService" render="Label" position="19,922" size="1880,65" font="{0}; 50" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="10">
		<convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="19,1006" size="1880,65" font="{0}; 50" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="10">
		<convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,915" size="1860,75" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="37,915" size="150,75" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};52"/>
	<widget source="session.FrontendStatus" render="Label" position="1552,915" size="330,75" halign="right" valign="center" transparent="1" font="{0};52">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,1000" size="1860,75" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="37,1000" size="150,75" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};52"/>
	<widget source="session.FrontendStatus" render="Label" position="1552,1000" size="330,75" halign="right" valign="center" transparent="1" font="{0};52">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<widget name="Positioner" position="677,12" size="400,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#ccffffff" foregroundColor="#00ff2525" transparent="1"/>
	<widget name="Satfinder" position="1123,12" size="400,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#ccffffff" foregroundColor="#000080ff" transparent="1"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Full_Screen_Picons
SKIN_Full_Screen_Picon_Vertical = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="30,7" size="1860,75" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};45" valign="center"/>
  <widget source="global.CurrentTime" render="Label" position="1665,22" size="225,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1440,52" size="450,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
    <convert type="ClockToText">Date</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <eLabel position="center,90" size="1920,2" backgroundColor="#16000000" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="312,403" size="1300,100" font="{0};60" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="784,284" size="315,97" font="{0};38" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="1048,284" size="541,97" font="{0};55" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="312,502" size="1300,100" font="{0};55" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="312,601" size="1300,100" font="{0};50" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <eLabel position="312,704" size="1300,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="312,795" size="1300,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="312,883" size="1300,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="312,709" size="1300,85" font="{0};36" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>  
  <widget source="session.CurrentService" render="Label" position="1388,709" size="220,85" font="{0};36" zPosition="2" backgroundColor="#16000000" foregroundColor="#00ee00" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="312,798" size="1300,85" font="{0};27" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="5,170" size="300,833" pixmap="{1}/images/icons_quick/icon_snr-scan5.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR:" position="5,1004" size="300,75" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};52" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="5,94" size="300,75" halign="center" valign="center" transparent="1" font="{0};52">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="1617,170" size="300,833" pixmap="{1}/images/icons_quick/icon_snr-scan5.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="AGC:" position="1617,1004" size="300,75" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};52" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="1617,94" size="300,75" halign="center" valign="center" transparent="1" font="{0};52">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="SNR:" position="405,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
  <widget source="session.FrontendStatus" render="Label" position="312,148" size="450,112" font="{0};108" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <eLabel text="AGC:" position="820,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
  <widget source="session.FrontendStatus" render="Label" position="715,150" size="450,112" backgroundColor="#16000000" transparent="1" font="{0};108" halign="center">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="BER:" position="1261,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
  <widget source="session.FrontendStatus" render="Label" position="1163,150" size="450,112" font="{0};108" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">BER</convert>
  </widget>
  <widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="312,265" size="465,135" font="{0};75" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">LOCK</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget name="Positioner" position="751,5" size="800,34" zPosition="1" font="{0};30" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
  <widget name="Satfinder" position="751,44" size="800,34" zPosition="1" font="{0};30" halign="center" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <!-- Picon -->
  <ePixmap position="346,892" size="280,180" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="354,900" size="265,165" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="662,892" size="280,180" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="670,900" size="265,165" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="982,892" size="280,180" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="989,900" size="265,165" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1298,892" size="280,180" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1305,900" size="265,165" transparent="1" alphatest="blend" zPosition="3"/>
  <ePixmap position="1572,15" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="715,358" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="715,358" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="715,358" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};45" position="790,352" size="143,50" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};45" position="950,352" size="19,50" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};45" position="981,352" size="143,50" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

SKIN_Full_Screen_Picon_media_Vertical = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="30,7" size="1860,75" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};45" valign="center"/>
  <widget source="global.CurrentTime" render="Label" position="1665,22" size="225,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1440,52" size="450,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
    <convert type="ClockToText">Date</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <eLabel position="center,90" size="1920,2" backgroundColor="#16000000" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="312,403" size="1300,100" font="{0};60" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="784,284" size="315,97" font="{0};38" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="1048,284" size="541,97" font="{0};55" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="312,502" size="1300,100" font="{0};55" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="312,601" size="1300,100" font="{0};50" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <eLabel position="312,704" size="1300,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="312,795" size="1300,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="312,883" size="1300,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="312,709" size="1300,85" font="{0};36" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>  
  <widget source="session.CurrentService" render="Label" position="1388,709" size="220,85" font="{0};36" zPosition="2" backgroundColor="#16000000" foregroundColor="#00ee00" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="312,798" size="1300,85" font="{0};27" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="5,170" size="300,833" pixmap="{1}/images/icons_quick/icon_snr-scan5.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR:" position="5,1004" size="300,75" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};52" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="5,94" size="300,75" halign="center" valign="center" transparent="1" font="{0};52">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="1617,170" size="300,833" pixmap="{1}/images/icons_quick/icon_snr-scan5.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="AGC:" position="1617,1004" size="300,75" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};52" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="1617,94" size="300,75" halign="center" valign="center" transparent="1" font="{0};52">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="SNR:" position="405,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
  <widget source="session.FrontendStatus" render="Label" position="312,148" size="450,112" font="{0};108" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <eLabel text="AGC:" position="820,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
  <widget source="session.FrontendStatus" render="Label" position="715,150" size="450,112" backgroundColor="#16000000" transparent="1" font="{0};108" halign="center">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="BER:" position="1261,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
  <widget source="session.FrontendStatus" render="Label" position="1163,150" size="450,112" font="{0};108" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">BER</convert>
  </widget>
  <widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="312,265" size="465,135" font="{0};75" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">LOCK</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget name="Positioner" position="751,5" size="800,34" zPosition="1" font="{0};30" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
  <widget name="Satfinder" position="751,44" size="800,34" zPosition="1" font="{0};30" halign="center" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <!-- Picon -->
  <ePixmap position="346,892" size="280,180" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="354,900" size="265,165" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="662,892" size="280,180" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="670,900" size="265,165" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="982,892" size="280,180" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="989,900" size="265,165" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1298,892" size="280,180" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1305,900" size="265,165" transparent="1" alphatest="blend" zPosition="3"/>
  <ePixmap position="1572,15" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="715,358" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="715,358" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="715,358" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};45" position="790,352" size="143,50" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};45" position="950,352" size="19,50" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};45" position="981,352" size="143,50" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Full_Screen_Picons_ECM
SKIN_Full_Screen_Picon_Ecm1_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/ArmyTouch/FHD/frame_base-fs8.png"/>
    <ePixmap position="119,140" size="383,629" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1419,140" size="383,629" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="center,140" size="270,30" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="42,947" size="601,108" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="660,947" size="601,108" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1278,947" size="601,108" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="548,559" size="825,209" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="83,780" size="1752,96" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="837,268" size="246,78" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="596,247" size="729,300" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="665,185" size="591,50" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <eLabel text="RAEDQuickSignal" position="60,16" size="1800,72" font="{0};54" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="672,186" size="576,44" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="663,954" size="595,45" zPosition="2" font="{0}; 38" halign="center" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="124,192" size="374,507" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="1424,192" size="374,507" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="846,271" size="233,74" zPosition="2" font="{0}; 60" halign="center" foregroundColor="#00ff7a00" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="867,137" size="185,44" zPosition="2" font="{0};48" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="234,141" size="150,50" zPosition="2" font="{0};48" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="1535,141" size="150,50" zPosition="2" font="{0};48" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="551,565" size="819,203" zPosition="2" font="{0};25" halign="center" valign="top"  foregroundColor="#000099ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="689,998" size="396,55" zPosition="2" font="{0};26" halign="left" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1092,1005" size="143,45" zPosition="2" font="{0};38" halign="right" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="462,833" size="992,38" zPosition="2" font="{0};27" halign="center" valign="top" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="575,788" size="420,38" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="920,788" size="410,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="920,788" size="410,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="920,788" size="410,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="920,788" size="410,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="86,784" size="358,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="86,829" size="358,40" zPosition="2" font="{0};38" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1474,784" size="358,38" zPosition="2" font="{0};38" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="827,361" size="267,165" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="830,364" size="261,159" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="617,268" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="620,271" size="186,114" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="617,406" size="192,120" zPosition="3" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="620,409" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1112,268" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="1115,271" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1112,406" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1115,409" size="186,114" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="45,954" size="595,45" font="{0};38" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="45,1005" size="595,45" font="{0};38" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1281,1005" size="595,45" font="{0};38" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1281,954" size="595,45" font="{0};38" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>
    <widget name="Positioner" position="60,16" size="575,72" zPosition="10" font="{0};35" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" />
    <widget name="Satfinder" position="1283,16" size="575,72" zPosition="10" font="{0};35" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1485,831" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1485,831" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1485,831" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="1729,833" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="1660,833" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="1660,833" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_media_Ecm1_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/ArmyTouch/FHD/frame_base-fs8.png"/>
    <ePixmap position="119,140" size="383,629" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1419,140" size="383,629" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="center,140" size="270,30" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="42,947" size="601,108" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="660,947" size="601,108" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1278,947" size="601,108" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="548,559" size="825,209" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="83,780" size="1752,96" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="837,268" size="246,78" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="596,247" size="729,300" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="665,185" size="591,50" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <eLabel text="RAEDQuickSignal" position="60,16" size="1800,72" font="{0};54" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="672,186" size="576,44" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="663,954" size="595,45" zPosition="2" font="{0}; 38" halign="center" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="124,192" size="374,507" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="1424,192" size="374,507" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="846,271" size="233,74" zPosition="2" font="{0}; 60" halign="center" foregroundColor="#00ff7a00" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="867,130" size="185,44" zPosition="2" font="{0};48" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="234,141" size="150,50" zPosition="2" font="{0};48" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="1535,141" size="150,50" zPosition="2" font="{0};48" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="551,565" size="819,203" zPosition="2" font="{0};25" halign="center" valign="top"  foregroundColor="#000099ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="689,998" size="396,55" zPosition="2" font="{0};26" halign="left" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1092,1005" size="143,45" zPosition="2" font="{0};38" halign="right" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="462,833" size="992,38" zPosition="2" font="{0};27" halign="center" valign="top" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="575,788" size="420,38" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="920,788" size="410,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="920,788" size="410,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="920,788" size="410,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="920,788" size="410,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="86,784" size="358,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="86,829" size="358,40" zPosition="2" font="{0};38" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1474,784" size="358,38" zPosition="2" font="{0};38" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="827,361" size="267,165" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="830,364" size="261,159" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="617,268" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="620,271" size="186,114" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="617,406" size="192,120" zPosition="3" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="620,409" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1112,268" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconCrypt" position="1115,271" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1112,406" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1115,409" size="186,114" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="45,954" size="595,45" font="{0};38" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="45,1005" size="595,45" font="{0};38" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1281,1005" size="595,45" font="{0};38" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1281,954" size="595,45" font="{0};38" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>
    <widget name="Positioner" position="60,16" size="575,72" zPosition="10" font="{0};35" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" />
    <widget name="Satfinder" position="1283,16" size="575,72" zPosition="10" font="{0};35" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1485,831" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1485,831" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1485,831" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="1729,833" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="1660,833" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="1660,833" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_Ecm2_Vertical = """
<screen backgroundColor="#ffffffff" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/ShabahNet/FHD/frame_base-fs8.png"/>
    <ePixmap position="119,140" size="383,629" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1419,140" size="383,629" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="center,135" size="272,80" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="42,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="660,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1278,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="548,559" size="825,209" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="83,780" size="1752,96" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="837,268" size="246,78" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="596,247" size="729,300" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="665,185" size="591,50" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <eLabel text="RAEDQuickSignal" position="60,16" size="1800,72" font="{0};45" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="672,186" size="576,44" zPosition="2" font="{0};28" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="663,954" size="595,45" zPosition="2" font="{0}; 30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="124,192" size="374,507" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="1424,192" size="374,507" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="846,271" size="233,74" zPosition="2" font="{0}; 50" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="867,130" size="185,44" zPosition="2" font="{0};40" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="234,141" size="150,50" zPosition="2" font="{0};40" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="1535,141" size="150,50" zPosition="2" font="{0};40" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="551,565" size="819,203" zPosition="2" font="{0};25" halign="center" valign="top"  foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="689,998" size="396,55" zPosition="2" font="{0};26" halign="left" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1092,1005" size="143,45" zPosition="2" font="{0};30" halign="right" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="462,833" size="992,38" zPosition="2" font="{0};27" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="575,788" size="420,38" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="920,788" size="410,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="920,788" size="410,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="920,788" size="410,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="920,788" size="410,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="86,784" size="358,38" zPosition="2" font="{0};30" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="86,829" size="358,40" zPosition="2" font="{0};30" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1474,784" size="358,38" zPosition="2" font="{0};30" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="827,361" size="267,165" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="830,364" size="261,159" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="617,268" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="620,271" size="186,114" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="617,406" size="192,120" zPosition="3" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="620,409" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1112,268" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="1115,271" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1112,406" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1115,409" size="186,114" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="45,954" size="595,45" font="{0};30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="45,1005" size="595,45" font="{0};30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1281,1005" size="595,45" font="{0};30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1281,954" size="595,45" font="{0};30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>
    <widget name="Positioner" position="60,16" size="575,72" zPosition="10" font="{0};30" halign="left" backgroundColor="#00ffffff" foregroundColor="#41ff9900" transparent="1" valign="center" />
    <widget name="Satfinder" position="1283,16" size="575,72" zPosition="10" font="{0};30" backgroundColor="#00ffffff" foregroundColor="#0000deff" transparent="1" valign="center" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1485,831" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1485,831" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1485,831" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="1729,833" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="1660,833" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="1660,833" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_media_Ecm2_Vertical = """
<screen backgroundColor="#ffffffff" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/ShabahNet/FHD/frame_base-fs8.png"/>
    <ePixmap position="119,140" size="383,629" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1419,140" size="383,629" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="center,135" size="272,80" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="42,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="660,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1278,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="548,559" size="825,209" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="83,780" size="1752,96" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="837,268" size="246,78" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="596,247" size="729,300" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="665,185" size="591,50" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <eLabel text="RAEDQuickSignal" position="60,16" size="1800,72" font="{0};48" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="672,186" size="576,44" zPosition="2" font="{0};28" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="663,954" size="595,45" zPosition="2" font="{0}; 30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="124,192" size="374,507" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="1424,192" size="374,507" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="846,271" size="233,74" zPosition="2" font="{0}; 50" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="867,137" size="185,44" zPosition="2" font="{0};40" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="234,141" size="150,50" zPosition="2" font="{0};40" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="1535,141" size="150,50" zPosition="2" font="{0};40" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="551,565" size="819,203" zPosition="2" font="{0};25" halign="center" valign="top"  foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="689,998" size="396,55" zPosition="2" font="{0};26" halign="left" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1092,1005" size="143,45" zPosition="2" font="{0};30" halign="right" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="462,833" size="992,38" zPosition="2" font="{0};27" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="575,788" size="420,38" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="920,788" size="410,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="920,788" size="410,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="920,788" size="410,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="920,788" size="410,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="86,784" size="358,38" zPosition="2" font="{0};30" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="86,829" size="358,40" zPosition="2" font="{0};30" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1474,784" size="358,38" zPosition="2" font="{0};30" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="827,361" size="267,165" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="830,364" size="261,159" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="617,268" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="620,271" size="186,114" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="617,406" size="192,120" zPosition="3" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="620,409" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1112,268" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconCrypt" position="1115,271" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1112,406" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1115,409" size="186,114" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="45,954" size="595,45" font="{0};30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="45,1005" size="595,45" font="{0};30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1281,1005" size="595,45" font="{0};30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1281,954" size="595,45" font="{0};30" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>
    <widget name="Positioner" position="60,16" size="575,72" zPosition="10" font="{0};30" halign="left" backgroundColor="#00ffffff" foregroundColor="#41ff9900" transparent="1" valign="center" />
    <widget name="Satfinder" position="1283,16" size="575,72" zPosition="10" font="{0};30" backgroundColor="#00ffffff" foregroundColor="#0000deff" transparent="1" valign="center" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1550,831" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1550,831" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1550,831" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="1729,833" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="1660,833" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="1660,833" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>  
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_Ecm3_Vertical = """
<screen name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/CobaltFHD/FHD/cool1.png"/>
    <ePixmap position="119,140" size="257,559" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/agc_snr.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1545,140" size="257,559" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/pogoda.png" alphatest="blend" transparent="1"/>
    <ePixmap position="67,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="669,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1269,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="573,484" size="794,209" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="108,720" size="1752,96" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="596,157" size="729,300" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick5.png" alphatest="blend" transparent="1"/>
	<widget source="session.Event_Now" render="Label" position="613,162" size="694,40" font="{0};35" halign="center" backgroundColor="#595959" foregroundColor="#00ffffff" transparent="1" zPosition="1">
      <convert type="EventName">Name</convert>
 </widget>
	<eLabel name="new eLabel" position="646,208" size="628,2" backgroundColor="#004f6ef2" />
	<widget backgroundColor="#16000000" font="{0};30" halign="left" position="612,223" render="Label" size="694,221" source="session.Event_Now" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
 </widget>
	  <widget source="global.CurrentTime" render="Label" position="920,50" size="920,50" font="{0};40" valign="center" halign="right" backgroundColor="#54111112" foregroundColor="#58bcff" transparent="1">
      <convert type="ClockToText">Format:%A  %e  %B  %Y     %H:%M </convert>
	   </widget>
    <widget source="Title" position="120,50" size="800,70" render="Label" font="{0};40" foregroundColor="#58bcff" backgroundColor="#00000000" transparent="1" halign="center"/>
    <widget source="session.CurrentService" render="Label" position="677,854" size="568,40" zPosition="2" font="{0};32"  halign="center" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
 <widget source="session.FrontendStatus" render="Progress" position="124,192" size="122,457" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/scale.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="250,192" size="122,457" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/scale.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="124,144" size="125,41" zPosition="2" font="{0};30" halign="center" valign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
 </widget>
    <widget source="session.FrontendStatus" render="Label" position="250,144" size="125,41" zPosition="2" font="{0};30" halign="center" valign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="580,487" size="765,203" zPosition="2" font="{0};24" halign="center" valign="center"  foregroundColor="#000090e6" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="676,900" size="455,53" zPosition="2" font="{0};26" halign="left" valign="top" foregroundColor="#00fffe9e" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1105,905" size="143,45" zPosition="2" font="{0};32" halign="right" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="462,773" size="992,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="487,728" size="120,38" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="602,728" render="Label" size="200,38" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};32" halign="left" position="905,728" size="80,38" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="845,728" size="50,38" font="{0};33" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
  <widget source="session.CurrentService" render="Label" position="120,769" size="300,40"  foregroundColor="#00389416" zPosition="3" font="{0};32" halign="center"  backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="947,728" size="300,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="947,728" size="300,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="947,728" size="300,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="947,728" size="300,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="1270,728" size="80,38" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="1350,728" render="Label" size="80,38" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="86,724" size="358,38" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1461,769" size="344,38" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="1580,728" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="1580,728" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="1580,728" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
<!--Picon-->
	<ePixmap position="393,158" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="397,162" size="182,110" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
	<ePixmap position="393,340" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="397,344" size="182,110" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
	<ePixmap position="1339,158" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1343,162" zPosition="5" size="182,110" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
	<ePixmap position="1339,340" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1343,344" size="182,110" transparent="1" alphatest="blend" zPosition="3" />
    <!--widget source="session.CurrentService" render="Label" position="76,854" size="568,45" font="{0};33" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Number</convert>
    </widget-->
    <widget source="session.CurrentService" render="Label" position="76,905" size="568,45" font="{0};33" halign="center" foregroundColor="#34a36e" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1250,905" size="610,45" font="{0};30" halign="center" foregroundColor="#00bab329" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1250,858" size="610,45" font="{0};30" halign="center" foregroundColor="#58bcff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
 </widget>
 <!--pogoda-->
 <eLabel text="{8}" position="1639,194" size="100,30" font="{0};25" backgroundColor="#54111112" halign="center" transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="1549,194" size="90,90" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="1720,194" size="66,30" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00c1ea02" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/wiatr.png" position="1638,224" size="30,30" zPosition="3" transparent="1" alphatest="blend" />
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/deszcz.png" position="1639,254" size="28,30" zPosition="4" transparent="1" alphatest="blend" />
 <widget source="session.CurrentService" render="Label" position="1676,224" size="120,30" font="{0}; 28" zPosition="3" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="1675,254" size="120,30" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
    <!--eLabel text="%" position="1738,254" size="30,30" zPosition="2" backgroundColor="#54111112" transparent="1" font="{0};25" foregroundColor="#00ffffff" /-->
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/FHD/wsch.png" position="1551,300" size="99,50" zPosition="2" />
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/FHD/zach.png" position="1551,350" size="99,50" zPosition="2" />
    <eLabel text="Rise." position="1655,325" size="75,30" font="{0};21" backgroundColor="#54111112"  transparent="1" zPosition="2" />
	<widget backgroundColor="#54111112" font="{0};25" halign="right" position="1715,321" zPosition="2" render="Label" size="71,30" source="global.CurrentTime" transparent="1" valign="center">
  <convert type="RaedQuickWeather">Sunrise</convert>
 </widget>
    <eLabel text="Set." position="1655,375" size="75,30" font="{0};21" backgroundColor="#54111112"  transparent="1" zPosition="2" />
    <widget backgroundColor="#54111112" font="{0};25" foregroundColor="#00ffffff" halign="right" position="1715,371" zPosition="2" render="Label" size="71,30" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunset</convert>
 </widget>
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather/MoonPhase" position="1561,425" size="80,80" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">PiconMoon</convert>
  </widget>
   <widget source="session.CurrentService" render="Label" position="1611,420" size="165,65" font="{0};25" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Moonlight</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1631,485" size="170,23" font="{0};25" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Moondist</convert>
  </widget>
    <eLabel name="new eLabel" position="1567,522" size="214,2" zPosition="2" backgroundColor="#004f6ef2" />
	<eLabel text="{9}" position="1551,525" size="245,30" font="{0};25" halign="center" valign="center" backgroundColor="#54111112"  transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
	<widget alphatest="blend" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="1551,557" size="90,90" source="session.CurrentService" transparent="1" zPosition="2">
    <convert type="RaedQuickWeather">Picon2</convert>
 </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/temp.png" position="1681,577" size="20,50" zPosition="2" transparent="1" alphatest="blend" />
	<widget source="session.CurrentService" render="Label" font="{0};25" position="1690,569" size="90,30" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Hightemp2</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" font="{0};25" position="1690,603" size="90,30" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Lowtemp2</convert>
 </widget>
<widget name="Positioner" position="522,980" size="575,72" zPosition="10" font="{0};30" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" valign="center" transparent="1"/>
<widget name="Satfinder" position="1160,980" size="575,72" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#0000deff"  valign="center" halign="center" transparent="1"/>
	<ePixmap position="120,990" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/menu.png" alphatest="blend" />
	<ePixmap position="300,990" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/exit.png" alphatest="blend" /> 
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="153,855" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="153,855" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="153,855" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="471,855" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="401,855" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="401,855" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>  
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85, title86, title87)

SKIN_Full_Screen_Picon_media_Ecm3_Vertical = """
<screen name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="Quick Signal Info" flags="wfNoBorder">
 <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/CobaltFHD/FHD/cool1.png"/>
 <ePixmap position="119,140" size="257,559" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/agc_snr.png" alphatest="blend" transparent="1"/>
 <ePixmap position="1545,140" size="257,559" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/pogoda.png" alphatest="blend" transparent="1"/>
 <ePixmap position="67,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
 <ePixmap position="669,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
 <ePixmap position="1269,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1"/>
 <ePixmap position="573,484" size="794,209" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick2.png" alphatest="blend" transparent="1"/>
 <ePixmap position="108,720" size="1752,96" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick3.png" alphatest="blend" transparent="1"/>
 <ePixmap position="596,157" size="729,300" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick5.png" alphatest="blend" transparent="1"/>
 <widget source="session.Event_Now" render="Label" position="613,162" size="694,40" font="{0};35" halign="center" backgroundColor="#595959" foregroundColor="#00ffffff" transparent="1" zPosition="1">
      <convert type="EventName">Name</convert>
 </widget>
 <eLabel name="new eLabel" position="646,208" size="628,2" backgroundColor="#004f6ef2" />
 <widget backgroundColor="#16000000" font="{0};30" halign="left" position="612,223" render="Label" size="694,221" source="session.Event_Now" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
 </widget>
 <widget source="global.CurrentTime" render="Label" position="920,50" size="920,50" font="{0};40" valign="center" halign="right" backgroundColor="#54111112" foregroundColor="#58bcff" transparent="1">
      <convert type="ClockToText">Format:%A  %e  %B  %Y     %H:%M </convert>
 </widget>
 <widget source="Title" position="120,50" size="800,70" render="Label" font="{0};40" foregroundColor="#58bcff" backgroundColor="#00000000" transparent="1" halign="center"/>
 <widget source="session.CurrentService" render="Label" position="677,854" size="568,40" zPosition="2" font="{0};32"  halign="center" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget> 
 <widget source="session.FrontendStatus" render="Progress" position="124,192" size="122,457" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/scale.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
 </widget>
 <widget source="session.FrontendStatus" render="Progress" position="250,192" size="122,457" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/scale.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
 </widget>
 <widget source="session.FrontendStatus" render="Label" position="124,144" size="125,41" zPosition="2" font="{0};30" halign="center" valign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
 </widget>
    <widget source="session.FrontendStatus" render="Label" position="250,144" size="125,41" zPosition="2" font="{0};30" halign="center" valign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="580,487" size="765,203" zPosition="2" font="{0};24" halign="center" valign="center"  foregroundColor="#000090e6" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="676,900" size="455,53" zPosition="2" font="{0};26" halign="left" valign="top" foregroundColor="#00fffe9e" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1105,905" size="143,45" zPosition="2" font="{0};32" halign="right" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="462,773" size="992,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="487,728" size="120,38" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="602,728" render="Label" size="200,38" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};32" halign="left" position="905,728" size="80,38" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="845,728" size="50,38" font="{0};33" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="120,769" size="300,40"  foregroundColor="#00389416" zPosition="3" font="{0};32" halign="center"  backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="947,728" size="300,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="947,728" size="300,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="947,728" size="300,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="947,728" size="300,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="1270,728" size="80,38" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="1350,728" render="Label" size="80,38" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="86,724" size="358,38" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1461,769" size="344,38" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="1580,728" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="1580,728" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="1580,728" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
<!--Picon-->
	<ePixmap position="393,158" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="397,162" size="182,110" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
	<ePixmap position="393,340" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="397,344" size="182,110" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
	<ePixmap position="1339,158" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="1343,162" zPosition="5" size="182,110" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
	<ePixmap position="1339,340" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1343,344" size="182,110" transparent="1" alphatest="blend" zPosition="3" />
	<!--widget source="session.CurrentService" render="Label" position="76,854" size="568,45" font="{0};33" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Number</convert>
 </widget-->
    <widget source="session.CurrentService" render="Label" position="76,905" size="568,45" font="{0};33" halign="center" foregroundColor="#34a36e" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1250,905" size="610,45" font="{0};30" halign="center" foregroundColor="#00bab329" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1250,858" size="610,45" font="{0};30" halign="center" foregroundColor="#58bcff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
 </widget>
 <!--pogoda-->
 <eLabel text="{8}" position="1639,194" size="100,30" font="{0};25" backgroundColor="#54111112" halign="center" transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="weather" position="1549,194" size="90,90" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="1720,194" size="66,30" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00c1ea02" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/wiatr.png" position="1638,224" size="30,30" zPosition="3" transparent="1" alphatest="blend" />
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/deszcz.png" position="1639,254" size="28,30" zPosition="4" transparent="1" alphatest="blend" />
 <widget source="session.CurrentService" render="Label" position="1676,224" size="120,30" font="{0}; 28" zPosition="3" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="1675,254" size="120,30" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
    <!--eLabel text="%" position="1738,254" size="30,30" zPosition="2" backgroundColor="#54111112" transparent="1" font="{0};25" foregroundColor="#00ffffff" /-->
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/FHD/wsch.png" position="1551,300" size="99,50" zPosition="2" />
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/FHD/zach.png" position="1551,350" size="99,50" zPosition="2" />
    <eLabel text="Rise." position="1655,325" size="75,30" font="{0};21" backgroundColor="#54111112"  transparent="1" zPosition="2" />
	<widget backgroundColor="#54111112" font="{0};25" halign="right" position="1715,321" zPosition="2" render="Label" size="71,30" source="global.CurrentTime" transparent="1" valign="center">
  <convert type="RaedQuickWeather">Sunrise</convert>
 </widget>
    <eLabel text="Set." position="1655,375" size="75,30" font="{0};21" backgroundColor="#54111112"  transparent="1" zPosition="2" />
    <widget backgroundColor="#54111112" font="{0};25" foregroundColor="#00ffffff" halign="right" position="1715,371" zPosition="2" render="Label" size="71,30" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunset</convert>
 </widget>
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="weather/MoonPhase" position="1561,425" size="80,80" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">PiconMoon</convert>
  </widget>
   <widget source="session.CurrentService" render="Label" position="1611,420" size="165,65" font="{0};25" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Moonlight</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1631,485" size="170,23" font="{0};25" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Moondist</convert>
  </widget>
    <eLabel name="new eLabel" position="1567,522" size="214,2" zPosition="2" backgroundColor="#004f6ef2" />
	<eLabel text="{9}" position="1551,525" size="245,30" font="{0};25" valign="center" halign="center" backgroundColor="#54111112"  transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
	<widget alphatest="blend" render="RaedQuickSignalPiconUni" path="weather" position="1551,557" size="90,90" source="session.CurrentService" transparent="1" zPosition="2">
    <convert type="RaedQuickWeather">Picon2</convert>
 </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/temp.png" position="1681,577" size="20,50" zPosition="2" transparent="1" alphatest="blend" />
	<widget source="session.CurrentService" render="Label" font="{0};25" position="1690,569" size="90,30" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Hightemp2</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" font="{0};25" position="1690,603" size="90,30" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Lowtemp2</convert>
 </widget> 
<widget name="Positioner" position="522,980" size="575,72" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#41ff9900"  transparent="1" valign="center" halign="center"/>
<widget name="Satfinder" position="1160,980" size="575,72" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center"/>
<ePixmap position="120,990" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/menu.png" alphatest="blend" />
<ePixmap position="300,990" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/exit.png" alphatest="blend" />
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="253,855" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="253,855" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="253,855" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="471,855" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="401,855" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="401,855" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>  
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85, title86, title87)

### SKIN_Full_Screen_Picons_ECM_SNR_ANALOG
SKIN_Full_Screen_Picon_Ecm3_SNR_ANALOG = """
<screen name="SKIN_Full_Screen_Picon_Ecm3_SNR_ANALOG" position="0,0" size="1920,1080" title="Quick Signal Info" backgroundColor="#16000000" flags="wfNoBorder">
  <ePixmap position="325,777" size="1200,250" zPosition="1" pixmap="{1}/images/analog/FHD/analog_tuner_bg.png" alphatest="blend" transparent="1"/>
  <widget source="session.Event_Now" render="Label" position="47,162" size="898,66" font="{0};35" halign="center" backgroundColor="#ff595959" foregroundColor="#7ad927" transparent="1" zPosition="1">
  <convert type="EventName">Name</convert>
</widget>
<widget backgroundColor="#16000000" font="{0};30" position="47,249" render="Label" size="900,220" source="session.Event_Now" transparent="1">
  <convert type="EventName">ExtendedDescription</convert>
</widget>
<widget source="session.CurrentService" render="Label" position="969,162" size="878,305" zPosition="2" font="{0};28" halign="center" valign="center"  foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">ecmfile</convert>
</widget>
  <widget source="global.CurrentTime" render="Label" position="920,50" size="920,50" font="{0};40" valign="center" halign="right" backgroundColor="#16000000" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y  -  %H:%M </convert>
  </widget>
  <widget source="Title" position="120,50" size="800,70" render="Label" font="{0};40" foregroundColor="#58bcff" backgroundColor="#16000000" transparent="1" halign="center"/>
  <!-- SNRdB -->
  <widget source="session.FrontendStatus" render="Label" position="735,969" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="340,969" size="150,45" font="{0}; 35" halign="left" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
<widget source="session.FrontendStatus" render="Label" position="430,969" size="150,45" font="{0}; 35" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="RaedQuickWatches" position="400,790" size="500,450" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">SNR_ANALOG</convert>
    </widget>
    <!-- AGC -->
    <widget source="session.FrontendStatus" render="RaedQuickWatches" position="1000,792" size="500,450" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">AGC_ANALOG</convert>
    </widget>
  <eLabel name="agc" text="AGC:" position="1278,969" size="150,45" font="{0}; 35" halign="right" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
  <widget source="session.FrontendStatus" render="Label" position="1434,969" size="150,45" font="{0}; 35" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <!--Picon-->
    <ePixmap position="203,500" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="208,505" size="240,140" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
    <ePixmap position="617,500" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="622,505" zPosition="5" size="240,140" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
    <ePixmap position="1040,500" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="1045,505" size="240,140" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <ePixmap position="1458,500" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1463,505" size="240,140" transparent="1" alphatest="blend" zPosition="3" />
    <ePixmap position="18,975" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/exit.png" alphatest="blend"/>
<ePixmap position="18,929" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/menu.png" alphatest="blend"/>
<widget name="Positioner" position="5,1020" size="575,60" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#41ff9900"  transparent="1" valign="center" halign="center"/>
<widget name="Satfinder" position="1340,1020" size="575,60" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center"/>
    <widget source="session.CurrentService" render="Label" position="462,719" size="992,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="487,664" size="120,38" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="602,664" render="Label" size="200,38" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};32" halign="left" position="905,664" size="80,38" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="845,664" size="50,38" font="{0};33" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="120,719" size="300,40"  foregroundColor="#00389416" zPosition="3" font="{0};32" halign="center"  backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="947,664" size="300,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="947,664" size="300,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="947,664" size="300,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="947,664" size="300,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="1270,664" size="80,38" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="1350,664" render="Label" size="80,38" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="86,664" size="358,38" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1461,719" size="344,38" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="1580,664" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="1580,664" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="1580,664" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1556,883" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1556,883" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1556,883" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="1786,883" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="1716,883" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="1716,883" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget> 
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85)

SKIN_Full_Screen_Picon_media_Ecm3_SNR_ANALOG = """
<screen name="SKIN_Full_Screen_Picon_media_Ecm3_SNR_ANALOG" position="0,0" size="1920,1080" title="Quick Signal Info" backgroundColor="#16000000" flags="wfNoBorder">
  <ePixmap position="325,777" size="1200,250" zPosition="1" pixmap="{1}/images/analog/FHD/analog_tuner_bg.png" alphatest="blend" transparent="1"/>
  <widget source="session.Event_Now" render="Label" position="47,162" size="898,66" font="{0};35" halign="center" backgroundColor="#ff595959" foregroundColor="#7ad927" transparent="1" zPosition="1">
  <convert type="EventName">Name</convert>
</widget>
<widget backgroundColor="#16000000" font="{0};30" position="47,249" render="Label" size="900,220" source="session.Event_Now" transparent="1">
  <convert type="EventName">ExtendedDescription</convert>
</widget>
<widget source="session.CurrentService" render="Label" position="969,162" size="878,305" zPosition="2" font="{0};28" halign="center" valign="center"  foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">ecmfile</convert>
</widget>
  <widget source="global.CurrentTime" render="Label" position="920,50" size="920,50" font="{0};40" valign="center" halign="right" backgroundColor="#16000000" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y  -  %H:%M </convert>
  </widget>
  <widget source="Title" position="120,50" size="800,70" render="Label" font="{0};40" foregroundColor="#58bcff" backgroundColor="#16000000" transparent="1" halign="center"/>
  <!-- SNRdB -->
  <widget source="session.FrontendStatus" render="Label" position="735,969" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="340,969" size="150,45" font="{0}; 35" halign="left" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
<widget source="session.FrontendStatus" render="Label" position="430,969" size="150,45" font="{0}; 35" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="RaedQuickWatches" position="400,790" size="500,450" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">SNR_ANALOG</convert>
    </widget>
    <!-- AGC -->
    <widget source="session.FrontendStatus" render="RaedQuickWatches" position="1000,792" size="500,450" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">AGC_ANALOG</convert>
    </widget>
  <eLabel name="agc" text="AGC:" position="1278,969" size="150,45" font="{0}; 35" halign="right" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
  <widget source="session.FrontendStatus" render="Label" position="1434,969" size="150,45" font="{0}; 35" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <!--Picon-->
    <ePixmap position="203,500" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="208,505" size="240,140" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
    <ePixmap position="617,500" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="622,505" zPosition="5" size="240,140" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
    <ePixmap position="1040,500" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="1045,505" size="240,140" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <ePixmap position="1458,500" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1463,505" size="240,140" transparent="1" alphatest="blend" zPosition="3" />
    <ePixmap position="18,975" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/exit.png" alphatest="blend"/>
<ePixmap position="18,929" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/menu.png" alphatest="blend"/>
<widget name="Positioner" position="5,1020" size="575,60" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#41ff9900"  transparent="1" valign="center" halign="center"/>
<widget name="Satfinder" position="1340,1020" size="575,60" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center"/>
    <widget source="session.CurrentService" render="Label" position="462,719" size="992,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="487,664" size="120,38" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="602,664" render="Label" size="200,38" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};32" halign="left" position="905,664" size="80,38" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="845,664" size="50,38" font="{0};33" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="120,719" size="300,40"  foregroundColor="#00389416" zPosition="3" font="{0};32" halign="center"  backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="947,664" size="300,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="947,664" size="300,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="947,664" size="300,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="947,664" size="300,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="1270,664" size="80,38" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="1350,664" render="Label" size="80,38" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="86,664" size="358,38" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1461,719" size="344,38" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="1580,664" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="1580,664" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="1580,664" size="125,35" font="{0};30" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1556,883" size="50,40" zPosition="1" pixmap="{1}/images/sd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1556,883" size="50,40" zPosition="2" pixmap="{1}/images/hd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1556,883" size="50,40" zPosition="3" pixmap="{1}/images/uhd_fhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="1786,883" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="1716,883" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="1716,883" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget> 
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85)
