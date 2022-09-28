import bpy
from bpy.types import Panel

class HIP_PT_Right_assignment(Panel):
    """ """
    bl_label = "Right Hip"
    bl_idname = "HIP_PT_Right_assignment"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HIP"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.pelviscentrer")
        row = layout.row()
        row.operator("object.neckcentrer")
        row = layout.row()
        row.operator("object.hipcentrer")
        row = layout.row()
        row.operator("object.proxantptr")
        row = layout.row()
        row.operator("object.disantptr")
        row = layout.row()
        row.operator("object.greatertrochanterr")
        row = layout.row()
        row.operator("object.lessertrochanterr")
        row = layout.row()
        row.operator("object.teardropr")
        
        row = layout.row()
        row.operator("object.femurcentrer")
        row = layout.row()
        row.operator("object.lateralepicondyler")
        row = layout.row()
        row.operator("object.medialepicondyler")
        row = layout.row()
        row.operator("object.posteriorlateralepicondyler")
        row = layout.row()
        row.operator("object.posteriormedialepicondyler")
        row = layout.row()
        row.operator("object.submit")
  

        # row = layout.row()
        # row.operator("object.femurcoronalplaner")
        # row = layout.row()
        # row.operator("object.femursagittalplaner")
        # row = layout.row()
        # row.operator("object.femurdistalplaner")

        # row = layout.row()
        # row.operator("object.posteriorlateralepicondyler")
        # row = layout.row()
        # row.operator("object.posteriormedialepicondyler")
        # row = layout.row()
        # row.operator("object.posteriorcondylaraxisr")