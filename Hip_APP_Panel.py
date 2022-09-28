import bpy
from bpy.types import Panel

class HIP_PT_APP_assignment(Panel):
    """ """
    bl_label = "APP"
    bl_idname = "HIP_PT_APP_assignment"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HIP"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.asisr")
        row.operator("object.asisl")
        row = layout.row()
        row.operator("object.pubicsymphysisr")
        row.operator("object.pubicsymphysisl")
        row = layout.row()
        row.operator("object.pubicsymphysisaxis")
        row = layout.row()
        row.operator("object.pubic")
        row = layout.row()
        row.operator("object.plane")
        # row.operator("object.coronalplane")
        # row.operator("object.sagittalplane")
        # row.operator("object.transverseplane")
        