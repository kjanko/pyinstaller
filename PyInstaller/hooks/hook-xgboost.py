#-----------------------------------------------------------------------------
# Copyright (c) 2014-2019, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all("xgboost")
