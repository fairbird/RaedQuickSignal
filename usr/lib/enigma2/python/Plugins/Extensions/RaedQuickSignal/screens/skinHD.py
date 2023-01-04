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

if config.plugins.RaedQuickSignal.numbers.value == "Numbers":
	NUMBERS = '''
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="{0}; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>'''.format(FontName)
elif config.plugins.RaedQuickSignal.numbers.value == "Resolution":
	NUMBERS = '''
  <widget source="session.CurrentService" render="Label" font="{0};18" position="40,398" size="60,25" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};18" position="98,398" size="19,25" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};18" position="112,398" size="60,25" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>'''.format(FontName)

### SKIN_setup
SKIN_setup = """
<screen name="RaedQuickSignal_setup" position="0,0" size="1280,720" title="RAED's RaedQuickSignal setup" backgroundColor="#16000000" flags="wfNoBorder">
  <widget source="Title" position="224,13" size="782,40" render="Label" font="{0};26" foregroundColor="#00ffa500" backgroundColor="#16000000" transparent="1" halign="center"/>
  <eLabel text="Background of VideoPicture" foregroundColor="#00ffffff" backgroundColor="#00ffffff" size="543,272" position="688,85" zPosition="-10"/>
  <widget source="session.VideoPicture" render="Pig" position="693,90" size="532,263" backgroundColor="#ff000000" zPosition="1"/>
  <widget font="{0};35" foregroundColor="#00ffffff" backgroundColor="#16000000" halign="center" position="1072,0" render="Label" size="206,44" source="global.CurrentTime" transparent="1" valign="center" zPosition="5">
    <convert type="ClockToText">Default</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1072,44" size="206,40" font="{0};28" halign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1">
    <convert type="ClockToText">Format:%d.%m.%Y</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="688,357" zPosition="1" size="543,40" font="{0};24" halign="center" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="ServiceName">Name</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="688,393" zPosition="2" size="543,40" font="{0};25" halign="center" foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="EventName">Name</convert>
  </widget>
  <widget name="config" position="10,69" size="667,460" scrollbarMode="showOnDemand" foregroundColor="#00f0f0f0" backgroundColor="#16000000"/>
  <widget source="key_red" render="Label" position="2,686" zPosition="2" size="299,25" font="{0};20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_green" render="Label" position="331,686" zPosition="2" size="299,25" font="{0};20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_yellow" render="Label" position="647,686" zPosition="2" size="299,25" font="{0};20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_blue" render="Label" position="975,689" zPosition="2" size="299,25" font="{0};20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <ePixmap position="47,713" zPosition="1" size="200,3" pixmap="{1}/images/red.png" alphatest="blend"/>
  <ePixmap position="381,713" zPosition="1" size="200,3" pixmap="{1}/images/green.png" alphatest="blend"/>
  <ePixmap position="692,713" zPosition="1" size="200,3" pixmap="{1}/images/yellow.png" alphatest="blend"/>
  <ePixmap position="1025,713" zPosition="1" size="200,3" pixmap="{1}/images/blue.png" alphatest="blend"/>
  <widget source="help" render="Label" position="10,539" size="723,142" font="{0};23" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="756,441" size="400,225" zPosition="5" alphatest="on"/>
  <ePixmap position="877,478" zPosition="3" size="150,150" pixmap="{1}/images/fairbirdhd.png" alphatest="blend"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_setup2
SKIN_setup2 = """
<screen backgroundColor="#16000000" name="RaedQuickSignal_setup" position="center,center" size="745,662" title="RAED's RaedQuickSignal setup" flags="wfNoBorder">
  <eLabel position="0,40" size="745,1" zPosition="10" backgroundColor="#00ffffff" transparent="0"/>
  <widget source="Title" render="Label" font="{0};24" foregroundColor="#00bab329" position="20,5" size="712,34" transparent="1" />
  <widget name="config" position="15,45" size="720,357" scrollbarMode="showOnDemand" foregroundColor="#00f0f0f0" backgroundColor="#16000000"/>
  <widget source="key_red" render="Label" position="17,625" zPosition="2" size="165,30" font="{0};20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_green" render="Label" position="206,625" zPosition="2" size="165,30" font="{0};20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <!--widget source="key_yellow" render="Label" position="387,625" zPosition="2" size="200,30" font="{0};20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" /-->
  <widget source="key_blue" render="Label" position="495,624" zPosition="2" size="234,30" font="{0};20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <ePixmap position="17,658" zPosition="1" size="165,2" pixmap="{1}/images/red.png" alphatest="blend" />
  <ePixmap position="206,658" zPosition="1" size="165,2" pixmap="{1}/images/green.png" alphatest="blend" />
  <!--ePixmap position="387,658" zPosition="1" size="200,2" pixmap="{1}/images/yellow.png" alphatest="blend" /-->
  <ePixmap position="515,658" zPosition="1" size="200,2" pixmap="{1}/images/blue.png" alphatest="blend" />
  <widget source="help" render="Label" position="15,406" size="309,225" font="{0};23" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="330,406" size="400,225" zPosition="5" alphatest="on"/>
  <ePixmap position="448,443" zPosition="3" size="150,150" pixmap="{1}/images/fairbirdhd.png" alphatest="blend" />
 </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Picons
SKIN_Picons = """
<screen name="PiconsScreen" backgroundColor="#16000000" position="center,center" size="1050,375" title="RAED's RaedQuickSignal Picons setup" flags="wfNoBorder">
  <eLabel position="0,53" size="1050,1" zPosition="10" backgroundColor="#00ffffff"/>
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bab329" position="30,5" size="981,45" transparent="1"/>
  <widget name="menu" position="15,60" size="615,229" foregroundColor="#00ffffff" backgroundColor="#16000000" foregroundColorSelected="#00000000" backgroundColorSelected="#00ffffff" scrollbarMode="showOnDemand" transparent="1" zPosition="1"/>
  <eLabel text="{1}" position="16,298" size="1015,32" font="{0};32" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <eLabel text="{2}" position="16,338" size="1015,32" font="{0};32" foregroundColor="#00bab329" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="638,62" size="400,225" zPosition="5" alphatest="blend"/>
</screen>
""".format(FontName, title75, title76)

