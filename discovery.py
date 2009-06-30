#!/usr/bin/env python

# discovery.py
# June 2009
# Terence Stenvold <tstenvold@gmail.com>
#
# Used for discoverying broadcasting Bluetooth devices and getting the services
# available on those devices.

import bluetooth
import deviceclass
import sys
import select
import sqlite

#This is really poorly done!
class harald_discoverer(bluetooth.DeviceDiscoverer):

    def pre_inquiry(self):
        self.done = False

    def device_discovered(self, addr, device_class, name):

        devclass = deviceclass.majordev_class(device_class)
        devman = sqlite.mac_resolve(addr)

        sqlite.insert_dev_table(addr, name, devclass, devman)

        #print "  %s - %s - %s" % (addr, name, devclass)

    def inquiry_complete(self):
        sqlite.write_dev_table('devices.txt')
        self.done = True


#Takes a mac address and tries to discover services available if in range.
#returns the service available or 0 if it couldn't find any
def service_discover(mac_addr):

    services = bluetooth.find_service(address=target)

    if len(services) > 0:
        return services
    else:
        return 0
