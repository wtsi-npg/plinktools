#! /usr/bin/env python

# Copyright (c) 2013 Genome Research Ltd. All rights reserved.
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# Author: Iain Bancarz, ib5@sanger.ac.uk

"""Script to merge two Plink .bed files"""


import os, sys
from plink import PlinkEquivalenceTester

stem1 = sys.argv[1]
stem2 = sys.argv[2]

pet = PlinkEquivalenceTester()
ok = pet.compare(stem1, stem2, verbose=True)

if ok: print "OK: .bed files match."
else: print "NOT_OK: .bed files do not match!"
