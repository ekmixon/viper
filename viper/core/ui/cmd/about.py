# -*- coding: utf-8 -*-
# This file is part of Viper - https://github.com/viper-framework/viper
# See the file 'LICENSE' for copying permission.

import os
import platform

from viper.common.abstracts import Command
from viper.common.version import __version__
from viper.core.database import Database
from viper.core.config import __config__
from viper.core.project import __project__


class About(Command):
    """
    This command prints some useful information regarding the running
    Viper instance
    """
    cmd = "about"
    description = "Show information about this Viper instance"

    def run(self, *args):
        try:
            self.parser.parse_args(args)
        except SystemExit:
            return

        rows = [
            ["Viper Version", __version__],
            ["Python Version", platform.python_version()],
            ["Homepage", "https://viper.li"],
            ["Issue Tracker", "https://github.com/viper-framework/viper/issues"],
        ]

        self.log('table', dict(header=['About', ''], rows=rows))

        rows = [["Configuration File", __config__.config_file]]
        module_path = os.path.join(__config__.paths.module_path, "modules")

        if __project__.name:
            rows.append(["Active Project", __project__.name])
        else:
            rows.append(["Active Project", "default"])
        rows.append(["Storage Path", __project__.path])
        rows.append(["Module Path", module_path])
        rows.append(["Database Path", Database().engine.url])
        self.log('table', dict(header=['Configuration', ''], rows=rows))
