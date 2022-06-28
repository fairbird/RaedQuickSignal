#!/usr/bin/python
# -*- coding: utf-8 -*-
#RAEDQuickSignal (c) RAED 07-02-2014

from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import os

### Share path
SHAREPATH='/usr/share/enigma2/'
### Picons + Icons path
EMUPATH=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/PICONS/emu")
WEATHEPATH=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/PICONS/weather")
PICONSATPATH=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/PICONS/piconSat")
PICONPROVPATH=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/PICONS/piconProv")
PICONCRYPTPATH=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/PICONS/piconCrypt")

keymapfile='KEY_TEXT'
try:
	fp = open("/etc/enigma2/settings", "r").readlines()
	for line in fp:
		if "config.plugins.RaedQuickSignal.keyname" in line:
			keymapfile = line.split('=')[1].strip()
except:
	pass

try:
	if not os.path.exists(SHAREPATH + 'emu'):
		os.symlink(EMUPATH, SHAREPATH + 'emu')
	if not os.path.exists(SHAREPATH + 'weather'):
		os.symlink(WEATHEPATH, SHAREPATH + 'weather')
	if not os.path.exists(SHAREPATH + 'piconSat'):
		os.symlink(PICONSATPATH, SHAREPATH + 'piconSat')
	if not os.path.exists(SHAREPATH + 'piconProv'):
		os.symlink(PICONPROVPATH, SHAREPATH + 'piconProv')
	if not os.path.exists(SHAREPATH + 'piconCrypt'):
		os.symlink(PICONCRYPTPATH, SHAREPATH + 'piconCrypt')
except:
	pass

if os.path.exists('/usr/lib64/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml'):
	keyfile = open("/usr/lib64/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml", "w")
else:
	keyfile = open("/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml", "w")
keyfile.write('<keymap>\n\t<map context="GlobalActions">\n\t\t<key id="%s" mapto="showRaedQuickSignal" flags="m" />\n\t</map>\n</keymap>' % keymapfile)
keyfile.close()
