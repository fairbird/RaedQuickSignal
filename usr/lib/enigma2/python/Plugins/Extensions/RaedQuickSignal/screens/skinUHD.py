#RAEDQuickSignal WQHD (2560x1440) (c) RAED 07-02-2014

import os
from enigma import addFont
from Screens.Screen import Screen
from Components.Pixmap import Pixmap
from Components.config import config
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Plugins.Extensions.RaedQuickSignal.tools.configs import *

## Add Fonts codes
IMAGEPLUGIN=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/images/")
# Font name
if config.plugins.RaedQuickSignal.fontsStyle.value == "Default":
	fontfilename='Regular'
else:
	fontfilename = config.plugins.RaedQuickSignal.fontsStyle.value
# Font size
if config.plugins.RaedQuickSignal.fontsSize.value == "Default":
	fontSize = 100
else:
	fontSize = config.plugins.RaedQuickSignal.fontsSize.value
# Add Font to skin
FontName='RSQFont'
addFont(fontfilename, 'RSQFont', int(fontSize), 1)
## End Add Fonts codes


def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

if config.plugins.RaedQuickSignal.numbers.value == "Numbers":
	NUMBERS = '''
  <widget source="session.CurrentService" render="Label" position="3,827" size="440,53" font="{0};40" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>'''.format(FontName)
elif config.plugins.RaedQuickSignal.numbers.value == "Resolution":
	NUMBERS = '''
  <widget source="session.CurrentService" render="Label" font="{0};40" position="107,823" size="116,53" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};40" position="228,823" size="25,53" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};40" position="260,823" size="107,53" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>'''.format(FontName)

### SKIN_setup
if DreamOS():
      SKIN_setup = """
<screen name="RaedQuickSignal_setup" position="0,0" size="2560,1440" title="RAED's RaedQuickSignal setup" flags="wfNoBorder" backgroundColor="#16000000">
  <widget source="Title" position="359,53" size="1613,87" render="Label" font="{0};67" foregroundColor="#00ffa500" backgroundColor="#16000000" transparent="1" halign="center"/>
  <widget source="session.VideoPicture" render="Pig" position="1356,224" size="1103,583" backgroundColor="#ff000000" zPosition="1"/>
  <eLabel text="Background of VideoPicture" foregroundColor="#00ffffff" backgroundColor="#00ffffff" size="1123,603" position="1347,213" zPosition="-10"/>
  <widget source="global.CurrentTime" font="{0};73" foregroundColor="#00ffffff" backgroundColor="#16000000" halign="center" position="2087,4" render="Label" size="471,112"  transparent="1" valign="center" zPosition="5">
    <convert type="ClockToText">Default</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="2087,104" size="471,87" font="{0};67" halign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" zPosition="6">
    <convert type="ClockToText">Format:%d.%m.%Y</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1347,815" zPosition="1" size="1123,91" font="{0};45" halign="center" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="ServiceName">Name</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="1347,895" zPosition="2" size="1123,91" font="{0};43" halign="center" foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="EventName">Name</convert>
  </widget>
  <widget name="config" position="20,187" size="1308,920" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" />
  <widget source="key_red" render="Label" position="1,1380" zPosition="2" size="508,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_green" render="Label" position="725,1380" zPosition="2" size="508,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_yellow" render="Label" position="1432,1380" zPosition="2" size="508,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_blue" render="Label" position="2045,1380" zPosition="2" size="508,43" font="{0};33" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <ePixmap position="91,1427" zPosition="1" size="333,5" pixmap="{1}/images/reduhd.png" alphatest="blend"/>
  <ePixmap position="807,1427" zPosition="1" size="333,5" pixmap="{1}/images/greenuhd.png" alphatest="blend"/>
  <ePixmap position="1516,1427" zPosition="1" size="333,5" pixmap="{1}/images/yellowuhd.png" alphatest="blend"/>
  <ePixmap position="2132,1427" zPosition="1" size="333,5" pixmap="{1}/images/blueuhd.png" alphatest="blend"/>
  <widget source="help" render="Label" position="20,1101" size="1583,265" font="{0};43" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="1639,1031" size="533,300" zPosition="5" alphatest="blend"/>
  <ePixmap position="1768,1047" zPosition="3" size="267,267" pixmap="{1}/images/fairbirduhd.png" alphatest="blend"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
else:
      SKIN_setup = """
<screen name="RaedQuickSignal_setup" position="0,0" size="2560,1440" title="RAED's RaedQuickSignal setup" flags="wfNoBorder" backgroundColor="#16000000">
  <widget source="Title" position="359,53" size="1613,87" render="Label" font="{0};67" foregroundColor="#00ffa500" backgroundColor="#16000000" transparent="1" halign="center"/>
  <widget source="session.VideoPicture" render="Pig" position="1356,224" size="1103,583" backgroundColor="#ff000000" zPosition="1"/>
  <eLabel text="Background of VideoPicture" foregroundColor="#00ffffff" backgroundColor="#00ffffff" size="1123,603" position="1347,213" zPosition="-10"/>
  <widget source="global.CurrentTime" font="{0};73" foregroundColor="#00ffffff" backgroundColor="#16000000" halign="center" position="2087,4" render="Label" size="471,112" transparent="1" valign="center" zPosition="5">
    <convert type="ClockToText">Default</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="2087,104" size="471,87" font="{0};67" halign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" zPosition="6">
    <convert type="ClockToText">Format:%d.%m.%Y</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1347,815" zPosition="1" size="1123,91" font="{0};45" halign="center" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="ServiceName">Name</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="1347,895" zPosition="2" size="1123,91" font="{0};43" halign="center" foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="EventName">Name</convert>
  </widget>
  <widget name="config" position="20,187" size="1308,920" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="2" font="{0};40" itemHeight="53" />
  <widget source="key_red" render="Label" position="1,1380" zPosition="2" size="508,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_green" render="Label" position="725,1380" zPosition="2" size="508,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_yellow" render="Label" position="1432,1380" zPosition="2" size="508,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget source="key_blue" render="Label" position="2045,1380" zPosition="2" size="508,43" font="{0};33" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1"/>
  <ePixmap position="91,1427" zPosition="1" size="333,5" pixmap="{1}/images/reduhd.png" alphatest="blend"/>
  <ePixmap position="807,1427" zPosition="1" size="333,5" pixmap="{1}/images/greenuhd.png" alphatest="blend"/>
  <ePixmap position="1516,1427" zPosition="1" size="333,5" pixmap="{1}/images/yellowuhd.png" alphatest="blend"/>
  <ePixmap position="2132,1427" zPosition="1" size="333,5" pixmap="{1}/images/blueuhd.png" alphatest="blend"/>
  <widget source="help" render="Label" position="20,1101" size="1583,265" font="{0};43" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="1639,1031" size="533,300" zPosition="5" alphatest="blend"/>
  <ePixmap position="1768,1047" zPosition="3" size="267,267" pixmap="{1}/images/fairbirduhd.png" alphatest="blend"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_setup2
if DreamOS():
      SKIN_setup2 = """
<screen backgroundColor="#16000000" name="RaedQuickSignal_setup" position="center,center" size="1400,1247" title="RAED's RaedQuickSignal setup" flags="wfNoBorder">
  <eLabel position="0,71" size="1400,1" zPosition="10" backgroundColor="#00ffffff" transparent="0"/>
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bab329" position="40,7" size="1308,60" transparent="1" />
  <widget name="config" position="20,80" size="1353,800" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" />
  <widget source="key_red" render="Label" position="60,1195" zPosition="2" size="220,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_green" render="Label" position="353,1195" zPosition="2" size="220,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <!--widget source="key_yellow" render="Label" position="640,1195" zPosition="2" size="267,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" /-->
  <widget source="key_blue" render="Label" position="800,1195" zPosition="2" size="379,43" font="{0};33" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <ePixmap position="60,1237" zPosition="1" size="220,3" pixmap="{1}/images/reduhd.png" alphatest="blend" />
  <ePixmap position="353,1237" zPosition="1" size="220,3" pixmap="{1}/images/greenuhd.png" alphatest="blend" />
  <!--ePixmap position="640,1237" zPosition="1" size="267,3" pixmap="{1}/images/yellowuhd.png" alphatest="blend" /-->
  <ePixmap position="853,1237" zPosition="1" size="267,3" pixmap="{1}/images/blueuhd.png" alphatest="blend" />
  <widget source="help" render="Label" position="60,889" size="739,300" font="{0};37" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="817,889" size="533,300" zPosition="5" alphatest="blend"/>
  <ePixmap position="949,907" size="267,267" zPosition="3" pixmap="{1}/images/fairbirduhd.png" alphatest="blend" />
 </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
else:
      SKIN_setup2 = """
<screen backgroundColor="#16000000" name="RaedQuickSignal_setup" position="center,center" size="1400,1247" title="RAED's RaedQuickSignal setup" flags="wfNoBorder">
  <eLabel position="0,71" size="1400,1" zPosition="10" backgroundColor="#00ffffff" transparent="0"/>
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bab329" position="40,7" size="1308,60" transparent="1" />
  <widget name="config" position="20,80" size="1353,800" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" font="{0};40" itemHeight="53" />
  <widget source="key_red" render="Label" position="60,1195" zPosition="2" size="220,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_green" render="Label" position="353,1195" zPosition="2" size="220,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <!--widget source="key_yellow" render="Label" position="640,1195" zPosition="2" size="267,43" font="{0};40" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" /-->
  <widget source="key_blue" render="Label" position="800,1195" zPosition="2" size="379,43" font="{0};33" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <ePixmap position="60,1237" zPosition="1" size="220,3" pixmap="{1}/images/reduhd.png" alphatest="blend" />
  <ePixmap position="353,1237" zPosition="1" size="220,3" pixmap="{1}/images/greenuhd.png" alphatest="blend" />
  <!--ePixmap position="640,1237" zPosition="1" size="267,3" pixmap="{1}/images/yellowuhd.png" alphatest="blend" /-->
  <ePixmap position="853,1237" zPosition="1" size="267,3" pixmap="{1}/images/blueuhd.png" alphatest="blend" />
  <widget source="help" render="Label" position="60,889" size="739,300" font="{0};37" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="817,889" size="533,300" zPosition="5" alphatest="blend"/>
  <ePixmap position="949,907" zPosition="3" size="267,267" pixmap="{1}/images/fairbirduhd.png" alphatest="blend" />
 </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

