import bpy

class HIP_coordinates_export(bpy.types.Panel):
    """ """
    bl_label = "Export measurements"
    bl_idname = "Hip_coordinates_outputpanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HIP"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        row = layout.row()
        row.prop(mytool, "HipMyFileName")
        row = layout.row()
        row.prop(mytool, "HipMyFileDir")
        row = layout.row()
        row.operator("object.hipsavetofile")