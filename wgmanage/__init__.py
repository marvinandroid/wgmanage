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
import shlex
import sys

from wgmanage.shell import WGManage


def main(args: tuple = tuple(sys.argv[1:])) -> int:
    """
    Main application entry point

    :param args: Command arguments
    :return: Exit code
    """
    app = WGManage()
    return app.run(args)


if __name__ == '__main__':
    sys.exit(main())
