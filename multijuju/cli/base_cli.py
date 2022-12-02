# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2022 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""multijuju base cli command."""
from craft_cli import BaseCommand, emit


class BaseCLICommand(BaseCommand):
    """base cli command for handling contexts."""

    def run(self, parsed_args):
        self.before(parsed_args)
        self.execute(parsed_args)
        self.after(parsed_args)

    def execute(self, parsed_args):
        pass

    def before(self, parsed_args):
        emit.message("-----------------------------------------------------")

    def after(self, parsed_args):
        emit.message("-----------------------------------------------------")
