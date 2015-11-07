	
	
	http://askubuntu.com/questions/472794/hostapd-error-nl80211-could-not-configure-driver-mode
As @bain has rightly pointed out, there is a bug raised in launchpad for this very purpose. This workaround suggested there works perfectly for me:

sudo nmcli nm wifi off
sudo rfkill unblock wlan


http://superuser.com/a/152830

#!/bin/bash
IPTABLES=/sbin/iptables

#start and flush
$IPTABLES -F
$IPTABLES -t nat -F
$IPTABLES -X
$IPTABLES -P FORWARD DROP
$IPTABLES -P INPUT   DROP
$IPTABLES -P OUTPUT  ACCEPT

#SSH traffic
$IPTABLES -A INPUT -p tcp --dport 22 -j ACCEPT
#HTTP traffic
$IPTABLES -A INPUT -p tcp --dport 80 -j ACCEPT

#loopback
iptables -A INPUT -i lo -p all -j ACCEPT



http://snikt.net/blog/2014/01/26/transparent-ssl-proxy-with-squid/
$ sudo iptables -t nat -A PREROUTING -i wlan1 -p tcp -m tcp --dport 443 -j DNAT --to-destination 127.0.0.1:3127

SET UP DRIVER
http://ubuntuhandbook.org/index.php/2014/09/wifi-hotspot-access-point-not-supported/


# SSL
openssl req -x509 -newkey rsa:2048 -keyout server.pem -out server.crt -days 3650 -nodes -subj "/C=US/ST=Oregon/L=Bend/O=SUNA/OU=Org/CN=www.sunasunasuna.com"