#### Selection Screen
SKIN_SelectionScreen = """
<screen name="SelectionScreen" position="center,center" size="984,699" title="Select Options">
        <widget source="list" render="Listbox" position="13,13" size="955,615" scrollbarMode="showOnDemand">
            <convert type="TemplatedMultiContent">
                {
                    "template": [
                        MultiContentEntryText(pos=(85,10), size=(867,67), font=0, text=0),
                        MultiContentEntryPixmapAlphaBlend(pos=(0,0), size=(67,67), png=1)
                    ],
                    "fonts": [gFont("Regular", 47)],
                    "itemHeight": 60
                }
            </convert>
        </widget>
<ePixmap pixmap="%s/images/reduhd.png" position="140,689" size="220,3" alphatest="blend"/>
<ePixmap pixmap="%s/images/greenuhd.png" position="643,689" size="220,3" alphatest="blend"/>
<widget name="key_red" position="93,640" zPosition="1" size="328,53" font="Regular;47" halign="center" valign="right" foregroundColor="#00ffffff" backgroundColor="#ff1f771f" transparent="1"/>
<widget name="key_green" position="593,640" zPosition="1" size="328,53" font="Regular;47" halign="center" valign="right" foregroundColor="#00ffffff" backgroundColor="#ff9f1313" transparent="1"/>
</screen>
""" % (resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal'), resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal'))

### SKIN_Picons
if DreamOS():
      SKIN_Picons = """
<screen name="PiconsScreen" backgroundColor="#16000000" position="center,center" size="1747,840" title="RAED's RaedQuickSignal Picons setup" flags="wfNoBorder">
  <eLabel position="0,71" size="1747,1" zPosition="10" backgroundColor="#00ffffff"/>
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bab329" position="40,7" size="1667,60" transparent="1"/>
  <widget name="menu" position="20,80" size="1141,600" foregroundColor="#00ffffff" backgroundColor="#16000000" foregroundColorSelected="#00000000" backgroundColorSelected="#00ffffff" scrollbarMode="showOnDemand" transparent="1" zPosition="1"/>
  <eLabel text="{1}" position="19,691" size="1701,67" font="{0};43" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <eLabel text="{2}" position="21,763" size="1701,67" font="{0};43" foregroundColor="#00bab329" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="1184,249" size="533,300" zPosition="5" alphatest="blend"/>
</screen>
""".format(FontName, title75, title76)
else:
      SKIN_Picons = """
<screen name="PiconsScreen" backgroundColor="#16000000" position="center,center" size="1747,840" title="RAED's RaedQuickSignal Picons setup" flags="wfNoBorder">
  <eLabel position="0,71" size="1747,1" zPosition="10" backgroundColor="#00ffffff"/>
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bab329" position="40,7" size="1667,60" transparent="1"/>
  <widget name="menu" position="20,80" size="1141,600" font="{0};47" itemHeight="60" foregroundColor="#00ffffff" backgroundColor="#16000000" foregroundColorSelected="#00000000" backgroundColorSelected="#00ffffff" scrollbarMode="showOnDemand" transparent="1" zPosition="1"/>
  <eLabel text="{1}" position="19,691" size="1701,67" font="{0};43" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <eLabel text="{2}" position="21,763" size="1701,67" font="{0};43" foregroundColor="#00bab329" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="1184,249" size="533,300" zPosition="5" alphatest="blend"/>
</screen>
""".format(FontName, title75, title76)

### SKIN_WeatherLocation
if DreamOS():
	SKIN_WeatherLocation = """
<screen backgroundColor="#16000000" name="WeatherLocationChoiceList" position="0,0" size="1023,1440" title="Location list" flags="wfNoBorder">
  <widget source="Title" render="Label" position="40,15" size="935,99" font="{0};60" transparent="1"/>
  <widget name="choicelist" position="40,127" size="935,1187" scrollbarMode="showOnDemand" scrollbarWidth="6" transparent="1"/>
  <eLabel position="100,1420" size="387,7" zPosition="-10" backgroundColor="#00ff2525"/>
  <eLabel position="507,1420" size="387,7" zPosition="-10" backgroundColor="#00389416"/>
  <widget name="key_red" position="100,1357" size="387,60" halign="center" valign="center" zPosition="1" font="{0};47" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget name="key_green" position="507,1357" size="387,60" halign="center" valign="center" zPosition="1" font="{0};47" foregroundColor="#00f0f0f0" transparent="1"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
else:
	SKIN_WeatherLocation = """
<screen backgroundColor="#16000000" name="WeatherLocationChoiceList" position="0,0" size="1023,1440" title="Location list" flags="wfNoBorder">
  <widget source="Title" render="Label" position="40,15" size="935,99" font="{0};60" transparent="1"/>
  <widget name="choicelist" font="{0};47" itemHeight="53" position="40,127" size="935,1187" scrollbarMode="showOnDemand" scrollbarWidth="6" transparent="1"/>
  <eLabel position="100,1420" size="387,7" zPosition="-10" backgroundColor="#00ff2525"/>
  <eLabel position="507,1420" size="387,7" zPosition="-10" backgroundColor="#00389416"/>
  <widget name="key_red" position="100,1357" size="387,60" halign="center" valign="center" zPosition="1" font="{0};47" foregroundColor="#00f0f0f0" transparent="1"/>
  <widget name="key_green" position="507,1357" size="387,60" halign="center" valign="center" zPosition="1" font="{0};47" foregroundColor="#00f0f0f0" transparent="1"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
### SKIN_SearchLocationMSN
if DreamOS():
	SKIN_SearchLocationMSN = """
		<!-- Search LocationMSN -->
		<screen name="SearchLocationMSN" position="center,center" size="1616,897" title="SearchLocationMSN">
		<widget name="menu" position="27,27" size="1576,853" scrollbarMode="showOnDemand" transparent="1" />
		</screen>
"""
else:
	SKIN_SearchLocationMSN = """
		<!-- Search LocationMSN -->
		<screen name="SearchLocationMSN" position="center,center" size="1616,897" title="SearchLocationMSN">
		<widget name="menu" position="27,27" size="1576,853" font="{0};48" itemHeight="67" scrollbarMode="showOnDemand" transparent="1" />
		</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
##different way ...
#SKIN_WeatherLocation = """
#<screen backgroundColor="#16000000" name="WeatherLocationChoiceList" position="center,center" size="1707,960" title="Location list" flags="wfNoBorder">
#			<widget source="Title" render="Label" position="93,63" size="1267,57" font="%(key)s;47" transparent="1" />
#			<widget name="choicelist" position="93,153" size="933,640" scrollbarMode="showOnDemand" scrollbarWidth="6" transparent="1" />
#			<eLabel position=" 55,675" size="290, 5" zPosition="-10" backgroundColor="#00ff2525" />
#			<eLabel position="467,900" size="290, 5" zPosition="-10" backgroundColor="#00389416" />
#			<eLabel position="860,900" size="290, 5" zPosition="-10" backgroundColor="#00bab329" />
#			<eLabel position="1253,900" size="290, 5" zPosition="-10" backgroundColor="#000080ff" />
#			<widget name="key_red" position="93,847" size="347,33" zPosition="1" font="%(key)s;27" halign="left" foregroundColor="#00f0f0f0" transparent="1" />
#			<widget name="key_green" position="487,847" size="347,33" zPosition="1" font="%(key)s;27" halign="left" foregroundColor="#00f0f0f0" transparent="1" />
#		</screen>
#""" % {'key': FontName,}

### SKIN_AGC_Picon
SKIN_AGC_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="745,7" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,156" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,149" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Picon -->
  <ePixmap position="447,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="453,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="720,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="729,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="995,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1004,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1272,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1281,832" size="253,147" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
    <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,156" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,149" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Picon -->
  <ePixmap position="447,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="453,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="720,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="729,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="995,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1004,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1272,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1281,832" size="253,147" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Event_Des
SKIN_AGC_Event_Des_SNRdB = """
 <screen backgroundColor="#16000000" name="AGC_Event_Des" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="745,7" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,156" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,149" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="453,833" size="1080,160" font="{0};37" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Event_Des_NOSNRdB = """
 <screen backgroundColor="#16000000" name="AGC_Event_Des" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,156" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,149" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="453,833" size="1080,160" font="{0};37" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Weather
SKIN_AGC_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="745,7" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,156" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,149" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="443,817" size="321,43" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="435,860" size="133,133" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="565,921" size="533,53" font="{0};40" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="565,848" size="200,80" font="{0};60" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="1033,925" size="67,67" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_uhd.png" />
<widget source="session.CurrentService" render="Label" position="836,924" size="196,67" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="1013,833" size="80,80" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_uhd.png" />
<widget source="session.CurrentService" render="Label" position="836,841" size="196,67" font="{0};47" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/riseuhd.png" position="1133,837" size="173,80" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1133,932" size="173,47" font="{0};43" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setuhd.png" position="1333,837" size="173,80" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1333,932" size="173,47" font="{0};43" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
      <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,156" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,149" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="443,817" size="321,43" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="435,860" size="133,133" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="565,921" size="533,53" font="{0};40" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="565,848" size="200,80" font="{0};60" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="1033,925" size="67,67" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_uhd.png" />
<widget source="session.CurrentService" render="Label" position="836,924" size="196,67" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="1013,833" size="80,80" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_uhd.png" />
<widget source="session.CurrentService" render="Label" position="836,841" size="196,67" font="{0};47" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/riseuhd.png" position="1133,837" size="173,80" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1133,932" size="173,47" font="{0};43" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setuhd.png" position="1333,837" size="173,80" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1333,932" size="173,47" font="{0};43" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Picon
SKIN_Event_Progress_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="745,7" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="213,149" size="1573,67" font="{0};47" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Picon -->
  <ePixmap position="447,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="453,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="720,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="729,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="995,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1004,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1272,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1281,832" size="253,147" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="213,149" size="1573,67" font="{0};47" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Picon -->
  <ePixmap position="447,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="453,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="720,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="729,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="995,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1004,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1272,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1281,832" size="253,147" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Event_Des