### SKIN_WeatherLocation
SKIN_WeatherLocation = """
<screen backgroundColor="#16000000" name="WeatherLocationChoiceList" position="0,0" size="600,720" title="Location list" flags="wfNoBorder">
  <widget source="Title" render="Label" position="15,8" size="568,43" font="{0};35" transparent="1"/>
  <widget name="choicelist" position="15,57" size="568,605" scrollbarMode="showOnDemand" scrollbarWidth="6" transparent="1"/>
  <eLabel position="5,710" size="290,5" zPosition="-10" backgroundColor="#00ff2525"/>
  <eLabel position="300,710" size="290,5" zPosition="-10" backgroundColor="#00389416"/>
  <widget name="key_red" position="15,680" size="260,25" halign="center" valign="center" zPosition="1" font="{0};20" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget name="key_green" position="315,680" size="260,25" halign="center" valign="center" zPosition="1" font="{0};20" foregroundColor="#00f0f0f0" transparent="1"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_AGC_Picon
SKIN_AGC_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="{0}; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="{0}; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="{0}; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Event_Des
SKIN_AGC_Event_Des_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Event_Des" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="{0}; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="{0}; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="185,403" size="410,65" font="{0}; 18" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
 <widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Event_Des_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Event_Des" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="{0}; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="185,403" size="410,65" font="{0}; 18" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
 <widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Weather
SKIN_AGC_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="{0}; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="{0}; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="180,400" size="80,22" font="{0}; 20" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="171,420" size="58,58" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="233,449" size="200,25" font="{0}; 17" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="236,420" size="77,30" font="{0}; 24" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="416,445" size="40,33" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind.png" />
<widget source="session.CurrentService" render="Label" position="336,436" size="80,30" font="{0}; 16" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="410,405" size="30,30" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd.png" />
<widget source="session.CurrentService" render="Label" position="329,405" size="80,30" font="{0}; 20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/rise.png" position="456,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="456,440" size="60,25" font="{0};20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/set.png" position="530,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="530,440" size="60,25" font="{0};20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="{0}; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="180,400" size="80,22" font="{0}; 20" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="171,420" size="58,58" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="233,449" size="200,25" font="{0}; 17" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="236,420" size="77,30" font="{0}; 24" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="416,445" size="40,33" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind.png" />
<widget source="session.CurrentService" render="Label" position="336,436" size="80,30" font="{0}; 16" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="410,405" size="30,30" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd.png" />
<widget source="session.CurrentService" render="Label" position="329,405" size="80,30" font="{0}; 20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/rise.png" position="456,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="456,440" size="60,25" font="{0};20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/set.png" position="530,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="530,440" size="60,25" font="{0};20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Picon
SKIN_Event_Progress_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="{0}; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="{0};30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="{0};30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Event_Des
SKIN_Event_Progress_Event_Des_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="{0}; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="{0};30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="185,403" size="410,65" font="{0}; 18" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
 <widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Event_Des_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="{0};30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="185,403" size="410,65" font="{0}; 18" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
 <widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Weather
SKIN_Event_Progress_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="{0}; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="{0};30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="180,400" size="80,22" font="{0}; 20" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="171,420" size="58,58" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="233,449" size="200,25" font="{0}; 17" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="236,420" size="77,30" font="{0}; 24" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="416,445" size="40,33" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind.png" />
<widget source="session.CurrentService" render="Label" position="336,436" size="80,30" font="{0}; 18" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="410,405" size="30,30" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd.png" />
<widget source="session.CurrentService" render="Label" position="329,405" size="80,30" font="{0}; 20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/rise.png" position="456,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="456,440" size="60,25" font="{0};20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/set.png" position="530,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="530,440" size="60,25" font="{0};20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="{0};30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="180,400" size="80,22" font="{0}; 20" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="171,420" size="58,58" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="233,449" size="200,25" font="{0}; 17" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="236,420" size="77,30" font="{0}; 24" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="416,445" size="40,33" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind.png" />
<widget source="session.CurrentService" render="Label" position="336,436" size="80,30" font="{0}; 18" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="410,405" size="30,30" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd.png" />
<widget source="session.CurrentService" render="Label" position="329,405" size="80,30" font="{0}; 20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/rise.png" position="456,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="456,440" size="60,25" font="{0};20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/set.png" position="530,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="530,440" size="60,25" font="{0};20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Picon_media
SKIN_AGC_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="{0}; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="{0}; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="{0}; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Picon_media
SKIN_Event_Progress_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="{0}; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="{0};30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="{0};23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="{0}; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="{1}/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="{0}; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="{0};30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,161" size="600,170" font="{0}; 18" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="{0}; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="{0}; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="{1}/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="{1}/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="{0}; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="17,400" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="{0}; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="{0}; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="495,319" size="300,18" zPosition="1" font="{0};15" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
   <widget name="Positioner" position="5,319" size="300,18" zPosition="1" font="{0};15" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
   {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Full_Screen
SKIN_Full_Screen1 = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1280,720" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,7" size="734,75" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};38" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="1050,17" size="225,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="825,52" size="450,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="352,353" size="907,95" font="{0}; 45" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="465,234" size="237,55" font="{0}; 38" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="661,289" size="488,55" font="{0}; 38" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="352,478" size="907,95" font="{0}; 40" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="354,584" size="907,95" font="{0}; 40" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,120" size="1240,60" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="37,120" size="150,60" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="{0};40"/>
	<widget source="session.FrontendStatus" render="Label" position="1042,120" size="230,60" halign="right" valign="center" transparent="1" font="{0};40">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,190" size="1240,60" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="37,190" size="150,60" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="{0};40"/>
	<widget source="session.FrontendStatus" render="Label" position="1042,190" size="230,60" halign="right" valign="center" transparent="1" font="{0};40">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="SNR:" position="30,260" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,296" size="300,80" backgroundColor="#16000000" font="{0};75" halign="left" transparent="1">
		<convert type="FrontendInfo">SNRdB</convert>
	</widget>
	<eLabel text="AGC:" position="30,385" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,425" size="300,80" backgroundColor="#16000000" font="{0};75" halign="left" transparent="1">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="BER:" position="30,510" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,550" size="300,80" font="{0};75" halign="left" backgroundColor="#16000000" transparent="1">
		<convert type="FrontendInfo">BER</convert>
	</widget>
	<widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="30,635" size="300,80" font="{0};75" halign="left" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" >
		<convert type="FrontendInfo">LOCK</convert>
		<convert type="ConditionalShowHide"/>
	</widget>
	<widget name="Positioner" position="30,87" size="507,28" halign="center"  zPosition="1" font="{0};25" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
	<widget name="Satfinder" position="765,87" size="507,28" halign="center"  zPosition="1" font="{0};25" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
	</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

SKIN_Full_Screen2_SNRdB = """
<screen backgroundColor="#ccffffff" name="RaedQuickSignalScreen" position="0,0" size="1280,720" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,7" size="734,75" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};38" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="1050,17" size="225,37" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="825,52" size="450,37" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="18,590" size="1258,52" font="{0}; 40" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="5">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="18,661" size="1258,52" font="{0}; 40" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="5">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,585" size="1240,60" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="37,585" size="150,60" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};40"/>
	<widget source="session.FrontendStatus" render="Label" position="1042,585" size="230,60" halign="right" valign="center" transparent="1" font="{0};40">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,655" size="1240,60" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="37,655" size="150,60" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};40"/>
	<widget source="session.FrontendStatus" render="Label" position="1042,655" size="230,60" halign="right" valign="center" transparent="1" font="{0};40">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Label" position="1042,525" size="230,60" foregroundColor="#00ff2525" backgroundColor="#00ff2525" font="{0};55" halign="right" transparent="1">
		<convert type="FrontendInfo">SNRdB</convert>
	</widget>
	<widget name="Positioner" position="538,27" size="300,28" halign="center"  zPosition="1" font="{0};25" backgroundColor="#00ff2525" foregroundColor="#00ff2525" transparent="1"/>
	<widget name="Satfinder" position="789,27" size="300,28" halign="center"  zPosition="1" font="{0};25" backgroundColor="#000080ff" foregroundColor="#000080ff" transparent="1"/>
	</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

