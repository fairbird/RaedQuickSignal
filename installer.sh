#!/bin/bash
##setup command=wget -q "--no-check-certificate" https://raw.githubusercontent.com/fairbird/RaedQuickSignal/main/installer.sh -O - | /bin/sh

######### Only These two lines to edit with new version ######
version=17.8
description="What is NEW:\n- Add Russian language support\n- Remove the option to select the city name for the weather condition from the cities list (this option is no longer useful) and only rely on the manual option\n\n*************************\nما هو الجديد:\n- حذف خيار اختيار اسم المدينة لحالة الطقس من خلال قائمة المدن (لم يعد ينفع هذا الخيار) فقط الإعتماد على الخيار اليدوي\n- إضافة دعم اللغة الروسية"
##############################################################

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
echo ""
if [ -f /usr/bin/python3 ] ; then
	echo "You have Python3 image"
	PYTHON=PY3
	Packagesix=python3-six
	Packagerequests=python3-requests
else
	echo "You have Python2 image"
	PYTHON=PY2
	Packagerequests=python-requests
fi

if [ $PYTHON = "PY3" ]; then
	if grep -qs "Package: $Packagesix" cat $STATUS ; then
		echo ""
	else
		opkg update && opkg install python3-six
	fi
fi
echo ""
if grep -qs "Package: $Packagerequests" cat $STATUS ; then
	echo ""
else
	echo "Need to install $Packagerequests"
	echo ""
	if [ $OSTYPE = "DreamOs" ]; then
		apt-get update && apt-get install python-requests -y
	elif [ $PYTHON = "PY3" ]; then
		opkg update && opkg install python3-requests
	elif [ $PYTHON = "PY2" ]; then
		opkg update && opkg install python-requests
	fi
fi
echo ""
## Remove old file from tmp directory
[ -d $BACKUPPATH ] && rm -rf $BACKUPPATH
[ -d $PLUGINPICONTMPPATH ] && rm -rf $PLUGINPICONTMPPATH > /dev/null 2>&1
[ -r /tmp/RaedQuickSignal-"$version".tar.gz ] && rm -f /tmp/RaedQuickSignal-"$version".tar.gz > /dev/null 2>&1
[ -r /tmp/RaedQuickServName2-dreamos.tar.gz ] && rm -f /tmp/RaedQuickServName2-dreamos.tar.gz > /dev/null 2>&1
### backup Current files/Folders and save it beffore delete old version of plugin
mkdir -p $BACKUPPATH
[ -r $PLUGINPATH/tools/keymap.xml ] && cp -f $PLUGINPATH/tools/keymap.xml $BACKUPPATH/keymap.xml > /dev/null 2>&1

[ -d $PLUGINPATH/PICONS/emu ] && cp -r $PLUGINPATH/PICONS/emu $BACKUPPATH > /dev/null 2>&1
[ -d $PLUGINPATH/PICONS/piconSat ] && cp -r $PLUGINPATH/PICONS/piconSat $BACKUPPATH > /dev/null 2>&1
[ -d $PLUGINPATH/PICONS/piconProv ] && cp -r $PLUGINPATH/PICONS/piconProv $BACKUPPATH > /dev/null 2>&1
[ -d $PLUGINPATH/PICONS/piconCrypt ] && cp -r $PLUGINPATH/PICONS/piconCrypt $BACKUPPATH > /dev/null 2>&1
[ -d $PLUGINPATH/PICONS/weather ] && cp -r $PLUGINPATH/PICONS/weather $BACKUPPATH > /dev/null 2>&1

[ -r $PLUGINPATH ] && rm -rf $PLUGINPATH
# Download and install plugin + converter files
# check depends packges
cd /tmp
set -e
rm -rf *RaedQuickSignal* > /dev/null 2>&1
if [ -f /var/lib/dpkg/status ]; then
   echo "# Your image is OE2.5/2.6 #"
   echo ""
   echo ""
   #cd /tmp
   #wget https://github.com/fairbird/RaedQuickSignal/archive/refs/heads/main.tar.gz
   #tar -xzf main.tar.gz
   #cp -r 'RaedQuickSignal-main/usr' '/'
   #cp -r 'RaedQuickSignal-main/tmp/RaedQuickSignal' '/tmp'
   #wget https://github.com/fairbird/RaedQuickSignal/raw/main/RaedQuickServName2-dreamos.tar.gz
   #if [ -f '/tmp/RaedQuickServName2-dreamos.tar.gz' ]; then
   #	rm -f /usr/lib/enigma2/python/Components/Converter/RaedQuickServName2.py > /dev/null 2>&1
   #fi
   #tar -xzf RaedQuickServName2-dreamos.tar.gz -C /