SKIN_Event_Progress_Event_Des_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="745,7" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="213,149" size="1573,67" font="{0};47" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="453,833" size="1080,160" font="{0};37" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Event_Des_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="213,149" size="1573,67" font="{0};47" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="453,833" size="1080,160" font="{0};37" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Weather
SKIN_Event_Progress_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="745,7" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="213,149" size="1573,67" font="{0};47" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="443,817" size="321,43" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="435,860" size="133,133" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="565,921" size="533,53" font="{0};40" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="565,848" size="200,80" font="{0};60" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="1033,925" size="67,67" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_uhd.png" />
<widget source="session.CurrentService" render="Label" position="836,924" size="196,67" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="1013,833" size="80,80" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_uhd.png" />
<widget source="session.CurrentService" render="Label" position="836,841" size="196,67" font="{0};47" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/riseuhd.png" position="1133,837" size="173,80" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1133,932" size="173,47" font="{0};43" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setuhd.png" position="1333,837" size="173,80" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1333,932" size="173,47" font="{0};43" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="213,149" size="1573,67" font="{0};47" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="443,817" size="321,43" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="435,860" size="133,133" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="565,921" size="533,53" font="{0};40" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="565,848" size="200,80" font="{0};60" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="1033,925" size="67,67" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_uhd.png" />
<widget source="session.CurrentService" render="Label" position="836,924" size="196,67" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="1013,833" size="80,80" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_uhd.png" />
<widget source="session.CurrentService" render="Label" position="836,841" size="196,67" font="{0};47" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/riseuhd.png" position="1133,837" size="173,80" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1133,932" size="173,47" font="{0};43" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setuhd.png" position="1333,837" size="173,80" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1333,932" size="173,47" font="{0};43" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Picon_media
SKIN_AGC_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="745,7" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,156" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,149" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Picon -->
  <ePixmap position="447,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="453,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="720,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="729,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="995,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="1004,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1272,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1281,832" size="253,147" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_AGC_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,156" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,149" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Picon -->
  <ePixmap position="447,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="453,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="720,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="729,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="995,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="1004,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1272,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1281,832" size="253,147" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Picon_media
SKIN_Event_Progress_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="745,7" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="213,149" size="1573,67" font="{0};47" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Picon -->
  <ePixmap position="447,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="453,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="720,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="729,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="995,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="1004,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1272,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1281,832" size="253,147" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

SKIN_Event_Progress_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="307,273" size="2000,1000" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};47" foregroundColor="#00bbbbbb" position="13,7" size="533,53" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1547,7" size="451,53" font="{0};43" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,79" size="200,53" font="{0};47" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="213,72" size="1573,67" pixmap="{1}/images/icons_quick/icon_snr-scan2uhd.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1797,79" size="200,53" font="{0};47" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="213,149" size="1573,67" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="213,149" size="1573,67" font="{0};47" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="197,683" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,747" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="193,812" size="1600,3" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="53,237" size="1867,400" font="{0};37" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center"  halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,685" size="1600,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1659,685" size="267,60" font="{0};43" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="53,752" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="53,751" size="1867,60" font="{0};43" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="165,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="171,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="43,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="181,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="187,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="193,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="200,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="207,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="213,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="220,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="227,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="233,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="240,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="247,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="253,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="260,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="400,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="407,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="413,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="420,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="427,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="493,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="827,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="893,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1093,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1293,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1333,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1520,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="80,244" size="1800,80" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1867,747" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png" />
  <!-- Picon -->
  <ePixmap position="447,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="453,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="720,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="729,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="995,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="1004,832" size="253,147" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1272,825" size="267,160" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon2_uhd.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1281,832" size="253,147" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="3,880" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="3,933" size="440,53" font="{0};37" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="40,820" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1541,833" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1541,907" size="453,73" font="{0};33" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="1327,639" size="667,43" zPosition="1" font="{0};37" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <widget name="Positioner" position="7,639" size="667,43" zPosition="1" font="{0};37" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Full_Screen
SKIN_Full_Screen1 = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="2560,1440" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="40,9" size="2480,100" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};60" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="2220,29" size="300,49" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};48" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="1920,69" size="600,49" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};32" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="721,709" size="1759,175" font="{0};80" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="1059,563" size="420,129" font="{0};73" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="1441,563" size="651,129" font="{0};73" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="721,955" size="1759,175" font="{0};73" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="721,1119" size="1759,175" font="{0};67" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3-uhd.png" position="40,200" size="2480,100" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="49,200" size="200,100" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="{0};69"/>
	<widget source="session.FrontendStatus" render="Label" position="2069,200" size="440,100" halign="right" valign="center" transparent="1" font="{0};69">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3-uhd.png" position="40,320" size="2480,100" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="49,320" size="200,100" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="{0};69"/>
	<widget source="session.FrontendStatus" render="Label" position="2069,320" size="440,100" halign="right" valign="center" transparent="1" font="{0};69">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="SNR:" position="40,480" size="333,67" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};47"/>
	<widget source="session.FrontendStatus" render="Label" position="40,520" size="600,149" font="{0};144" halign="left" backgroundColor="#16000000" transparent="1">
		<convert type="FrontendInfo">SNRdB</convert>
	</widget>
	<eLabel text="AGC:" position="40,720" size="333,67" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};47"/>
	<widget source="session.FrontendStatus" render="Label" position="40,760" size="600,149" backgroundColor="#16000000" transparent="1" font="{0};144" halign="left">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="BER:" position="40,960" size="333,67" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};47"/>
	<widget source="session.FrontendStatus" render="Label" position="40,1000" size="600,149" font="{0};144" halign="left" backgroundColor="#16000000" transparent="1">
		<convert type="FrontendInfo">BER</convert>
	</widget>
	<widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="40,1200" size="620,180" font="{0};144" halign="left" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" >
		<convert type="FrontendInfo">LOCK</convert>
		<convert type="ConditionalShowHide"/>
	</widget>
	<widget name="Positioner" position="43,123" size="1067,67" zPosition="1" font="{0};47" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
	<widget name="Satfinder" position="1449,123" size="1067,67" zPosition="1" font="{0};47" halign="center" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1341,651" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1341,651" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1341,651" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};60" position="1420,643" size="191,67" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};60" position="1620,643" size="25,67" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};60" position="1652,643" size="191,67" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

SKIN_Full_Screen2_SNRdB = """
<screen backgroundColor="#ccffffff" name="RaedQuickSignalScreen" position="0,0" size="2560,1440" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="40,9" size="2480,100" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};60" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="2220,29" size="300,49" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};48" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="1920,69" size="600,49" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};32" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
	<!-- Tuner Info  -->
	<widget source="session.CurrentService" render="Label" position="25,1229" size="2507,87" font="{0};67" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="10">
		<convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="25,1341" size="2507,87" font="{0};67" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="10">
		<convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3-uhd.png" position="40,1220" size="2480,100" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="49,1220" size="200,100" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};69"/>
	<widget source="session.FrontendStatus" render="Label" position="2069,1220" size="440,100" halign="right" valign="center" transparent="1" font="{0};69">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3-uhd.png" position="40,1333" size="2480,100" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="49,1333" size="200,100" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};69"/>
	<widget source="session.FrontendStatus" render="Label" position="2069,1333" size="440,100" halign="right" valign="center" transparent="1" font="{0};69">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Label" position="2069,1120" size="440,107" font="{0};93" halign="right" foregroundColor="#00ff2525" backgroundColor="#00ff2525" transparent="1">
		<convert type="FrontendInfo">SNRdB</convert>
	</widget>
	<widget name="Positioner" position="903,16" size="533,67" zPosition="1" font="{0};47" halign="center" backgroundColor="#ccffffff" foregroundColor="#00ff2525" transparent="1"/>
	<widget name="Satfinder" position="1497,16" size="533,67" zPosition="1" font="{0};47" halign="center" backgroundColor="#ccffffff" foregroundColor="#000080ff" transparent="1"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

SKIN_Full_Screen2_NOSNRdB = """
<screen backgroundColor="#ccffffff" name="RaedQuickSignalScreen" position="0,0" size="2560,1440" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="40,9" size="2480,100" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};60" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="2220,29" size="300,49" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};48" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="1920,69" size="600,49" foregroundColor="#00000000" backgroundColor="#00000000" transparent="1" zPosition="1" font="{0};32" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
	<!-- Tuner Info  -->
	<widget source="session.CurrentService" render="Label" position="25,1229" size="2507,87" font="{0};67" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="10">
		<convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="25,1341" size="2507,87" font="{0};67" halign="center" backgroundColor="#000064c7" foregroundColor="#000064c7" transparent="1" zPosition="10">
		<convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3-uhd.png" position="40,1220" size="2480,100" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="49,1220" size="200,100" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};69"/>
	<widget source="session.FrontendStatus" render="Label" position="2069,1220" size="440,100" halign="right" valign="center" transparent="1" font="{0};69">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3-uhd.png" position="40,1333" size="2480,100" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="49,1333" size="200,100" valign="center" foregroundColor="#00ff2525" backgroundColor="#00000000" transparent="1" font="{0};69"/>
	<widget source="session.FrontendStatus" render="Label" position="2069,1333" size="440,100" halign="right" valign="center" transparent="1" font="{0};69">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<widget name="Positioner" position="903,16" size="533,67" zPosition="1" font="{0};47" halign="center" backgroundColor="#ccffffff" foregroundColor="#00ff2525" transparent="1"/>
	<widget name="Satfinder" position="1497,16" size="533,67" zPosition="1" font="{0};47" halign="center" backgroundColor="#ccffffff" foregroundColor="#000080ff" transparent="1"/>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Full_Screen_Picons
