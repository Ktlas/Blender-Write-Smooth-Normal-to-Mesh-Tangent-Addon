# Blender Add-on for create normal in tangent
# Contributor(s): zhoufeiy
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.types import Menu

#
# Add additional functions here
#


class MyPanel(Menu):
    bl_idname = 'CALCULATE_AVERAGE_NORMAL_WRITE_TO_TANGENT'
    bl_label = 'Write average normal to tangent'

    def draw(self, context):
        layout = self.layout
        layout.operator('object.select_all',
                        text='Select/Deselect All').action = 'TOOGLE'
        # layout.operator


def register():
    bpy.utils.register_class(MyPanel)


def unregister():
    bpy.utils.unregister_class(MyPanel)
