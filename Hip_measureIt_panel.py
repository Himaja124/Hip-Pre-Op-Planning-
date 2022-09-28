import bpy
from bpy.types import Panel

class MyPropertyHip(bpy.types.PropertyGroup):
    my_bool : bpy.props.BoolProperty(
        name="Enable or Disable",
        description="For measureIt enbling/disabling",
        default = False
        )

    HipMyFileDir : bpy.props.StringProperty(name= "File Directory", maxlen = 1000, subtype='DIR_PATH') 
    HipMyFileName : bpy.props.StringProperty(name= "File name", maxlen = 1000, subtype= 'FILE_NAME') 
    # mypicdir : bpy.props.StringProperty(name= " ", maxlen = 1000, subtype='FILE_PATH') 

class HIP_PT_MeasureIt(Panel):
    """ """
    bl_label = "Measurit"
    bl_idname = "Hip_PT_Measureit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HIP"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        row = layout.row()
        layout.prop(mytool, "my_bool", text="Tick box")
        row = layout.row()
        row.operator("object.enabledisablemeasureit", text = "Enable/Disable Measureit")
        row = layout.row()
        row.operator("measureit.addangle", text = "Angle")
        row = layout.row()
        row.operator("measureit.addsegment",text = "Distance")
        row = layout.row()
        row.operator("measureit.runopengl", text = "Show/Hide")
        row = layout.row()
        row.operator("measureit.deleteallsegment", text = "Delete")
        