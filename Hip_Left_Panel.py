import bpy
from bpy.types import Panel

class HIP_PT_Left_assignment(Panel):
    """ """
    bl_label = "Left Hip"
    bl_idname = "HIP_PT_Left_assignment"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HIP"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.pelviscentrel")
        row = layout.row()
        row.operator("object.neckcentrel")
        row = layout.row()
        row.operator("object.hipcentrel")
        row = layout.row()
        row.operator("object.proxantptl")
        row = layout.row()
        row.operator("object.disantptl")
        row = layout.row()
        row.operator("object.greatertrochanterl")
        row = layout.row()
        row.operator("object.lessertrochanterl")
        row = layout.row()
        row.operator("object.teardropl")

        row = layout.row()
        row.operator("object.femurcentrel")
        row = layout.row()
        row.operator("object.lateralepicondylel")
        row = layout.row()
        row.operator("object.medialepicondylel")
        row = layout.row()
        row.operator("object.posteriorlateralepicondylel")
        row = layout.row()
        row.operator("object.posteriormedialepicondylel")
        row = layout.row()
        row.operator("object.submitt")
        