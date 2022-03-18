i=0
while read line
do
	let i++
	wget $line -O $i
done < $1
