# -*- coding: utf-8 -*-
# 
# Massengeschmack XBMC add-on
# Copyright (C) 2013 by Janek Bevendorff
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import xbmcaddon
import xbmc
import urlparse
import sys
import json

# globals
ADDON_ID          = 'plugin.video.massengeschmack'
ADDON             = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME        = ADDON.getAddonInfo('name')
ADDON_ICON        = ADDON.getAddonInfo('icon')
ADDON_VERSION     = ADDON.getAddonInfo('version')
ADDON_BASE_PATH   = xbmc.translatePath(ADDON.getAddonInfo('path')).decode('utf-8')
ADDON_HANDLE      = int(sys.argv[1])
ADDON_ARGS        = dict(urlparse.parse_qsl(sys.argv[2][1:]))

HTTP_USER_AGENT      = 'Massengeschmack XBMC add-on v' + ADDON_VERSION
HTTP_TIMEOUT         = 20
HTTP_BASE_URI        = 'https://massengeschmack.tv/'
HTTP_BASE_FEED_URI   = HTTP_BASE_URI + 'feed/'

IS_XBOX = bool(xbmc.getCondVisibility("System.Platform.xbox"))