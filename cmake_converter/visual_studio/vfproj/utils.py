#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016-2018:
#   Matthieu Estrada, ttamalfor@gmail.com
#   Pavel Liavonau, liavonlida@gmail.com
#
# This file is part of (CMakeConverter).
#
# (CMakeConverter) is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# (CMakeConverter) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with (CMakeConverter).  If not, see <http://www.gnu.org/licenses/>.

from cmake_converter.utils import Utils


class VFUtils(Utils):
    def init_context_current_setting(self, context):
        """
        Define settings of converter.

        :param context: converter context
        :type context: Context
        """

        super(VFUtils, self).init_context_current_setting(context)
        context.settings[context.current_setting]['inc_dirs'] = ['${CMAKE_CURRENT_SOURCE_DIR}/']
        context.settings[context.current_setting]['inc_dirs_list'] = ['./']
        context.settings[context.current_setting]['ifort_cl_win'] = []
        context.settings[context.current_setting]['ifort_cl_unix'] = []
        context.settings[context.current_setting]['ifort_ln'] = []
        context.settings[context.current_setting]['assume_args'] = []
        context.settings[context.current_setting]['warn_args'] = []
        context.settings[context.current_setting]['check_args'] = []
