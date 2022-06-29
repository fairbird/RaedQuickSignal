#!/bin/sh
##setup command=wget -q "--no-check-certificate" https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/installer._Version8.8.sh -O - | /bin/sh

version=8.8
description=old version 8.8

BACKUPPATH=/tmp/Backup
PLUGINPICONTMPPATH=/tmp/RaedQuickSignal

if [ ! -d /usr/lib64 ]; then
	PLUGINPATH=/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal
else
	PLUGINPATH=/usr/lib64/enigma2/python/Plugins/Extensions/RaedQuickSignal
fi

# check depends packges
if [ -f /var/lib/dpkg/status ]; then
   STATUS=/var/lib/dpkg/status
   OSTYPE=DreamOs
else
   STATUS=/var/lib/opkg/status
   OSTYPE=Dream
fi

if python --version 2>&1 | grep -q '^Python 3\.'; then
	echo "You have Python3 image"
	PYTHON=PY3
	Package=python3-six
else
	echo "You have Python2 image"
	PYTHON=PY2
	Package=python-six
fi

if grep -qs "Package: $Package" cat $STATUS ; then
	echo ""
else
	echo "Need to install $Package"
	echo ""
	if [ $OSTYPE = "DreamOs" ]; then
		apt-get update && apt-get install python-six -y
	elif [ $PYTHON = "PY3" ]; then
		opkg update && opkg install python3-six
	elif [ $PYTHON = "PY2" ]; then
		opkg update && opkg install python-six
	fi
fi
echo ""
#if grep -qs 'Package: python-six' cat $STATUS ; then
#     echo "python-six Installed"
#else
#     echo "Missing (python-six) package"
#     echo "You need first to install it then install plugin again"
#exit 1
#fi
echo ""
## Remove old file from tmp directory
[ -d $BACKUPPATH ] && rm -rf $BACKUPPATH
[ -d $PLUGINPICONTMPPATH ] && rm -rf $PLUGINPICONTMPPATH
[ -r /tmp/RaedQuickSignal-"$version".tar.gz ] && rm -f /tmp/RaedQuickSignal-"$version".tar.gz
[ -r /tmp/RaedQuickServName2-dreamos.tar.gz ] && rm -f /tmp/RaedQuickServName2-dreamos.tar.gz
### backup Current files/Folders and save it beffore delete old version of plugin
mkdir -p $BACKUPPATH
[ -r $PLUGINPATH/keymap.xml ] && cp -f $PLUGINPATH/keymap.xml $BACKUPPATH/keymap.xml

[ -d $PLUGINPATH/emu ] && cp -r $PLUGINPATH/emu $BACKUPPATH
[ -d $PLUGINPATH/weather ] && cp -r $PLUGINPATH/weather $BACKUPPATH
[ -d $PLUGINPATH/piconSat ] && cp -r $PLUGINPATH/piconSat $BACKUPPATH
[ -d $PLUGINPATH/piconSat ] && cp -r $PLUGINPATH/piconSat $BACKUPPATH
[ -d $PLUGINPATH/piconProv ] && cp -r $PLUGINPATH/piconProv $BACKUPPATH
[ -d $PLUGINPATH/piconCrypt ] && cp -r $PLUGINPATH/piconCrypt $BACKUPPATH
[ -d $PLUGINPATH/PICONS/emu ] && cp -r $PLUGINPATH/PICONS/emu $BACKUPPATH
[ -d $PLUGINPATH/PICONS/weather ] && cp -r $PLUGINPATH/PICONS/weather $BACKUPPATH
[ -d $PLUGINPATH/PICONS/piconSat ] && cp -r $PLUGINPATH/PICONS/piconSat $BACKUPPATH
[ -d $PLUGINPATH/PICONS/piconProv ] && cp -r $PLUGINPATH/PICONS/piconProv $BACKUPPATH
[ -d $PLUGINPATH/PICONS/piconCrypt ] && cp -r $PLUGINPATH/PICONS/piconCrypt $BACKUPPATH

[ -r $PLUGINPATH ] && rm -rf $PLUGINPATH
# Download and install plugin + converter files
# check depends packges
cd /tmp
set -e
wget --no-check-certificate https://github.com/fairbird/RaedQuickSignal/raw/main/RaedQuickSignal-8.8_old_devices.tar.gz
tar -xzf RaedQuickSignal-8.8_old_devices.tar.gz -C /
set +e
cd ..
sleep 2
mkdir -p $PLUGINPATH/PICONS
### move backup files/Folders save to plugin
[ -r $BACKUPPATH/keymap.xml ] && mv $BACKUPPATH/keymap.xml $PLUGINPATH
[ -d $BACKUPPATH/emu ] && mv $BACKUPPATH/emu $PLUGINPATH/PICONS
[ -d $BACKUPPATH/weather ] && mv $BACKUPPATH/weather $PLUGINPATH/PICONS
[ -d $BACKUPPATH/piconSat ] && mv $BACKUPPATH/piconSat $PLUGINPATH/PICONS
[ -d $BACKUPPATH/piconProv ] && mv $BACKUPPATH/piconProv $PLUGINPATH/PICONS
[ -d $BACKUPPATH/piconCrypt ] && mv $BACKUPPATH/piconCrypt $PLUGINPATH/PICONS
### Checking if picons folder avinable on plugin
if [ ! -d $PLUGINPATH/PICONS/emu ]; then
	echo "Missing emu folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/emu $PLUGINPATH/PICONS
else
	cp -u $PLUGINPICONTMPPATH/emu/* $PLUGINPATH/PICONS/emu
fi
if [ ! -d $PLUGINPATH/PICONS/piconProv ]; then
	echo "Missing piconProv folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/piconProv $PLUGINPATH/PICONS
else
	cp -u $PLUGINPICONTMPPATH/piconProv/* $PLUGINPATH/PICONS/piconProv
fi
if [ ! -d $PLUGINPATH/PICONS/piconSat ]; then
	echo "Missing piconSat folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/piconSat $PLUGINPATH/PICONS
else
	cp -u $PLUGINPICONTMPPATH/piconSat/* $PLUGINPATH/PICONS/piconSat
fi
if [ ! -d $PLUGINPATH/PICONS/weather ]; then
	echo "Missing weather folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/weather $PLUGINPATH/PICONS
else
	cp -u $PLUGINPICONTMPPATH/weather/* $PLUGINPATH/PICONS/weather
fi
if [ ! -d $PLUGINPATH/PICONS/piconCrypt ]; then
	echo "Missing piconCrypt folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/piconCrypt $PLUGINPATH/PICONS
else
	cp -u $PLUGINPICONTMPPATH/piconCrypt/* $PLUGINPATH/PICONS/piconCrypt
fi
rm -rf $PLUGINPICONTMPPATH
rm -rf $BACKUPPATH
rm -f /tmp/RaedQuickSignal-"$version".tar.gz
rm -f /tmp/RaedQuickServName2-dreamos.tar.gz
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
