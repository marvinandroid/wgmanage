# This file is part of the wgmanage distibution
# Copyright (C) 2022 Alexander Zakharov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os

from cliff.app import App
from cliff.commandmanager import CommandManager

from wgmanage.core import get_version, DESCRIPTION
from wgmanage.database import db


class WGManage(App):
    """WGManage main application"""

    def __init__(self):
        super().__init__(
            description=DESCRIPTION,
            version=get_version(),
            command_manager=CommandManager('wgmanage.cli')
        )

    def build_option_parser(self,
                            description,
                            version,
                            argparse_kwargs=None):
        """Builds top-level option parser"""
        parser = super().build_option_parser(description, version, argparse_kwargs=argparse_kwargs)
        parser.add_argument('--database', '-d', help='WGManage database file (default /etc/wireguard/wgmanage.db',
                            default='/etc/wireguard/wgmanage.db')
        return parser

    def initialize_app(self, argv):
        """Set wgmanage database uri before main application starts"""
        if not os.access(self.options.database, os.W_OK):
            self.LOG.fatal('Unable to access database file. Maybe you should run script as root')
            exit(1)
        os.putenv('WGMANAGE_DATABSE', self.options.database)
