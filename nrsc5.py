#!/usr/bin/python3

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

global station
global artist
global title
global oldartist
global oldtitle
global upd
station = ''
oldartist = ''
oldtitle  = ''
upd = 0

store = Gtk.ListStore(str, str, str)
treeview = Gtk.TreeView(model=store)

renderer_Station = Gtk.CellRendererText()
column_Station = Gtk.TreeViewColumn("Station", renderer_Station, text=0)
treeview.append_column(column_Station)

renderer_Artist = Gtk.CellRendererText()
column_Artist = Gtk.TreeViewColumn("Artist", renderer_Artist, text=1)
treeview.append_column(column_Artist)

renderer_Title = Gtk.CellRendererText()
column_Title = Gtk.TreeViewColumn("Title", renderer_Title, text=2)
treeview.append_column(column_Title)

def mainloop():
  
   global station
   global artist
   global title
   global oldtitle
   global oldartist
   global upd
   
   count = 0
   for line in sys.stdin:
      count = count + 1
      if "Title:" in line:
         title = line.split("Title: ",1)[1].rstrip()
         if title != oldtitle:
            upd = upd + 1
            oldtitle = title
      elif "Artist:" in line:
         artist = line.split("Artist: ",1)[1].rstrip()
         if artist != oldartist:
            upd = upd + 1
            oldartist = artist
      elif "Station Name:" in line:
         station = line.split("Station Name: ",1)[1].rstrip()

      if upd == 2:
         store.clear()
         store.append([station, artist, title])
         upd = 0
         return (True)
 
      if count == 10:
         return (True)

win = Gtk.Window()
win.add(treeview)

win.set_default_size(425,75)
win.set_title('NRSC-5 Metadata by K2DLS v 0.1')
win.connect("delete-event", Gtk.main_quit)
win.show_all()
GObject.idle_add(mainloop)
Gtk.main()
