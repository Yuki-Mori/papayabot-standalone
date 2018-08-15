#! /bin/sh

python3 envmaker.py
mv env /etc/sysconfig/sa-papayabotd
cp ./sa-papayabotd.service /etc/systemd/system/
