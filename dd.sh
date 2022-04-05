#
file=$1
dd if="${file}" of="${file}.1" bs=4 skip=53
mv -f "${file}.1" ${file}
