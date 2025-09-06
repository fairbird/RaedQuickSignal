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
#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------1--------------------------------------------------------

### SKIN_setup
if DreamOS():
      SKIN_setup = """
<screen name="RaedQuickSignal_setup" position="0,0" size="1920,1080" title="RAED's RaedQuickSignal setup" flags="wfNoBorder" backgroundColor="#16000000">
  <widget source="Title" position="269,35" size="1210,65" render="Label" font="{0};50" foregroundColor="#ffa500" backgroundColor="#16000000" transparent="1" halign="center" />
  <widget source="session.VideoPicture" render="Pig" position="1037,158" size="827,437" backgroundColor="transparent" zPosition="1" />
  <eLabel text="Background of VideoPicture" foregroundColor="#ffffff" backgroundColor="#ffffff" size="842,452" position="1030,150" zPosition="-10" />
  <widget source="global.CurrentTime" font="{0};55" foregroundColor="#ffffff" backgroundColor="#16000000" halign="center" position="1565,3" render="Label" size="353,84" transparent="1" valign="center" zPosition="5">
    <convert type="ClockToText">Default</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1565,78" size="353,65" font="{0};50" halign="center" foregroundColor="#ffffff" backgroundColor="#16000000" transparent="1" zPosition="6">
    <convert type="ClockToText">Format:%d.%m.%Y</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1030,601" zPosition="1" size="842,68" font="{0};34" halign="center" foregroundColor="#ff2525" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="ServiceName">Name</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="1030,661" zPosition="2" size="842,68" font="{0};32" halign="center" foregroundColor="yellow" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="EventName">Name</convert>
  </widget>
  <widget name="config" position="25,130" size="981,690" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" /><widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1312,933" size="300,80" alphatest="on" scale="1" zPosition="4" />
  <widget source="key_red" render="Label" position="1,1030" zPosition="2" size="381,34" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="transponderinfo" transparent="1" />
  <widget source="key_green" render="Label" position="544,1030" zPosition="2" size="381,34" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="transponderinfo" transparent="1" />
  <widget source="key_yellow" render="Label" position="1074,1030" zPosition="2" size="381,34" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="transponderinfo" transparent="1" />
  <widget source="key_blue" render="Label" position="1534,1030" zPosition="2" size="381,34" font="{0};25" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="transponderinfo" transparent="1" />
  <ePixmap position="68,1070" zPosition="1" size="250,4" pixmap="{1}/images/red.png" alphatest="blend" />
  <ePixmap position="605,1070" zPosition="1" size="250,4" pixmap="{1}/images/green.png" alphatest="blend" />
  <ePixmap position="1137,1070" zPosition="1" size="250,4" pixmap="{1}/images/yellow.png" alphatest="blend" />
  <ePixmap position="1599,1070" zPosition="1" size="250,4" pixmap="{1}/images/blue.png" alphatest="blend" />
  <widget source="help" render="Label" position="25,816" size="1187,199" font="{0};32" foregroundColor="une5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5" />
  <widget name="Picture" position="1259,788" size="400,225" scale="1" zPosition="5" alphatest="blend" />
  <ePixmap position="1360,719" zPosition="3" size="200,200" pixmap="{1}/images/fairbirdfhd.png" alphatest="blend" />
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
else:
#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------2--------------------------------------------------------

      SKIN_setup = """
<screen name="RaedQuickSignal_setup" position="0,0" size="1920,1080" title="RAED's RaedQuickSignal setup" flags="wfNoBorder" backgroundColor="#16000000">
  <widget source="Title" position="269,35" size="1210,65" render="Label" font="{0};50" foregroundColor="#ffa500" backgroundColor="#16000000" transparent="1" halign="center" />
  <widget source="session.VideoPicture" render="Pig" position="1037,158" size="827,437" backgroundColor="transparent" zPosition="1" />
  <eLabel text="Background of VideoPicture" foregroundColor="#ffffff" backgroundColor="#ffffff" size="842,452" position="1030,150" zPosition="-10" />
  <widget source="global.CurrentTime" font="{0};55" foregroundColor="#ffffff" backgroundColor="#16000000" halign="center" position="1565,3" render="Label" size="353,84" transparent="1" valign="center" zPosition="5">
    <convert type="ClockToText">Default</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1565,78" size="353,65" font="{0};50" halign="center" foregroundColor="#ffffff" backgroundColor="#16000000" transparent="1" zPosition="6">
    <convert type="ClockToText">Format:%d.%m.%Y</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1030,601" zPosition="1" size="842,68" font="{0};34" halign="center" foregroundColor="#ff2525" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="ServiceName">Name</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="1030,661" zPosition="2" size="842,68" font="{0};32" halign="center" foregroundColor="yellow" backgroundColor="#16000000" transparent="1" valign="center">
    <convert type="EventName">Name</convert>
  </widget>
  <widget name="config" position="25,130" size="981,690" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="2" font="{0};30" itemHeight="40" /> <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1312,933" size="300,80" alphatest="on" scale="1" zPosition="4" />
  <widget source="key_red" render="Label" position="6,1030" zPosition="2" size="381,34" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="transponderinfo" transparent="1" />
  <widget source="key_green" render="Label" position="544,1030" zPosition="2" size="381,34" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="transponderinfo" transparent="1" />
  <widget source="key_yellow" render="Label" position="1074,1030" zPosition="2" size="381,34" font="{0};30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="transponderinfo" transparent="1" />
  <widget source="key_blue" render="Label" position="1529,1030" zPosition="2" size="381,34" font="{0};25" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="transponderinfo" transparent="1" />
  <ePixmap position="68,1070" zPosition="1" size="250,4" pixmap="{1}/images/red.png" alphatest="blend" />
  <ePixmap position="605,1070" zPosition="1" size="250,4" pixmap="{1}/images/green.png" alphatest="blend" />
  <ePixmap position="1137,1070" zPosition="1" size="250,4" pixmap="{1}/images/yellow.png" alphatest="blend" />
  <ePixmap position="1599,1070" zPosition="1" size="250,4" pixmap="{1}/images/blue.png" alphatest="blend" />
  <widget source="help" render="Label" position="25,816" size="1187,199" font="{0};32" foregroundColor="une5b243" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5" />
  <widget name="Picture" position="1259,788" size="400,225" scale="1" zPosition="5" alphatest="blend" />
  <ePixmap position="1360,719" zPosition="3" size="200,200" pixmap="{1}/images/fairbirdfhd.png" alphatest="blend" />
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_setup2 #------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------3--------------------------------------------------------

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

#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------4--------------------------------------------------------
      SKIN_setup2 = """
<screen backgroundColor="#16000000" name="RaedQuickSignal_setup" position="center,center" size="1050,935" title="RAED's RaedQuickSignal setup" flags="wfNoBorder">
  <eLabel position="0,53" size="1050,1" zPosition="10" backgroundColor="#00ffffff" transparent="0"/>
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bab329" position="30,5" size="981,45" transparent="1" />
  <widget name="config" position="15,60" size="1015,600" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" font="{0};30" itemHeight="40" />
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

#### Selection Screen#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------5--------------------------------------------------------

SKIN_SelectionScreen = """
<screen name="SelectionScreen" position="center,center" size="738,524" title="Select Options">
        <widget source="list" render="Listbox" position="10,10" size="716,461" scrollbarMode="showOnDemand">
            <convert type="TemplatedMultiContent">
                {
                    "template": [
                        MultiContentEntryText(pos=(85,10), size=(650,50), font=0, text=0),
                        MultiContentEntryPixmapAlphaBlend(pos=(0,0), size=(50,50), png=1)
                    ],
                    "fonts": [gFont("Regular", 35)],
                    "itemHeight": 60
                }
            </convert>
        </widget>
<ePixmap pixmap="%s/images/red.png" position="105,517" size="165,2" alphatest="blend"/>
<ePixmap pixmap="%s/images/green.png" position="482,517" size="165,2" alphatest="blend"/>
<widget name="key_red" position="70,480" zPosition="1" size="246,40" font="Regular;35" halign="center" valign="right" foregroundColor="#00ffffff" backgroundColor="#ff1f771f" transparent="1"/>
<widget name="key_green" position="445,480" zPosition="1" size="246,40" font="Regular;35" halign="center" valign="right" foregroundColor="#00ffffff" backgroundColor="#ff9f1313" transparent="1"/>
</screen>
""" % (resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal'), resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal'))

### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------6--------------------------------------------------------

if DreamOS():
      SKIN_Picons = """
<screen name="PiconsScreen" backgroundColor="#30000000" position="center,center" size="1120,469" title="RAED's RaedQuickSignal Picons setup" flags="wfNoBorder">
  <eLabel position="0,63" size="1120,1" zPosition="10" backgroundColor="#ffffff" />
  <widget source="Title" render="Label" font="{0};35" foregroundColor="yellow" position="90,12" size="1028,45" transparent="1" />
  <widget name="menu" position="15,70" size="662,285" foregroundColor="#00ffffff" backgroundColor="#16000000" foregroundColorSelected="#00000000" backgroundColorSelected="#00ffffff" scrollbarMode="showOnDemand" transparent="1" zPosition="1" itemCornerRadius="13" />
  <eLabel text="{1}" position="29,370" size="1072,38" font="{0};32" foregroundColor="#ff2525" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5" />
  <eLabel text="{2}" position="29,415" size="1072,38" font="{0};32" foregroundColor="yellow" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5" />
  <ePixmap position="12,2" zPosition="30" size="70,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" />
 <widget name="Picture" position="698,97" size="400,225" zPosition="5" alphatest="blend" />
</screen>
""".format(FontName, title75, title76)
else:
#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------7--------------------------------------------------------

      SKIN_Picons = """
<screen name="PiconsScreen" backgroundColor="#30000000" position="center,center" size="1120,469" title="RAED's RaedQuickSignal Picons setup" flags="wfNoBorder" zPosition="100">
  <eLabel position="0,63" size="1120,1" zPosition="10" backgroundColor="#ffffff" />
  <widget source="Title" render="Label" font="{0};35" foregroundColor="yellow" position="90,12" size="1028,45" transparent="1" />
  <widget name="menu" position="25,70" size="662,285" font="{0};35" itemHeight="45" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#00000000" backgroundColorSelected="#00ffffff" scrollbarMode="showOnDemand" transparent="1" zPosition="1" itemCornerRadius="13" />
  <eLabel text="{1}" position="31,370" size="1072,38" font="{0};32" foregroundColor="#ff2525" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5" />
  <eLabel text="{2}" position="31,415" size="1072,38" font="{0};32" foregroundColor="yellow" backgroundColor="#16000000" valign="center" halign="center" transparent="1" zPosition="5" />
  <ePixmap position="12,2" zPosition="30" size="70,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" />
