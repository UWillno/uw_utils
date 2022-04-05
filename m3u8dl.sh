#/bin/sh
unset http_proxy
unset https_proxy
temp=$1
if [[ $temp == *http* ]];then
    wget "$temp"
    temp=$(echo $temp |awk -F/ '{print $NF}')
fi
if [ ! -d "${temp}temp" ];then
	mkdir "${temp}temp"
fi
cp -rf $temp ${temp}temp/
cp -rf dd.sh ${temp}temp/
cd ${temp}temp
sed -i '/^#/d' $temp
# wget -O "temp.m3u8" "$1"
# sed -i '/^#/d' $temp
# i=1
# l=$(cat "$temp"| wc -l)

# while read line
# do
# 	b=$i
# 	while [ ${#b} -lt ${#l} ];
# 	do
# 		b="0$b"
# 	done
# 	
# 	wget -O "$b.ts" "$line" -b
# 	dd if="$b" of=$b.ts bs=4 skip=53
# 	let i++
# done < $temp

cat $temp | xargs -n 1 -P 100 wget -q
# rm $temp
cat $temp | awk -F/ '{printf "file #%s#\n",$NF}'>video.txt
# ls -l *.$tx | awk '{printf "file #%s#\n",$9}'
sed -i "s/#/'/g" video.txt
test=$(head -1 $temp|awk -F/ '{print $NF}')
chmod +x dd.sh
echo 分段下载完成
if [[ $(hexdump -C -n4 $test ) == *PNG* ]];then 
    echo 是png格式
    awk -F/ '{print $NF}' $temp | xargs -n 1 -P 100 ./dd.sh
fi
echo 开始合并
ffmpeg -f concat -i video.txt -vcodec copy "$temp.mp4"
mv "$temp.mp4" ..
cd ..
rm -rf "${temp}temp"
echo "$date下载完成"
