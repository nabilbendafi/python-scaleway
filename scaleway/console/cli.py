#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nabil BENDAFI. All Rights Reserved.
#                    Nabil BENDAFI <nabil@bendafi.fr>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

import click

from .__init__ import __version__
from prompt_toolkit import prompt


@click.group()
def cli():
    """
        \b
                       _
         ___  ___ __ _| | _____      ____ _ _   _
        / __|/ __/ _` | |/ _ \ \ /\ / / _` | | | |
        \__ \ (_| (_| | |  __/\ V  V / (_| | |_| |
        |___/\___\__,_|_|\___| \_/\_/ \__,_|\__, |
                                            |___/
                                        Python CLI
        \b
    """
    pass


@cli.command()
def version():
    """Prints the current version and exists."""
    click.secho('Scaleway python CLI: {0}'.format(__version__))


if __name__ == '__main__':
    # Rock'n'Roll
    cli()