<widget name="Picture" position="703,102" size="400,225" zPosition="5" alphatest="blend" />
</screen>
""".format(FontName, title75, title76)

### SKIN_WeatherLocation  #------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------8--------------------------------------------------------

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

### SKIN_AGC_Picon  ### SKIN_Picons#--1----------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------9--------------------------------------------------------


SKIN_AGC_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" cornerRadius="35" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="25,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">AGC</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
  <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Picon -->
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="336,619" size="200,120" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="340,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="542,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="748,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="753,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="953,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="958,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
    <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Picons#------2------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------10--------------------------------------------------------

SKIN_AGC_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" cornerRadius="35" zPosition="1" flags="wfNoBorder">
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">AGC</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
    <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
 <widget source="global.CurrentTime" render="Label" position="1150,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
 <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="20,5" size="400,40" transparent="1" />
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Picon -->
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="336,619" size="200,120" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="340,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="542,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="748,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="753,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="953,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="958,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
    <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Event_Des ### SKIN_Picons#-2-----------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------11--------------------------------------------------------


SKIN_AGC_Event_Des_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Event_Des" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
 <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="25,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">AGC</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
    <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
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
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,612" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
  <widget name="Positioner" position="10,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Picons#--2----------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------12--------------------------------------------------------

SKIN_AGC_Event_Des_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Event_Des" position="230,205" size="1500,750" title="RAED's Quick Signal Info" cornerRadius="35" zPosition="1" flags="wfNoBorder">
 <widget source="Title" render="Label" font="{0};35" foregroundColor="#00bbbbbb" position="25,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">AGC</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
    <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
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
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
     <widget name="Satfinder" position="980,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Weather ### SKIN_Picons#-----3-------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------13--------------------------------------------------------

SKIN_AGC_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" cornerRadius="35" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="20,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">AGC</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
    <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
 <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Weather -->
  <!-- Today -->
  <widget source="session.CurrentService" render="Label" position="431,659" size="241,32" font="{0}; 27" zPosition="3" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Day</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,635" size="100,100" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">Picon</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="426,696" size="400,40" font="{0}; 30" zPosition="3" halign="left" valign="center" foregroundColor="#f37104" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Location</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="430,616" size="170,40" font="{0}; 40" zPosition="3" halign="left" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Temp</convert>
  </widget>
  <ePixmap position="805,694" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_fhd.png" />
  <widget source="session.CurrentService" render="Label" position="653,693" size="147,50" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Windspeed</convert>
  </widget>
  <ePixmap position="805,632" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_fhd.png" scale="1" />
  <widget source="session.CurrentService" render="Label" position="652,631" size="147,50" font="{0}; 35" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Humidity</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/risefhd.png" position="865,628" size="130,60" zPosition="2" />
  <widget source="session.CurrentService" render="Label" position="865,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setfhd.png" position="1009,628" size="130,60" zPosition="2" />
  <widget source="session.CurrentService" render="Label" position="1010,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,616" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,616" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,616" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,616" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1151,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1151,683" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="20,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Picons#---3---------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------14--------------------------------------------------------

SKIN_AGC_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" cornerRadius="35" flags="wfNoBorder">
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="20,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">AGC</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
    <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
 <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Weather -->
  <!-- Today -->
  <widget source="session.CurrentService" render="Label" position="431,659" size="241,32" font="{0}; 27" zPosition="3" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Day</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,635" size="100,100" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">Picon</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="426,696" size="400,40" font="{0}; 30" zPosition="3" halign="left" valign="center" foregroundColor="#f37104" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Location</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="430,616" size="170,40" font="{0}; 40" zPosition="3" halign="left" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Temp</convert>
  </widget>
  <ePixmap position="805,694" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_fhd.png" />
  <widget source="session.CurrentService" render="Label" position="653,693" size="147,50" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Windspeed</convert>
  </widget>
  <ePixmap position="805,632" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_fhd.png" scale="1" />
  <widget source="session.CurrentService" render="Label" position="652,631" size="147,50" font="{0}; 35" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Humidity</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/risefhd.png" position="865,628" size="130,60" zPosition="2" />
  <widget source="session.CurrentService" render="Label" position="865,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setfhd.png" position="1009,628" size="130,60" zPosition="2" />
  <widget source="session.CurrentService" render="Label" position="1010,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,616" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,616" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,616" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,616" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1151,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1151,683" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="20,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Picon  ### SKIN_Picons#---4-----------------------------------ksa----------------skin author:By BO-HLALA.FHD--.. ^_^ ------15--------------------------------------------------------


SKIN_Event_Progress_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="15,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" transparent="1">
  <convert type="EventTime">Progress</convert>
</widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="black1" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
   <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
 <!-- Picon -->
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="336,619" size="200,120" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="340,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="542,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="748,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="753,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="953,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="958,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)
### SKIN_Picons#--------4----------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------16--------------------------------------------------------

SKIN_Event_Progress_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="15,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" transparent="1">
  <convert type="EventTime">Progress</convert>
</widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="black1" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
  <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
 <!-- Picon -->
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="336,619" size="200,120" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="340,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="542,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="748,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="753,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="953,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="958,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Event_Des ### SKIN_Picons#-----5-------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------17--------------------------------------------------------

SKIN_Event_Progress_Event_Des_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="20,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" transparent="1">
  <convert type="EventTime">Progress</convert>
</widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="black1" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
    <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
 <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="{0}; 28" halign="center" foregroundColor="#bbbbbb" backgroundColor="#54111112" transparent="1">
    <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)
### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------19--------------------------------------------------------

SKIN_Event_Progress_Event_Des_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="20,5" size="700,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" transparent="1">
  <convert type="EventTime">Progress</convert>
</widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="black1" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
    <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="{0}; 28" halign="center" foregroundColor="#bbbbbb" backgroundColor="#54111112" transparent="1">
    <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Weather   ### SKIN_Picons#---6---------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------20--------------------------------------------------------

SKIN_Event_Progress_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#bbbbbb" position="25,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" transparent="1">
  <convert type="EventTime">Progress</convert>
</widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="black1" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
    <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Weather -->
  <!-- Today -->
  <widget source="session.CurrentService" render="Label" position="434,663" size="241,32" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Day</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">Picon</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="424,701" size="400,40" font="{0}; 30" zPosition="3" halign="left" valign="center" foregroundColor="#f37104" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Location</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="430,616" size="170,40" font="{0}; 40" zPosition="3" halign="left" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1">
  <convert type="RaedQuickWeather">Temp</convert>
</widget>
  <ePixmap position="812,694" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_fhd.png" scale="1" />
  <widget source="session.CurrentService" render="Label" position="657,693" size="147,50" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Windspeed</convert>
  </widget>
  <ePixmap position="810,625" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_fhd.png" scale="1" />
  <widget source="session.CurrentService" render="Label" position="657,631" size="147,50" font="{0}; 35" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Humidity</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/risefhd.png" position="870,628" size="130,60" zPosition="2" />
  <widget source="session.CurrentService" render="Label" position="872,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setfhd.png" position="1013,628" size="130,60" zPosition="2" />
  <widget source="session.CurrentService" render="Label" position="1015,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
 <!-- Icons VideoWidth  -->
   <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget> 
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Picons#--------7----------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------21--------------------------------------------------------

SKIN_Event_Progress_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="20,5" size="600,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
  <convert type="FrontendInfo">SNR</convert>
</widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" transparent="1">
  <convert type="EventTime">Progress</convert>
</widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="black1" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
    <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1206,390" size="270,70" alphatest="on" scale="1" zPosition="99" />
    <ePixmap position="22,333" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
   <!-- Weather -->
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Today -->
  <widget source="session.CurrentService" render="Label" position="434,663" size="241,32" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Day</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">Picon</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="424,701" size="400,40" font="{0}; 30" zPosition="3" halign="left" valign="center" foregroundColor="#f37104" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Location</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="430,616" size="170,40" font="{0}; 40" zPosition="3" halign="left" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Temp</convert>
  </widget>
  <ePixmap position="812,694" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/wind_fhd.png" scale="1" />
  <widget source="session.CurrentService" render="Label" position="657,693" size="147,50" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Windspeed</convert>
  </widget>
  <ePixmap position="810,625" size="50,50" zPosition="4" alphatest="blend" pixmap="{1}/PICONS/weather/humd_fhd.png" scale="1" />
  <widget source="session.CurrentService" render="Label" position="657,631" size="147,50" font="{0}; 35" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Humidity</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/risefhd.png" position="870,628" size="130,60" zPosition="2" />
  <widget source="session.CurrentService" render="Label" position="872,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="{1}/PICONS/weather/setfhd.png" position="1013,628" size="130,60" zPosition="2" />
  <widget source="session.CurrentService" render="Label" position="1015,699" size="130,35" font="{0};32" zPosition="3" halign="center" valign="center" foregroundColor="#deff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,618" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_AGC_Picon_media### SKIN_Picons#-----------------------------X-------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------22--------------------------------------------------------

SKIN_AGC_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="20,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1150,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Picon -->
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="336,619" size="200,120" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="340,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="542,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="748,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="753,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="953,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="958,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)
### SKIN_Picons#--------------------------------X----------------------skin author:By BO-HLALA.FHD--.. ^_^ ------23--------------------------------------------------------

SKIN_AGC_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
   <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="20,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1150,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Picon -->
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="336,619" size="200,120" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="340,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="542,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="748,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="753,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="953,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="958,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,611" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Event_Progress_Picon_media   ### SKIN_Picons#--------------X----------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------24--------------------------------------------------------

SKIN_Event_Progress_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="15,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" transparent="1">
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="black1" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Picon -->
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="336,619" size="200,120" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="340,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="542,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="748,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="753,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="953,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="958,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Picons#------------------------------X------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------25--------------------------------------------------------

SKIN_Event_Progress_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="35">
   <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="15,5" size="500,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1145,5" size="338,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>  
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="{0}; 35" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="{1}/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="{0}; 35" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="{1}/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" transparent="1">
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="{0};35" valign="center" backgroundColor="black1" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1219,515" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="right">
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
  <ePixmap position="1425,565" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="1433,508" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Picon -->
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="336,619" size="200,120" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="340,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="542,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="748,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="753,624" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="953,619" size="200,120" zPosition="-5" transparent="1" alphatest="blend" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="958,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="7,613" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="985,469" size="500,32" zPosition="1" font="{0};28" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget name="Positioner" position="15,469" size="500,32" zPosition="1" font="{0};28" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), NUMBERS)

### SKIN_Full_Screen### SKIN_Picons#-----12-------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------26--------------------------------------------------------
SKIN_Full_Screen1 = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="30,7" size="1860,75" backgroundColor="#16000000" transparent="1" zPosition="2" font="{0};45" valign="center" halign="left" />
  <widget source="global.CurrentTime" render="Label" position="1665,15" size="225,41" backgroundColor="#16000000" transparent="1" zPosition="10" font="{0};36" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1340,58" size="550,43" backgroundColor="#16000000" transparent="1" zPosition="10" font="{0} 26" valign="center" halign="right">
  <convert type="ClockToText">Date</convert>
</widget> 
 <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="541,652" size="1319,131" font="{0}; 60" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="539,547" size="355,97" font="{0}; 55" backgroundColor="#54111112" foregroundColor="#ff00" transparent="1" halign="right" />
  <widget source="session.CurrentService" render="Label" position="906,542" size="950,97" font="{0}; 55" backgroundColor="#54111112" foregroundColor="#ff00" transparent="1" halign="left">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="541,801" size="1319,131" font="{0}; 55" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="541,944" size="1319,131" font="{0}; 50" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="30,415" size="450,112" halign="left" valign="center" transparent="1" font="{0};108" zPosition="9">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
<widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,165" size="1860,75" borderWidth="1" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR:" position="37,165" size="150,75" valign="center" foregroundColor="#ffffff" backgroundColor="#00000000" transparent="1" font="{0};52" />
  <widget source="session.FrontendStatus" render="Label" position="1552,165" size="330,75" halign="right" valign="center" transparent="1" font="{0};52" zPosition="9">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,255" size="1860,75" borderWidth="1" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="AGC:" position="37,255" size="150,75" valign="center" foregroundColor="#ffffff" backgroundColor="#00000000" transparent="1" font="{0};52" zPosition="9" />
  <widget source="session.FrontendStatus" render="Label" position="1552,255" size="330,75" halign="right" valign="center" transparent="1" font="{0};52" zPosition="9">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="SNR:" position="30,350" size="470,56" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};45" halign="left" />
  <widget source="session.FrontendStatus" render="Label" position="841,336" size="470,112" font="{0};108" halign="left" backgroundColor="#101010" transparent="1" foregroundColor="#ff0000">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <eLabel text="AGC:" position="30,544" size="470,56" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};45" halign="left" />
  <widget source="session.FrontendStatus" render="Label" position="30,610" size="450,112" backgroundColor="#16000000" transparent="1" font="{0};108" halign="left">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="BER:" position="30,745" size="470,56" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};45" halign="left" />
  <widget source="session.FrontendStatus" render="Label" position="30,810" size="450,112" font="{0};108" halign="left" backgroundColor="#16000000" transparent="1" foregroundColor="#ff0000">
    <convert type="FrontendInfo">BER</convert>
  </widget>
  <widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="30,940" size="465,135" font="{0};108" halign="left" foregroundColor="#ee00" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">LOCK</convert>
    <convert type="ConditionalShowHide" />
  </widget>
<ePixmap position="1836,959" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
<ePixmap position="1821,1016" size="75,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" scale="1" />
<eLabel text="SNRdB:" position="544,374" size="290,54" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};45" halign="right" />
 <eLabel text="Channel number:" position="534,480" size="390,54" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};45" halign="right" />
<widget name="Positioner" position="31,107" size="700,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  <widget name="Satfinder" position="1182,107" size="700,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="850,76" size="300,80" alphatest="on" scale="1" zPosition="99" />
<widget source="session.CurrentService" render="ChannelNumber" position="929,482" size="158,50" font="{0};40" foregroundColor="#fec000" backgroundColor="transpBlack" valign="center" halign="Left" transparent="1" zPosition="9" />
<!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="1095,482" size="95,50" font="Bold;45" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="1095,482" size="95,50" shadowOffset="4,3" font="Bold;45" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="1095,482" size="95,50" font="Bold;45" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="1095,482" size="95,50" font="Bold;45" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="1197,482" size="95,50" font="Bold;45" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="1197,482" size="95,50" font="Bold;45" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
  </widget>
  <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};45" position="1303,482" size="183,50" halign="right" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};45" position="1493,482" size="19,50" halign="center" foregroundColor="#8cec" backgroundColor="#54111112" transparent="1" />
  <widget source="session.CurrentService" render="Label" font="{0};45" position="1520,482" size="183,50" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoHeight</convert>
  </widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------27--------------------------------------------------------

SKIN_Full_Screen2_SNRdB = """
<screen backgroundColor="#ccffffff" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="16,10" size="1860,50" foregroundColor="#00000000" backgroundColor="black1" transparent="1" zPosition="1" font="{0};35" valign="center" halign="left" />
  <widget source="global.CurrentTime" render="Label" position="1665,22" size="225,37" foregroundColor="#00000000" backgroundColor="black1" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
  <convert type="ClockToText">Format:%-H:%M</convert>
</widget>
  <widget source="global.CurrentTime" render="Label" position="1440,52" size="450,37" foregroundColor="#00000000" backgroundColor="black1" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
    <convert type="ClockToText">Date</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="19,922" size="1880,65" font="{0}; 50" halign="center" backgroundColor="#64c7" foregroundColor="#64c7" transparent="1" zPosition="10">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="19,1006" size="1880,65" font="{0}; 50" halign="center" backgroundColor="#64c7" foregroundColor="#64c7" transparent="1" zPosition="10">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,915" size="1860,75" borderWidth="1" borderColor="#808888" transparent="0">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR:" position="37,915" size="150,75" valign="center" foregroundColor="#ffffff" backgroundColor="black1" transparent="1" font="{0};50" zPosition="11" borderWidth="1" borderColor="black1" />
  <widget source="session.FrontendStatus" render="Label" position="1552,915" size="330,75" halign="right" valign="center" transparent="1" font="{0};52" zPosition="11" borderWidth="2" borderColor="#101010">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,1000" size="1860,75" borderWidth="1" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="0">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
  <eLabel text="AGC:" position="37,1000" size="150,75" valign="center" foregroundColor="#ffffff" backgroundColor="black1" transparent="1" font="{0};50" zPosition="11" borderWidth="1" borderColor="black1" />
  <widget source="session.FrontendStatus" render="Label" position="1552,1000" size="330,75" halign="right" valign="center" transparent="1" font="{0};52" zPosition="11" borderWidth="2" borderColor="#101010">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1552,840" size="330,80" font="{0};70" halign="right" foregroundColor="#ff2525" backgroundColor="#ff2525" transparent="1" borderWidth="2" borderColor="#101010">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <widget name="Positioner" position="607,12" size="400,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#ccffffff" foregroundColor="#ff2525" transparent="1" />
  <widget name="Satfinder" position="1033,12" size="400,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#ccffffff" foregroundColor="#80ff" transparent="1" />
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))
### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------28--------------------------------------------------------

