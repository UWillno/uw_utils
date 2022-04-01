#/bin/sh
unset http_proxy
unset https_proxy
if [ ! -d "${2}temp" ];then
	mkdir "${2}temp"
fi
cd ${2}temp
temp=temp.m3u8
wget -O "temp.m3u8" "$1"
sed -i '/^#/d' $temp
i=1
l=$(cat "$temp"| wc -l)
while read line
do
	b=$i
	while [ ${#b} -lt ${#l} ];
	do
		b="0$b"
	done
	wget -O "$b" "$line"
	dd if="$b" of=$b.ts bs=4 skip=53
	let i++
done < $temp
all=$(ls -l *.ts | awk -F" " '{print $9}' | tr '\n' '|'| sed 's/.$//')
ffmpeg -i "concat:$all" -vcodec copy "$2.mp4"
mv "$2.mp4" ..
cd ..
rm -rf "${2}temp"
echo "$date下载完成"
