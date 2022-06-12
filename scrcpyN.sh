adb kill-server
adb shell ifconfig wlan0
if [ $? -eq 0 ]; then 
ip=$(adb shell ifconfig wlan0 | awk NR==2 | awk -F":" '{print $2}'| awk -F" " '{print $1}')
adb tcpip 5555
echo "可以拔掉数据线了"
scrcpy --tcpip=$ip 
else
adb devices
read -p "输入设备名称:" name
ip=$(adb -s $name shell ifconfig wlan0 | awk NR==2 | awk -F":" '{print $2}'| awk -F" " '{print $1}')
adb -s $name tcpip 5555 
echo "可以拔掉数据线了"
scrcpy --tcpip=$ip 
fi
