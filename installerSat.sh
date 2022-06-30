#!/bin/bash
##setup command=wget -q "--no-check-certificate" https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/installerSat.sh -O - | /bin/sh

BRANDOS=/var/lib/dpkg/status
BRANDVU=/proc/stb/info/vumodel
BlackHole=/usr/lib/enigma2/python/Blackhole/BhAddons.pyo
VTI=/usr/lib/enigma2/python/Plugins/SystemPlugins/VTIPanel/plugin.pyo
BRANATV=/usr/lib/enigma2/python/boxbranding.so
BRANDOPEN=/usr/lib/enigma2/python/Tools/StbHardware.pyo

rm -f /tmp/OSdream-Satfinder-5.7-RAED.tar.gz > /dev/null 2>&1
rm -f /tmp/Signalfinder-2.4.tar.gz > /dev/null 2>&1

if [ ! -d /usr/lib64 ]; then
	SatfinderPATH=/usr/lib/enigma2/python/Plugins/SystemPlugins/Satfinder
	SignalfinderPATH=/usr/lib/enigma2/python/Plugins/SystemPlugins/Signalfinder
else
	SatfinderPATH=/usr/lib64/enigma2/python/Plugins/SystemPlugins/Satfinder
	SignalfinderPATH=/usr/lib64/enigma2/python/Plugins/SystemPlugins/Signalfinder
fi

cd /tmp
set -e

if [ -f $BRANDOPEN ] && [ ! -d $SatfinderPATH ]; then
	echo "*** open source images ***"
	opkg update && opkg install enigma2-plugin-systemplugins-satfinder
fi

if [ -f $BRANDOS ]; then
	echo "*** DreamOS images ***"
	[ -d $SatfinderPATH ] && rm -rf $SatfinderPATH > /dev/null 2>&1
	[ -d $SignalfinderPATH ] && rm -rf $SignalfinderPATH > /dev/null 2>&1
	wget -q "--no-check-certificate" https://github.com/fairbird/RaedQuickSignal/raw/main/OSdream-Satfinder-5.7-RAED.tar.gz
	tar -xzf OSdream-Satfinder-5.7-RAED.tar.gz -C /
elif [ -f $BRANDVU ] && [ -f $BlackHole  ] || [ -f $VTI ] ; then
	echo "*** BH or VTI images ***"
	[ -d $SatfinderPATH ] && rm -rf $SatfinderPATH > /dev/null 2>&1
	[ -d $SignalfinderPATH ] && rm -rf $SignalfinderPATH > /dev/null 2>&1
	wget -q "--no-check-certificate" https://github.com/fairbird/RaedQuickSignal/raw/main/Signalfinder-2.4.tar.gz
	tar -xzf Signalfinder-2.4.tar.gz -C / > /dev/null 2>&1
fi
set +e
cd ..
sleep 2
##################################
rm -f /tmp/*.tar.gz > /dev/null 2>&1
sync
echo ""
echo ""
echo "#########################################################"
echo "#       RaedQuickSignal INSTALLED SUCCESSFULLY          #"
echo "#                 Raed  (fairbird)                      #"              
echo "#                     support                           #"
echo "#  https://www.tunisia-sat.com/forums/threads/2890989   #"
echo "#########################################################"
echo "#           your Device will RESTART Now                #"
echo "#########################################################"
sleep 3
killall -9 enigma2
exit 0