SKIN_Full_Screen2_NOSNRdB = """
<screen backgroundColor="#ccffffff" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="16,10" size="1860,50" foregroundColor="#00000000" backgroundColor="black1" transparent="1" zPosition="1" font="{0};35" valign="center" halign="left" />
  <widget source="global.CurrentTime" render="Label" position="1665,22" size="225,37" foregroundColor="#00000000" backgroundColor="black1" transparent="1" zPosition="1" font="{0};36" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1440,52" size="450,37" foregroundColor="#101010" backgroundColor="black1" transparent="1" zPosition="1" font="{0};24" valign="center" halign="right">
    <convert type="ClockToText">Date</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="19,922" size="1880,65" font="{0}; 50" halign="center" backgroundColor="#64c7" foregroundColor="#64c7" transparent="1" zPosition="10">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="19,1006" size="1880,65" font="{0}; 50" halign="center" backgroundColor="#64c7" foregroundColor="#64c7" transparent="1" zPosition="10">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,915" size="1860,75" borderWidth="1" borderColor="#808888">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR:" position="37,915" size="150,75" valign="center" foregroundColor="#ffffff" backgroundColor="black1" transparent="1" font="{0};52" zPosition="11" borderWidth="1" borderColor="black1" />
  <widget source="session.FrontendStatus" render="Label" position="1552,915" size="330,75" halign="right" valign="center" transparent="1" font="{0};52" zPosition="11" borderWidth="2" borderColor="#101010">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="30,1000" size="1860,75" borderWidth="1" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" borderColor="#656565" transparent="0">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
  <eLabel text="AGC:" position="37,1000" size="150,75" valign="center" foregroundColor="#ffffff" backgroundColor="black1" transparent="1" font="{0};52" zPosition="11" borderWidth="1" borderColor="black1" />
  <widget source="session.FrontendStatus" render="Label" position="1552,1000" size="330,75" halign="right" valign="center" transparent="1" font="{0};52" zPosition="11" borderWidth="2" borderColor="#101010">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget name="Positioner" position="622,12" size="400,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#ccffffff" foregroundColor="#ff2525" transparent="1" />
  <widget name="Satfinder" position="1058,12" size="400,50" zPosition="1" font="{0};35" halign="center" backgroundColor="#ccffffff" foregroundColor="#80ff" transparent="1" />
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Full_Screen_Picons   ### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------29--------------------------------------------------------

SKIN_Full_Screen_Picon_Vertical = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="30,7" size="1860,75" backgroundColor="#16000000" transparent="1" zPosition="-1" font="{0};35" valign="center" halign="center" />
  <widget source="global.CurrentTime" render="Label" position="1664,13" size="225,41" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};39" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="29,13" size="490,41" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};30" valign="center" halign="left">
    <convert type="ClockToText">Date</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <eLabel position="center,90" size="1920,2" backgroundColor="#16000000" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="312,405" size="1300,100" font="{0};60" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="784,284" size="315,97" font="{0};38" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center" />
  <widget source="session.CurrentService" render="Label" position="1038,284" size="570,97" font="{0};50" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="312,504" size="1300,100" font="{0};55" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="312,601" size="1300,100" font="{0};50" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <eLabel position="312,704" size="1300,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="312,795" size="1300,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="312,883" size="1300,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="312,709" size="1300,85" font="{0};36" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1388,709" size="220,85" font="{0};36" zPosition="2" backgroundColor="#16000000" foregroundColor="#ee00" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="312,798" size="1300,85" font="{0};27" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="5,170" size="300,833" pixmap="{1}/images/icons_quick/icon_snr-scan5.png" scale="1" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR" position="5,1004" size="300,75" valign="center" foregroundColor="#00bbbbbb" backgroundColor="#16000000" transparent="1" font="{0};52" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="5,94" size="300,75" halign="center" valign="center" transparent="1" font="{0};52" foregroundColor="#e5e5e5">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="1617,170" size="300,833" pixmap="{1}/images/icons_quick/icon_snr-scan5.png" scale="1" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="AGC" position="1617,1004" size="300,75" valign="center" foregroundColor="#00bbbbbb" backgroundColor="#16000000" transparent="1" font="{0};52" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="1617,94" size="300,75" halign="center" valign="center" transparent="1" font="{0};52" foregroundColor="#e5e5e5">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="SNRdB" position="395,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="312,150" size="450,112" font="{0};108" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <eLabel text="AGC" position="835,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="740,150" size="450,112" backgroundColor="#16000000" transparent="1" font="{0};108" halign="center">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="BER" position="1261,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="1163,150" size="450,112" font="{0};108" backgroundColor="#16000000" transparent="1" halign="center" foregroundColor="#ff0000">
    <convert type="FrontendInfo">BER</convert>
  </widget>
  <widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="335,306" size="388,108" font="{0};75" foregroundColor="#ee00" backgroundColor="#16000000" transparent="1" halign="left">
    <convert type="FrontendInfo">LOCK</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget name="Positioner" position="313,1040" size="800,34" zPosition="1" font="{0};27" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  <widget name="Satfinder" position="812,1041" size="800,34" zPosition="1" font="{0};27" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <!-- Picon -->
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="354,890" size="250,150" zPosition="3" alphatest="blend" scale="1" cornerRadius="20">
  <convert type="RaedQuickServName2">Reference</convert>
</widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="655,890" size="250,150" zPosition="3" alphatest="blend" scale="1" cornerRadius="20">
  <convert type="RaedQuickServName2">Provider</convert>
</widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1009,890" size="250,150" zPosition="3" alphatest="blend" scale="1" cornerRadius="20">
  <convert type="RaedQuickServName2">OrbitalPos</convert>
</widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1305,890" size="250,150" transparent="1" alphatest="blend" zPosition="3" scale="1" cornerRadius="20" />
  <ePixmap position="928,1013" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="936,959" size="48,48" zPosition="49" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
 <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="614,353" size="120,47" font="Bold;45" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="right" transparent="1" zPosition="300" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="614,353" size="120,47" shadowOffset="4,3" font="Bold;45" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="right" transparent="1" zPosition="300" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="614,353" size="120,47" font="Bold;45" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="right" transparent="1" zPosition="300" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="614,353" size="120,47" font="Bold;45" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="right" transparent="1" zPosition="300" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
 <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};45" position="743,352" size="143,50" halign="right" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};45" position="895,352" size="19,50" halign="center" foregroundColor="#8cec" backgroundColor="#54111112" transparent="1" />
  <widget source="session.CurrentService" render="Label" font="{0};45" position="921,352" size="143,50" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
  <convert type="ServiceInfo">VideoHeight</convert>
</widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------30--------------------------------------------------------

SKIN_Full_Screen_Picon_media_Vertical = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" position="30,7" size="1860,75" backgroundColor="#16000000" transparent="1" zPosition="-1" font="{0};35" valign="center" halign="center" />
  <widget source="global.CurrentTime" render="Label" position="1664,13" size="225,41" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};39" valign="center" halign="right">
    <convert type="ClockToText">Format:%-H:%M</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="29,13" size="490,41" backgroundColor="#16000000" transparent="1" zPosition="1" font="{0};30" valign="center" halign="left">
    <convert type="ClockToText">Date</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <eLabel position="center,90" size="1920,2" backgroundColor="#16000000" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="312,405" size="1300,100" font="{0};60" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="784,284" size="315,97" font="{0};38" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center" />
  <widget source="session.CurrentService" render="Label" position="1038,284" size="570,97" font="{0};50" backgroundColor="#54111112" foregroundColor="#3c9dff" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="312,504" size="1300,100" font="{0};55" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="312,601" size="1300,100" font="{0};50" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <eLabel position="312,704" size="1300,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="312,795" size="1300,2" backgroundColor="#bbbbbb" zPosition="4" />
  <eLabel position="312,883" size="1300,2" backgroundColor="#bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="312,709" size="1300,85" font="{0};36" zPosition="2" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1388,709" size="220,85" font="{0};36" zPosition="2" backgroundColor="#16000000" foregroundColor="#ee00" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="312,798" size="1300,85" font="{0};27" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="5,170" size="300,833" pixmap="{1}/images/icons_quick/icon_snr-scan5.png" scale="1" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <eLabel text="SNR" position="5,1004" size="300,75" valign="center" foregroundColor="#00bbbbbb" backgroundColor="#16000000" transparent="1" font="{0};52" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="5,94" size="300,75" halign="center" valign="center" transparent="1" font="{0};52" foregroundColor="#e5e5e5">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="1617,170" size="300,833" pixmap="{1}/images/icons_quick/icon_snr-scan5.png" scale="1" zPosition="4" backgroundColor="#16000000" borderWidth="4" borderColor="#656565" orientation="orBottomToTop">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="AGC" position="1617,1004" size="300,75" valign="center" foregroundColor="#00bbbbbb" backgroundColor="#16000000" transparent="1" font="{0};52" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="1617,94" size="300,75" halign="center" valign="center" transparent="1" font="{0};52" foregroundColor="#e5e5e5">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="SNRdB" position="395,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="312,150" size="450,112" font="{0};108" backgroundColor="#16000000" transparent="1" halign="center">
    <convert type="FrontendInfo">SNRdB</convert>
  </widget>
  <eLabel text="AGC" position="835,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="740,150" size="450,112" backgroundColor="#16000000" transparent="1" font="{0};108" halign="center">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel text="BER" position="1261,95" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="{0};35" halign="center" />
  <widget source="session.FrontendStatus" render="Label" position="1163,150" size="450,112" font="{0};108" backgroundColor="#16000000" transparent="1" halign="center" foregroundColor="#ff0000">
    <convert type="FrontendInfo">BER</convert>
  </widget>
  <widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="335,306" size="388,108" font="{0};75" foregroundColor="#ee00" backgroundColor="#16000000" transparent="1" halign="left">
    <convert type="FrontendInfo">LOCK</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget name="Positioner" position="313,1040" size="800,34" zPosition="1" font="{0};27" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" />
  <widget name="Satfinder" position="812,1041" size="800,34" zPosition="1" font="{0};27" halign="right" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" />
  <!-- Picon -->
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="354,890" size="250,150" zPosition="3" alphatest="blend" scale="1" cornerRadius="20">
  <convert type="RaedQuickServName2">Reference</convert>
</widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="655,890" size="250,150" zPosition="3" alphatest="blend" scale="1" cornerRadius="20">
  <convert type="RaedQuickServName2">Provider</convert>
</widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1009,890" size="250,150" zPosition="3" alphatest="blend" scale="1" cornerRadius="20">
  <convert type="RaedQuickServName2">OrbitalPos</convert>
</widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1305,890" size="250,150" transparent="1" alphatest="blend" zPosition="3" scale="1" cornerRadius="20" />
  <ePixmap position="928,1013" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
  <ePixmap position="936,959" size="48,48" zPosition="49" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
 <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="614,353" size="120,47" font="Bold;45" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="right" transparent="1" zPosition="300" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="614,353" size="120,47" shadowOffset="4,3" font="Bold;45" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="right" transparent="1" zPosition="300" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="614,353" size="120,47" font="Bold;45" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="right" transparent="1" zPosition="300" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="614,353" size="120,47" font="Bold;45" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="right" transparent="1" zPosition="300" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
 <!-- Test VideoWidth  -->
  <widget source="session.CurrentService" render="Label" font="{0};45" position="743,352" size="143,50" halign="right" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
    <convert type="ServiceInfo">VideoWidth</convert>
  </widget>
  <eLabel text="x" font="{0};45" position="895,352" size="19,50" halign="center" foregroundColor="#8cec" backgroundColor="#54111112" transparent="1" />
  <widget source="session.CurrentService" render="Label" font="{0};45" position="921,352" size="143,50" foregroundColor="#ff00" backgroundColor="#54111112" transparent="1">
  <convert type="ServiceInfo">VideoHeight</convert>
</widget>
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"))

### SKIN_Full_Screen_Picons_ECM      ### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------31--------------------------------------------------------

SKIN_Full_Screen_Picon_Ecm1_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" flags="wfNoBorder">
  <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/ArmyTouch/FHD/frame_base-fs8.png" />
  <ePixmap position="119,140" size="383,629" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/ind_snr2.png" alphatest="blend" transparent="1" />
  <ePixmap position="1419,140" size="383,629" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/ind_agc2.png" alphatest="blend" transparent="1" />
  <ePixmap position="center,140" size="270,30" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/arrow_quick1.png" alphatest="blend" transparent="1" />
  <ePixmap position="42,942" size="601,122" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" scale="1" alphatest="blend" transparent="1" />
  <ePixmap position="660,942" size="601,122" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" scale="1" alphatest="blend" transparent="1" />
  <ePixmap position="1278,942" size="601,122" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" scale="1" alphatest="blend" transparent="1" />
  <ePixmap position="548,559" size="825,209" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick2.png" alphatest="blend" transparent="1" />
  <ePixmap position="83,780" size="1752,96" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick3.png" alphatest="blend" transparent="1" />
  <ePixmap position="837,268" size="246,78" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick4.png" alphatest="blend" transparent="1" />
  <ePixmap position="596,247" size="729,300" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick5.png" alphatest="blend" transparent="1" />
  <ePixmap position="665,185" size="591,50" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick6.png" alphatest="blend" transparent="1" />
  <ePixmap position="637,17" zPosition="30" size="80,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" />
 <eLabel text="RAEDQuickSignal" position="60,16" size="1800,72" font="{0};54" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="672,186" size="576,44" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
    <convert type="ClockToText">Date</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="663,1015" size="595,45" zPosition="2" font="{0}; 30" halign="center" foregroundColor="#ff00" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="124,192" size="374,507" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="1424,192" size="374,507" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
    <convert type="RaedQuickFrontendInfo2">AGC</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="846,271" size="233,74" zPosition="2" font="{0}; 60" halign="center" foregroundColor="#ff7a00" backgroundColor="#16000000" transparent="1">
    <convert type="ClockToText">Format:%H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="867,137" size="185,44" zPosition="2" font="{0};48" halign="center" foregroundColor="#ff0080" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="234,141" size="150,50" zPosition="2" font="{0};48" halign="center" foregroundColor="#ff0080" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1535,141" size="150,50" zPosition="2" font="{0};48" halign="center" foregroundColor="#ff0080" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="551,565" size="819,203" zPosition="2" font="{0};25" halign="center" valign="top" foregroundColor="#99ff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="663,953" size="592,60" zPosition="2" font="{0};26" halign="center" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1098,897" size="143,45" zPosition="2" font="{0};33" halign="right" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="462,833" size="992,38" zPosition="2" font="{0};27" halign="center" valign="top" foregroundColor="#ff00" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1383,892" size="420,38" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="755,787" size="410,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="bbeyaz" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="755,787" size="410,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="755,787" size="410,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="755,787" size="410,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#ee00" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Net</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Label" position="86,784" size="358,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="86,829" size="358,40" zPosition="2" font="{0};30" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">emuname</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1474,784" size="358,38" zPosition="2" font="{0};38" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">%s</convert>
  </widget>
  <!--Picon-->
  <ePixmap position="827,361" size="267,165" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon2.png" alphatest="blend" transparent="1" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="830,364" size="261,159" zPosition="1" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="617,268" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="620,271" size="186,114" zPosition="2" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="617,406" size="192,120" zPosition="3" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="620,409" size="186,114" zPosition="1" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1112,268" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="1115,271" size="186,114" zPosition="1" alphatest="blend">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
  </widget>
  <ePixmap position="1112,406" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" alphatest="blend" transparent="1" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1115,409" size="186,114" transparent="1" alphatest="blend" zPosition="3" />
  <widget source="session.CurrentService" render="Label" position="45,1010" size="595,48" font="{0};35" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="45,950" size="595,48" font="{0};35" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1281,950" size="595,48" font="{0};30" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1281,1010" size="595,48" font="{0};32" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Positioner" position="60,16" size="575,72" zPosition="10" font="{0};35" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" />
  <widget name="Satfinder" position="1283,16" size="575,72" zPosition="10" font="{0};35" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" valign="center" halign="right" />
   <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#9fcff" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" shadowOffset="4,3" font="Bold;42" foregroundColor="#e5e5e5" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#e5e5e5" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#ffffff" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
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
### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------32--------------------------------------------------------

SKIN_Full_Screen_Picon_media_Ecm1_Vertical = """
<screen name="QuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" flags="wfNoBorder">
  <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/ArmyTouch/FHD/frame_base-fs8.png" />
  <ePixmap position="119,140" size="383,629" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/ind_snr2.png" alphatest="blend" transparent="1" />
  <ePixmap position="1419,140" size="383,629" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/ind_agc2.png" alphatest="blend" transparent="1" />
  <ePixmap position="center,140" size="270,30" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/arrow_quick1.png" alphatest="blend" transparent="1" />
  <ePixmap position="42,942" size="601,122" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" scale="1" alphatest="blend" transparent="1" />
  <ePixmap position="660,942" size="601,122" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" scale="1" alphatest="blend" transparent="1" />
  <ePixmap position="1278,942" size="601,122" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick1.png" scale="1" alphatest="blend" transparent="1" />
  <ePixmap position="548,559" size="825,209" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick2.png" alphatest="blend" transparent="1" />
  <ePixmap position="83,780" size="1752,96" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick3.png" alphatest="blend" transparent="1" />
  <ePixmap position="837,268" size="246,78" zPosition="1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick4.png" alphatest="blend" transparent="1" />
  <ePixmap position="596,247" size="729,300" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick5.png" alphatest="blend" transparent="1" />
  <ePixmap position="665,185" size="591,50" zPosition="-1" pixmap="{1}/images/ArmyTouch/FHD/frame_quick6.png" alphatest="blend" transparent="1" />
  <ePixmap position="637,17" zPosition="30" size="80,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" />
 <eLabel text="RAEDQuickSignal" position="60,16" size="1800,72" font="{0};54" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="672,186" size="576,44" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1">
    <convert type="ClockToText">Date</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="663,1015" size="595,45" zPosition="2" font="{0}; 30" halign="center" foregroundColor="#ff00" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="124,192" size="374,507" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Progress" position="1424,192" size="374,507" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/icon_scale1.png" orientation="orBottomToTop" transparent="1">
    <convert type="RaedQuickFrontendInfo2">AGC</convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="846,271" size="233,74" zPosition="2" font="{0}; 60" halign="center" foregroundColor="#ff7a00" backgroundColor="#16000000" transparent="1">
    <convert type="ClockToText">Format:%H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="867,137" size="185,44" zPosition="2" font="{0};48" halign="center" foregroundColor="#ff0080" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="234,141" size="150,50" zPosition="2" font="{0};48" halign="center" foregroundColor="#ff0080" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1535,141" size="150,50" zPosition="2" font="{0};48" halign="center" foregroundColor="#ff0080" backgroundColor="#16000000" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="551,565" size="819,203" zPosition="2" font="{0};25" halign="center" valign="top" foregroundColor="#99ff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="663,953" size="592,60" zPosition="2" font="{0};26" halign="center" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1098,897" size="143,45" zPosition="2" font="{0};33" halign="right" valign="top" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="462,833" size="992,38" zPosition="2" font="{0};27" halign="center" valign="top" foregroundColor="#ff00" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1383,892" size="420,38" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="755,787" size="410,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="bbeyaz" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="755,787" size="410,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="755,787" size="410,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#fec000" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="755,787" size="410,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#ee00" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Net</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="Label" position="86,784" size="358,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="86,829" size="358,40" zPosition="2" font="{0};30" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">emuname</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1474,784" size="358,38" zPosition="2" font="{0};38" halign="center" valign="top" foregroundColor="#ff00ff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">%s</convert>
  </widget>
  <!--Picon-->
  <ePixmap position="827,361" size="267,165" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon2.png" alphatest="blend" transparent="1" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="830,364" size="261,159" zPosition="1" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="617,268" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="620,271" size="186,114" zPosition="2" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="617,406" size="192,120" zPosition="3" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="620,409" size="186,114" zPosition="1" alphatest="blend">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="1112,268" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="1115,271" size="186,114" zPosition="1" alphatest="blend">
    <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
  </widget>
  <ePixmap position="1112,406" size="192,120" zPosition="2" pixmap="{1}/images/ArmyTouch/FHD/frame_of_picon3s.png" alphatest="blend" transparent="1" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1115,409" size="186,114" transparent="1" alphatest="blend" zPosition="3" />
  <widget source="session.CurrentService" render="Label" position="45,1010" size="595,48" font="{0};35" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="45,950" size="595,48" font="{0};35" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1281,950" size="595,48" font="{0};30" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1281,1010" size="595,48" font="{0};32" halign="center" foregroundColor="#9fcff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Positioner" position="60,16" size="575,72" zPosition="10" font="{0};35" halign="left" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" />
  <widget name="Satfinder" position="1283,16" size="575,72" zPosition="10" font="{0};35" backgroundColor="#54111112" foregroundColor="#deff" transparent="1" valign="center" halign="right" />
   <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#9fcff" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" shadowOffset="4,3" font="Bold;42" foregroundColor="#e5e5e5" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#e5e5e5" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#ffffff" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
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

### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------33--------------------------------------------------------

SKIN_Full_Screen_Picon_Ecm2_Vertical = """
<screen backgroundColor="#ffffffff" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/ShabahNet/FHD/frame_base-fs8.png" />
    <ePixmap position="119,140" size="383,629" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/ind_snr2.png" alphatest="blend" transparent="1" />
    <ePixmap position="1419,140" size="383,629" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/ind_agc2.png" alphatest="blend" transparent="1" />
    <ePixmap position="center,135" size="272,80" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/arrow_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="42,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="660,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="1278,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="548,559" size="825,209" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" scale="1" alphatest="blend" transparent="1" />
    <ePixmap position="83,780" size="1752,96" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick3.png" alphatest="blend" transparent="1" />
    <ePixmap position="837,268" size="246,78" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/frame_quick4.png" alphatest="blend" transparent="1" />
    <ePixmap position="596,247" size="729,300" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick5.png" alphatest="blend" transparent="1" />
    <ePixmap position="665,185" size="591,50" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick6.png" alphatest="blend" transparent="1" />
    <ePixmap position="916,63" zPosition="30" size="80,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" />
    <ePixmap position="890,888" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
    <ePixmap position="974,888" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
    <eLabel text="RAEDQuickSignal" position="60,11" size="1800,72" font="{0};45" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1" />
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
    <widget source="session.CurrentService" render="Label" position="551,565" size="819,203" zPosition="2" font="{0};25" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
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
    <widget source="session.CurrentService" render="Label" position="460,788" size="420,38" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="845,788" size="410,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="845,788" size="410,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="845,788" size="410,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="845,788" size="410,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
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
    <ePixmap position="827,361" size="267,165" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon2.png" alphatest="blend" transparent="1" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="830,364" size="261,159" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="617,268" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="620,271" size="186,114" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="617,406" size="192,120" zPosition="3" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="620,409" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1112,268" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="1115,271" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1112,406" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" alphatest="blend" transparent="1" />
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
    <widget name="Satfinder" position="1283,16" size="575,72" zPosition="10" font="{0};30" backgroundColor="#00ffffff" foregroundColor="#0000deff" transparent="1" valign="center" halign="right" />
 <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#9fcff" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" shadowOffset="4,3" font="Bold;42" foregroundColor="#e5e5e5" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#e5e5e5" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#ffffff" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
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
### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------34--------------------------------------------------------

SKIN_Full_Screen_Picon_media_Ecm2_Vertical = """
<screen backgroundColor="#ffffffff" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/ShabahNet/FHD/frame_base-fs8.png" />
    <ePixmap position="119,140" size="383,629" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/ind_snr2.png" alphatest="blend" transparent="1" />
    <ePixmap position="1419,140" size="383,629" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/ind_agc2.png" alphatest="blend" transparent="1" />
    <ePixmap position="center,135" size="272,80" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/arrow_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="42,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="660,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="1278,947" size="601,108" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="548,559" size="825,209" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" scale="1" alphatest="blend" transparent="1" />
    <ePixmap position="83,780" size="1752,96" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick3.png" alphatest="blend" transparent="1" />
    <ePixmap position="837,268" size="246,78" zPosition="1" pixmap="{1}/images/ShabahNet/FHD/frame_quick4.png" alphatest="blend" transparent="1" />
    <ePixmap position="596,247" size="729,300" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick5.png" alphatest="blend" transparent="1" />
    <ePixmap position="665,185" size="591,50" zPosition="-1" pixmap="{1}/images/ShabahNet/FHD/frame_quick6.png" alphatest="blend" transparent="1" />
    <ePixmap position="916,63" zPosition="30" size="80,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" />
    <ePixmap position="890,888" size="65,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" />
    <ePixmap position="974,888" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
    <eLabel text="RAEDQuickSignal" position="60,11" size="1800,72" font="{0};45" halign="center" valign="center" foregroundColor="#5395c3" backgroundColor="#16000000" transparent="1" />
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
    <widget source="session.CurrentService" render="Label" position="551,565" size="819,203" zPosition="2" font="{0};25" halign="center" valign="top" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
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
    <widget source="session.CurrentService" render="Label" position="460,788" size="420,38" zPosition="2" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickEcmInfo">bitrate</convert>
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{2}" position="845,788" size="410,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{3}" position="845,788" size="410,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="845,788" size="410,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
      <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
      <convert type="ConditionalShowHide" />
    </widget>
    <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="845,788" size="410,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#005395c3" backgroundColor="#16000000" transparent="1">
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
    <ePixmap position="827,361" size="267,165" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon2.png" alphatest="blend" transparent="1" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="830,364" size="261,159" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">Reference</convert>
    </widget>
    <ePixmap position="617,268" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="620,271" size="186,114" zPosition="2" alphatest="blend">
      <convert type="RaedQuickServName2">Provider</convert>
    </widget>
    <ePixmap position="617,406" size="192,120" zPosition="3" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="620,409" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickServName2">OrbitalPos</convert>
    </widget>
    <ePixmap position="1112,268" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" transparent="2" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconCrypt" position="1115,271" size="186,114" zPosition="1" alphatest="blend">
      <convert type="RaedQuickSignalCaidInfo2">CryptInfo2</convert>
    </widget>
    <ePixmap position="1112,406" size="192,120" zPosition="2" pixmap="{1}/images/ShabahNet/FHD/frame_of_picon3s.png" alphatest="blend" transparent="1" />
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
    <widget name="Satfinder" position="1283,16" size="575,72" zPosition="10" font="{0};30" backgroundColor="#00ffffff" foregroundColor="#0000deff" transparent="1" valign="center" halign="right" />
 <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#9fcff" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" shadowOffset="4,3" font="Bold;42" foregroundColor="#e5e5e5" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#e5e5e5" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="1485,831" size="120,40" font="Bold;42" foregroundColor="#ffffff" backgroundColor="#00000000" valign="center" halign="left" transparent="1" zPosition="30" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
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
### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------35--------------------------------------------------------

