start=$1
end=$2
name=$3
url=$4
mkdir $name
cd $name
while(( $start <= $end ))
do
	temp=$(echo $url | awk -F"=" '{print $1}')
	temp="$temp"=$start
	you-get "$temp"
	#echo $temp
	let start++
done
