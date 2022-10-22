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

bl_info = {
    "name": "Smooth Normal To Tangent",
    "description": "Calculate average normal of mesh and write to mesh's tangent.",
    "author": "zhoufeiy",
    "version": (1, 0),
    "blender": (3, 30, 0),
    "location": "View 3D > Object > Write average normal to tangent",
    "warning": "",  # used for warning icon and text in add-ons panel
    "wiki_url": "",
    "tracker_url": "",
    "support": "TESTING",
    "category": "Mesh"
}


#
# Add additional functions here
#


def register():
    from . import properties
    from . import ui
    properties.register()
    ui.register()


def unregister():
    from . import properties
    from . import ui
    properties.unregister()
    ui.unregister()


if __name__ == '__main__':
    register()