SKIN_Full_Screen_Picon_Ecm3_Vertical = """
<screen name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/CobaltFHD/FHD/cool1.png" />
    <ePixmap position="119,140" size="257,559" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/agc_snr.png" alphatest="blend" transparent="1" />
    <ePixmap position="1545,140" size="257,559" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/pogoda.png" alphatest="blend" transparent="1" />
    <ePixmap position="67,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="669,847" size="601,139" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" scale="1" alphatest="blend" transparent="1" />
    <ePixmap position="1274,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="573,484" size="794,209" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick2.png" alphatest="blend" transparent="1" />
    <ePixmap position="108,720" size="1752,96" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick3.png" alphatest="blend" transparent="1" />
    <ePixmap position="210,49" zPosition="30" size="80,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" />
    <ePixmap position="919,991" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
    <ePixmap position="596,157" size="729,300" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick5.png" alphatest="blend" transparent="1" />
	<widget source="session.Event_Now" render="Label" position="613,162" size="694,40" font="{0};32" halign="center" backgroundColor="#595959" foregroundColor="#00ffffff" transparent="1" zPosition="1">
      <convert type="EventName">Name</convert>
 </widget>
	<eLabel name="new eLabel" position="646,208" size="628,2" backgroundColor="#004f6ef2" />
	<widget backgroundColor="#16000000" font="{0};27" halign="center" position="612,223" render="Label" size="694,221" source="session.Event_Now" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
 </widget>
	  <widget source="global.CurrentTime" render="Label" position="920,53" size="920,50" font="{0};40" valign="center" halign="right" backgroundColor="#54111112" foregroundColor="#58bcff" transparent="1">
      <convert type="ClockToText">Format:%A  %e  %B  %Y     %H:%M </convert>
	   </widget>
    <widget source="Title" position="135,52" size="800,70" render="Label" font="{0};40" foregroundColor="#58bcff" backgroundColor="#00000000" transparent="1" halign="center" />
    <widget source="session.CurrentService" render="Label" position="683,857" size="568,40" zPosition="2" font="{0};32" halign="center" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
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
    <widget source="session.CurrentService" render="Label" position="585,487" size="765,203" zPosition="2" font="{0};24" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="683,919" size="568,62" zPosition="2" font="{0};26" halign="left" valign="center" foregroundColor="#00fffe9e" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1274,958" size="153,43" zPosition="2" font="{0};30" halign="left" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="462,773" size="992,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="487,728" size="120,38" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="602,728" render="Label" size="200,38" source="session.CurrentService" transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};32" halign="left" position="905,728" size="80,38" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="845,728" size="50,38" font="{0};33" halign="right" backgroundColor="#00000000" transparent="1">
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
  <widget source="session.CurrentService" render="Label" position="120,769" size="300,40" foregroundColor="#00389416" zPosition="3" font="{0};27" halign="center" backgroundColor="#16000000" transparent="1">
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
	<ePixmap position="393,158" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" alphatest="blend" transparent="1" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="397,162" size="182,110" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
	<ePixmap position="393,340" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="397,344" size="182,110" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
	<ePixmap position="1339,158" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1343,162" zPosition="5" size="182,110" alphatest="blend">
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
	<ePixmap position="1339,340" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1343,344" size="182,110" transparent="1" alphatest="blend" zPosition="3" />
    <!--widget source="session.CurrentService" render="Label" position="76,854" size="568,45" font="{0};33" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Number</convert>
    </widget-->
    <widget source="session.CurrentService" render="Label" position="76,905" size="568,45" font="{0};32" halign="center" foregroundColor="#34a36e" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1255,905" size="610,45" font="{0};30" halign="center" foregroundColor="#00bab329" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1255,858" size="610,45" font="{0};30" halign="center" foregroundColor="#58bcff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
 </widget>
 <!--pogoda-->
 <eLabel text="{8}" position="1639,194" size="100,30" font="{0};25" backgroundColor="#54111112" halign="center" transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="1549,194" size="90,90" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="1720,194" size="66,30" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00c1ea02" backgroundColor="#54111112" transparent="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/wiatr.png" position="1638,224" size="30,30" zPosition="3" transparent="1" alphatest="blend" />
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/deszcz.png" position="1639,254" size="28,30" zPosition="4" transparent="1" alphatest="blend" />
 <widget source="session.CurrentService" render="Label" position="1676,224" size="120,30" font="{0}; 28" zPosition="3" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#54111112" transparent="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="1675,254" size="120,30" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
    <!--eLabel text="%" position="1738,254" size="30,30" zPosition="2" backgroundColor="#54111112" transparent="1" font="{0};25" foregroundColor="#00ffffff" /-->
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/FHD/wsch.png" position="1551,300" size="99,50" zPosition="2" />
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/FHD/zach.png" position="1551,350" size="99,50" zPosition="2" />
    <eLabel text="Rise." position="1655,325" size="75,30" font="{0};21" backgroundColor="#54111112" transparent="1" zPosition="2" />
	<widget backgroundColor="#54111112" font="{0};25" halign="right" position="1715,321" zPosition="2" render="Label" size="71,30" source="global.CurrentTime" transparent="1" valign="center">
  <convert type="RaedQuickWeather">Sunrise</convert>
 </widget>
    <eLabel text="Set." position="1655,375" size="75,30" font="{0};21" backgroundColor="#54111112" transparent="1" zPosition="2" />
    <widget backgroundColor="#54111112" font="{0};25" foregroundColor="#00ffffff" halign="right" position="1715,371" zPosition="2" render="Label" size="71,30" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunset</convert>
 </widget>
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather/MoonPhase" position="1561,425" size="80,80" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">PiconMoon</convert>
  </widget>
   <widget source="session.CurrentService" render="Label" position="1611,420" size="165,65" font="{0};25" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Moonlight</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1631,485" size="170,23" font="{0};25" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Moondist</convert>
  </widget>
    <eLabel name="new eLabel" position="1567,522" size="214,2" zPosition="2" backgroundColor="#004f6ef2" />
	<eLabel text="{9}" position="1551,525" size="245,30" font="{0};25" halign="center" valign="center" backgroundColor="#54111112" transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
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
<widget name="Positioner" position="56,963" size="575,50" zPosition="10" font="{0};30" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" valign="center" transparent="1" />
<widget name="Satfinder" position="1292,967" size="575,50" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#0000deff" valign="center" halign="center" transparent="1" />
	<ePixmap position="788,992" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/menu.png" alphatest="blend" />
	<ePixmap position="1002,992" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/exit.png" alphatest="blend" /> 
 <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="173,855" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="173,855" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="173,855" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="173,855" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="275,855" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="275,855" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
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

### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------36--------------------------------------------------------

SKIN_Full_Screen_Picon_media_Ecm3_Vertical = """
<screen name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="Quick Signal Info" flags="wfNoBorder">
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="{1}/images/CobaltFHD/FHD/cool1.png" />
    <ePixmap position="119,140" size="257,559" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/agc_snr.png" alphatest="blend" transparent="1" />
    <ePixmap position="1545,140" size="257,559" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/pogoda.png" alphatest="blend" transparent="1" />
    <ePixmap position="67,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="669,847" size="601,139" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" scale="1" alphatest="blend" transparent="1" />
    <ePixmap position="1274,847" size="601,108" zPosition="-1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick1.png" alphatest="blend" transparent="1" />
    <ePixmap position="573,484" size="794,209" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick2.png" alphatest="blend" transparent="1" />
    <ePixmap position="108,720" size="1752,96" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick3.png" alphatest="blend" transparent="1" />
    <ePixmap position="210,49" zPosition="30" size="80,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" />
    <ePixmap position="919,991" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
    <ePixmap position="596,157" size="729,300" zPosition="1" pixmap="{1}/images/CobaltFHD/FHD/frame_quick5.png" alphatest="blend" transparent="1" />
	<widget source="session.Event_Now" render="Label" position="613,162" size="694,40" font="{0};32" halign="center" backgroundColor="#595959" foregroundColor="#00ffffff" transparent="1" zPosition="1">
      <convert type="EventName">Name</convert>
 </widget>
	<eLabel name="new eLabel" position="646,208" size="628,2" backgroundColor="#004f6ef2" />
	<widget backgroundColor="#16000000" font="{0};27" halign="center" position="612,223" render="Label" size="694,221" source="session.Event_Now" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
 </widget>
	  <widget source="global.CurrentTime" render="Label" position="920,53" size="920,50" font="{0};40" valign="center" halign="right" backgroundColor="#54111112" foregroundColor="#58bcff" transparent="1">
      <convert type="ClockToText">Format:%A  %e  %B  %Y     %H:%M </convert>
	   </widget>
    <widget source="Title" position="135,52" size="800,70" render="Label" font="{0};40" foregroundColor="#58bcff" backgroundColor="#00000000" transparent="1" halign="center" />
    <widget source="session.CurrentService" render="Label" position="683,857" size="568,40" zPosition="2" font="{0};32" halign="center" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
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
    <widget source="session.CurrentService" render="Label" position="585,487" size="765,203" zPosition="2" font="{0};24" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="683,919" size="568,62" zPosition="2" font="{0};26" halign="left" valign="center" foregroundColor="#00fffe9e" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">caids</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1274,958" size="153,43" zPosition="2" font="{0};30" halign="left" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="462,773" size="992,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="487,728" size="120,38" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="602,728" render="Label" size="200,38" source="session.CurrentService" transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};32" halign="left" position="905,728" size="80,38" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="845,728" size="50,38" font="{0};33" halign="right" backgroundColor="#00000000" transparent="1">
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
  <widget source="session.CurrentService" render="Label" position="120,769" size="300,40" foregroundColor="#00389416" zPosition="3" font="{0};27" halign="center" backgroundColor="#16000000" transparent="1">
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
	<ePixmap position="393,158" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" alphatest="blend" transparent="1" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="397,162" size="182,110" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
	<ePixmap position="393,340" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="397,344" size="182,110" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
	<ePixmap position="1339,158" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="1343,162" zPosition="5" size="182,110" alphatest="blend">
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
	<ePixmap position="1339,340" size="192,120" zPosition="2" pixmap="{1}/images/CobaltFHD/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1343,344" size="182,110" transparent="1" alphatest="blend" zPosition="3" />
    <!--widget source="session.CurrentService" render="Label" position="76,854" size="568,45" font="{0};33" halign="center" foregroundColor="#F0A30A" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Number</convert>
    </widget-->
    <widget source="session.CurrentService" render="Label" position="76,905" size="568,45" font="{0};32" halign="center" foregroundColor="#34a36e" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1255,905" size="610,45" font="{0};30" halign="center" foregroundColor="#00bab329" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
 </widget>
    <widget source="session.CurrentService" render="Label" position="1255,858" size="610,45" font="{0};30" halign="center" foregroundColor="#58bcff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
 </widget>
 <!--pogoda-->
 <eLabel text="{8}" position="1639,194" size="100,30" font="{0};25" backgroundColor="#54111112" halign="center" transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="1549,194" size="90,90" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="1720,194" size="66,30" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00c1ea02" backgroundColor="#54111112" transparent="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/wiatr.png" position="1638,224" size="30,30" zPosition="3" transparent="1" alphatest="blend" />
    <ePixmap pixmap="{1}/images/CobaltFHD/FHD/deszcz.png" position="1639,254" size="28,30" zPosition="4" transparent="1" alphatest="blend" />
 <widget source="session.CurrentService" render="Label" position="1676,224" size="120,30" font="{0}; 28" zPosition="3" halign="center" valign="center" foregroundColor="#000090e6" backgroundColor="#54111112" transparent="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
 <widget source="session.CurrentService" render="Label" position="1675,254" size="120,30" font="{0}; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
    <!--eLabel text="%" position="1738,254" size="30,30" zPosition="2" backgroundColor="#54111112" transparent="1" font="{0};25" foregroundColor="#00ffffff" /-->
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/FHD/wsch.png" position="1551,300" size="99,50" zPosition="2" />
    <ePixmap alphatest="blend" pixmap="{1}/images/CobaltFHD/FHD/zach.png" position="1551,350" size="99,50" zPosition="2" />
    <eLabel text="Rise." position="1655,325" size="75,30" font="{0};21" backgroundColor="#54111112" transparent="1" zPosition="2" />
	<widget backgroundColor="#54111112" font="{0};25" halign="right" position="1715,321" zPosition="2" render="Label" size="71,30" source="global.CurrentTime" transparent="1" valign="center">
  <convert type="RaedQuickWeather">Sunrise</convert>
 </widget>
    <eLabel text="Set." position="1655,375" size="75,30" font="{0};21" backgroundColor="#54111112" transparent="1" zPosition="2" />
    <widget backgroundColor="#54111112" font="{0};25" foregroundColor="#00ffffff" halign="right" position="1715,371" zPosition="2" render="Label" size="71,30" source="global.CurrentTime" transparent="1" valign="center">
    <convert type="RaedQuickWeather">Sunset</convert>
 </widget>
 <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather/MoonPhase" position="1561,425" size="80,80" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">PiconMoon</convert>
  </widget>
   <widget source="session.CurrentService" render="Label" position="1611,420" size="165,65" font="{0};25" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Moonlight</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1631,485" size="170,23" font="{0};25" zPosition="3" halign="center" valign="center" foregroundColor="foreground" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Moondist</convert>
  </widget>
    <eLabel name="new eLabel" position="1567,522" size="214,2" zPosition="2" backgroundColor="#004f6ef2" />
	<eLabel text="{9}" position="1551,525" size="245,30" font="{0};25" halign="center" valign="center" backgroundColor="#54111112" transparent="1" foregroundColor="#00c1ea02" zPosition="2" />
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
<widget name="Positioner" position="56,963" size="575,50" zPosition="10" font="{0};30" halign="center" backgroundColor="#54111112" foregroundColor="#41ff9900" valign="center" transparent="1" />
<widget name="Satfinder" position="1292,967" size="575,50" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#0000deff" valign="center" halign="center" transparent="1" />
	<ePixmap position="788,992" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/menu.png" alphatest="blend" />
	<ePixmap position="1002,992" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/exit.png" alphatest="blend" /> 
 <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="173,855" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="173,855" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="173,855" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="173,855" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="275,855" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="275,855" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
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

