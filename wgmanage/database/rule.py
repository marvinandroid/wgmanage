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

from peewee import PrimaryKeyField, CharField, DateTimeField, ForeignKeyField, TextField, IntegerField

from wgmanage.database.base_model import BaseModel
from wgmanage.database.server import Server


class Rule(BaseModel):
    """Server-side iptables rules"""

    id = PrimaryKeyField(null=False)
    name = CharField(null=False)
    description = TextField(null=True)
    rule_order = IntegerField(null=False)
    post_up_command = TextField(null=False)
    post_down_command = TextField(null=False)
    server = ForeignKeyField(Server, backref='rules', on_delete='CASCADE')
    
    created_at = DateTimeField(null=False, default=datetime.now)