SKIN_Full_Screen2_NOSNRdB = """
<screen backgroundColor="#ccffffff" name="RaedQuickSignalScreen" position="0,0" size="1280,720" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,7" size="734,75" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};38" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="1050,17" size="225,37" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="825,52" size="450,37" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="18,590" size="1258,52" font="{0}; 40" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="5">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="18,661" size="1258,52" font="{0}; 40" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="5">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,585" size="1240,60" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="37,585" size="150,60" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};40"/>
	<widget source="session.FrontendStatus" render="Label" position="1042,585" size="230,60" halign="right" valign="center" transparent="1" font="{0};40">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,655" size="1240,60" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="37,655" size="150,60" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};40"/>
	<widget source="session.FrontendStatus" render="Label" position="1042,655" size="230,60" halign="right" valign="center" transparent="1" font="{0};40">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<widget name="Positioner" position="538,27" size="300,28" halign="center"  zPosition="1" font="{0};25" backgroundColor="#00ff2525" foregroundColor="#00ff2525" transparent="1"/>
	<widget name="Satfinder" position="789,27" size="300,28" halign="center"  zPosition="1" font="{0};25" backgroundColor="#000080ff" foregroundColor="#000080ff" transparent="1"/>
	</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Full_Screen_Picons
SKIN_Full_Screen_Picon_Vertical = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1280,720" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="5,7" size="734,75" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};38" valign="center"/>
  <widget source="global.CurrentTime" render="Label" position="1050,17" size="225,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="825,52" size="450,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
    <convert type="ClockToText">Date</convert>
  </widget>
  <eLabel position="0,84" size="1280,2" backgroundColor="#16000000" zPosition="4"/>
  <eLabel position="165,492" size="956,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="165,542" size="956,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="165,589" size="956,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="165,495" size="771,45" font="{0};32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="938,494" size="181,45" font="{0};32" zPosition="2" backgroundColor="#16000000" foregroundColor="#00ee00" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="165,544" size="956,45" font="{0};20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="165,308" size="956,60" font="{0};45" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center" valign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="435,234" size="237,55" font="{0};38" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="628,234" size="488,55" font="{0};38" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="165,371" size="956,60" font="{0};40" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="center">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="165,433" size="956,60" font="{0}; 50" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="5,150" size="150,506" pixmap="{1}/images/icons_quick/icon_snr-scan4.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR:" position="5,658" size="150,60" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};40" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" foregroundColor="#00ffffff" backgroundColor="#16000000" position="5,88" size="150,60" halign="right" valign="center" transparent="1" font="{0};40" >
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="1127,150" size="150,506" pixmap="{1}/images/icons_quick/icon_snr-scan4.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="AGC:" position="1127,658" size="150,60" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};40" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" foregroundColor="#00ffffff" backgroundColor="#16000000" position="1127,88" size="150,60" halign="right" valign="center" transparent="1" font="{0};40">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="SNRD:" position="208,94" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="160,136" size="300,80" backgroundColor="#16000000" font="{0};75" halign="center" transparent="1">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <eLabel text="AGC:" position="537,94" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="482,136" size="300,80" backgroundColor="#16000000" font="{0};75" halign="center" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="BER:" position="875,94" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="813,136" size="300,80" font="{0};75" halign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">BER</convert>
  </widget>
  <widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="160,223" size="300,80" font="{0};75" halign="left" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" >
    <convert type="FrontendInfo">LOCK</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget name="Positioner" position="465,15" size="507,28" zPosition="1" font="{0};25" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
  <widget name="Satfinder" position="465,45" size="507,28" zPosition="1" font="{0};25" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="center"/>
  <eLabel size="1280,2" position="0,84" backgroundColor="#16000000"/>
  <!-- Picon -->
  <ePixmap position="197,597" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="201,602" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="434,597" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv"  position="439,602" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="664,597" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="669,602" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="893,597" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="897,602" size="190,110" transparent="1" alphatest="blend" zPosition="3"/>
<ePixmap position="989,14" size="45,30" zPosition="4" alphatest="blend" pixmap="{1}/images/menu.png"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="578,289" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="578,289" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="578,289" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};18" position="601,288" size="60,25" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};18" position="663,288" size="19,25" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};18" position="682,288" size="60,25" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

SKIN_Full_Screen_Picon_media_Vertical = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1280,720" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="5,7" size="734,75" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};38" valign="center"/>
  <widget source="global.CurrentTime" render="Label" position="1050,17" size="225,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="825,52" size="450,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
    <convert type="ClockToText">Date</convert>
  </widget>
  <eLabel position="0,84" size="1280,2" backgroundColor="#16000000" zPosition="4"/>
  <eLabel position="165,492" size="956,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="165,542" size="956,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="165,589" size="956,2" backgroundColor="#00bbbbbb" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="165,495" size="771,45" font="{0};32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="938,494" size="181,45" font="{0};32" zPosition="2" backgroundColor="#16000000" foregroundColor="#00ee00" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="165,544" size="956,45" font="{0};20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="165,308" size="956,60" font="{0};45" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center" valign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="435,234" size="237,55" font="{0};38" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="628,234" size="488,55" font="{0};38" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="165,371" size="956,60" font="{0};40" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="center">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="165,433" size="956,60" font="{0}; 50" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="5,150" size="150,506" pixmap="{1}/images/icons_quick/icon_snr-scan4.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR:" position="5,658" size="150,60" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};40" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" foregroundColor="#00ffffff" backgroundColor="#16000000" position="5,88" size="150,60" halign="right" valign="center" transparent="1" font="{0};40" >
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="1127,150" size="150,506" pixmap="{1}/images/icons_quick/icon_snr-scan4.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="AGC:" position="1127,658" size="150,60" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};40" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" foregroundColor="#00ffffff" backgroundColor="#16000000" position="1127,88" size="150,60" halign="right" valign="center" transparent="1" font="{0};40">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="SNRD:" position="208,94" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="160,136" size="300,80" backgroundColor="#16000000" font="{0};75" halign="center" transparent="1">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <eLabel text="AGC:" position="537,94" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="482,136" size="300,80" backgroundColor="#16000000" font="{0};75" halign="center" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="BER:" position="875,94" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="813,136" size="300,80" font="{0};75" halign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">BER</convert>
  </widget>
  <widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="160,223" size="300,80" font="{0};75" halign="left" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" >
    <convert type="FrontendInfo">LOCK</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget name="Positioner" position="465,15" size="507,28" zPosition="1" font="{0};25" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
  <widget name="Satfinder" position="465,45" size="507,28" zPosition="1" font="{0};25" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="center"/>
  <eLabel size="1280,2" position="0,84" backgroundColor="#16000000"/>
  <!-- Picon -->
  <ePixmap position="197,597" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="201,602" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="434,597" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv"  position="439,602" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="664,597" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="669,602" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="893,597" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="897,602" size="190,110" transparent="1" alphatest="blend" zPosition="3"/>
<ePixmap position="989,14" size="45,30" zPosition="4" alphatest="blend" pixmap="{1}/images/menu.png"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="578,289" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="578,289" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="578,289" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};18" position="601,288" size="60,25" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};18" position="663,288" size="19,25" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};18" position="682,288" size="60,25" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Full_Screen_Picons_ECM
SKIN_Full_Screen_Picon_Ecm1_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="1280,720" title="RAED's Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="{1}/images/ArmyTouch/HD/frame_base-fs8.png"/>
    <ePixmap position="59,105" size="236,384" zPosition="1" pixmap="{1}/images/ArmyTouch/HD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="984,105" size="243,386" zPosition="1" pixmap="{1}/images/ArmyTouch/HD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="571,97" size="168,30" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="23,623" size="400,75" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="441,623" size="400,75" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="859,623" size="400,75" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="384,367" size="528,140" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="58,518" size="1177,65" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="556,177" size="182,61" zPosition="1" pixmap="{1}/images/ArmyTouch/HD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="405,160" size="481,205" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="456,124" size="400,30" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <!-- Channel and mumber and Provider -->  
    <eLabel text="RAEDQuickSignal" position="36,20" size="1202,32" font="{0};30" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="460,126" size="392,26" zPosition="2" font="{0};25" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="444,627" size="388,30" zPosition="2" font="{0};25" halign="center" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <!-- Tuner Info  -->  
    <widget source="session.FrontendStatus" render="Progress" position="63,139" size="227,308" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="986,139" size="227,308" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="560,185" size="170,49" zPosition="2" font="{0};38" halign="center" foregroundColor="#00ff7a00" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="597,94" size="119,25" zPosition="2" font="{0};23" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="110,106" size="147,28" zPosition="2" font="{0};26" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>    
    <widget source="session.FrontendStatus" render="Label" position="1029,106" size="147,28" zPosition="2" font="{0};26" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="394,373" size="507,123" zPosition="2" font="{0};18" halign="center" valign="top" noWrap="1" foregroundColor="#000099ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="447,662" size="287,30" zPosition="2" font="{0};25" halign="left" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="730,662" size="103,30" zPosition="2" font="{0};25" halign="right" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="307,554" size="680,23" zPosition="2" font="{0};18" halign="center" valign="top" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>    
    <widget source="session.CurrentService" render="Label" position="367,523" size="350,23" zPosition="2" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="664,523" size="270,23" zPosition="4" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="664,523" size="270,23" zPosition="5" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="664,523" size="270,23" zPosition="6" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="664,523" size="270,23" zPosition="7" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="88,523" size="185,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="68,554" size="229,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1001,523" size="229,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="554,246" size="186,98" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="561,252" size="171,84" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="414,173" size="133,79" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="420,180" size="120,68" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="414,267" size="133,79" zPosition="3" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="419,274" size="120,68" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="746,173" size="133,79" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="751,179" size="120,68" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="746,267" size="133,79" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="751,274" size="120,68" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="29,627" size="388,30" font="{0};25" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="29,662" size="388,30" font="{0};25" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="866,662" size="388,30" font="{0};22" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="867,627" size="388,30" font="{0};23" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>  
    <widget name="Positioner" position="36,20" size="335,32" zPosition="6" font="{0};25" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
    <widget name="Satfinder" position="900,20" size="335,32" zPosition="6" font="{0};25" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <<!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_hd.png" position="1150,558" size="40,20" zPosition="2" alphatest="on">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_hd.png" position="1100,558" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_hd.png" position="1100,558" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_media_Ecm1_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="1280,720" title="RAED's Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="{1}/images/ArmyTouch/HD/frame_base-fs8.png"/>
    <ePixmap position="59,105" size="236,384" zPosition="1" pixmap="{1}/images/ArmyTouch/HD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="984,105" size="243,386" zPosition="1" pixmap="{1}/images/ArmyTouch/HD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="571,97" size="168,30" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="23,623" size="400,75" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="441,623" size="400,75" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="859,623" size="400,75" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="384,367" size="528,140" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="58,518" size="1177,65" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="556,177" size="182,61" zPosition="1" pixmap="{1}/images/ArmyTouch/HD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="405,160" size="481,205" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="456,124" size="400,30" zPosition="-1" pixmap="{1}/images/ArmyTouch/HD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <!-- Channel and mumber and Provider -->  
    <eLabel text="RAEDQuickSignal" position="36,20" size="1202,32" font="{0};30" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="460,126" size="392,26" zPosition="2" font="{0};25" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="444,627" size="388,30" zPosition="2" font="{0};25" halign="center" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <!-- Tuner Info  -->  
    <widget source="session.FrontendStatus" render="Progress" position="63,139" size="227,308" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="986,139" size="227,308" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="560,185" size="170,49" zPosition="2" font="{0};38" halign="center" foregroundColor="#00ff7a00" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="597,94" size="119,25" zPosition="2" font="{0};23" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="110,106" size="147,28" zPosition="2" font="{0};26" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>    
    <widget source="session.FrontendStatus" render="Label" position="1029,106" size="147,28" zPosition="2" font="{0};26" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="394,373" size="507,123" zPosition="2" font="{0};18" halign="center" valign="top" noWrap="1" foregroundColor="#000099ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="447,662" size="287,30" zPosition="2" font="{0};25" halign="left" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="730,662" size="103,30" zPosition="2" font="{0};25" halign="right" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="307,554" size="680,23" zPosition="2" font="{0};18" halign="center" valign="top" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>    
    <widget source="session.CurrentService" render="Label" position="367,523" size="350,23" zPosition="2" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="664,523" size="270,23" zPosition="4" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="664,523" size="270,23" zPosition="5" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="664,523" size="270,23" zPosition="6" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="664,523" size="270,23" zPosition="7" font="{0};22" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="88,523" size="185,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="68,554" size="229,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1001,523" size="229,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="554,246" size="186,98" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="561,252" size="171,84" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="414,173" size="133,79" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="420,180" size="120,68" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="414,267" size="133,79" zPosition="3" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="419,274" size="120,68" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="746,173" size="133,79" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconCrypt" position="751,179" size="120,68" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="746,267" size="133,79" zPosition="2" pixmap="{1}/images/ArmyTouch/HD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="751,274" size="120,68" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="29,627" size="388,30" font="{0};25" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="29,662" size="388,30" font="{0};25" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="866,662" size="388,30" font="{0};22" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="867,627" size="388,30" font="{0};23" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>    
   <widget name="Positioner" position="36,20" size="335,32" zPosition="6" font="{0};25" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
    <widget name="Satfinder" position="900,20" size="335,32" zPosition="6" font="{0};25" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_hd.png" position="1150,558" size="40,20" zPosition="2" alphatest="on">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_hd.png" position="1100,558" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_hd.png" position="1100,558" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_Ecm2_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="1280,720" backgroundColor="#ffffffff" title="RAED's Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="{1}/images/ShabahNet/HD/frame_base-fs8.png"/>
    <ePixmap position="59,105" size="236,384" zPosition="1" pixmap="{1}/images/ShabahNet/HD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="984,105" size="243,386" zPosition="1" pixmap="{1}/images/ShabahNet/HD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="571,97" size="168,30" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="23,623" size="400,75" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="441,623" size="400,75" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="859,623" size="400,75" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="384,367" size="528,140" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="58,518" size="1177,65" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="556,177" size="182,61" zPosition="1" pixmap="{1}/images/ShabahNet/HD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="405,160" size="481,205" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="456,124" size="400,30" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <!-- Channel and mumber and Provider -->  
    <eLabel text="RAEDQuickSignal" position="36,20" size="1202,32" font="{0};30" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="460,126" size="392,26" zPosition="2" font="{0};25" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="444,627" size="388,30" zPosition="2" font="{0};25" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <!-- Tuner Info  -->  
    <widget source="session.FrontendStatus" render="Progress" position="63,139" size="227,308" zPosition="2" pixmap="{1}/images/ShabahNet/HD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="986,139" size="227,308" zPosition="2" pixmap="{1}/images/ShabahNet/HD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="560,185" size="170,49" zPosition="2" font="{0};38" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="597,94" size="119,25" zPosition="2" font="{0};23" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="110,106" size="147,28" zPosition="2" font="{0};26" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>    
    <widget source="session.FrontendStatus" render="Label" position="1029,106" size="147,28" zPosition="2" font="{0};26" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="394,373" size="507,123" zPosition="2" font="{0};18" halign="center" valign="top" noWrap="1" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="447,662" size="287,30" zPosition="2" font="{0};25" halign="left" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="730,662" size="103,30" zPosition="2" font="{0};25" halign="right" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="307,554" size="680,23" zPosition="2" font="{0};18" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>    
    <widget source="session.CurrentService" render="Label" position="367,523" size="350,23" zPosition="2" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="664,523" size="270,23" zPosition="4" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="664,523" size="270,23" zPosition="5" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="664,523" size="270,23" zPosition="6" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="664,523" size="270,23" zPosition="7" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="88,523" size="185,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="68,554" size="229,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1001,523" size="229,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="554,246" size="186,98" zPosition="2" pixmap="{1}/images/ShabahNet/HD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="561,252" size="171,84" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="414,173" size="133,79" zPosition="2" pixmap="{1}/images/ShabahNet/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="420,180" size="120,68" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="414,267" size="133,79" zPosition="3" pixmap="{1}/images/ShabahNet/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="419,274" size="120,68" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="746,173" size="133,79" zPosition="2" pixmap="{1}/images/ShabahNet/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="751,179" size="120,68" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="746,267" size="133,79" zPosition="2" pixmap="{1}/images/ShabahNet/HD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="751,274" size="120,68" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="29,627" size="388,30" font="{0};25" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="29,662" size="388,30" font="{0};25" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="866,662" size="388,30" font="{0};22" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="867,627" size="388,30" font="{0};23" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>  
<widget name="Positioner" position="36,20" size="335,32" zPosition="6" font="{0};25" halign="left" backgroundColor="#00ffffff" foregroundColor="#41ff9900" transparent="1" />
    <widget name="Satfinder" position="900,20" size="335,32" zPosition="6" font="{0};25" backgroundColor="#00ffffff" foregroundColor="#0000deff" transparent="1" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_hd.png" position="1150,558" size="40,20" zPosition="2" alphatest="on">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_hd.png" position="1100,558" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_hd.png" position="1100,558" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_media_Ecm2_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="1280,720" backgroundColor="#ffffffff" title="RAED's Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="{1}/images/ShabahNet/HD/frame_base-fs8.png"/>
    <ePixmap position="59,105" size="236,384" zPosition="1" pixmap="{1}/images/ShabahNet/HD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="984,105" size="243,386" zPosition="1" pixmap="{1}/images/ShabahNet/HD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="571,97" size="168,30" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="23,623" size="400,75" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="441,623" size="400,75" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="859,623" size="400,75" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="384,367" size="528,140" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="58,518" size="1177,65" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="556,177" size="182,61" zPosition="1" pixmap="{1}/images/ShabahNet/HD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="405,160" size="481,205" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="456,124" size="400,30" zPosition="-1" pixmap="{1}/images/ShabahNet/HD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <!-- Channel and mumber and Provider -->  
    <eLabel text="RAEDQuickSignal" position="36,20" size="1202,32" font="{0};30" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="460,126" size="392,26" zPosition="2" font="{0};25" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="444,627" size="388,30" zPosition="2" font="{0};25" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <!-- Tuner Info  -->  
    <widget source="session.FrontendStatus" render="Progress" position="63,139" size="227,308" zPosition="2" pixmap="{1}/images/ShabahNet/HD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="986,139" size="227,308" zPosition="2" pixmap="{1}/images/ShabahNet/HD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="560,185" size="170,49" zPosition="2" font="{0};38" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="597,94" size="119,25" zPosition="2" font="{0};23" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="110,106" size="147,28" zPosition="2" font="{0};26" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>    
    <widget source="session.FrontendStatus" render="Label" position="1029,106" size="147,28" zPosition="2" font="{0};26" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="394,373" size="507,123" zPosition="2" font="{0};18" halign="center" valign="top" noWrap="1" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="447,662" size="287,30" zPosition="2" font="{0};25" halign="left" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="730,662" size="103,30" zPosition="2" font="{0};25" halign="right" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="307,554" size="680,23" zPosition="2" font="{0};18" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>    
    <widget source="session.CurrentService" render="Label" position="367,523" size="350,23" zPosition="2" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="664,523" size="270,23" zPosition="4" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="664,523" size="270,23" zPosition="5" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="664,523" size="270,23" zPosition="6" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="664,523" size="270,23" zPosition="7" font="{0};22" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="88,523" size="185,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="68,554" size="229,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1001,523" size="229,23" zPosition="2" font="{0};22" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="554,246" size="186,98" zPosition="2" pixmap="{1}/images/ShabahNet/HD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="561,252" size="171,84" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="414,173" size="133,79" zPosition="2" pixmap="{1}/images/ShabahNet/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="420,180" size="120,68" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="414,267" size="133,79" zPosition="3" pixmap="{1}/images/ShabahNet/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="419,274" size="120,68" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="746,173" size="133,79" zPosition="2" pixmap="{1}/images/ShabahNet/HD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconCrypt" position="751,179" size="120,68" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="746,267" size="133,79" zPosition="2" pixmap="{1}/images/ShabahNet/HD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="751,274" size="120,68" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="29,627" size="388,30" font="{0};25" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="29,662" size="388,30" font="{0};25" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="866,662" size="388,30" font="{0};22" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="867,627" size="388,30" font="{0};23" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>
    <widget name="Positioner" position="36,20" size="335,32" zPosition="6" font="{0};25" halign="left" backgroundColor="#00ffffff" foregroundColor="#41ff9900" transparent="1" />
    <widget name="Satfinder" position="900,20" size="335,32" zPosition="6" font="{0};25" backgroundColor="#00ffffff" foregroundColor="#0000deff" transparent="1" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1020,558" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_hd.png" position="1150,558" size="40,20" zPosition="2" alphatest="on">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_hd.png" position="1100,558" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_hd.png" position="1100,558" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_Ecm3_Vertical = """
