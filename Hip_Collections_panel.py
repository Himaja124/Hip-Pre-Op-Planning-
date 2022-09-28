import bpy
from bpy.types import Panel

class HIP_PT_Collections(Panel):
    """ """
    bl_label = "Collections"
    bl_idname = "Hip_PT_collections"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HIP"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.addcollections")