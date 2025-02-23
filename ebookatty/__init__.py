#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""ebookatty Package."""


########################################################################
#  Copyright (C) 2021  alexpdev
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#########################################################################
"""__init__ module for application."""

from ebookatty.metadata import MetadataFetcher
from ebookatty.cli import execute

__version__ = "0.3.1"

__all__ = ["MetadataFetcher", "execute"]