SKIN_Full_Screen_Picon_Vertical = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="2560,1440" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="40,9" size="2480,100" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};60" valign="center"/>
  <widget source="global.CurrentTime" render="Label" position="2220,29" size="300,49" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};48" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1920,69" size="600,49" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};32" valign="center" halign="right">
    <convert type="ClockToText">Date</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <eLabel position="center,90" size="2560,3" backgroundColor="#16000000" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="416,537" size="1733,133" font="{0};80" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="1045,379" size="420,129" font="{0};51" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="1397,379" size="721,129" font="{0};73" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="416,669" size="1733,133" font="{0};73" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="416,801" size="1733,133" font="{0};67" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <eLabel position="416,939" size="1733,3" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="416,1060" size="1733,3" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="416,1177" size="1733,3" backgroundColor="#00bbbbbb" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="416,945" size="1733,113" font="{0};48" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>  
  <widget source="session.CurrentService" render="Label" position="1851,945" size="293,113" font="{0};48" zPosition="2" backgroundColor="#16000000" foregroundColor="#00ee00" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="416,1064" size="1733,113" font="{0};36" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="7,227" size="400,1111" pixmap="{1}/images/icons_quick/icon_snr-scan5_uhd.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR:" position="7,1339" size="400,100" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};69" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="7,125" size="400,100" halign="center" valign="center" transparent="1" font="{0};69">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="2156,227" size="400,1111" pixmap="{1}/images/icons_quick/icon_snr-scan5_uhd.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="AGC:" position="2156,1339" size="400,100" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};69" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="2156,125" size="400,100" halign="center" valign="center" transparent="1" font="{0};69">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="SNR:" position="540,127" size="333,67" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};47"/>
  <widget source="session.FrontendStatus" render="Label" position="416,197" size="600,149" font="{0};144" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <eLabel text="AGC:" position="1093,127" size="333,67" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};47"/>
  <widget source="session.FrontendStatus" render="Label" position="953,200" size="600,149" backgroundColor="#16000000" transparent="1" font="{0};144" halign="center">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="BER:" position="1681,127" size="333,67" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};47"/>
  <widget source="session.FrontendStatus" render="Label" position="1551,200" size="600,149" font="{0};144" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">BER</convert>
  </widget>
  <widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="416,353" size="620,180" font="{0};100" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">LOCK</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget name="Positioner" position="1001,7" size="1067,45" zPosition="1" font="{0};40" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
  <widget name="Satfinder" position="1001,59" size="1067,45" zPosition="1" font="{0};40" halign="center" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <!-- Picon -->
  <ePixmap position="461,1189" size="373,240" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3_uhd.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="472,1200" size="353,220" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="883,1189" size="373,240" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3_uhd.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="893,1200" size="353,220" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="1309,1189" size="373,240" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3_uhd.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1319,1200" size="353,220" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1731,1189" size="373,240" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3_uhd.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1740,1200" size="353,220" transparent="1" alphatest="blend" zPosition="3"/>
  <ePixmap position="2096,20" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="953,477" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="953,477" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="953,477" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};60" position="1053,469" size="191,67" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};60" position="1267,469" size="25,67" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};60" position="1308,469" size="191,67" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

SKIN_Full_Screen_Picon_media_Vertical = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="2560,1440" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="40,9" size="2480,100" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};60" valign="center"/>
  <widget source="global.CurrentTime" render="Label" position="2220,29" size="300,49" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};48" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1920,69" size="600,49" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};32" valign="center" halign="right">
    <convert type="ClockToText">Date</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <eLabel position="center,90" size="2560,3" backgroundColor="#16000000" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="416,537" size="1733,133" font="{0};80" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="1045,379" size="420,129" font="{0};51" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="1397,379" size="721,129" font="{0};73" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="416,669" size="1733,133" font="{0};73" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="416,801" size="1733,133" font="{0};67" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <eLabel position="416,939" size="1733,3" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="416,1060" size="1733,3" backgroundColor="#00bbbbbb" zPosition="4"/>
  <eLabel position="416,1177" size="1733,3" backgroundColor="#00bbbbbb" zPosition="4"/>
  <widget source="session.CurrentService" render="Label" position="416,945" size="1733,113" font="{0};48" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>  
  <widget source="session.CurrentService" render="Label" position="1851,945" size="293,113" font="{0};48" zPosition="2" backgroundColor="#16000000" foregroundColor="#00ee00" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="416,1064" size="1733,113" font="{0};36" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="7,227" size="400,1111" pixmap="{1}/images/icons_quick/icon_snr-scan5_uhd.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR:" position="7,1339" size="400,100" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};69" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="7,125" size="400,100" halign="center" valign="center" transparent="1" font="{0};69">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="2156,227" size="400,1111" pixmap="{1}/images/icons_quick/icon_snr-scan5_uhd.png" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="AGC:" position="2156,1339" size="400,100" valign="center" foregroundColor="#00ffffff" backgroundColor="#16000000" transparent="1" font="{0};69" halign="center"/>
  <widget source="session.FrontendStatus" render="Label" position="2156,125" size="400,100" halign="center" valign="center" transparent="1" font="{0};69">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="SNR:" position="540,127" size="333,67" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};47"/>
  <widget source="session.FrontendStatus" render="Label" position="416,197" size="600,149" font="{0};144" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <eLabel text="AGC:" position="1093,127" size="333,67" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};47"/>
  <widget source="session.FrontendStatus" render="Label" position="953,200" size="600,149" backgroundColor="#16000000" transparent="1" font="{0};144" halign="center">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="BER:" position="1681,127" size="333,67" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};47"/>
  <widget source="session.FrontendStatus" render="Label" position="1551,200" size="600,149" font="{0};144" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">BER</convert>
  </widget>
  <widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="416,353" size="620,180" font="{0};100" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">LOCK</convert>
    <convert type="ConditionalShowHide"/>
  </widget>
  <widget name="Positioner" position="1001,7" size="1067,45" zPosition="1" font="{0};40" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1"/>
  <widget name="Satfinder" position="1001,59" size="1067,45" zPosition="1" font="{0};40" halign="center" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
  <!-- Picon -->
  <ePixmap position="461,1189" size="373,240" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3_uhd.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="472,1200" size="353,220" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="883,1189" size="373,240" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3_uhd.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="893,1200" size="353,220" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="1309,1189" size="373,240" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3_uhd.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="1319,1200" size="353,220" zPosition="3" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1731,1189" size="373,240" zPosition="5" transparent="1" alphatest="blend" pixmap="{1}/images/icons_quick/picon_fon3_uhd.png"/>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1740,1200" size="353,220" transparent="1" alphatest="blend" zPosition="3"/>
  <ePixmap position="2096,20" size="87,67" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2_uhd.png"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="953,477" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="953,477" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="953,477" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};60" position="1053,469" size="191,67" halign="right" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};60" position="1267,469" size="25,67" halign="center" foregroundColor="#00008cec" backgroundColor="#54111112" transparent="1"/>
  <widget source="session.CurrentService" render="Label" font="{0};60" position="1308,469" size="191,67" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Full_Screen_Picons_ECM