### SKIN_Full_Screen_Picons_ECM_SNR_ANALOG  ### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------37--------------------------------------------------------

SKIN_Full_Screen_Picon_Ecm3_SNR_ANALOG = """
<screen name="SKIN_Full_Screen_Picon_Ecm3_SNR_ANALOG" position="0,0" size="1920,1080" title="Quick Signal Info" backgroundColor="#16000000" flags="wfNoBorder">
  <ePixmap position="325,777" size="1200,250" zPosition="1" pixmap="{1}/images/analog/FHD/analog_tuner_bg.png" alphatest="blend" transparent="1" />
  <ePixmap position="44,868" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
<widget source="session.Event_Now" render="Label" position="38,249" size="598,66" font="{0};35" halign="left" backgroundColor="#ff595959" foregroundColor="#7ad927" transparent="1" zPosition="1">
  <convert type="EventName">Name</convert>
</widget>
<widget backgroundColor="#16000000" font="{0};30" position="33,324" render="Label" size="1855,132" source="session.Event_Now" transparent="1">
  <convert type="EventName">ExtendedDescription</convert>
</widget>
<widget source="session.CurrentService" render="Label" position="538,44" size="878,305" zPosition="2" font="{0};28" halign="center" valign="center" foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">ecmfile</convert>
</widget>
  <widget source="global.CurrentTime" render="Label" position="987,15" size="920,50" font="{0};30" valign="center" halign="right" backgroundColor="#16000000" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y  -  %H:%M </convert>
  </widget>
  <widget source="Title" position="120,17" size="800,70" render="Label" font="{0};30" foregroundColor="#58bcff" backgroundColor="#16000000" transparent="1" halign="left" />
  <!-- SNRdB -->
 <eLabel name="snr" text="SNRdB" position="877,1031" size="150,45" font="{0}; 32" halign="center" foregroundColor="#00f0f0f0" backgroundColor="#16000000" transparent="1" zPosition="2" />
 <widget source="session.FrontendStatus" render="Label" position="735,969" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR" position="347,969" size="150,45" font="{0}; 35" halign="left" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2" />
<widget source="session.FrontendStatus" render="Label" position="445,969" size="150,45" font="{0}; 35" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="RaedQuickWatches" position="400,790" size="500,450" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">SNR_ANALOG</convert>
    </widget>
    <!-- AGC -->
    <widget source="session.FrontendStatus" render="RaedQuickWatches" position="1000,792" size="500,450" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">AGC_ANALOG</convert>
    </widget>
  <eLabel name="agc" text="AGC" position="1267,969" size="150,45" font="{0}; 35" halign="right" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2" />
  <widget source="session.FrontendStatus" render="Label" position="1423,969" size="150,45" font="{0}; 35" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <!--Picon-->
    <ePixmap position="203,480" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="208,485" size="240,140" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
    <ePixmap position="617,485" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="622,490" zPosition="5" size="240,140" alphatest="blend">
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
    <ePixmap position="1040,485" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="1045,490" size="240,140" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <ePixmap position="1458,485" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1463,490" size="240,140" transparent="1" alphatest="blend" zPosition="3" />
    <ePixmap position="18,975" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/exit.png" alphatest="blend" />
   <ePixmap position="30,15" zPosition="30" size="80,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" /> 
   <ePixmap position="18,929" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/menu.png" alphatest="blend" />
<widget name="Positioner" position="10,1020" size="575,60" zPosition="-10" font="{0};30" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="left" />
<widget name="Satfinder" position="1350,1020" size="575,60" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center" />
    <widget source="session.CurrentService" render="Label" position="462,719" size="992,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="487,664" size="120,38" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="602,664" render="Label" size="200,38" source="session.CurrentService" transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};32" halign="left" position="905,664" size="80,38" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="845,664" size="50,38" font="{0};33" halign="right" backgroundColor="#00000000" transparent="1">
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="59,719" size="385,40" foregroundColor="#00389416" zPosition="3" font="{0};32" halign="center" backgroundColor="#16000000" transparent="1">
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
   <widget source="session.CurrentService" render="Label" position="61,664" size="385,40" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
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
  <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" scale="1" backgroundColor="background" position="95,467" size="1694,190" zPosition="-3" alphatest="blend" transparent="1">
    <convert type="ServiceInfo">IsCrypted</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="1540,881" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="1540,881" size="90,40" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="1540,881" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="1540,881" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="1637,881" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="1637,881" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
  </widget>
  <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="1806,883" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="1741,883" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="1741,883" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget> 
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85)

### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------38--------------------------------------------------------

SKIN_Full_Screen_Picon_media_Ecm3_SNR_ANALOG = """
<screen name="SKIN_Full_Screen_Picon_Ecm3_SNR_ANALOG" position="0,0" size="1920,1080" title="Quick Signal Info" backgroundColor="#16000000" flags="wfNoBorder">
  <ePixmap position="325,777" size="1200,250" zPosition="1" pixmap="{1}/images/analog/FHD/analog_tuner_bg.png" alphatest="blend" transparent="1" />
  <ePixmap position="44,868" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
<widget source="session.Event_Now" render="Label" position="38,249" size="598,66" font="{0};35" halign="left" backgroundColor="#ff595959" foregroundColor="#7ad927" transparent="1" zPosition="1">
  <convert type="EventName">Name</convert>
</widget>
<widget backgroundColor="#16000000" font="{0};30" position="33,324" render="Label" size="1855,132" source="session.Event_Now" transparent="1">
  <convert type="EventName">ExtendedDescription</convert>
</widget>
<widget source="session.CurrentService" render="Label" position="538,44" size="878,305" zPosition="2" font="{0};28" halign="center" valign="center" foregroundColor="#00bab329" backgroundColor="#16000000" transparent="1">
  <convert type="RaedQuickEcmInfo">ecmfile</convert>
</widget>
  <widget source="global.CurrentTime" render="Label" position="987,15" size="920,50" font="{0};30" valign="center" halign="right" backgroundColor="#16000000" foregroundColor="#58bcff" transparent="1">
    <convert type="ClockToText">Format:%A  %e  %B  %Y  -  %H:%M </convert>
  </widget>
  <widget source="Title" position="120,17" size="800,70" render="Label" font="{0};30" foregroundColor="#58bcff" backgroundColor="#16000000" transparent="1" halign="left" />
  <!-- SNRdB -->
 <eLabel name="snr" text="SNRdB" position="877,1031" size="150,45" font="{0}; 32" halign="center" foregroundColor="#00f0f0f0" backgroundColor="#16000000" transparent="1" zPosition="2" />
 <widget source="session.FrontendStatus" render="Label" position="735,969" zPosition="2" size="400,45" font="{0}; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR" position="347,969" size="150,45" font="{0}; 35" halign="left" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2" />
<widget source="session.FrontendStatus" render="Label" position="445,969" size="150,45" font="{0}; 35" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="RaedQuickWatches" position="400,790" size="500,450" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">SNR_ANALOG</convert>
    </widget>
    <!-- AGC -->
    <widget source="session.FrontendStatus" render="RaedQuickWatches" position="1000,792" size="500,450" borderColor="#008f8f8f" foregroundColor="#00ff2525" zPosition="4" transparent="1" alphatest="blend">
      <convert type="RaedQuickFrontendInfo2">AGC_ANALOG</convert>
    </widget>
  <eLabel name="agc" text="AGC" position="1267,969" size="150,45" font="{0}; 35" halign="right" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1" zPosition="2" />
  <widget source="session.FrontendStatus" render="Label" position="1423,969" size="150,45" font="{0}; 35" foregroundColor="#00f23d21" transparent="1" zPosition="2">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
    <!--Picon-->
    <ePixmap position="203,480" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="208,485" size="240,140" zPosition="5" alphatest="blend">
    <convert type="RaedQuickServName2">Reference</convert>
 </widget>
    <ePixmap position="617,485" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="622,490" zPosition="5" size="240,140" alphatest="blend">
	<convert type="RaedQuickServName2">OrbitalPos</convert>
 </widget>
    <ePixmap position="1040,485" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="1045,490" size="240,140" zPosition="5" transparent="1" alphatest="blend">
    <convert type="RaedQuickServName2">Provider</convert>
 </widget>
    <ePixmap position="1458,485" size="250,150" zPosition="2" pixmap="{1}/images/analog/FHD/frame_of_picon3c.png" transparent="1" alphatest="blend" />
    <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="1463,490" size="240,140" transparent="1" alphatest="blend" zPosition="3" />
    <ePixmap position="18,975" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/exit.png" alphatest="blend" />
   <ePixmap position="30,15" zPosition="30" size="80,70" pixmap="{1}/images/fairbirdfhd.png" scale="1" alphatest="blend" /> 
   <ePixmap position="18,929" size="100,40" pixmap="{1}/images/CobaltFHD/FHD/menu.png" alphatest="blend" />
<widget name="Positioner" position="10,1020" size="575,60" zPosition="-10" font="{0};30" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="left" />
<widget name="Satfinder" position="1350,1020" size="575,60" zPosition="10" font="{0};30" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" valign="center" halign="center" />
    <widget source="session.CurrentService" render="Label" position="462,719" size="992,38" zPosition="2" font="{0};32" halign="center" valign="top" foregroundColor="#7ad927" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickEcmInfo">pids</convert>
 </widget>
    <eLabel backgroundColor="#00000000" font="{0};32" foregroundColor="#004f6ef2" halign="left" position="487,664" size="120,38" text="{2}" transparent="1" />
    <widget backgroundColor="#00000000" font="{0};32" halign="left" position="602,664" render="Label" size="200,38" source="session.CurrentService" transparent="1">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
 </widget>
 <eLabel backgroundColor="#00000000" font="{0};32" halign="left" position="905,664" size="80,38" text="fps" transparent="1" />
    <widget source="session.CurrentService" render="Label" position="845,664" size="50,38" font="{0};33" halign="right" backgroundColor="#00000000" transparent="1">
    <convert type="RaedQuickServiceInfo2">Framerate</convert>
    </widget>
    <widget source="session.CurrentService" render="Label" position="59,719" size="385,40" foregroundColor="#00389416" zPosition="3" font="{0};32" halign="center" backgroundColor="#16000000" transparent="1">
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
   <widget source="session.CurrentService" render="Label" position="61,664" size="385,40" zPosition="2" font="{0};33" halign="center" valign="top" foregroundColor="#00ff2525" backgroundColor="#16000000" transparent="1">
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
  <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" scale="1" backgroundColor="background" position="95,467" size="1694,190" zPosition="-3" alphatest="blend" transparent="1">
    <convert type="ServiceInfo">IsCrypted</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="1540,881" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="1540,881" size="90,40" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="1540,881" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="1540,881" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="1637,881" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="1637,881" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
  </widget>
   <!-- Network -->
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/inet_green_fhd.png" position="1806,883" size="50,40" zPosition="2" alphatest="blend">
    <convert type="RaedQuickTestConnection">google.com</convert>
    <convert type="ConditionalShowHide" />
  </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/lan_green_fhd.png" position="1741,883" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Lan</convert>
      <convert type="ConditionalShowHide" />
    </widget>
   <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/wlan_green_fhd.png" position="1741,883" size="50,40" zPosition="2" alphatest="blend">
   <convert type="RaedQuickRouteInfo">Wifi</convert>
      <convert type="ConditionalShowHide" />
    </widget> 
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85)

### SKIN_Picons#----0---