<screen name="RaedQuickSignalScreen" position="0,0" size="1280,720" title="Quick Signal Info" flags="wfNoBorder">
  <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="{1}/images/CobaltFHD/HD/cool1.png"/>
  <ePixmap position="58,96" size="180,400" zPosition="1" pixmap="{1}/images/CobaltFHD/HD/agc_snr.png" alphatest="blend" transparent="1"/>
  <ePixmap position="1024,96" size="205,400" zPosition="1" pixmap="{1}/images/CobaltFHD/HD/pogoda.png" alphatest="blend" transparent="1"/>
  <ePixmap position="47,587" size="390,55" zPosition="-1" pixmap="{1}/images/CobaltFHD/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
  <ePixmap position="445,587" size="390,55" zPosition="-1" pixmap="{1}/images/CobaltFHD/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
  <ePixmap position="844,587" size="390,55" zPosition="-1" pixmap="{1}/images/CobaltFHD/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
  <ePixmap position="314,335" size="650,160" zPosition="1" pixmap="{1}/images/CobaltFHD/HD/frame_quick2.png" alphatest="blend" transparent="1"/>
  <ePixmap position="47,511" size="1188,65" pixmap="{1}/images/CobaltFHD/HD/frame_quick3.png" alphatest="blend" transparent="1"/>
  <ePixmap position="382,105" size="500,220" zPosition="1" pixmap="{1}/images/CobaltFHD/HD/frame_quick5.png" alphatest="blend" transparent="1"/>
  <widget source="session.Event_Now" render="Label" position="386,110" size="490,30" font="{0};25" halign="center" backgroundColor="#ff595959" foregroundColor="#00ffffff" transparent="1" zPosition="1" valign="center">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel name="new eLabel" position="405,145" size="450,2" backgroundColor="#004f6ef2" zPosition="1"/>
  <widget backgroundColor="#25101010" font="{0};22" position="391,150" render="Label" size="485,169" source="session.Event_Now" transparent="1" zPosition="1">
    <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="698,35" size="524,40" font="{0};30" valign="center" halign="right" backgroundColor="#54111112" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y     %H:%M </convert>
  </widget>
  <widget source="Title" position="80,35" size="604,40" render="Label" font="{0};30" foregroundColor="#58bcff" backgroundColor="#00000000" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="450,590" size="381,24" zPosition="2" font="{0};23" halign="center" foregroundColor="#7ad927" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="64,133" size="81,324" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/scale.png" orientation="orBottomToTop" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="151,133" size="81,324" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/scale.png" orientation="orBottomToTop" transparent="1">
    <convert type="RaedQuickFrontendInfo2">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="62,100" size="83,28" zPosition="2" font="{0};25" halign="center" valign="center" backgroundColor="#25101010" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="151,100" size="83,28" zPosition="2" font="{0};25" halign="center" valign="center" backgroundColor="#25101010" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="320,340" size="637,152" zPosition="2" font="{0};22" halign="center" valign="center" noWrap="1" foregroundColor="#000090e6" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="450,618" size="305,24" zPosition="2" font="{0};20" foregroundColor="#00fffe9e" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="755,618" size="75,24" zPosition="2" font="{0};23" halign="right" foregroundColor="#00ff2525" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="299,546" size="686,25" zPosition="2" font="{0};20" halign="center" foregroundColor="#7ad927" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <eLabel backgroundColor="#00000000" font="{0};23" foregroundColor="#004f6ef2" position="300,517" size="100,25" text="{2}" transparent="1" zPosition="1"/>
  <widget backgroundColor="#00000000" font="{0};23" position="386,517" render="Label" size="150,25" source="session.CurrentService" transparent="1" zPosition="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget>
  <eLabel backgroundColor="#00000000" font="{0};23" position="580,517" size="52,25" text="fps" transparent="1" zPosition="1"/>
  <widget source="session.CurrentService" render="Label" position="521,517" size="50,25" font="{0};23" halign="right" backgroundColor="#00000000" transparent="1" zPosition="1">
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="51,546" size="236,25" foregroundColor="#00389416" zPosition="3" font="{0};23" halign="center" noWrap="1" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">emuname</convert>
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="650,517" size="156,25" zPosition="4" font="{0};23" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="650,517" size="156,25" zPosition="5" font="{0};23" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="650,517" size="156,25" zPosition="6" font="{0};23" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="650,517" size="156,25" zPosition="7" font="{0};23" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  <eLabel backgroundColor="#00000000" font="{0};23" foregroundColor="#004f6ef2" position="836,517" size="80,25" text="{3}" transparent="1" zPosition="1"/>
  <widget backgroundColor="#00000000" font="{0};23" position="895,517" render="Label" size="80,25" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="51,517" size="236,25" zPosition="2" font="{0};23" halign="center" foregroundColor="#00ff2525" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="996,546" size="233,25" zPosition="2" font="{0};23" halign="center" foregroundColor="#00ff2525" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">vtype</convert>
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="1050,517" size="132,25" font="{0};23" backgroundColor="#00000000" transparent="1" halign="center" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="1050,517" size="132,25" font="{0};23" backgroundColor="#00000000" transparent="1" halign="center" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="1050,517" size="132,25" font="{0};23" backgroundColor="#00000000" transparent="1" halign="center" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <!--Picon-->
  <ePixmap position="245,105" size="130,90" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/frame_of_picon3c.png" alphatest="blend" transparent="1"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="250,110" size="120,80" zPosition="5" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="245,235" size="130,90" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="250,240" size="120,80" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="888,105" size="130,90" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="893,110" zPosition="5" size="120,80" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="888,235" size="130,90" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="893,240" size="120,80" transparent="1" alphatest="blend" zPosition="3"/>
  <!--widget source="session.CurrentService" render="Label" position="52,590" size="381,24" font="{0};23" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Number</convert>
  </widget-->
  <widget source="session.CurrentService" render="Label" position="52,618" size="381,24" font="{0};23" halign="center" foregroundColor="#34a36e" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="848,618" size="385,24" font="{0};23" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="848,590" size="385,24" font="{0};23" halign="center" foregroundColor="#58bcff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <eLabel text="{8}" position="1104,139" size="59,24" font="{0};20" backgroundColor="#54111112" halign="center" transparent="1" foregroundColor="#00c1ea02" zPosition="2"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="1030,139" size="70,70" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">Picon</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1165,137" size="52,27" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="#00c1ea02" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Temp</convert>
  </widget>
  <ePixmap pixmap="{1}/images/CobaltFHD/HD/wiatr.png" position="1106,161" size="25,25" zPosition="3" transparent="1" alphatest="blend"/>
  <ePixmap pixmap="{1}/images/CobaltFHD/HD/deszcz.png" position="1106,187" size="25,25" zPosition="4" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="Label" position="1130,161" size="88,25" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Windspeed</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1130,187" size="88,25" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Humidity</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/HD/wsch.png" position="1031,215" size="70,30" zPosition="2"/>
  <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/HD/zach.png" position="1031,249" size="70,30" zPosition="2"/>
  <eLabel text="Rise" position="1105,218" size="49,24" font="{0};18" backgroundColor="#54111112" transparent="1" zPosition="2"/>
  <widget backgroundColor="#54111112" font="{0};23" halign="right" position="1138,218" zPosition="2" render="Label" size="71,24" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <eLabel text="Set" position="1105,250" size="49,24" font="{0};18" backgroundColor="#54111112" transparent="1" zPosition="2"/>
  <widget backgroundColor="#54111112" font="{0};23" foregroundColor="#00ffffff" halign="right" position="1138,250" zPosition="2" render="Label" size="71,24" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather/MoonPhase" position="1037,292" size="60,60" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">PiconMoon</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1105,289" size="105,25" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Moonlight</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1105,326" size="113,25" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Moondist</convert>
  </widget>
  <eLabel name="new eLabel" position="1038,360" size="177,2" zPosition="2" backgroundColor="#004f6ef2"/>
  <eLabel text="{9}" position="1034,362" size="185,23" font="{0};20" valign="center" halign="center" backgroundColor="#54111112" transparent="1" foregroundColor="#00c1ea02" zPosition="2"/>
  <widget alphatest="on" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="1030,388" size="70,70" source="session.CurrentService" transparent="1" zPosition="2">
    <convert type="RaedQuickWeather">Picon2</convert>
  </widget>
  <ePixmap pixmap="{1}/images/CobaltFHD/HD/temp.png" position="1105,400" size="20,44" zPosition="2" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="Label" font="{0};22" position="1118,397" size="90,25" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Hightemp2</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" font="{0};22" position="1118,421" size="90,25" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Lowtemp2</convert>
  </widget>
        <widget name="Positioner" position="333,656" size="335,32" zPosition="6" font="{0};25" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
    <widget name="Satfinder" position="748,656" size="335,32" zPosition="6" font="{0};25" backgroundColor="#54111112" foregroundColor="#0000deff"  halign="right" transparent="1"/>
  <ePixmap position="62,660" size="65,25" pixmap="{1}/images/CobaltFHD/HD/menu.png" alphatest="blend"/>
  <ePixmap position="145,660" size="65,25" pixmap="{1}/images/CobaltFHD/HD/exit.png" alphatest="blend"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="145,591" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="145,591" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="145,591" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_hd.png" position="285,590" size="40,20" zPosition="2" alphatest="on">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_hd.png" position="235,590" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_hd.png" position="235,590" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85, title86, title87)

