
for image in $(ls $1 |grep png && ls $1 | grep jpg):
do
	w=$(identify "$1$image" | awk '{print $3}'|awk -F'x' '{print $1}')
	h=$(identify "$1$image" | awk '{print $3}'|awk -F'x' '{print $2}')
	#echo $w
	#echo $h
	if [ $w -gt $h ] && [ $w -gt 1500 ] && [ $h -gt 1000 ];then
		cp "$1$image" $2
	fi
done
