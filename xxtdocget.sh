http=$1
name=$2
mkdir $2
cd $2
wget -O "html" $http
cat "html" | grep .png | cut -d '"' -f2 > pngurls
cat pngurls | xargs -n 1 -P 10 wget
