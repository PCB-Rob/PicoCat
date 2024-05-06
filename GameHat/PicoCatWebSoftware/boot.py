# This file is executed on every boot
import config, rp2

rp2.country('US')  # change to your country code

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
        print("AP turned off ...")
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(config.ssid,config.password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig()[0])

print("Starting network ...")
do_connect()
