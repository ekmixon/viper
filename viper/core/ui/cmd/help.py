# -*- coding: utf-8 -*-
# This file is part of Viper - https://github.com/viper-framework/viper
# See the file "LICENSE" for copying permission.

from viper.common.abstracts import Command
from viper.core.plugins import load_commands, __modules__


class Help(Command):
    """
    This command simply prints the help message.
    It lists both embedded commands and loaded modules.
    """
    cmd = "help"
    description = "Show this help message"

    def run(self, *args):
        try:
            args = self.parser.parse_args(args)
        except SystemExit:
            return

        self.log("info", "Commands")

        commands = load_commands()
        rows = [
            [command_name, command_item["description"]]
            for command_name, command_item in commands.items()
        ]

        rows.append(["exit, quit", "Exit Viper"])
        rows = sorted(rows, key=lambda entry: entry[0])

        self.log("table", dict(header=["Command", "Description"], rows=rows))

        if len(__modules__) == 0:
            self.log("info", "No modules installed.")
        else:
            self.log("info", "Modules")
            rows = [
                [
                    module_name,
                    module_item["description"],
                    ", ".join(module_item["categories"]),
                ]
                for module_name, module_item in __modules__.items()
            ]

            rows = sorted(rows, key=lambda entry: entry[0])

            self.log("table", dict(header=["Command", "Description", "Categories"], rows=rows))
