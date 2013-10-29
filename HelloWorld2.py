
# This class implements a window with two buttons.
# The buttons each print their names to the console.

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld2():

    def __init__(self):
        # Create necessary objects
        self.window  = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.box1    = gtk.HBox(False, 0)
        self.button1 = gtk.Button('Button 1')
        self.button2 = gtk.Button('Button 2')
        
        # Set Window attributes
        self.window.set_title('Button Window')
        self.window.set_border_width(10)
        self.window.connect('delete_event', self.delete_event)

        # Set button attributes
        self.button1.connect('clicked', self.callback, 'Button 1')
        self.button2.connect('clicked', self.callback, 'Button 2')

        # Add buttons to the box
        self.box1.pack_start(self.button1, True, True, 10)
        self.box1.pack_start(self.button2, True, True, 10)

        # Add the box to the window
        self.window.add(self.box1)

        # Show all elements
        self.button1.show()
        self.button2.show()
        self.box1.show()
        self.window.show()

    def callback(self, widget, data):
        print '%s was pressed!'%data

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

def main():
    HelloWorld2()
    gtk.main()
