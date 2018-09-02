#!/usr/bin/python
'''
MCGPUFI:
An accelerated targeted facet imager
Category: Radio Astronomy / Widefield synthesis imaging

Authors: Baoqiang Lao
Contact: lbq@shao.ac.cn
Copyright (C) 2018-2020
SHAO
China

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''

from gi.repository import Gtk,Gdk, GLib
from viewcontrollers import frmMain
import threading

if __name__ == "__main__":
  wnd = frmMain.frmMain()
  GLib.threads_init()
  #Gdk.threads_init()
  #Gdk.threads_enter()
  Gtk.main()
  #Gdk.threads_leave()
