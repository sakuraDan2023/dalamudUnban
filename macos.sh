#!/bin/bash

cd $(dirname "$(realpath "${BASH_SOURCE[0]}")")
chmod +x ./src/core/mitmdump
#set system proxy
networksetup -setwebproxy Ethernet 127.0.0.1 3000
networksetup -setsecurewebproxy Ethernet 127.0.0.1 3000
#system proxy on
networksetup -setwebproxystate Ethernet on
networksetup -setsecurewebproxystate Ethernet on
#no other vpn used
./core/mitmdump --listen-host 127.0.0.1 -p 3000 -s ./src/main.py --set termlog_verbosity=error --flow-detail 0
#upstream mode
#./core/mitmdump --listen-host 127.0.0.1 -p 3000 -s ./src/main.py --set termlog_verbosity=error --flow-detail 0 --mode=upstream:http://127.0.0.1:7890
