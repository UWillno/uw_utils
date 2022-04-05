if [[ $(cat $1) != *https* ]];then sed -i "s#^#$2#g" $1; fi
