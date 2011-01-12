#! /usr/bin/env python
# -*- coding: utf-8 -*-
#profilechanger for n900
#copyright 2010 devnox-it.com by Bert Desmet <bert@devnox-it.com>
#http://opensource.devnox-it.com
#This software is released under the GPL3+ licence

import dbus
import dbus.mainloop.glib
import gobject
from threading import Thread
from time import sleep, time
from cellinfo import CellInfo
from sys import exit
from osso import Context, DeviceState
from helper import array_value

def add_signals():
    global bus

    try:
        bus.add_signal_receiver(signal_cell_info_change, dbus_interface = "Phone.Net", signal_name = "cell_info_change")
    except:
        return False
    return true

def main():
    global bus
    global cell
    global lac
    global ruleset

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=true)
    bus = dbus.SystemBus()
    add_signals()


    

if __name__ == "__main__":
    ret = main()
    exit(ret)
