import network
import config
import time
import ntptime

def SortKey(e):
    return e[3]

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
hspots = wlan.scan()             # scan for access points
hspots.sort(key=SortKey)
for h in hspots:
    if(h[0]==b''):
        print(h)
    else:
        print(h[0].decode() + ',' + str(h[3]))
print()
print(str(len(hspots)) + " Hot Spots Found")
while not wlan.isconnected():      # check if the station is connected to an AP
    wlan.connect(config.ssid, config.password) # connect to an AP
    if not wlan.isconnected():
        print('...waiting...')
        time.sleep(5)

print("IP/netmask/gw/DNS addresses")
print(wlan.ifconfig()[0])         # get the interface's IP

print("Local time before synchronization：%s" %str(time.localtime()))
ntptime.settime()
print("Local time after synchronization：%s" %str(time.localtime()))
wlan.disconnect()

