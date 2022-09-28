import bpy
from bpy.types import Operator
from .Hip_functions import create_all_collections, coll_list

class HIP_OT_Collections(Operator):
    """ """
    bl_label = "Add collections"
    bl_idname = "object.addcollections"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        collection_list = coll_list()
        create_all_collections(collection_list)

        return {'FINISHED'}