SKIN_Full_Screen_Picon_media_Ecm3_Vertical = """
<screen name="RaedQuickSignalScreen" position="0,0" size="1280,720" title="Quick Signal Info" flags="wfNoBorder">
  <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="{1}/images/CobaltFHD/HD/cool1.png"/>
  <ePixmap position="58,96" size="180,400" zPosition="1" pixmap="{1}/images/CobaltFHD/HD/agc_snr.png" alphatest="blend" transparent="1"/>
  <ePixmap position="1024,96" size="205,400" zPosition="1" pixmap="{1}/images/CobaltFHD/HD/pogoda.png" alphatest="blend" transparent="1"/>
  <ePixmap position="47,587" size="390,55" zPosition="-1" pixmap="{1}/images/CobaltFHD/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
  <ePixmap position="445,587" size="390,55" zPosition="-1" pixmap="{1}/images/CobaltFHD/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
  <ePixmap position="844,587" size="390,55" zPosition="-1" pixmap="{1}/images/CobaltFHD/HD/frame_quick1.png" alphatest="blend" transparent="1"/>
  <ePixmap position="314,335" size="650,160" zPosition="1" pixmap="{1}/images/CobaltFHD/HD/frame_quick2.png" alphatest="blend" transparent="1"/>
  <ePixmap position="47,511" size="1188,65" pixmap="{1}/images/CobaltFHD/HD/frame_quick3.png" alphatest="blend" transparent="1"/>
  <ePixmap position="382,105" size="500,220" zPosition="1" pixmap="{1}/images/CobaltFHD/HD/frame_quick5.png" alphatest="blend" transparent="1"/>
  <widget source="session.Event_Now" render="Label" position="386,110" size="490,30" font="{0};25" halign="center" backgroundColor="#ff595959" foregroundColor="#00ffffff" transparent="1" zPosition="1" valign="center">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel name="new eLabel" position="405,145" size="450,2" backgroundColor="#004f6ef2" zPosition="1"/>
  <widget backgroundColor="#25101010" font="{0};22" position="391,150" render="Label" size="485,169" source="session.Event_Now" transparent="1" zPosition="1">
    <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="698,35" size="524,40" font="{0};30" valign="center" halign="right" backgroundColor="#54111112" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y     %H:%M </convert>
  </widget>
  <widget source="Title" position="80,35" size="604,40" render="Label" font="{0};30" foregroundColor="#58bcff" backgroundColor="#00000000" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="450,590" size="381,24" zPosition="2" font="{0};23" halign="center" foregroundColor="#7ad927" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="64,133" size="81,324" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/scale.png" orientation="orBottomToTop" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="151,133" size="81,324" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/scale.png" orientation="orBottomToTop" transparent="1">
    <convert type="RaedQuickFrontendInfo2">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="62,100" size="83,28" zPosition="2" font="{0};25" halign="center" valign="center" backgroundColor="#25101010" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="151,100" size="83,28" zPosition="2" font="{0};25" halign="center" valign="center" backgroundColor="#25101010" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="320,340" size="637,152" zPosition="2" font="{0};22" halign="center" valign="center" noWrap="1" foregroundColor="#000090e6" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="450,618" size="305,24" zPosition="2" font="{0};20" foregroundColor="#00fffe9e" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="755,618" size="75,24" zPosition="2" font="{0};23" halign="right" foregroundColor="#00ff2525" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="299,546" size="686,25" zPosition="2" font="{0};20" halign="center" foregroundColor="#7ad927" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <eLabel backgroundColor="#00000000" font="{0};23" foregroundColor="#004f6ef2" position="300,517" size="100,25" text="{2}" transparent="1" zPosition="1"/>
  <widget backgroundColor="#00000000" font="{0};23" position="386,517" render="Label" size="150,25" source="session.CurrentService" transparent="1" zPosition="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget>
  <eLabel backgroundColor="#00000000" font="{0};23" position="580,517" size="52,25" text="fps" transparent="1" zPosition="1"/>
  <widget source="session.CurrentService" render="Label" position="521,517" size="50,25" font="{0};23" halign="right" backgroundColor="#00000000" transparent="1" zPosition="1">
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="51,546" size="236,25" foregroundColor="#00389416" zPosition="3" font="{0};23" halign="center" noWrap="1" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">emuname</convert>
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="650,517" size="156,25" zPosition="4" font="{0};23" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="650,517" size="156,25" zPosition="5" font="{0};23" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="650,517" size="156,25" zPosition="6" font="{0};23" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="650,517" size="156,25" zPosition="7" font="{0};23" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  <eLabel backgroundColor="#00000000" font="{0};23" foregroundColor="#004f6ef2" position="836,517" size="80,25" text="{3}" transparent="1" zPosition="1"/>
  <widget backgroundColor="#00000000" font="{0};23" position="895,517" render="Label" size="80,25" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="51,517" size="236,25" zPosition="2" font="{0};23" halign="center" foregroundColor="#00ff2525" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="996,546" size="233,25" zPosition="2" font="{0};23" halign="center" foregroundColor="#00ff2525" backgroundColor="#25101010" transparent="1">
    <convert type="RaedQuickEcmInfo">vtype</convert>
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="1050,517" size="132,25" font="{0};23" backgroundColor="#00000000" transparent="1" halign="center" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="1050,517" size="132,25" font="{0};23" backgroundColor="#00000000" transparent="1" halign="center" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="1050,517" size="132,25" font="{0};23" backgroundColor="#00000000" transparent="1" halign="center" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <ePixmap position="245,105" size="130,90" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/frame_of_picon3c.png" alphatest="blend" transparent="1"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="250,110" size="120,80" zPosition="5" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="245,235" size="130,90" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="250,240" size="120,80" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="888,105" size="130,90" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="893,110" zPosition="5" size="120,80" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="888,235" size="130,90" zPosition="2" pixmap="{1}/images/CobaltFHD/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="893,240" size="120,80" transparent="1" alphatest="blend" zPosition="3"/>
  <!--widget source="session.CurrentService" render="Label" position="52,590" size="381,24" font="{0};23" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Number</convert>
  </widget-->
  <widget source="session.CurrentService" render="Label" position="52,618" size="381,24" font="{0};23" halign="center" foregroundColor="#34a36e" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="848,618" size="385,24" font="{0};23" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="848,590" size="385,24" font="{0};23" halign="center" foregroundColor="#58bcff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <eLabel text="{8}" position="1104,139" size="59,24" font="{0};20" backgroundColor="#54111112" halign="center" transparent="1" foregroundColor="#00c1ea02" zPosition="2"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="weather" position="1030,139" size="70,70" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">Picon</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1165,137" size="52,27" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="#00c1ea02" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Temp</convert>
  </widget>
  <ePixmap pixmap="{1}/images/CobaltFHD/HD/wiatr.png" position="1106,161" size="25,25" zPosition="3" transparent="1" alphatest="blend"/>
  <ePixmap pixmap="{1}/images/CobaltFHD/HD/deszcz.png" position="1106,187" size="25,25" zPosition="4" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="Label" position="1130,161" size="88,25" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Windspeed</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1130,187" size="88,25" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Humidity</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/HD/wsch.png" position="1031,215" size="70,30" zPosition="2"/>
  <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/HD/zach.png" position="1031,249" size="70,30" zPosition="2"/>
  <eLabel text="Rise" position="1105,218" size="49,24" font="{0};18" backgroundColor="#54111112" transparent="1" zPosition="2"/>
  <widget backgroundColor="#54111112" font="{0};23" halign="right" position="1138,218" zPosition="2" render="Label" size="71,24" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <eLabel text="Set" position="1105,250" size="49,24" font="{0};18" backgroundColor="#54111112" transparent="1" zPosition="2"/>
  <widget backgroundColor="#54111112" font="{0};23" foregroundColor="#00ffffff" halign="right" position="1138,250" zPosition="2" render="Label" size="71,24" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="weather/MoonPhase" position="1037,292" size="60,60" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">PiconMoon</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1105,289" size="105,25" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Moonlight</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1105,326" size="113,25" font="{0};22" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Moondist</convert>
  </widget>
  <eLabel name="new eLabel" position="1038,360" size="177,2" zPosition="2" backgroundColor="#004f6ef2"/>
  <eLabel text="{9}" position="1034,362" size="185,23" font="{0};20" valign="center" halign="center" backgroundColor="#54111112" transparent="1" foregroundColor="#00c1ea02" zPosition="2"/>
  <widget alphatest="on" render="RaedQuickSignalPiconUni" path="weather" position="1030,388" size="70,70" source="session.CurrentService" transparent="1" zPosition="2">
    <convert type="RaedQuickWeather">Picon2</convert>
  </widget>
  <ePixmap pixmap="{1}/images/CobaltFHD/HD/temp.png" position="1105,400" size="20,44" zPosition="2" transparent="1" alphatest="blend"/>
  <widget source="session.CurrentService" render="Label" font="{0};22" position="1118,397" size="90,25" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Hightemp2</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" font="{0};22" position="1118,421" size="90,25" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Lowtemp2</convert>
  </widget>
      <widget name="Positioner" position="333,656" size="335,32" zPosition="6" font="{0};25" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
    <widget name="Satfinder" position="748,656" size="335,32" zPosition="6" font="{0};25" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" halign="right"/>
  <ePixmap position="62,660" size="65,25" pixmap="{1}/images/CobaltFHD/HD/menu.png" alphatest="blend"/>
  <ePixmap position="145,660" size="65,25" pixmap="{1}/images/CobaltFHD/HD/exit.png" alphatest="blend"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="145,591" size="25,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="145,591" size="25,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="145,591" size="25,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_hd.png" position="285,590" size="40,20" zPosition="2" alphatest="on">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_hd.png" position="235,590" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_hd.png" position="235,590" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85, title86, title87)

### SKIN_Full_Screen_Picons_ECM_SNR_ANALOG
SKIN_Full_Screen_Picon_Ecm3_SNR_ANALOG = """
<screen name="SKIN_Full_Screen_Picon_media_Ecm3_SNR_ANALOG" position="0,0" size="1280,720" title="Quick Signal Info" backgroundColor="#16000000" flags="wfNoBorder">
  <ePixmap position="242,503" size="820,180" zPosition="1" pixmap="{1}/images/analog/HD/analog_tuner_bg.png" alphatest="blend" transparent="1"/>
  <widget source="session.Event_Now" render="Label" position="27,80" size="651,41" font="{0};25" halign="center" backgroundColor="#ff595959" foregroundColor="#7ad927" transparent="1" zPosition="1">
  <convert type="EventName">Name</convert>
