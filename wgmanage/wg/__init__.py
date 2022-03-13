# This file is part of the wgmanage distibution
# Copyright (C) 2021 Alexander Zakharov
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

from wgmanage.wg.communicator import execute


def generate_private_key() -> str:
    """Generate and return private key"""
    with execute('wg genkey') as pipe:
        key = pipe.communicate()
        return key


def get_public_key(private_key: str) -> str:
    """Generate public key from private key and return it"""
    with execute('wg pubkey') as pipe:
        key = pipe.communicate(private_key)
        return key


def generate_psk() -> str:
    """Generate pre-shared key"""
    with execute('wg genpsk') as pipe:
        key = pipe.communicate()
        return key
