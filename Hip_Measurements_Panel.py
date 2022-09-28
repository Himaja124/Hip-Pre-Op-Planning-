import bpy
from bpy.types import Panel

class HIP_PT_Measurements(Panel):
    """ """
    bl_label = "Angles"
    bl_idname = "Hip_PT_Angles"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HIP"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool 
        
        row = layout.row()
        row.operator("object.inclinationangler")
        row.operator("object.inclinationanglel")
        row = layout.row()
        row.operator("object.versionangler")
        row.operator("object.versionanglel")
        row = layout.row()
        row.operator("object.acetabularoffsetr")
        row.operator("object.acetabularoffsetl")
        row = layout.row()
        row.operator("object.neckshaftangler")
        row.operator("object.neckshaftanglel")
        row = layout.row()
        row.operator("object.femoraloffsetr")
        row.operator("object.femoraloffsetl")
        row = layout.row()
        row.operator("object.hiplengthr")
        row.operator("object.hiplengthl")
        row = layout.row()
        row.operator("object.leglengthr")
        row.operator("object.leglengthl")
        