</widget>
<widget backgroundColor="#16000000" font="{0};22" position="27,128" render="Label" size="657,185" source="session.Event_Now" transparent="1">
  <convert type="EventName">ExtendedDescription</convert>
</widget>
<widget source="session.CurrentService" render="Label" position="693,80" size="567,232" zPosition="2" font="{0};22" halign="center" valign="center" noWrap="1" foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">ecmfile</convert>
</widget>
  <widget source="global.CurrentTime" render="Label" position="681,20" size="572,37" font="{0};28" valign="center" halign="right" backgroundColor="#16000000" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y  -  %H:%M </convert>
  </widget>
  <widget source="Title" position="55,20" size="613,44" render="Label" font="{0};28" foregroundColor="#58bcff" backgroundColor="#16000000" transparent="1" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="508,647" zPosition="2" size="327,32" font="{0}; 28" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <widget source="session.FrontendStatus" render="RaedQuickWatches" position="295,510" size="391,315" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="on">
      <convert type="RaedQuickFrontendInfo2">SNR_ANALOG</convert>
    </widget>
    <widget source="session.FrontendStatus" render="RaedQuickWatches" position="705,510" size="391,315" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="on">
      <convert type="RaedQuickFrontendInfo2">AGC_ANALOG</convert>
    </widget>
    <!--Picon-->
    <ePixmap position="171,330" size="150,90" zPosition="2" pixmap="{1}/images/analog/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="174,333" size="144,84" zPosition="5" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
    <ePixmap position="428,330" size="150,90" zPosition="2" pixmap="{1}/images/analog/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="430,333" zPosition="5" size="144,84" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
    <ePixmap position="672,330" size="150,90" zPosition="2" pixmap="{1}/images/analog/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="675,333" size="144,84" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <ePixmap position="922,330" size="150,90" zPosition="2" pixmap="{1}/images/analog/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="925,333" size="144,84" transparent="1" alphatest="blend" zPosition="3" />
