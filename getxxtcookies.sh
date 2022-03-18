read -p "输入你的学习通账号：" uname
read -p "输入你的密码：" password
curl -A "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.0)" -d "uname=$uname&password=$password" -X POST https://passport2.chaoxing.com/fanyalogin -c cookies.txt
echo -e "\n若以上信息含有true，且目录下出现cookies.txt即登录成功"