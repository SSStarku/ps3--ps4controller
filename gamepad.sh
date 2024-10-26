#!/bin/sh
GREEN='\033[1;31m'
NORMAL='\033[0;37m'
echo -e "${GREEN}please connect the ps3 controller via usb${NORMAL}"
sleep 2
echo -e "${GREEN}installing libraries...${NORMAL}"
sudo pip3 install vgamepad  --break-system-packages
echo -e "${GREEN}vgamepad installed!${NORMAL}"
sudo pip3 install approxeng.input --break-system-packages
echo -e "${GREEN}input installed!${NORMAL}"
echo -e "${GREEN}putting everything in order...${NORMAL}"
sudo apt-get install bluetooth libbluetooth3 libusb-dev
sed -i~ 'ClassicBondedOnly=false' /etc/bluetooth/input.conf
sudo systemctl enable bluetooth.service
sudo usermod -G bluetooth -a pi
echo -e "${GREEN}installing sixpair...${NORMAL}"
sudo wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb
echo -e "${GREEN}connect the ps3 controller via usb ${NORMAL}"
echo -e "${GREEN}10${NORMAL}"
sleep 1
echo -e "${GREEN}9${NORMAL}"
sleep 1
echo -e "${GREEN}8${NORMAL}"
sleep 1
echo -e "${GREEN}7${NORMAL}"
sleep 1
echo -e "${GREEN}6${NORMAL}"
sleep 1
echo -e "${GREEN}5${NORMAL}"
sleep 1
echo -e "${GREEN}4${NORMAL}"
sleep 1
echo -e "${GREEN}3${NORMAL}"
sleep 1
echo -e "${GREEN}2${NORMAL}"
sleep 1
echo -e "${GREEN}1${NORMAL}"
sleep 1
sudo ./sixpair
echo -e "${GREEN}disconect the ps3 controller and press the button ps${NORMAL}"
sleep 5
echo -e "${GREEN}trying conecting to ps3 controler with bluetoothctl${NORMAL}${NORMAL}"
bluetoothctl <<EOF
agent on
pair 00:21:4F:1E:2C:FC
exit
EOF
echo -e "${GREEN}ps3 controller conected successfully!!!${NORMAL}"
sleep 2
echo -e "${GREEN}now try the ps3-ps4.py${NORMAL}"
sleep 2


