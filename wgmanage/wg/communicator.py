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

from contextlib import contextmanager

import locale
import shlex
import subprocess
from typing import Union, ContextManager


class ProcessError(Exception):
    """Raises when process return anything in stderr pipe"""
    pass


class Communicator(object):
    """`Pipe` emulation class"""

    def __init__(self, pipe: subprocess.Popen):
        self._pipe = pipe

    def communicate(self, command_input: str = None, timeout: int = 60) -> Union[str, None]:
        """
        Send input to process, read output and stderr channels,
        raises ProcessError if stderr value is not empty

        :param command_input: Value that `communicate` sends to process stdin
        :param timeout: Response wait timeout
        :return Value from process stdout
        """
        try:
            output, error = self._pipe.communicate(input=command_input, timeout=timeout)
            if len(error) > 0:
                raise ProcessError(error.strip())
            return output.strip()
        except ValueError:
            return None


@contextmanager
def execute(command: str, shell: bool = False) -> ContextManager[Communicator]:
    """Execute shell command in context manager style"""
    command = shlex.split(command)
    _lang, encoding = locale.getlocale()
    proc = subprocess.Popen(command,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=shell,
                            encoding=encoding)
    try:
        yield Communicator(proc)
    finally:
        return proc.wait()
