import bpy
from bpy.types import Panel

class HIP_PT_Projections(Panel):
    """ """
    bl_label = "Projections"
    bl_idname = "Hip_PT_Projections"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HIP"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.projections")