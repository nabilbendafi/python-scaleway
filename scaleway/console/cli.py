#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nabil BENDAFI. All Rights Reserved.
#                    Nabil BENDAFI <nabil@bendafi.fr>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

from prompt_toolkit import prompt


def cli():
    answer = prompt('Give me some input: ')
    print('You said: %s' % answer)


if __name__ == '__main__':
    # Rock'n'Roll
    cli()
