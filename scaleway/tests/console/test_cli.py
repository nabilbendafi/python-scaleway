# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nabil BENDAFI. All Rights Reserved.
#                    Nabil BENDAFI <nabil@bendafi.fr>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

import unittest

from click.testing import CliRunner
from unittest import mock


class TestCli(unittest.TestCase):

    def test_make_requests_session(self):
        runner = CliRunner()
