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

from peewee import Model

from wgmanage.database import db
from wgmanage.wg import generate_private_key, generate_psk, get_public_key


class BaseModel(Model):
    """Base model for convenient access"""

    class Meta:
        database = db


class BasePeerModel(BaseModel):
    """Base model for peers - servers, clients"""

    def generate_keys(self, generate_psk_key: bool = False):
        """
        Generates private/public/pre-shared keys

        :param generate_psk_key: Indicates
        """
        self.private_key = generate_private_key()
        self.public_key = get_public_key(self.private_key)
        if generate_psk_key and hasattr(self, 'preshared_key'):
            self.preshared_key = generate_psk()