SKIN_Full_Screen_Picon_Ecm1_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="2560,1440" title="RAED's Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="2560,1440" zPosition="-10" pixmap="{1}/images/ArmyTouch/UHD/frame_base-fs8.png"/>
    <ePixmap position="159,187" size="511,839" zPosition="1" pixmap="{1}/images/ArmyTouch/UHD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1892,187" size="511,839" zPosition="1" pixmap="{1}/images/ArmyTouch/UHD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="center,140" size="360,40" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="56,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="880,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1704,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="731,745" size="1100,279" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="111,1040" size="2336,128" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1116,357" size="328,104" zPosition="1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="795,329" size="972,400" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="887,247" size="788,67" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <eLabel text="RAEDQuickSignal" position="80,21" size="2400,96" font="{0};72" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="896,248" size="768,59" zPosition="2" font="{0};40" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="884,1272" size="793,60" zPosition="2" font="{0};51" halign="center" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="165,256" size="499,676" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="1899,256" size="499,676" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="1128,361" size="311,99" zPosition="2" font="{0};80" halign="center" foregroundColor="#00ff7a00" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="1156,183" size="247,59" zPosition="2" font="{0};64" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="312,188" size="200,67" zPosition="2" font="{0};64" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="2047,188" size="200,67" zPosition="2" font="{0};64" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="735,753" size="1092,271" zPosition="2" font="{0};33" halign="center" valign="top"  foregroundColor="#000099ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="919,1331" size="528,73" zPosition="2" font="{0};35" halign="left" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1456,1340" size="191,60" zPosition="2" font="{0};51" halign="right" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="616,1111" size="1323,51" zPosition="2" font="{0};36" halign="center" valign="top" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="767,1051" size="560,51" zPosition="2" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="1227,1051" size="547,51" zPosition="4" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="1227,1051" size="547,51" zPosition="5" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="1227,1051" size="547,51" zPosition="6" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="1227,1051" size="547,51" zPosition="7" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="115,1045" size="477,51" zPosition="2" font="{0};43" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="115,1105" size="477,53" zPosition="2" font="{0};51" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1965,1045" size="477,51" zPosition="2" font="{0};51" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="1103,481" size="356,220" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="1107,485" size="348,212" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="823,357" size="256,160" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="827,361" size="248,152" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="823,541" size="256,160" zPosition="3" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="827,545" size="248,152" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1483,357" size="256,160" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="1487,361" size="248,152" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1483,541" size="256,160" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1487,545" size="248,152" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="60,1272" size="793,60" font="{0};51" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="60,1340" size="793,60" font="{0};51" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1708,1340" size="793,60" font="{0};51" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1708,1272" size="793,60" font="{0};51" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>
    <widget name="Positioner" position="80,21" size="767,96" zPosition="10" font="{0};47" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" />
    <widget name="Satfinder" position="1711,21" size="767,96" zPosition="10" font="{0};47" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1980,1108" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1980,1108" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1980,1108" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_uhd.png" position="2305,1111" size="67,53" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_uhd.png" position="2213,1111" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_uhd.png" position="2213,1111" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_media_Ecm1_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="2560,1440" title="RAED's Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="2560,1440" zPosition="-10" pixmap="{1}/images/ArmyTouch/UHD/frame_base-fs8.png"/>
    <ePixmap position="159,187" size="511,839" zPosition="1" pixmap="{1}/images/ArmyTouch/UHD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1892,187" size="511,839" zPosition="1" pixmap="{1}/images/ArmyTouch/UHD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="center,140" size="360,40" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="56,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="880,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1704,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="731,745" size="1100,279" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="111,1040" size="2336,128" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1116,357" size="328,104" zPosition="1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="795,329" size="972,400" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="887,247" size="788,67" zPosition="-1" pixmap="{1}/images/ArmyTouch/UHD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <eLabel text="RAEDQuickSignal" position="80,21" size="2400,96" font="{0};72" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="896,248" size="768,59" zPosition="2" font="{0};40" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="884,1272" size="793,60" zPosition="2" font="{0};51" halign="center" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="165,256" size="499,676" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="1899,256" size="499,676" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="1128,361" size="311,99" zPosition="2" font="{0};80" halign="center" foregroundColor="#00ff7a00" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="1156,173" size="247,59" zPosition="2" font="{0};64" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="312,188" size="200,67" zPosition="2" font="{0};64" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="2047,188" size="200,67" zPosition="2" font="{0};64" halign="center" foregroundColor="#00ff0080" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="735,753" size="1092,271" zPosition="2" font="{0};33" halign="center" valign="top"  foregroundColor="#000099ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="919,1331" size="528,73" zPosition="2" font="{0};35" halign="left" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1456,1340" size="191,60" zPosition="2" font="{0};51" halign="right" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="616,1111" size="1323,51" zPosition="2" font="{0};36" halign="center" valign="top" foregroundColor="#0000ff00" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="767,1051" size="560,51" zPosition="2" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="1227,1051" size="547,51" zPosition="4" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="1227,1051" size="547,51" zPosition="5" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="1227,1051" size="547,51" zPosition="6" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="1227,1051" size="547,51" zPosition="7" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="115,1045" size="477,51" zPosition="2" font="{0};43" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="115,1105" size="477,53" zPosition="2" font="{0};51" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1965,1045" size="477,51" zPosition="2" font="{0};51" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="1103,481" size="356,220" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="1107,485" size="348,212" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="823,357" size="256,160" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="827,361" size="248,152" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="823,541" size="256,160" zPosition="3" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="827,545" size="248,152" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1483,357" size="256,160" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconCrypt" position="1487,361" size="248,152" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1483,541" size="256,160" zPosition="2" pixmap="{1}/images/ArmyTouch/UHD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1487,545" size="248,152" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="60,1272" size="793,60" font="{0};51" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="60,1340" size="793,60" font="{0};51" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1708,1340" size="793,60" font="{0};51" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1708,1272" size="793,60" font="{0};51" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>
    <widget name="Positioner" position="80,21" size="767,96" zPosition="10" font="{0};47" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" />
    <widget name="Satfinder" position="1711,21" size="767,96" zPosition="10" font="{0};47" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1980,1108" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1980,1108" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1980,1108" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_uhd.png" position="2305,1111" size="67,53" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_uhd.png" position="2213,1111" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_uhd.png" position="2213,1111" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_Ecm2_Vertical = """
<screen backgroundColor="#ffffffff" name="RaedQuickSignalScreen" position="0,0" size="2560,1440" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
    <ePixmap position="0,0" size="2560,1440" zPosition="-10" pixmap="{1}/images/ShabahNet/UHD/frame_base-fs8.png"/>
    <ePixmap position="159,187" size="511,839" zPosition="1" pixmap="{1}/images/ShabahNet/UHD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1892,187" size="511,839" zPosition="1" pixmap="{1}/images/ShabahNet/UHD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="center,135" size="363,107" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="56,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="880,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1704,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="731,745" size="1100,279" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="111,1040" size="2336,128" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1116,357" size="328,104" zPosition="1" pixmap="{1}/images/ShabahNet/UHD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="795,329" size="972,400" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="887,247" size="788,67" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <eLabel text="RAEDQuickSignal" position="80,21" size="2400,96" font="{0};60" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="896,248" size="768,59" zPosition="2" font="{0};37" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="884,1272" size="793,60" zPosition="2" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="165,256" size="499,676" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="1899,256" size="499,676" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="1128,361" size="311,99" zPosition="2" font="{0};67" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="1156,173" size="247,59" zPosition="2" font="{0};53" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="312,188" size="200,67" zPosition="2" font="{0};53" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="2047,188" size="200,67" zPosition="2" font="{0};53" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="735,753" size="1092,271" zPosition="2" font="{0};33" halign="center" valign="top"  foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="919,1331" size="528,73" zPosition="2" font="{0};35" halign="left" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1456,1340" size="191,60" zPosition="2" font="{0};40" halign="right" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="616,1111" size="1323,51" zPosition="2" font="{0};36" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="767,1051" size="560,51" zPosition="2" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="1227,1051" size="547,51" zPosition="4" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="1227,1051" size="547,51" zPosition="5" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="1227,1051" size="547,51" zPosition="6" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="1227,1051" size="547,51" zPosition="7" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="115,1045" size="477,51" zPosition="2" font="{0};40" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="115,1105" size="477,53" zPosition="2" font="{0};40" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1965,1045" size="477,51" zPosition="2" font="{0};40" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="1103,481" size="356,220" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="1107,485" size="348,212" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="823,357" size="256,160" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="827,361" size="248,152" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="823,541" size="256,160" zPosition="3" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="827,545" size="248,152" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1483,357" size="256,160" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="1487,361" size="248,152" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1483,541" size="256,160" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1487,545" size="248,152" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="60,1272" size="793,60" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="60,1340" size="793,60" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1708,1340" size="793,60" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1708,1272" size="793,60" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>
    <widget name="Positioner" position="80,21" size="767,96" zPosition="10" font="{0};40" halign="left" backgroundColor="#00ffffff" foregroundColor="#41ff9900" transparent="1" valign="center" />
    <widget name="Satfinder" position="1711,21" size="767,96" zPosition="10" font="{0};40" backgroundColor="#00ffffff" foregroundColor="#0000deff" transparent="1" valign="center" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="1980,1108" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1980,1108" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="1980,1108" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_uhd.png" position="2305,1111" size="67,53" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_uhd.png" position="2213,1111" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_uhd.png" position="2213,1111" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_media_Ecm2_Vertical = """
<screen backgroundColor="#ffffffff" name="RaedQuickSignalScreen" position="0,0" size="2560,1440" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
    <ePixmap position="0,0" size="2560,1440" zPosition="-10" pixmap="{1}/images/ShabahNet/UHD/frame_base-fs8.png"/>
    <ePixmap position="159,187" size="511,839" zPosition="1" pixmap="{1}/images/ShabahNet/UHD/ind_snr2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1892,187" size="511,839" zPosition="1" pixmap="{1}/images/ShabahNet/UHD/ind_agc2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="center,135" size="363,107" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/arrow_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="56,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="880,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1704,1263" size="801,144" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="731,745" size="1100,279" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="111,1040" size="2336,128" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1116,357" size="328,104" zPosition="1" pixmap="{1}/images/ShabahNet/UHD/frame_quick4.png" alphatest="blend" transparent="1"/>
    <ePixmap position="795,329" size="972,400" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick5.png" alphatest="blend" transparent="1"/>
    <ePixmap position="887,247" size="788,67" zPosition="-1" pixmap="{1}/images/ShabahNet/UHD/frame_quick6.png" alphatest="blend" transparent="1"/>
    <eLabel text="RAEDQuickSignal" position="80,21" size="2400,96" font="{0};64" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1"/>
    <widget source="global.CurrentTime" render="Label" position="896,248" size="768,59" zPosition="2" font="{0};37" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Date</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="884,1272" size="793,60" zPosition="2" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="165,256" size="499,676" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="1899,256" size="499,676" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="1128,361" size="311,99" zPosition="2" font="{0};67" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="ClockToText">Format:%H:%M:%S</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="1156,183" size="247,59" zPosition="2" font="{0};53" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="312,188" size="200,67" zPosition="2" font="{0};53" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="2047,188" size="200,67" zPosition="2" font="{0};53" halign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="FrontendInfo">AGC</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="735,753" size="1092,271" zPosition="2" font="{0};33" halign="center" valign="top"  foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="919,1331" size="528,73" zPosition="2" font="{0};35" halign="left" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">caids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1456,1340" size="191,60" zPosition="2" font="{0};40" halign="right" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">activecaid</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="616,1111" size="1323,51" zPosition="2" font="{0};36" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">pids</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="767,1051" size="560,51" zPosition="2" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="1227,1051" size="547,51" zPosition="4" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="1227,1051" size="547,51" zPosition="5" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="1227,1051" size="547,51" zPosition="6" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="1227,1051" size="547,51" zPosition="7" font="{0};40" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="Label" position="115,1045" size="477,51" zPosition="2" font="{0};40" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">ecmfile</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="115,1105" size="477,53" zPosition="2" font="{0};40" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">emuname</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1965,1045" size="477,51" zPosition="2" font="{0};40" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%s</convert>
    </widget>
   <!--Picon-->
    <ePixmap position="1103,481" size="356,220" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon2.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="1107,485" size="348,212" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="823,357" size="256,160" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="827,361" size="248,152" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="823,541" size="256,160" zPosition="3" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="827,545" size="248,152" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1483,357" size="256,160" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon3s.png" transparent="2" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconCrypt" position="1487,361" size="248,152" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1483,541" size="256,160" zPosition="2" pixmap="{1}/images/ShabahNet/UHD/frame_of_picon3s.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1487,545" size="248,152" transparent="1" alphatest="blend" zPosition="3" />
    <widget source="session.CurrentService" render="Label" position="60,1272" size="793,60" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Name</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="60,1340" size="793,60" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1708,1340" size="793,60" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="1708,1272" size="793,60" font="{0};40" halign="center" foregroundColor="#00808888" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
    </widget>
    <widget name="Positioner" position="80,21" size="767,96" zPosition="10" font="{0};40" halign="left" backgroundColor="#00ffffff" foregroundColor="#41ff9900" transparent="1" valign="center" />
    <widget name="Satfinder" position="1711,21" size="767,96" zPosition="10" font="{0};40" backgroundColor="#00ffffff" foregroundColor="#0000deff" transparent="1" valign="center" halign="right"/>
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="2067,1108" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="2067,1108" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="2067,1108" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_uhd.png" position="2305,1111" size="67,53" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_uhd.png" position="2213,1111" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_uhd.png" position="2213,1111" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>  
  </screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title82, title83, title84, title85)