<ePixmap position="17,644" size="65,25" pixmap="{1}/images/CobaltFHD/HD/menu.png" alphatest="blend"/>
<ePixmap position="17,608" size="65,25" pixmap="{1}/images/CobaltFHD/HD/exit.png" alphatest="blend"/>
<widget name="Positioner" position="11,687" size="410,31" zPosition="10" font="{0};24" backgroundColor="#54111112" foregroundColor="#41ff9900"  transparent="1" valign="center" halign="center"/>
<widget name="Satfinder" position="855,687" size="410,31" zPosition="10" font="{0};24" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center"/>
    <widget source="session.CurrentService" render="Label" position="318,466" size="692,28" zPosition="2" font="{0};18" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};24" foregroundColor="#004f6ef2" halign="left" position="367,428" size="120,28" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};24" halign="left" position="458,428" render="Label" size="140,28" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};24" halign="left" position="663,428" size="61,28" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="614,428" size="50,28" font="{0};24" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="69,466" size="243,28" foregroundColor="#00389416" zPosition="3" font="{0};24" halign="center" noWrap="1" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="740,428" size="174,28" zPosition="4" font="{0};24" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="740,428" size="174,28" zPosition="5" font="{0};24" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="740,428" size="174,28" zPosition="6" font="{0};24" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="740,428" size="174,28" zPosition="7" font="{0};24" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};24" foregroundColor="#004f6ef2" halign="left" position="925,428" size="80,28" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};24" halign="left" position="989,428" render="Label" size="80,28" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="64,428" size="297,28" zPosition="2" font="{0};24" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1015,466" size="231,28" zPosition="2" font="{0};24" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="1083,428" size="125,28" font="{0};24" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="1083,428" size="125,28" font="{0};24" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="1083,428" size="125,28" font="{0};24" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap" position="1088,582" size="40,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap" position="1088,582" size="40,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap" position="1088,582" size="40,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_hd.png" position="1230,582" size="40,20" zPosition="2" alphatest="on">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_hd.png" position="1171,582" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_hd.png" position="1171,582" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget> 
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85)

