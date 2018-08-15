#! /bin/sh

python3 envmaker.py
mv env /etc/sysconfig/sa-papayabotd
ln -s ./sa-papayabotd.service /etc/systemd/system