SKIN_AGC_Event_Des_SNRdB5 = """ 
<screen name="AGC_Event_Des" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" backgroundColor="#90000000">
  <!-- 5 -->
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#bbbbbb" position="50,1110" size="400,40" transparent="1" halign="left" />
  <widget source="global.CurrentTime" render="Label" position="407,695" size="239,40" font="{0};32" valign="top" halign="left" foregroundColor="#ffffff" transparent="1" backgroundColor="#80ff" zPosition="-3" borderWidth="2" borderColor="#101010">
    <convert type="ClockToText">Format: %d-%m-%Y  </convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1281,695" size="235,40" font="{0};32" valign="top" halign="right" foregroundColor="#ffffff" transparent="1" backgroundColor="#80ff" zPosition="-3" borderWidth="2" borderColor="#101010" cornerRadius="9">
    <convert type="ClockToText">Format:%H:%M %A </convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="754,955" zPosition="2" size="270,55" font="{0}; 45" foregroundColor="#f23d21" halign="center" valign="center" transparent="1" backgroundColor="#00000000">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="agc" text="SNR" position="1731,688" size="200,100" font="{0}; 70" halign="center" foregroundColor="#c5c6c7" transparent="1" zPosition="88" />
  <widget source="session.FrontendStatus" render="RaedQuickSignalCircleProgress" mode="event" scale="2" pixmapCircle="{1}/images/icons_quick/prgrs150green2.png" pixmapCircleBack="{1}/images/icons_quick/prgrs150back.png" zPosition="35" backgroundColor="#90000000" position="15,350" size="360,360" transparent="1" cornerRadius="37">
  <convert type="RaedQuickSignal">SNR</convert>
</widget> 
  <!-- AGC -->
  <eLabel name="agc" text="AGC" position="211,688" size="200,100" font="{0}; 70" halign="left" foregroundColor="#c5c6c7" transparent="1" zPosition="39" />
  <widget source="session.FrontendStatus" render="RaedQuickSignalCircleProgress" mode="event" scale="2" pixmapCircle="{1}/images/icons_quick/prgrs150orange.png" pixmapCircleBack="{1}/images/icons_quick/prgrs150back.png" zPosition="35" backgroundColor="#90000000" position="1536,350" size="360,360" transparent="1" foregroundColor="#ff00">
  <convert type="RaedQuickSignal">AGC</convert>
</widget> 
  <widget source="session.CurrentService" render="Label" position="399,426" size="1125,314" font="{0}; 28" zPosition="-2" backgroundColor="#31000000" foregroundColor="#c400" valign="center" halign="center" transparent="1" borderWidth="2" borderColor="#101010">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="273,767" size="1375,70" font="{0}; 32" zPosition="-2" backgroundColor="#00000000" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1443,781" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="175,855" size="1570,50" font="{0}; 32" zPosition="2" backgroundColor="#7f000000" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget render="VideoSize" source="session.CurrentService" position="7,1024" size="179,40" backgroundColor="#00000000" font="{0}; 32" foregroundColor="#bbbbbb" halign="center" valign="center" transparent="1" zPosition="5" />
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.CurrentService" render="ChannelNumber" position="5,859" size="158,40" font="{0};38" foregroundColor="#fec000" backgroundColor="transpBlack" cornerRadius="30" valign="center" halign="center" transparent="0" zPosition="9" />
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="295,323" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="295,323" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,323" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,323" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="275,323" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="275,323" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,323" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1768,860" size="75,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" scale="1" />
  <ePixmap position="1855,860" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="1660,778" size="255,63" cornerRadius="37" zPosition="-10" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="746,950" size="284,119" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="5,778" size="255,63" cornerRadius="37" zPosition="-10" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="171,848" size="1578,63" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" transparent="0" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="265,762" size="1390,80" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap position="0,913" size="1973,291" zPosition="-70" alphatest="blend" pixmap="{1}/images/InfoBar.png" scale="1" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="1219,950" size="180,110" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="1035,950" size="180,110" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="560,950" size="180,110" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="375,950" size="180,110" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
 <eLabel name="background" position="1536,355" size="360,360" cornerRadius="170" transparent="0" zPosition="34" backgroundColor="#90000000" borderWidth="4" borderColor="#656565" />
<!-- Event IsCrypted -->
  <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" cornerRadius="37" scale="1" backgroundColor="background" position="392,416" size="1136,336" zPosition="-11" alphatest="blend" transparent="1">
    <convert type="ServiceInfo">IsCrypted</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="8,920" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center" cornerRadius="37">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="8,970" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#c5c6c7" transparent="1" halign="center" cornerRadius="37" borderWidth="2" borderColor="#101010">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="380,952" size="170,102" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" scale="1" position="565,953" size="170,102" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="1040,953" size="170,102" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="1224,953" size="170,102" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="189,1025" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="189,1025" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="189,1025" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="189,1025" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="277,1025" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="277,1025" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
  </widget>
  <!-- IsFta  -->
  <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="733,1020" size="300,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="733,1020" size="300,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#6f9ef5" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="733,1020" size="300,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="733,1020" size="300,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#5a115" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Net</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1406,928" size="500,66" font="{0}; 25" halign="center" backgroundColor="#00000000" foregroundColor="#fec000" shadowOffset="3,2" transparent="1" cornerRadius="37" valign="bottom" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1407,1006" size="499,60" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" cornerRadius="37" valign="bottom">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="1505,786" size="395,50" zPosition="1" font="{0};24" halign="right" backgroundColor="#2444444" foregroundColor="#41ff9900" transparent="1" cornerRadius="37" valign="center" />
  <widget name="Positioner" position="18,778" size="390,50" zPosition="1" font="{0};22" halign="left" backgroundColor="#00000000" foregroundColor="#41ff9900" transparent="1" cornerRadius="37" valign="center" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title41, title42, title80, title81, title82, title83, title84, title85, title86, title87)

### SKIN_Picons#---1----
SKIN_AGC_Event_Des_SNRdB1 = """ 
<screen backgroundColor="#31000000" name="AGC_Event_Des" position="103,41" size="1712,997" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="57">
  <!-- 1 -->
  <ePixmap pixmap="{1}/images/icons_quick/progress_mediumbg.png" position="204,142" size="1350,50" cornerRadius="37" zPosition="-1" scale="1" alphatest="blend" transparent="1" />
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="55,10" size="500,40" transparent="1" halign="left" />
  <widget source="global.CurrentTime" render="Label" position="1220,10" size="458,40" font="{0};31" valign="top" halign="right" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y  %H:%M:%S</convert>
  </widget>
 <eLabel name="snr" text="SNRdB:" position="572,14" size="191,50" font="{0}; 37" halign="right" foregroundColor="#bbbbbb" transparent="1" />
 <widget source="session.FrontendStatus" render="Label" position="770,11" zPosition="2" size="450,55" font="{0}; 45" foregroundColor="#f23d21" halign="left" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="3,75" size="191,50" font="{0}; 37" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.CurrentService" render="RaedQuickSignalAglareBoxImage" position="1340,390" size="300,80" alphatest="on" scale="1" zPosition="99" />
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/731.png" scale="1" position="202,74" size="1350,50" zPosition="2" borderWidth="4" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#1d8503" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1561,75" size="135,50" font="{0}; 37" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="3,143" size="191,50" font="{0}; 37" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/731.png" scale="1" position="204,142" size="1350,50" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1561,143" size="135,50" font="{0}; 37" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="130,203" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#00000000" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="35,562" size="1633,68" font="{0}; 32" zPosition="-2" backgroundColor="#31000000" foregroundColor="#bbbbbb" transparent="0" valign="center" halign="center" cornerRadius="38">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="745,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#101010" foregroundColor="#fec000" transparent="1" valign="top" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="35,649" size="1633,50" font="{0}; 32" zPosition="2" backgroundColor="#101010" foregroundColor="#41ff9900" transparent="0" valign="center" halign="center" cornerRadius="36">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget render="VideoSize" source="session.CurrentService" position="7,811" size="179,40" backgroundColor="#00000000" font="{0}; 32" foregroundColor="#bbbbbb" halign="center" valign="center" transparent="1" zPosition="5" />
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.CurrentService" render="ChannelNumber" position="52,655" size="158,40" font="{0};38" foregroundColor="#fec000" backgroundColor="transpBlack" valign="center" halign="Left" transparent="1" zPosition="9" />
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1612,925" size="75,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" scale="1" />
  <ePixmap position="1624,865" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <ePixmap position="79,344" size="120,130" zPosition="4" alphatest="blend" pixmap="{1}/images/service_info_sat.png" scale="1" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/titleframe-fs.png" position="28,645" size="1652,60" cornerRadius="37" zPosition="-5" scale="1" alphatest="blend" transparent="1" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/titleframe-fs.png" position="28,555" size="1652,81" cornerRadius="37" zPosition="-5" scale="1" alphatest="blend" transparent="1" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/titleframe-fs.png" position="1276,480" size="420,60" cornerRadius="37" zPosition="-5" scale="1" alphatest="blend" transparent="1" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/titleframe-fs.png" position="20,480" size="420,60" cornerRadius="37" zPosition="-5" scale="1" alphatest="blend" transparent="1" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="45,864" size="1543,125" font="{0}; 25" halign="center" foregroundColor="#bbbbbb" backgroundColor="#54111112" transparent="1">
    <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="8,717" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center" cornerRadius="37">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="8,765" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center" cornerRadius="37">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="387,724" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" scale="1" position="586,724" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="788,724" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="990,724" size="190,110" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="189,811" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="189,811" size="90,40" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="189,811" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="189,811" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="277,811" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="277,811" size="90,35" font="Bold;40" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
  </widget>
  <!-- IsFta  -->
  <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="693,472" size="300,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="693,472" size="300,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#6f9ef5" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="693,472" size="300,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="693,472" size="300,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#5a115" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Net</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1201,720" size="500,73" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" cornerRadius="37">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1201,801" size="500,50" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" cornerRadius="37">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="1293,487" size="380,50" zPosition="1" font="{0}; 28" halign="right" backgroundColor="#101010" foregroundColor="#41ff9900" transparent="1" cornerRadius="37" valign="center" />
  <widget name="Positioner" position="47,487" size="380,50" zPosition="1" font="{0}; 27" halign="left" backgroundColor="#101010" foregroundColor="#41ff9900" transparent="1" cornerRadius="37" valign="center" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85, title86, title87)
### SKIN_Picons#---2---
SKIN_AGC_Event_Des_SNRdB2 = """ 
<screen backgroundColor="#31000000" name="AGC_Event_Des" position="103,51" size="1712,988" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" cornerRadius="57">
  <!-- 2 -->
  <widget source="Title" render="Label" font="{0};30" foregroundColor="#bbbbbb" position="55,10" size="500,40" transparent="1" halign="left" />
  <widget source="global.CurrentTime" render="Label" position="1220,10" size="458,40" font="{0};31" valign="top" halign="right" foregroundColor="#bbbbbb" transparent="1">
    <convert type="ClockToText">Format:%d-%m-%Y  %H:%M:%S</convert>
  </widget>
 <eLabel name="snr" text="SNRdB:" position="572,14" size="191,50" font="{0}; 37" halign="right" foregroundColor="#bbbbbb" transparent="1" />
 <widget source="session.FrontendStatus" render="Label" position="770,11" zPosition="2" size="450,55" font="{0}; 45" foregroundColor="#f23d21" halign="left" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="3,75" size="191,50" font="{0}; 37" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/731.png" scale="1" position="202,74" size="1350,50" foregroundGradient="red,yellow,#00008000,horizontal" foregroundColor="#1d8503" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1561,75" size="135,50" font="{0}; 37" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="3,143" size="191,50" font="{0}; 37" halign="right" foregroundColor="#bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/731.png" scale="1" position="204,142" size="1350,50" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#30394" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1561,143" size="135,50" font="{0}; 37" foregroundColor="#bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="130,203" size="1400,300" font="{0}; 28" zPosition="2" backgroundColor="#00000000" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="145,562" size="1400,70" font="{0}; 32" zPosition="-2" backgroundColor="#2444444" foregroundColor="#bbbbbb" transparent="0" valign="center" halign="center" cornerRadius="37" borderWidth="1" borderColor="#101010">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="745,514" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="60,644" size="1570,50" font="{0}; 32" zPosition="2" backgroundColor="#656565" foregroundColor="#41ff9900" transparent="0" valign="center" halign="center" cornerRadius="37" borderWidth="2" borderColor="#101010">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget render="VideoSize" source="session.CurrentService" position="7,796" size="179,40" backgroundColor="#00000000" font="{0}; 32" foregroundColor="#bbbbbb" halign="center" valign="center" transparent="1" zPosition="5" />
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.CurrentService" render="ChannelNumber" position="67,649" size="158,40" font="{0};38" foregroundColor="#fec000" backgroundColor="transpBlack" valign="center" halign="Left" transparent="1" zPosition="9" borderWidth="1" borderColor="#101010" />
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="155,208" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1612,910" size="75,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" scale="1" />
  <ePixmap position="1624,850" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="338,845" size="1160,136" font="{0}; 27" halign="center" foregroundColor="#bbbbbb" backgroundColor="#54111112" transparent="1">
    <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="8,702" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center" cornerRadius="37">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="8,750" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center" cornerRadius="37">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="387,714" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" scale="1" position="586,714" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="788,714" size="190,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="990,714" size="190,110" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="189,796" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="189,796" size="90,40" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="189,796" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="189,796" size="90,40" font="Bold;40" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="277,796" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="277,796" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
  </widget>
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="15,877" size="65,65" zPosition="3" transparent="1" alphatest="blend">
    <convert type="RaedQuickWeather">Picon</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="13,843" size="150,29" font="{0}; 27" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Temp</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="36,947" size="300,31" font="{0}; 25" zPosition="3" halign="left" valign="center" foregroundColor="#f37104" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Location</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="102,897" size="201,32" font="{0}; 27" zPosition="3" halign="left" valign="center" foregroundColor="#ffffff" backgroundColor="#54111112" transparent="1">
    <convert type="RaedQuickWeather">Day</convert>
  </widget>
  <!-- IsFta  -->
  <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="693,472" size="300,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="693,472" size="300,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#6f9ef5" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="693,472" size="300,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="693,472" size="300,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#5a115" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Net</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1201,705" size="500,73" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" cornerRadius="37">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1201,786" size="500,50" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" cornerRadius="37">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="1110,506" size="500,50" zPosition="1" font="{0};33" halign="center" backgroundColor="#2444444" foregroundColor="#41ff9900" transparent="0" cornerRadius="37" />
  <widget name="Positioner" position="90,506" size="500,50" zPosition="1" font="{0};33" halign="center" backgroundColor="#2444444" foregroundColor="#41ff9900" transparent="0" cornerRadius="37" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85)
### SKIN_Picons#----3---
SKIN_AGC_Event_Des_SNRdB3 = """ 
<screen backgroundColor="transparent" name="AGC_Event_Des" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <!-- 3 -->
  <widget source="session.FrontendStatus" render="Label" position="774,941" zPosition="2" size="235,55" font="{0}; 45" foregroundColor="#ff0000" halign="center" valign="center" transparent="1" backgroundColor="#00000000">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="68,815" size="191,50" font="{0}; 37" halign="left" foregroundColor="#c5c6c7" transparent="1" zPosition="4" backgroundColor="#00000000" />
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" scale="1" position="58,815" size="1760,50" foregroundGradient="red,yellow,#00008000,horizontal" foregroundColor="#1d8503" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1674,815" size="135,50" font="{0}; 37" foregroundColor="#bbbbbb" transparent="1" zPosition="4" halign="right">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="68,873" size="191,50" font="{0}; 37" halign="left" foregroundColor="#c5c6c7" transparent="1" zPosition="4" backgroundColor="#00000000" />
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" scale="1" position="59,873" size="1760,50" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#030394" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1676,875" size="135,50" font="{0}; 37" foregroundColor="#bbbbbb" transparent="1" zPosition="4" halign="right">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="264,354" size="1400,307" font="{0}; 28" zPosition="-2" backgroundColor="#31000000" foregroundColor="#41ff9900" valign="center" halign="center" transparent="1" borderWidth="2" borderColor="#101010">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="262,672" size="1400,70" font="{0}; 32" zPosition="-2" backgroundColor="#2444444" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1453,684" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="175,754" size="1570,50" font="{0}; 32" zPosition="2" backgroundColor="#656565" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget render="VideoSize" source="session.CurrentService" position="7,1028" size="179,40" backgroundColor="#00000000" font="{0}; 32" foregroundColor="#bbbbbb" halign="center" valign="center" transparent="1" zPosition="5" />
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="global.CurrentTime" render="Label" position="768,1005" size="248,60" font="Regular; 28" valign="bottom" halign="center" foregroundColor="#bbbbbb" transparent="1" backgroundColor="#00000000">
    <convert type="ClockToText">Format:%H:%M:%S %A  %d-%m-%Y</convert>
  </widget>
  <widget source="session.CurrentService" render="ChannelNumber" position="8,933" size="158,40" font="{0};35" foregroundColor="#fec000" backgroundColor="transpBlack" valign="center" halign="left" transparent="1" zPosition="9" cornerRadius="30" />
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="305,358" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="295,358" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="295,358" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="295,358" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="300,358" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="300,358" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="300,358" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="300,358" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="295,358" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,358" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1832,865" size="75,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" scale="1" />
  <ePixmap position="1841,807" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <ePixmap position="0,804" size="1973,425" zPosition="-89" alphatest="off" pixmap="{1}/images/InfoBar.png" scale="1" />
  <eLabel name="background" position="175,754" size="1570,50" cornerRadius="37" transparent="0" itemGradientSelected="selbutton,background,#bd9771,transpBlack" itemGradient="transpBlack,#372113,background,horizontal" zPosition="-8" backgroundColor="transpBlack" />
  <eLabel name="background" position="262,672" size="1400,70" cornerRadius="37" transparent="0" itemGradientSelected="selbutton,background,#bd9771,transpBlack" itemGradient="transpBlack,#372113,background,horizontal" zPosition="-8" backgroundColor="transpBlack" borderWidth="4" borderColor="#656565" />
  <eLabel name="background" position="1670,682" size="250,50" cornerRadius="37" transparent="0" itemGradientSelected="selbutton,background,#bd9771,transpBlack" itemGradient="transpBlack,#372113,background,horizontal" zPosition="-8" backgroundColor="transpBlack" borderWidth="4" borderColor="#656565" />
  <eLabel name="background" position="5,682" size="250,50" cornerRadius="37" transparent="0" itemGradientSelected="selbutton,background,#bd9771,transpBlack" itemGradient="transpBlack,#372113,background,horizontal" zPosition="-8" backgroundColor="transpBlack" borderWidth="4" borderColor="#656565" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="1665,677" size="258,59" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="170,747" size="1581,63" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" />
  
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="259,665" size="1409,82" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="0,678" size="258,59" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" />
<!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="129,933" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="left" cornerRadius="37">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="8,980" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" halign="center" cornerRadius="37">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="392,958" size="180,110" zPosition="3" alphatest="blend" cornerRadius="20" transparent="0">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" scale="1" position="584,958" size="180,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="1019,958" size="180,110" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="1209,958" size="180,110" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Icons VideoWidth  -->
  <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" scale="1" backgroundColor="background" position="255,343" size="1416,327" zPosition="-3" alphatest="blend" transparent="1">
    <convert type="ServiceInfo">IsCrypted</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="189,1028" size="90,40" font="Bold;35" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="189,1028" size="90,40" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="189,1028" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="189,1028" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="277,1028" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="277,1028" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
  </widget>
  <!-- IsFta  -->
  <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="834,623" size="250,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#7f000000" cornerRadius="35" transparent="0">
    <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="834,623" size="250,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#6f9ef5" backgroundColor="#2444444" transparent="1" cornerRadius="30">
    <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="834,623" size="250,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="834,623" size="250,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#5a115" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Net</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1406,933" size="500,73" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" cornerRadius="37" valign="bottom">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1406,1018" size="500,50" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" cornerRadius="37">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="1670,682" size="250,50" zPosition="1" font="{0};24" halign="center" backgroundColor="#2444444" foregroundColor="#41ff9900" transparent="1" cornerRadius="37" valign="center" />
  <widget name="Positioner" position="5,682" size="250,50" zPosition="1" font="{0};22" halign="center" backgroundColor="#2444444" foregroundColor="#41ff9900" transparent="1" cornerRadius="37" valign="center" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title80, title81, title82, title83, title84, title85, title86, title87)
