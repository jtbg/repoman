#!/usr/bin/python3
'''
   Copyright 2022 Ian Santopietro (ian@system76.com)

   This file is part of Repoman.

    Repoman is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Repoman is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Repoman.  If not, see <http://www.gnu.org/licenses/>.

    This is the Application for installing local flatpaks.
'''
import sys
from pathlib import Path

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

try:
    from systemd.journal import JournalHandler
except ImportError:
    JournalHandler = False

from .dialog import InstallDialog

def do_open(app, files, *hint):
    print(f'app: {app}')
    print(f'files: {files}')
    print(f'hint: {hint}')

    install_dialog = InstallDialog(None)
    install_dialog.file_button.set_filename(files[0].get_path())
    install_dialog.set_install_sensitive(install_dialog.file_button)
    install_dialog.file_button.set_sensitive(False)
    install_dialog.run()
    install_dialog.destroy()

def do_activate(app):
    print(f'Activate app {app}')

fp_installer = Gtk.Application(
    application_id='com.system76.Repoman.FlatpakInstaller',
    flags=Gio.ApplicationFlags.HANDLES_OPEN
)
fp_installer.set_inactivity_timeout(10000)
fp_installer.connect('open', do_open)
fp_installer.connect('activate', do_activate)
fp_installer.run(sys.argv)
