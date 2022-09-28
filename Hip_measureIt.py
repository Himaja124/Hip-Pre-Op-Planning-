import bpy
from bpy.types import Operator

class HIP_OT_EnableOrDisableMeasureIt(Operator):
    """ """
    bl_label = "Enable/ Disable Measureit"
    bl_idname = "object.enabledisablemeasureit"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        if (mytool.my_bool == True):
            bpy.ops.preferences.addon_enable(module="measureit")
            bpy.context.scene.measureit_debug = True
            bpy.context.scene.measureit_debug_precision = 2
            bpy.context.scene.measureit_units = '2'
            bpy.context.scene.measureit_gl_precision = 2


        else:
            bpy.ops.preferences.addon_disable(module="measureit")
        
        return {'FINISHED'}


