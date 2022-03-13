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

from datetime import datetime

from peewee import PrimaryKeyField, CharField, TextField, DateTimeField, ForeignKeyField

from wgmanage.database.base_model import BasePeerModel
from wgmanage.database.server import Server


class Client(BasePeerModel):
    """Wireguard Client model"""

    id = PrimaryKeyField(null=False)
    name = CharField(null=False)
    private_key = CharField(null=False, max_length=64)
    public_key = CharField(null=False, max_length=64)
    preshared_key = CharField(max_length=64)
    description = TextField(null=True)
    dns = CharField(null=True)
    server = ForeignKeyField(Server, null=True, backref='clients')

    created_at = DateTimeField(null=False, default=datetime.now)