SKIN_Full_Screen_Picon_Ecm3_Vertical = """
<screen name="RaedQuickSignalScreen" position="0,0" size="2560,1440" title="Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="2560,1440" zPosition="-10" pixmap="{1}/images/CobaltFHD/UHD/cool1.png"/>
    <ePixmap position="159,187" size="343,745" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/agc_snr.png" alphatest="blend" transparent="1"/>
    <ePixmap position="2060,187" size="343,745" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/pogoda.png" alphatest="blend" transparent="1"/>
    <ePixmap position="89,1129" size="801,144" zPosition="-1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="892,1129" size="801,144" zPosition="-1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="1692,1129" size="801,144" zPosition="-1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
    <ePixmap position="764,645" size="1059,279" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick2.png" alphatest="blend" transparent="1"/>
    <ePixmap position="144,960" size="2336,128" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick3.png" alphatest="blend" transparent="1"/>
    <ePixmap position="795,209" size="972,400" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick5.png" alphatest="blend" transparent="1"/>
	<widget source="session.Event_Now" render="Label" position="817,216" size="925,53" font="{0};47" halign="center" backgroundColor="#595959" foregroundColor="#00ffffff" transparent="1" zPosition="1">
      <convert type="EventName">Name</convert>
 </widget>
	<eLabel name="new eLabel" position="861,277" size="837,3" backgroundColor="#004f6ef2" />
	<widget backgroundColor="#16000000" font="{0};40" halign="left" position="816,297" render="Label" size="925,295" source="session.Event_Now" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
 </widget>
	  <widget source="global.CurrentTime" render="Label" position="1227,67" size="1227,67" font="{0};53" valign="center" halign="right" backgroundColor="#54111112" foregroundColor="#58bcff" transparent="1">
      <convert type="ClockToText">Format:%A  %e  %B  %Y     %H:%M </convert>
	   </widget>
    <widget source="Title" position="160,67" size="1067,93" render="Label" font="{0};53" foregroundColor="#58bcff" backgroundColor="#00000000" transparent="1" halign="center"/>
    <widget source="session.CurrentService" render="Label" position="903,1139" size="757,53" zPosition="2" font="{0};43"  halign="center" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
 <widget source="session.FrontendStatus" render="Progress" position="165,256" size="163,609" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/scale.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Progress" position="333,256" size="163,609" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/scale.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
    </widget>
    <widget source="session.FrontendStatus" render="Label" position="165,192" size="167,55" zPosition="2" font="{0};40" halign="center" valign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
 </widget>
    <widget source="session.FrontendStatus" render="Label" position="333,192" size="167,55" zPosition="2" font="{0};40" halign="center" valign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="773,649" size="1020,271" zPosition="2" font="{0};32" halign="center" valign="center"  foregroundColor="#000090e6" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="901,1200" size="607,71" zPosition="2" font="{0};35" halign="left" valign="top" foregroundColor="#00fffe9e" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1473,1207" size="191,60" zPosition="2" font="{0};43" halign="right" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="616,1031" size="1323,51" zPosition="2" font="{0};43" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};43" foregroundColor="#004f6ef2" halign="left" position="649,971" size="160,51" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};43" halign="left" position="803,971" render="Label" size="333,51" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};43" halign="left" position="1207,971" size="107,51" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="1127,971" size="67,51" font="{0};44" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
  <widget source="session.CurrentService" render="Label" position="160,1025" size="400,53"  foregroundColor="#00389416" zPosition="3" font="{0};43" halign="center"  backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="1263,971" size="400,51" zPosition="4" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="1263,971" size="400,51" zPosition="5" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="1263,971" size="400,51" zPosition="6" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="1263,971" size="400,51" zPosition="7" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};43" foregroundColor="#004f6ef2" halign="left" position="1693,971" size="107,51" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};43" halign="left" position="1800,971" render="Label" size="107,51" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="115,965" size="477,51" zPosition="2" font="{0};44" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1948,1025" size="459,51" zPosition="2" font="{0};44" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="2107,971" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="2107,971" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="2107,971" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
<!--Picon-->
	<ePixmap position="524,211" size="256,160" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/frame_of_picon3c.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="529,216" size="243,147" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
	<ePixmap position="524,453" size="256,160" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="529,459" size="243,147" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
	<ePixmap position="1785,211" size="256,160" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1791,216" zPosition="5" size="243,147" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
	<ePixmap position="1785,453" size="256,160" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1791,459" size="243,147" transparent="1" alphatest="blend" zPosition="3" />
    <!--widget source="session.CurrentService" render="Label" position="101,1139" size="757,60" font="{0};44" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Number</convert>
    </widget-->
    <widget source="session.CurrentService" render="Label" position="101,1207" size="757,60" font="{0};44" halign="center" foregroundColor="#34a36e" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1667,1207" size="813,60" font="{0};40" halign="center" foregroundColor="#00bab329" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1667,1144" size="813,60" font="{0};40" halign="center" foregroundColor="#58bcff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
 </widget>
 <!--pogoda-->
 <eLabel text="{8}" position="2185,259" size="133,40" font="{0};33" backgroundColor="#54111112" halign="center" transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="2065,259" size="120,120" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="2293,259" size="88,40" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#00c1ea02" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/UHD/wiatr.png" position="2184,299" size="40,40" zPosition="3" transparent="1" alphatest="blend" />
    <ePixmap pixmap="{1}/images/CobaltFHD/UHD/deszcz.png" position="2185,339" size="40,40" zPosition="4" transparent="1" alphatest="blend" />
 <widget source="session.CurrentService" render="Label" position="2235,299" size="160,40" font="{0};37" zPosition="3" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="2233,339" size="160,40" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
    <!--eLabel text="%" position="2317,339" size="40,40" zPosition="2" backgroundColor="#54111112" transparent="1" font="{0};33" foregroundColor="#00ffffff" /-->
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/UHD/wsch.png" position="2068,400" size="132,67" zPosition="2" />
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/UHD/zach.png" position="2068,467" size="132,67" zPosition="2" />
    <eLabel text="Rise." position="2207,433" size="100,40" font="{0};28" backgroundColor="#54111112"  transparent="1" zPosition="2" />
	<widget backgroundColor="#54111112" font="{0};33" halign="right" position="2287,428" zPosition="2" render="Label" size="95,40" source="global.CurrentTime" transparent="1" valign="center">
  <convert type="RaedQuickWeather">Sunrise</convert>
 </widget>
    <eLabel text="Set." position="2207,500" size="100,40" font="{0};28" backgroundColor="#54111112"  transparent="1" zPosition="2" />
    <widget backgroundColor="#54111112" font="{0};33" foregroundColor="#00ffffff" halign="right" position="2287,495" zPosition="2" render="Label" size="95,40" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunset</convert>
 </widget>
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather/MoonPhase" position="2081,567" size="107,107" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">PiconMoon</convert>
  </widget>
   <widget source="session.CurrentService" render="Label" position="2148,560" size="220,87" font="{0};33" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Moonlight</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2175,647" size="227,31" font="{0};33" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Moondist</convert>
  </widget>
    <eLabel name="new eLabel" position="2089,696" size="285,3" zPosition="2" backgroundColor="#004f6ef2" />
	<eLabel text="{9}" position="2068,700" size="327,40" font="{0};33" halign="center" valign="center" backgroundColor="#54111112"  transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
	<widget alphatest="blend" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="2068,743" size="120,120" source="session.CurrentService" transparent="1" zPosition="2">
    <convert type="RaedQuickWeather">Picon2</convert>
 </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/UHD/temp.png" position="2241,769" size="27,67" zPosition="2" transparent="1" alphatest="blend" />
	<widget source="session.CurrentService" render="Label" font="{0};33" position="2253,759" size="120,40" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Hightemp2</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" font="{0};33" position="2253,804" size="120,40" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Lowtemp2</convert>
 </widget>
<widget name="Positioner" position="696,1307" size="767,96" zPosition="10" font="{0};40" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" valign="center" transparent="1"/>
<widget name="Satfinder" position="1547,1307" size="767,96" zPosition="10" font="{0};40" backgroundColor="#54111112" foregroundColor="#0000deff"  valign="center" halign="center" transparent="1"/>
	<ePixmap position="160,1320" size="133,53" pixmap="{1}/images/CobaltFHD/UHD/menu.png" alphatest="blend" />
	<ePixmap position="400,1320" size="133,53" pixmap="{1}/images/CobaltFHD/UHD/exit.png" alphatest="blend" /> 
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="204,1140" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="204,1140" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="204,1140" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_uhd.png" position="628,1140" size="67,53" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_uhd.png" position="535,1140" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_uhd.png" position="535,1140" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>  
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85, title86, title87)

SKIN_Full_Screen_Picon_media_Ecm3_Vertical = """
<screen name="RaedQuickSignalScreen" position="0,0" size="2560,1440" title="Quick Signal Info" flags="wfNoBorder">
 <ePixmap position="0,0" size="2560,1440" zPosition="-10" pixmap="{1}/images/CobaltFHD/UHD/cool1.png"/>
 <ePixmap position="159,187" size="343,745" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/agc_snr.png" alphatest="blend" transparent="1"/>
 <ePixmap position="2060,187" size="343,745" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/pogoda.png" alphatest="blend" transparent="1"/>
 <ePixmap position="89,1129" size="801,144" zPosition="-1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
 <ePixmap position="892,1129" size="801,144" zPosition="-1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
 <ePixmap position="1692,1129" size="801,144" zPosition="-1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick1.png" alphatest="blend" transparent="1"/>
 <ePixmap position="764,645" size="1059,279" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick2.png" alphatest="blend" transparent="1"/>
 <ePixmap position="144,960" size="2336,128" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick3.png" alphatest="blend" transparent="1"/>
 <ePixmap position="795,209" size="972,400" zPosition="1" pixmap="{1}/images/CobaltFHD/UHD/frame_quick5.png" alphatest="blend" transparent="1"/>
 <widget source="session.Event_Now" render="Label" position="817,216" size="925,53" font="{0};47" halign="center" backgroundColor="#595959" foregroundColor="#00ffffff" transparent="1" zPosition="1">
      <convert type="EventName">Name</convert>
 </widget>
 <eLabel name="new eLabel" position="861,277" size="837,3" backgroundColor="#004f6ef2" />
 <widget backgroundColor="#16000000" font="{0};40" halign="left" position="816,297" render="Label" size="925,295" source="session.Event_Now" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
 </widget>
 <widget source="global.CurrentTime" render="Label" position="1227,67" size="1227,67" font="{0};53" valign="center" halign="right" backgroundColor="#54111112" foregroundColor="#58bcff" transparent="1">
      <convert type="ClockToText">Format:%A  %e  %B  %Y     %H:%M </convert>
 </widget>
 <widget source="Title" position="160,67" size="1067,93" render="Label" font="{0};53" foregroundColor="#58bcff" backgroundColor="#00000000" transparent="1" halign="center"/>
 <widget source="session.CurrentService" render="Label" position="903,1139" size="757,53" zPosition="2" font="{0};43"  halign="center" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget> 
 <widget source="session.FrontendStatus" render="Progress" position="165,256" size="163,609" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/scale.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">SNR</convert>
 </widget>
 <widget source="session.FrontendStatus" render="Progress" position="333,256" size="163,609" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/scale.png" orientation="orBottomToTop" transparent="1">
      <convert type="RaedQuickFrontendInfo2">AGC</convert>
 </widget>
 <widget source="session.FrontendStatus" render="Label" position="165,192" size="167,55" zPosition="2" font="{0};40" halign="center" valign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
 </widget>
    <widget source="session.FrontendStatus" render="Label" position="333,192" size="167,55" zPosition="2" font="{0};40" halign="center" valign="center" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="773,649" size="1020,271" zPosition="2" font="{0};32" halign="center" valign="center"  foregroundColor="#000090e6" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="901,1200" size="607,71" zPosition="2" font="{0};35" halign="left" valign="top" foregroundColor="#00fffe9e" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1473,1207" size="191,60" zPosition="2" font="{0};43" halign="right" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="616,1031" size="1323,51" zPosition="2" font="{0};43" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};43" foregroundColor="#004f6ef2" halign="left" position="649,971" size="160,51" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};43" halign="left" position="803,971" render="Label" size="267,51" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};43" halign="left" position="1207,971" size="107,51" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="1127,971" size="67,51" font="{0};44" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="160,1025" size="400,53"  foregroundColor="#00389416" zPosition="3" font="{0};43" halign="center"  backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="1263,971" size="400,51" zPosition="4" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="1263,971" size="400,51" zPosition="5" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="1263,971" size="400,51" zPosition="6" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="1263,971" size="400,51" zPosition="7" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};43" foregroundColor="#004f6ef2" halign="left" position="1693,971" size="107,51" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};43" halign="left" position="1800,971" render="Label" size="107,51" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="115,965" size="477,51" zPosition="2" font="{0};44" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1948,1025" size="459,51" zPosition="2" font="{0};44" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="2107,971" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="2107,971" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="2107,971" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
