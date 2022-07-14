#!/bin/sh
##setup command=wget -q "--no-check-certificate" https://raw.githubusercontent.com/fairbird/RaedQuickSignal/picons/main/installerBlackPicons.sh -O - | /bin/sh
## This script to downlaod and install Black Picon by () to inside plugin

if [ ! -d /usr/lib64 ]; then
	PLUGINPATH=/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal
else
	PLUGINPATH=/usr/lib64/enigma2/python/Plugins/Extensions/RaedQuickSignal
fi

## Remove old file from tmp directory
[ -r /tmp/BlackPicons.tar.gz ] && rm -f /tmp/BlackPicons.tar.gz

### Remove Currenty file from plugin
rm -rf $PLUGINPATH/PICONS/emu
rm -rf $PLUGINPATH/PICONS/piconSat
rm -rf $PLUGINPATH/PICONS/piconProv
rm -rf $PLUGINPATH/PICONS/piconCrypt

# Download and install Black Picon
cd /tmp
set -e
wget -q "--no-check-certificate" https://github.com/fairbird/RaedQuickSignal/picons/raw/main/BlackPicons.tar.gz
tar -xzf BlackPicons.tar.gz -C /
set +e
cd ..

### delete tmp files
rm -f /tmp/BlackPicons.tar.gz
sync
echo ""
echo ""
echo "#########################################################"
echo "#       RaedQuickSignal INSTALLED SUCCESSFULLY          #"
echo "#                 Raed  (fairbird)                      #"              
echo "#                     support                           #"
echo "#  https://www.tunisia-sat.com/forums/threads/2890989   #"
echo "#########################################################"
echo ""
echo ""
echo "#########################################################"
echo "#            Press ok to Exit from Console              #"
echo "#########################################################"
exit 0