### SKIN_Picons#----4---
SKIN_AGC_Event_Des_SNRdB4 = """ 
<screen name="AGC_Event_Des" position="0,0" size="1920,1080" title="RAED's Quick Signal Info" zPosition="1" flags="wfNoBorder" backgroundColor="transparent">  
<!-- 4 -->
  <widget source="Title" render="Label" font="{0};35" foregroundColor="#bbbbbb" position="50,1110" size="400,40" transparent="1" halign="left" />
  <widget source="global.CurrentTime" render="Label" position="20,541" size="239,40" font="{0};32" valign="top" halign="left" foregroundColor="#bbbbbb" transparent="1" backgroundColor="#80ff" zPosition="-70" borderWidth="2" borderColor="#101010">
    <convert type="ClockToText">Format: %d-%m-%Y  </convert>
  </widget>
  <widget source="global.CurrentTime" render="Label" position="1658,541" size="235,40" font="{0};32" valign="top" halign="right" foregroundColor="#bbbbbb" transparent="1" backgroundColor="#80ff" zPosition="-70" borderWidth="2" borderColor="#101010" cornerRadius="9">
    <convert type="ClockToText">Format:%H:%M %A </convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="754,885" zPosition="2" size="270,55" font="{0}; 45" foregroundColor="#f23d21" halign="center" valign="center" transparent="1" backgroundColor="#00000000">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="68,953" size="191,50" font="{0}; 37" halign="left" foregroundColor="#c5c6c7" transparent="1" backgroundColor="#101010" borderWidth="1" borderColor="#101010" />
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" position="59,953" size="1760,50" scale="1" foregroundGradient="red,yellow,#00008000,horizontal" foregroundColor="#1d8503" zPosition="-2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1676,954" size="135,50" font="{0}; 36" foregroundColor="#bbbbbb" transparent="1" halign="right" backgroundColor="#101010">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="68,1018" size="191,50" font="{0}; 37" halign="left" foregroundColor="#c5c6c7" transparent="1" backgroundColor="#101010" borderWidth="1" borderColor="#101010" />
  <widget source="session.FrontendStatus" render="Progress" pixmap="{1}/images/icons_quick/icon_snr-scan3.png" scale="1" position="59,1018" size="1760,50" foregroundGradient="red,yellow,green,horizontal" foregroundColor="#7502f7" zPosition="-2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1676,1019" size="135,50" font="{0}; 36" foregroundColor="#bbbbbb" transparent="1" halign="right" backgroundColor="#101010">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="274,331" size="1371,314" font="{0}; 28" zPosition="-2" backgroundColor="#31000000" foregroundColor="#41ff9900" valign="center" halign="center" transparent="1" borderWidth="2" borderColor="#101010">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="257,662" size="1400,70" font="{0}; 32" zPosition="-2" backgroundColor="#00000000" foregroundColor="#bbbbbb" transparent="1" valign="center" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1453,676" size="200,45" font="{0}; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="175,750" size="1570,50" font="{0}; 32" zPosition="2" backgroundColor="#7f000000" foregroundColor="#41ff9900" transparent="0" valign="center" halign="center" cornerRadius="37">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <widget render="VideoSize" source="session.CurrentService" position="7,900" size="179,40" backgroundColor="#00000000" font="{0}; 32" foregroundColor="#bbbbbb" halign="center" valign="center" transparent="1" zPosition="5" />
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="{0}; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.CurrentService" render="ChannelNumber" position="5,759" size="158,40" font="{0};38" foregroundColor="#fec000" backgroundColor="transpBlack" cornerRadius="30" valign="center" halign="center" transparent="0" zPosition="9" />
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="124,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="295,323" size="128,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="32,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="136,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="145,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="150,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="155,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="160,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="165,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="170,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="295,323" size="175,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="180,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,323" size="185,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,323" size="190,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="195,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="275,323" size="300,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="275,323" size="305,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="290,323" size="310,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="315,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="320,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="370,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="620,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="670,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="820,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="970,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="1000,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="280,323" size="1140,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="285,323" size="1350,60" zPosition="2" pixmap="{1}/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1832,1015" size="75,50" zPosition="4" alphatest="blend" pixmap="{1}/images/menu2.png" scale="1" />
  <ePixmap position="1843,957" size="48,48" zPosition="4" alphatest="blend" pixmap="{1}/images/blue48x48.png" scale="1" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="1660,588" size="255,63" cornerRadius="37" zPosition="-10" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="746,826" size="284,119" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="5,588" size="255,63" cornerRadius="37" zPosition="-10" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="171,743" size="1578,63" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="249,657" size="1418,80" cornerRadius="37" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap position="0,789" size="1973,315" zPosition="-70" alphatest="blend" pixmap="{1}/images/InfoBar.png" scale="1" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="1219,828" size="180,110" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="1035,828" size="180,110" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="560,828" size="180,110" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <ePixmap pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" position="375,828" size="180,110" cornerRadius="20" zPosition="-50" scale="1" alphatest="blend" />
  <!-- Event IsCrypted -->
  <widget source="session.CurrentService" render="Pixmap" pixmap="{1}/images/ShabahNet/FHD/frame_quick2.png" cornerRadius="37" scale="1" backgroundColor="background" position="267,316" size="1385,335" zPosition="-11" alphatest="blend" transparent="1">
    <convert type="ServiceInfo">IsCrypted</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="8,810" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center" cornerRadius="37">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="8,853" size="359,40" font="{0}; 28" backgroundColor="#54111112" foregroundColor="#c5c6c7" transparent="1" halign="center" cornerRadius="37" borderWidth="2" borderColor="#101010">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" scale="1" position="380,832" size="170,102" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" scale="1" position="565,832" size="170,102" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" scale="1" position="1040,832" size="170,102" zPosition="3" alphatest="blend" cornerRadius="20">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" scale="1" position="1224,832" size="170,102" alphatest="blend" zPosition="3" cornerRadius="20" />
  <!-- Icons VideoWidth  -->
  <widget text="UHD" render="FixedLabel" source="session.CurrentService" position="189,900" size="90,40" font="Bold;40" foregroundColor="#deff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsUHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="FHD" render="FixedLabel" source="session.CurrentService" position="189,900" size="90,40" shadowOffset="4,3" font="Bold;35" foregroundColor="#fec000" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsFHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="HD" render="FixedLabel" source="session.CurrentService" position="189,900" size="90,40" font="Bold;35" foregroundColor="green" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsHD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="SD" render="FixedLabel" source="session.CurrentService" position="189,900" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickSignalServiceInfo">IsSD</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="16:9" render="FixedLabel" source="session.CurrentService" position="277,900" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget text="4:3" render="FixedLabel" source="session.CurrentService" position="277,900" size="90,40" font="Bold;35" foregroundColor="#ffffff" backgroundColor="#40000000" valign="center" halign="center" transparent="1" zPosition="3">
    <convert type="RaedQuickSignalServiceInfo">IsWidescreen</convert>
    <convert type="ConditionalShowHide">Invert</convert>
  </widget>
  <!-- IsFta  -->
  <widget source="session.CurrentService" render="FixedLabel" text="{4}" position="733,837" size="300,38" zPosition="4" font="{0};30" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">IsFta</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{5}" position="733,837" size="300,38" zPosition="5" font="{0};30" halign="center" valign="center" foregroundColor="#6f9ef5" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Emu</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{6}" position="733,837" size="300,38" zPosition="6" font="{0};30" halign="center" valign="center" foregroundColor="#7b68ee" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Crd</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.CurrentService" render="FixedLabel" text="{7}" position="733,837" size="300,38" zPosition="7" font="{0};30" halign="center" valign="center" foregroundColor="#5a115" backgroundColor="#16000000" transparent="1">
    <convert type="RaedQuickSignalCaidInfo2">Net</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1406,813" size="500,66" font="{0}; 25" halign="center" backgroundColor="#00000000" foregroundColor="#fec000" shadowOffset="3,2" transparent="1" cornerRadius="37" valign="bottom" borderWidth="2" borderColor="#00000000">
    <convert type="RaedQuickServName2">%F %p %Y %f %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1407,886" size="499,60" font="{0}; 25" halign="center" backgroundColor="#54111112" foregroundColor="#bbbbbb" transparent="1" cornerRadius="37" valign="bottom">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="1505,596" size="395,50" zPosition="1" font="{0};24" halign="right" backgroundColor="#2444444" foregroundColor="#41ff9900" transparent="1" cornerRadius="37" valign="center" />
  <widget name="Positioner" position="18,596" size="390,50" zPosition="1" font="{0};22" halign="left" backgroundColor="#00000000" foregroundColor="#41ff9900" transparent="1" cornerRadius="37" valign="center" />
  {2}
</screen>
""".format(FontName, resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal"), title41, title42, title80, title81, title82, title83, title84, title85, title86, title87)
### SKIN_Picons#------------------------------------------------------skin author:By BO-HLALA.FHD--.. ^_^ ------38--------------------------------------------------------