<!--Picon-->
	<ePixmap position="524,211" size="256,160" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/frame_of_picon3c.png" alphatest="blend" transparent="1"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="529,216" size="243,147" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
	<ePixmap position="524,453" size="256,160" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="529,459" size="243,147" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
	<ePixmap position="1785,211" size="256,160" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="1791,216" zPosition="5" size="243,147" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
	<ePixmap position="1785,453" size="256,160" zPosition="2" pixmap="{1}/images/CobaltFHD/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1791,459" size="243,147" transparent="1" alphatest="blend" zPosition="3" />
	<!--widget source="session.CurrentService" render="Label" position="101,1139" size="757,60" font="{0};44" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Number</convert>
 </widget-->
    <widget source="session.CurrentService" render="Label" position="101,1207" size="757,60" font="{0};44" halign="center" foregroundColor="#34a36e" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1667,1207" size="813,60" font="{0};40" halign="center" foregroundColor="#00bab329" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1667,1144" size="813,60" font="{0};40" halign="center" foregroundColor="#58bcff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
 </widget>
 <!--pogoda-->
 <eLabel text="{8}" position="2185,259" size="133,40" font="{0};33" backgroundColor="#54111112" halign="center" transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="weather" position="2065,259" size="120,120" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="2293,259" size="88,40" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#00c1ea02" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/UHD/wiatr.png" position="2184,299" size="40,40" zPosition="3" transparent="1" alphatest="blend" />
    <ePixmap pixmap="{1}/images/CobaltFHD/UHD/deszcz.png" position="2185,339" size="37,40" zPosition="4" transparent="1" alphatest="blend" />
 <widget source="session.CurrentService" render="Label" position="2235,299" size="160,40" font="{0};37" zPosition="3" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="2233,339" size="160,40" font="{0};40" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" >
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
    <!--eLabel text="%" position="2317,339" size="40,40" zPosition="2" backgroundColor="#54111112" transparent="1" font="{0};33" foregroundColor="#00ffffff" /-->
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/UHD/wsch.png" position="2068,400" size="132,67" zPosition="2" />
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/UHD/zach.png" position="2068,467" size="132,67" zPosition="2" />
    <eLabel text="Rise." position="2207,433" size="100,40" font="{0};28" backgroundColor="#54111112"  transparent="1" zPosition="2" />
	<widget backgroundColor="#54111112" font="{0};33" halign="right" position="2287,428" zPosition="2" render="Label" size="95,40" source="global.CurrentTime" transparent="1" valign="center">
  <convert type="RaedQuickWeather">Sunrise</convert>
 </widget>
    <eLabel text="Set." position="2207,500" size="100,40" font="{0};28" backgroundColor="#54111112"  transparent="1" zPosition="2" />
    <widget backgroundColor="#54111112" font="{0};33" foregroundColor="#00ffffff" halign="right" position="2287,495" zPosition="2" render="Label" size="95,40" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunset</convert>
 </widget>
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="weather/MoonPhase" position="2081,567" size="107,107" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">PiconMoon</convert>
  </widget>
   <widget source="session.CurrentService" render="Label" position="2148,560" size="220,87" font="{0};33" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Moonlight</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2175,647" size="227,31" font="{0};33" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1" >
    <convert type="RaedQuickWeather">Moondist</convert>
  </widget>
    <eLabel name="new eLabel" position="2089,696" size="285,3" zPosition="2" backgroundColor="#004f6ef2" />
	<eLabel text="{9}" position="2068,700" size="327,40" font="{0};33" valign="center" halign="center" backgroundColor="#54111112"  transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
	<widget alphatest="blend" render="RaedQuickSignalPiconUni" path="weather" position="2068,743" size="120,120" source="session.CurrentService" transparent="1" zPosition="2">
    <convert type="RaedQuickWeather">Picon2</convert>
 </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/UHD/temp.png" position="2241,769" size="27,67" zPosition="2" transparent="1" alphatest="blend" />
	<widget source="session.CurrentService" render="Label" font="{0};33" position="2253,759" size="120,40" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Hightemp2</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" font="{0};33" position="2253,804" size="120,40" backgroundColor="#54111112" zPosition="3" transparent="1" valign="center" halign="right">
    <convert type="RaedQuickWeather">Lowtemp2</convert>
 </widget> 
<widget name="Positioner" position="696,1307" size="767,96" zPosition="10" font="{0};40" backgroundColor="#54111112" foregroundColor="#41ff9900"  transparent="1" valign="center" halign="center"/>
<widget name="Satfinder" position="1547,1307" size="767,96" zPosition="10" font="{0};40" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center"/>
<ePixmap position="160,1320" size="133,53" pixmap="{1}/images/CobaltFHD/UHD/menu.png" alphatest="blend" />
<ePixmap position="400,1320" size="133,53" pixmap="{1}/images/CobaltFHD/UHD/exit.png" alphatest="blend" />
<!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="337,1140" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="337,1140" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="337,1140" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_uhd.png" position="628,1140" size="67,53" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_uhd.png" position="535,1140" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_uhd.png" position="535,1140" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget>  
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85, title86, title87)

