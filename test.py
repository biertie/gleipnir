import dbus
import dbus.mainloop.glib
import gobject

bus = dbus.SystemBus()
dbus_object = bus.get_object('com.nokia.phone.net', '/com/nokia/phone/net')
cellinfo = dbus.Interface(dbus_object, 'Phone.Net')
foo = cellinfo.get_registration_status()

#print "cell id: " + cellid
#print "lac: " + lac

