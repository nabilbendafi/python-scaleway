# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nabil BENDAFI. All Rights Reserved.
#                    Nabil BENDAFI <nabil@bendafi.fr>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause
import sys

__version__ = '0.0.1'

if sys.version_info < (3,):
    raise ImportError(
        '''
        Scaleway python CLI {0} is Python3 compatible only.
        '''.format(__version__))