### SKIN_Full_Screen_Picons_ECM_SNR_ANALOG
SKIN_Full_Screen_Picon_Ecm3_SNR_ANALOG = """
<screen name="SKIN_Full_Screen_Picon_Ecm3_SNR_ANALOG" position="0,0" size="2560,1440" title="Quick Signal Info" backgroundColor="#16000000" flags="wfNoBorder">
  <ePixmap position="433,1036" size="1600,333" zPosition="1" pixmap="{1}/images/analog/UHD/analog_tuner_bg.png" alphatest="blend" transparent="1"/>
  <widget source="session.Event_Now" render="Label" position="63,216" size="1197,88" font="{0};47" halign="center" backgroundColor="#ff595959" foregroundColor="#7ad927" transparent="1" zPosition="1">
  <convert type="EventName">Name</convert>
</widget>
<widget backgroundColor="#16000000" font="{0};40" position="63,332" render="Label" size="1200,293" source="session.Event_Now" transparent="1">
  <convert type="EventName">ExtendedDescription</convert>
</widget>
<widget source="session.CurrentService" render="Label" position="1292,216" size="1171,407" zPosition="2" font="{0};37" halign="center" valign="center"  foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">ecmfile</convert>
</widget>
  <widget source="global.CurrentTime" render="Label" position="1227,67" size="1227,67" font="{0};53" valign="center" halign="right" backgroundColor="#16000000" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y  -  %H:%M </convert>
  </widget>
  <widget source="Title" position="160,67" size="1067,93" render="Label" font="{0};53" foregroundColor="#58bcff" backgroundColor="#16000000" transparent="1" halign="center"/>
  <!-- SNRdB -->
  <widget source="session.FrontendStatus" render="Label" position="980,1292" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="453,1292" size="200,60" font="{0};47" halign="left" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
<widget source="session.FrontendStatus" render="Label" position="573,1292" size="200,60" font="{0};47" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="RaedQuickWatches" position="533,1053" size="667,600" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">SNR_ANALOG</convert>
    </widget>
    <!-- AGC -->
    <widget source="session.FrontendStatus" render="RaedQuickWatches" position="1333,1056" size="667,600" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">AGC_ANALOG</convert>
    </widget>
  <eLabel name="agc" text="AGC:" position="1704,1292" size="200,60" font="{0};47" halign="right" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
  <widget source="session.FrontendStatus" render="Label" position="1912,1292" size="200,60" font="{0};47" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <!--Picon-->
    <ePixmap position="271,667" size="333,200" zPosition="2" pixmap="{1}/images/analog/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="277,673" size="320,187" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
    <ePixmap position="823,667" size="333,200" zPosition="2" pixmap="{1}/images/analog/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="829,673" zPosition="5" size="320,187" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
    <ePixmap position="1387,667" size="333,200" zPosition="2" pixmap="{1}/images/analog/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="1393,673" size="320,187" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <ePixmap position="1944,667" size="333,200" zPosition="2" pixmap="{1}/images/analog/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1951,673" size="320,187" transparent="1" alphatest="blend" zPosition="3" />
    <ePixmap position="24,1300" size="133,53" pixmap="{1}/images/CobaltFHD/UHD/exit.png" alphatest="blend"/>
<ePixmap position="24,1239" size="133,53" pixmap="{1}/images/CobaltFHD/UHD/menu.png" alphatest="blend"/>
<widget name="Positioner" position="7,1360" size="767,80" zPosition="10" font="{0};40" backgroundColor="#54111112" foregroundColor="#41ff9900"  transparent="1" valign="center" halign="center"/>
<widget name="Satfinder" position="1787,1360" size="767,80" zPosition="10" font="{0};40" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center"/>
    <widget source="session.CurrentService" render="Label" position="616,959" size="1323,51" zPosition="2" font="{0};43" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};43" foregroundColor="#004f6ef2" halign="left" position="649,885" size="160,51" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};43" halign="left" position="803,885" render="Label" size="267,51" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};43" halign="left" position="1207,885" size="107,51" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="1127,885" size="67,51" font="{0};44" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="160,959" size="400,53"  foregroundColor="#00389416" zPosition="3" font="{0};43" halign="center"  backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="1263,885" size="400,51" zPosition="4" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="1263,885" size="400,51" zPosition="5" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="1263,885" size="400,51" zPosition="6" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="1263,885" size="400,51" zPosition="7" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};43" foregroundColor="#004f6ef2" halign="left" position="1693,885" size="107,51" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};43" halign="left" position="1800,885" render="Label" size="107,51" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="115,885" size="477,51" zPosition="2" font="{0};44" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1948,959" size="459,51" zPosition="2" font="{0};44" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="2107,885" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="2107,885" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="2107,885" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="2075,1177" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="2075,1177" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="2075,1177" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_uhd.png" position="2381,1177" size="67,53" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_uhd.png" position="2288,1177" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_uhd.png" position="2288,1177" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget> 
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85)

SKIN_Full_Screen_Picon_media_Ecm3_SNR_ANALOG = """
<screen name="SKIN_Full_Screen_Picon_media_Ecm3_SNR_ANALOG" position="0,0" size="2560,1440" title="Quick Signal Info" backgroundColor="#16000000" flags="wfNoBorder">
  <ePixmap position="433,1036" size="1600,333" zPosition="1" pixmap="{1}/images/analog/UHD/analog_tuner_bg.png" alphatest="blend" transparent="1"/>
  <widget source="session.Event_Now" render="Label" position="63,216" size="1197,88" font="{0};47" halign="center" backgroundColor="#ff595959" foregroundColor="#7ad927" transparent="1" zPosition="1">
  <convert type="EventName">Name</convert>
</widget>
<widget backgroundColor="#16000000" font="{0};40" position="63,332" render="Label" size="1200,293" source="session.Event_Now" transparent="1">
  <convert type="EventName">ExtendedDescription</convert>
</widget>
<widget source="session.CurrentService" render="Label" position="1292,216" size="1171,407" zPosition="2" font="{0};37" halign="center" valign="center"  foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">ecmfile</convert>
</widget>
  <widget source="global.CurrentTime" render="Label" position="1227,67" size="1227,67" font="{0};53" valign="center" halign="right" backgroundColor="#16000000" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y  -  %H:%M </convert>
  </widget>
  <widget source="Title" position="160,67" size="1067,93" render="Label" font="{0};53" foregroundColor="#58bcff" backgroundColor="#16000000" transparent="1" halign="center"/>
  <!-- SNRdB -->
  <widget source="session.FrontendStatus" render="Label" position="980,1292" zPosition="2" size="533,60" font="{0};53" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="453,1292" size="200,60" font="{0};47" halign="left" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
<widget source="session.FrontendStatus" render="Label" position="573,1292" size="200,60" font="{0};47" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="RaedQuickWatches" position="533,1053" size="667,600" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">SNR_ANALOG</convert>
    </widget>
    <!-- AGC -->
    <widget source="session.FrontendStatus" render="RaedQuickWatches" position="1333,1056" size="667,600" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">AGC_ANALOG</convert>
    </widget>
  <eLabel name="agc" text="AGC:" position="1704,1292" size="200,60" font="{0};47" halign="right" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2"/>
  <widget source="session.FrontendStatus" render="Label" position="1912,1292" size="200,60" font="{0};47" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <!--Picon-->
    <ePixmap position="271,667" size="333,200" zPosition="2" pixmap="{1}/images/analog/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="277,673" size="320,187" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
    <ePixmap position="823,667" size="333,200" zPosition="2" pixmap="{1}/images/analog/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="829,673" zPosition="5" size="320,187" alphatest="blend" >
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
    <ePixmap position="1387,667" size="333,200" zPosition="2" pixmap="{1}/images/analog/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="1393,673" size="320,187" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <ePixmap position="1944,667" size="333,200" zPosition="2" pixmap="{1}/images/analog/UHD/frame_of_picon3c.png" transparent="1" alphatest="blend"/>
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="emu" position="1951,673" size="320,187" transparent="1" alphatest="blend" zPosition="3" />
    <ePixmap position="24,1300" size="133,53" pixmap="{1}/images/CobaltFHD/UHD/exit.png" alphatest="blend"/>
<ePixmap position="24,1239" size="133,53" pixmap="{1}/images/CobaltFHD/UHD/menu.png" alphatest="blend"/>
<widget name="Positioner" position="7,1360" size="767,80" zPosition="10" font="{0};40" backgroundColor="#54111112" foregroundColor="#41ff9900"  transparent="1" valign="center" halign="center"/>
<widget name="Satfinder" position="1787,1360" size="767,80" zPosition="10" font="{0};40" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center"/>
    <widget source="session.CurrentService" render="Label" position="616,959" size="1323,51" zPosition="2" font="{0};43" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};43" foregroundColor="#004f6ef2" halign="left" position="649,885" size="160,51" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};43" halign="left" position="803,885" render="Label" size="267,51" source="session.CurrentService"  transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};43" halign="left" position="1207,885" size="107,51" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="1127,885" size="67,51" font="{0};44" halign="right" backgroundColor="#00000000" transparent="1" >
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="160,959" size="400,53"  foregroundColor="#00389416" zPosition="3" font="{0};43" halign="center"  backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">emuname</convert>
</widget>
<widget source="session.CurrentService" render="FixedLabel" text="{4}" position="1263,885" size="400,51" zPosition="4" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="1263,885" size="400,51" zPosition="5" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="1263,885" size="400,51" zPosition="6" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="1263,885" size="400,51" zPosition="7" font="{0};40" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Net</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel backgroundColor="#00000000" font="{0};43" foregroundColor="#004f6ef2" halign="left" position="1693,885" size="107,51" text="{3}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};43" halign="left" position="1800,885" render="Label" size="107,51" source="session.CurrentService" transparent="1" zPosition="3">
    <convert type="RaedQuickCpuUsage">Total</convert>
 </widget>
   <widget source="session.CurrentService" render="Label" position="115,885" size="477,51" zPosition="2" font="{0};44" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
 </widget>
	<widget source="session.CurrentService" render="Label" position="1948,959" size="459,51" zPosition="2" font="{0};44" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">vtype</convert>
 </widget>
	  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-T" position="2107,885" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="4" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">2,2</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-C" position="2107,885" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="3" foregroundColor="#00bab329">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">1,1</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendInfo" render="FixedLabel" text="DVB-S2" position="2107,885" size="167,47" font="{0};40" backgroundColor="#00000000" transparent="1" halign="left" zPosition="2" foregroundColor="#00389416">
    <convert type="FrontendInfo">TYPE</convert>
    <convert type="ValueRange">0,0</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap"  position="2075,1177" size="67,53" zPosition="1" pixmap="{1}/images/sd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">0,720</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="2075,1177" size="67,53" zPosition="2" pixmap="{1}/images/hd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">721,1980</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Pixmap"  position="2075,1177" size="67,53" zPosition="3" pixmap="{1}/images/uhd_uhd.png" alphatest="blend">
    <convert type="ServiceInfo">VideoWidth</convert>
    <convert type="ValueRange">1921,3840</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_uhd.png" position="2381,1177" size="67,53" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_uhd.png" position="2288,1177" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_uhd.png" position="2288,1177" size="67,53" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget> 
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85)
