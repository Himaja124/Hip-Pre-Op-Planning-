import bpy 
from bpy.types import Operator
from .Hip_functions import copy_object, make_axis, unhide_list, unhide, move_to_collection, delete_obj, check_obj_list, check_create_collection,save_orientation_InEditMode,join_obj, move_to_collection,deselect, select_activate, cursor_to_obj, add_plane, copy_object, delete_obj, save_orientation_obj, unhide_list, move_to_collection, check_obj_list, check_create_collection


class HIP_OT_ASIS_L(Operator):
    """"""
    bl_label = "ASIS-L"
    bl_idname = "object.asisl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):    
        check_create_collection(["APP"])
        try:
            unhide(bpy.data.objects["ASIS-L"])
            delete_obj(bpy.data.objects["ASIS-L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "ASIS-L"
        
        move_to_collection("APP", bpy.data.objects["ASIS-L"])
        return {'FINISHED'}

        
class HIP_OT_ASIS_R(Operator):
    """ """
    bl_label = "ASIS-R"
    bl_idname = "object.asisr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["APP"])
        try:
            unhide(bpy.data.objects["ASIS-R"])
            delete_obj(bpy.data.objects["ASIS-R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "ASIS-R"

        move_to_collection("APP", bpy.data.objects["ASIS-R"])
        return {'FINISHED'}


class HIP_OT_PubicSymphysis_L(Operator):
    """ """
    bl_label = "PubicSymphysis-L"
    bl_idname = "object.pubicsymphysisl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["APP"])
        try:
            unhide(bpy.data.objects["PubicSymphysis-L"])
            delete_obj(bpy.data.objects["PubicSymphysis-L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "PubicSymphysis-L"

        move_to_collection("APP", bpy.data.objects["PubicSymphysis-L"])
        return {'FINISHED'}

class HIP_OT_PubicSymphysis_R(Operator):
    """ """
    bl_label = "PubicSymphysis-R"
    bl_idname = "object.pubicsymphysisr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["APP"])
        try:
            unhide(bpy.data.objects["PubicSymphysis-R"])
            delete_obj(bpy.data.objects["PubicSymphysis-R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "PubicSymphysis-R"

        move_to_collection("APP", bpy.data.objects["PubicSymphysis-R"])
        return {'FINISHED'}

class Hip_OT_PubicSymphysis_Axis(Operator):
    """ """
    bl_label = "PubicSymphysis Axis"
    bl_idname = "object.pubicsymphysisaxis"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["APP"])
        unhide_list(["PubicSymphysis Axis", 'PubicSymphysis-L', 'PubicSymphysis-R'])
        
        try:
            delete_obj(bpy.data.objects["PubicSymphysis Axis"])
        except:
            pass
        
        check_list = check_obj_list(['PubicSymphysis-L', 'PubicSymphysis-R'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['PubicSymphysis-L'], "PubicSymphysis-L for PubicSymphysis Axis")
            copy_object(bpy.data.objects['PubicSymphysis-R'], "PubicSymphysis-R for PubicSymphysis Axis")
            make_axis([bpy.data.objects['PubicSymphysis-L for PubicSymphysis Axis'], bpy.data.objects['PubicSymphysis-R for PubicSymphysis Axis']], "PubicSymphysis Axis")

            move_to_collection("APP", bpy.data.objects["PubicSymphysis Axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        return {'FINISHED'}

class Hip_OT_Pubic(Operator):
    """ """
    bl_label = "Pubic"
    bl_idname = "object.pubic"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["APP"])
        try:
            unhide(bpy.data.objects["Pubic"])
            delete_obj(bpy.data.objects["Pubic"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Pubic"

        move_to_collection("APP", bpy.data.objects["Pubic"])
        return {'FINISHED'}


class Hip_OT_Plane(Operator):
    """ """
    bl_label = "Plane"
    bl_idname = "object.plane"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        check_create_collection(["APP"])
        unhide_list(["Referance Plane", 'ASIS-L', 'ASIS-R', 'Pubic'])
        
        try:
            delete_obj(bpy.data.objects["Referance Plane"])
        except:
            pass
        
        check_list = check_obj_list(['ASIS-L', 'ASIS-R', 'Pubic'])
        if len(check_list) == 0:

           copy_object(bpy.data.objects['ASIS-L'], "ASIS-L for Referance Plane")
           copy_object(bpy.data.objects['ASIS-R'], "ASIS-R for Referance Plane")
           copy_object(bpy.data.objects['Pubic'], "Pubic for Referance Plane")

           join_obj([bpy.data.objects['ASIS-L for Referance Plane'], bpy.data.objects['ASIS-R for Referance Plane'],bpy.data.objects['Pubic for Referance Plane']], "Referance Plane")

           
           bpy.ops.object.editmode_toggle()
           bpy.ops.mesh.edge_face_add()
           bpy.ops.transform.create_orientation(use=True)
           bpy.ops.object.editmode_toggle()

        #    cursor_to_obj(bpy.data.objects['Pubic'])

        #    add_plane("Referance Plane")
        #    bpy.ops.transform.transform(mode = 'ALIGN')
           move_to_collection("APP", bpy.data.objects["Referance Plane"])
           
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        

    
        
        check_create_collection(["APP"])
        unhide_list(["Coronal Plane", 'Referance Plane'])

        try:
            delete_obj(bpy.data.objects["Coronal Plane"])
        except:
            pass
        
        check_list = check_obj_list(['Referance Plane','Pubic'])
        if len(check_list) == 0:
            save_orientation_InEditMode(bpy.data.objects['Referance Plane'], "FACE")
            

            cursor_to_obj(bpy.data.objects['Pubic'])
            

            add_plane("Coronal Plane")

        
            bpy.ops.transform.transform(mode = 'ALIGN')

            # delete_obj(bpy.data.objects['TransEpicondylar Axis L for Femur coronal plane L'])

            move_to_collection("APP", bpy.data.objects["Coronal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        check_create_collection(["APP"])
        unhide_list(["Transverse Plane", 'Coronal Plane', 'Pubic'])

        try:
            delete_obj(bpy.data.objects["Transverse Plane"])
        except:
            pass
        
        check_list = check_obj_list(['Coronal Plane', 'Pubic'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Coronal Plane'])
            cursor_to_obj(bpy.data.objects['Pubic'])
            add_plane("Transverse Plane")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', orient_type='Coronal Plane', orient_matrix_type='Coronal Plane', constraint_axis=(False, True, False))

            move_to_collection("APP", bpy.data.objects["Transverse Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        check_create_collection(["APP"])
        unhide_list(["Sagittal Plane ", 'Pubic'])
        
        try:
            delete_obj(bpy.data.objects["Sagittal Plane"])
        except:
            pass 
        
        check_list = check_obj_list(['Coronal Plane', 'Pubic'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Coronal Plane'])
            cursor_to_obj(bpy.data.objects['Pubic'])
            add_plane("Sagittal Plane")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X',  constraint_axis=(True, False, False))

            move_to_collection("APP", bpy.data.objects["Sagittal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        return {'FINISHED'}