else
   echo "# Your image is OE2.0 #"
   echo ""
   echo ""
   #wget https://github.com/fairbird/RaedQuickSignal/archive/refs/heads/main.tar.gz
   #tar -xzf main.tar.gz
   #cp -r 'RaedQuickSignal-main/usr' '/'
   #cp -r 'RaedQuickSignal-main/tmp/RaedQuickSignal' '/tmp'
fi
wget https://github.com/fairbird/RaedQuickSignal/archive/refs/heads/main.tar.gz
tar -xzf main.tar.gz
cp -r 'RaedQuickSignal-main/usr' '/'
cp -r 'RaedQuickSignal-main/tmp/RaedQuickSignal' '/tmp'
set +e
cd ..
sleep 2

### Check if plugin installed correctly
if [ ! -d $PLUGINPATH ]; then
	echo "Some thing wrong .. Plugin not installed"
	exit 1
fi

mkdir -p $PLUGINPATH/PICONS
### move backup files/Folders save to plugin
[ -r $BACKUPPATH/keymap.xml ] && mv $BACKUPPATH/keymap.xml $PLUGINPATH/tools > /dev/null 2>&1
[ -d $BACKUPPATH/emu ] && mv $BACKUPPATH/emu $PLUGINPATH/PICONS > /dev/null 2>&1
[ -d $BACKUPPATH/piconSat ] && mv $BACKUPPATH/piconSat $PLUGINPATH/PICONS > /dev/null 2>&1
[ -d $BACKUPPATH/piconProv ] && mv $BACKUPPATH/piconProv $PLUGINPATH/PICONS > /dev/null 2>&1
[ -d $BACKUPPATH/piconCrypt ] && mv $BACKUPPATH/piconCrypt $PLUGINPATH/PICONS > /dev/null 2>&1
[ -d $BACKUPPATH/weather ] && mv $BACKUPPATH/weather $PLUGINPATH/PICONS > /dev/null 2>&1
### Checking if picons folder avinable on plugin
if [ ! -d $PLUGINPATH/PICONS/emu ]; then
	echo "Missing emu folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/emu $PLUGINPATH/PICONS > /dev/null 2>&1
else
	cp -u $PLUGINPICONTMPPATH/emu/* $PLUGINPATH/PICONS/emu > /dev/null 2>&1
fi
if [ ! -d $PLUGINPATH/PICONS/piconProv ]; then
	echo "Missing piconProv folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/piconProv $PLUGINPATH/PICONS > /dev/null 2>&1
else
	cp -u $PLUGINPICONTMPPATH/piconProv/* $PLUGINPATH/PICONS/piconProv > /dev/null 2>&1
fi
if [ ! -d $PLUGINPATH/PICONS/piconSat ]; then
	echo "Missing piconSat folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/piconSat $PLUGINPATH/PICONS > /dev/null 2>&1
else
	cp -u $PLUGINPICONTMPPATH/piconSat/* $PLUGINPATH/PICONS/piconSat > /dev/null 2>&1
fi
if [ ! -d $PLUGINPATH/PICONS/piconCrypt ]; then
	echo "Missing piconCrypt folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/piconCrypt $PLUGINPATH/PICONS > /dev/null 2>&1
else
	cp -u $PLUGINPICONTMPPATH/piconCrypt/* $PLUGINPATH/PICONS/piconCrypt > /dev/null 2>&1
fi
if [ ! -d $PLUGINPATH/PICONS/weather ]; then
	echo "Missing weather folder will be send it to plugin path"
	cp -r $PLUGINPICONTMPPATH/weather $PLUGINPATH/PICONS > /dev/null 2>&1
else
	cp -u $PLUGINPICONTMPPATH/weather/* $PLUGINPATH/PICONS/weather > /dev/null 2>&1
fi
rm -rf /tmp/*RaedQuickSignal* > /dev/null 2>&1
rm -rf /tmp/*main* > /dev/null 2>&1
rm -rf $PLUGINPICONTMPPATH > /dev/null 2>&1
rm -rf $BACKUPPATH > /dev/null 2>&1
rm -f /tmp/RaedQuickSignal-"$version".tar.gz > /dev/null 2>&1
rm -f /tmp/RaedQuickServName2-dreamos.tar.gz > /dev/null 2>&1
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