SKIN_Full_Screen_Picon_media_Ecm3_SNR_ANALOG = """
<screen name="SKIN_Full_Screen_Picon_media_Ecm3_SNR_ANALOG" position="0,0" size="1280,720" title="Quick Signal Info" backgroundColor="#16000000" flags="wfNoBorder">
  <ePixmap position="242,503" size="820,180" zPosition="1" pixmap="{1}/images/analog/HD/analog_tuner_bg.png" alphatest="blend" transparent="1"/>
  <widget source="session.Event_Now" render="Label" position="27,80" size="651,41" font="{0};25" halign="center" backgroundColor="#ff595959" foregroundColor="#7ad927" transparent="1" zPosition="1">
  <convert type="EventName">Name</convert>
</widget>
<widget backgroundColor="#16000000" font="{0};22" position="27,128" render="Label" size="657,185" source="session.Event_Now" transparent="1">
  <convert type="EventName">ExtendedDescription</convert>
</widget>
<widget source="session.CurrentService" render="Label" position="693,80" size="567,232" zPosition="2" font="{0};22" halign="center" valign="center" noWrap="1" foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">ecmfile</convert>
</widget>
  <widget source="global.CurrentTime" render="Label" position="681,20" size="572,37" font="{0};28" valign="center" halign="right" backgroundColor="#16000000" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y  -  %H:%M </convert>
  </widget>
  <widget source="Title" position="55,20" size="613,44" render="Label" font="{0};28" foregroundColor="#58bcff" backgroundColor="#16000000" transparent="1" halign="center"/>
  <!-- SNRdB -->
  <widget source="session.FrontendStatus" render="Label" position="508,647" zPosition="2" size="327,32" font="{0}; 28" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
    <eLabel name="snr" text="SNR:" position="260,647" size="80,32" font="{0}; 25" halign="left" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
  <widget source="session.FrontendStatus" render="Label" position="325,647" size="110,32" font="{0}; 25" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="RaedQuickWatches" position="295,510" size="391,315" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="on">
      <convert type="RaedQuickFrontendInfo2">SNR_ANALOG</convert>
    </widget>
  <!-- AGC -->
    <widget source="session.FrontendStatus" render="RaedQuickWatches" position="705,510" size="391,315" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="on">
      <convert type="RaedQuickFrontendInfo2">AGC_ANALOG</convert>
    </widget>
    <eLabel name="agc" text="AGC:" position="912,647" size="80,32" font="{0}; 25" halign="right" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
  <widget source="session.FrontendStatus" render="Label" position="997,647" size="110,32" font="{0}; 25" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <!--Picon-->
    <ePixmap position="171,330" size="150,90" zPosition="2" pixmap="{1}/images/analog/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="174,333" size="144,84" zPosition="5" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
    <ePixmap position="428,330" size="150,90" zPosition="2" pixmap="{1}/images/analog/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="430,333" zPosition="5" size="144,84" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
    <ePixmap position="672,330" size="150,90" zPosition="2" pixmap="{1}/images/analog/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="675,333" size="144,84" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <ePixmap position="922,330" size="150,90" zPosition="2" pixmap="{1}/images/analog/HD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="925,333" size="144,84" transparent="1" alphatest="blend" zPosition="3" />
<ePixmap position="17,644" size="65,25" pixmap="{1}/images/CobaltFHD/HD/menu.png" alphatest="blend"/>
<ePixmap position="17,608" size="65,25" pixmap="{1}/images/CobaltFHD/HD/exit.png" alphatest="blend"/>
<widget name="Positioner" position="11,687" size="410,31" zPosition="10" font="{0};24" backgroundColor="#54111112" foregroundColor="#41ff9900"  transparent="1" valign="center" halign="center"/>
<widget name="Satfinder" position="855,687" size="410,31" zPosition="10" font="{0};24" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center"/>
    <widget source="session.CurrentService" render="Label" position="318,466" size="692,28" zPosition="2" font="{0};18" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};24" foregroundColor="#004f6ef2" halign="left" position="367,428" size="120,28" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};24" halign="left" position="458,428" render="Label" size="140,28" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};24" halign="left" position="663,428" size="61,28" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="614,428" size="50,28" font="{0};24" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="69,466" size="243,28" foregroundColor="#00389416" zPosition="3" font="{0};24" halign="center" noWrap="1" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="740,428" size="174,28" zPosition="4" font="{0};24" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="740,428" size="174,28" zPosition="5" font="{0};24" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="740,428" size="174,28" zPosition="6" font="{0};24" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="740,428" size="174,28" zPosition="7" font="{0};24" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};24" foregroundColor="#004f6ef2" halign="left" position="925,428" size="80,28" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};24" halign="left" position="989,428" render="Label" size="80,28" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="64,428" size="297,28" zPosition="2" font="{0};24" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1015,466" size="231,28" zPosition="2" font="{0};24" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="1083,428" size="125,28" font="{0};24" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="1083,428" size="125,28" font="{0};24" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="1083,428" size="125,28" font="{0};24" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap" position="1088,582" size="40,20" zPosition="1" pixmap="{1}/images/sd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap" position="1088,582" size="40,20" zPosition="2" pixmap="{1}/images/hd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap" position="1088,582" size="40,20" zPosition="3" pixmap="{1}/images/uhd_hd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_hd.png" position="1230,582" size="40,20" zPosition="2" alphatest="on">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_hd.png" position="1171,582" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_hd.png" position="1171,582" size="40,20" zPosition="2" alphatest="on">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget> 
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85)
