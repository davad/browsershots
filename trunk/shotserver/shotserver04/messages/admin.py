# browsershots.org - Test your web design in different browsers
# Copyright (C) 2007 Johann C. Rocholl <johann@browsershots.org>
#
# Browsershots is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Browsershots is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Admin for messages app.
"""

__revision__ = "$Rev: 1464 $"
__date__ = "$Date: 2007-06-08 13:12:43 -0700 (Fri, 08 Jun 2007) $"
__author__ = "$Author: johann $"

from django.contrib import admin
from shotserver04.messages.models import FactoryError


class FactoryErrorAdmin(admin.ModelAdmin):
    list_display = ('factory', 'code', 'message', 'occurred')
    list_filter = ('factory', 'code')
    date_hierarchy = 'occurred'


admin.site.register(FactoryError, FactoryErrorAdmin)