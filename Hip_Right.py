import bpy 
from bpy.types import Operator
from .Hip_functions import make_axis, save_orientation_InEditMode,join_obj, move_to_collection,deselect, select_activate, cursor_to_obj, add_plane, copy_object, delete_obj, save_orientation_obj, unhide, unhide_collection, unhide_list, move_to_collection, check_obj_list, check_create_collection,copy_object, make_axis, unhide_list, unhide, move_to_collection, delete_obj, check_obj_list, check_create_collection


class Hip_OT_PelvisCentre_R(Operator):
    """ """
    bl_label = "Pelvis Centre R"
    bl_idname = "object.pelviscentrer"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["Pelvis Centre R"])
            delete_obj(bpy.data.objects["Pelvis Centre R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Pelvis Centre R"

        move_to_collection("Right", bpy.data.objects["Pelvis Centre R"])
        return {'FINISHED'}


class Hip_OT_Neckcentre_R(Operator):
    """ """
    bl_label = "Neck centre R"
    bl_idname = "object.neckcentrer"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["Neck centre R"])
            delete_obj(bpy.data.objects["Neck centre R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Neck centre R"

        move_to_collection("Right", bpy.data.objects["Neck centre R"])
        return {'FINISHED'}


class Hip_OT_HipCentre_R(Operator):
    """ """
    bl_label = "Hip Centre R"
    bl_idname = "object.hipcentrer"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["Hip Centre R"])
            delete_obj(bpy.data.objects["Hip Centre R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Hip Centre R"

        move_to_collection("Right", bpy.data.objects["Hip Centre R"])
        return {'FINISHED'}
        

class Hip_OT_ProxAntPt_R(Operator):
    """ """
    bl_label = "Prox Ant Pt R"
    bl_idname = "object.proxantptr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["ProxAntPt R"])
            delete_obj(bpy.data.objects["ProxAntPt R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "ProxAntPt R"

        move_to_collection("Right", bpy.data.objects["ProxAntPt R"])
        return {'FINISHED'}      


class Hip_OT_DistAntPt_R(Operator):
    """ """
    bl_label = "Dist Ant Pt R"
    bl_idname = "object.disantptr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["DistAntPt R"])
            delete_obj(bpy.data.objects["DistAntPt R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "DistAntPt R"

        move_to_collection("Right", bpy.data.objects["DistAntPt R"])
        return {'FINISHED'}        

class Hip_OT_GreaterTrochanter_R(Operator):
    """ """
    bl_label = "GreaterTrochanter R"
    bl_idname = "object.greatertrochanterr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["GreaterTrochanter R"])
            delete_obj(bpy.data.objects["GreaterTrochanter R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "GreaterTrochanter R"

        move_to_collection("Right", bpy.data.objects["GreaterTrochanter R"])
        return {'FINISHED'}    


class Hip_OT_LesserTrochanter_R(Operator):
    """ """
    bl_label = "LesserTrochanter R"
    bl_idname = "object.lessertrochanterr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["LesserTrochanter R"])
            delete_obj(bpy.data.objects["LesserTrochanter R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "LesserTrochanter R"

        move_to_collection("Right", bpy.data.objects["LesserTrochanter R"])
        return {'FINISHED'}   



class Hip_OT_TearDrop_R(Operator):
    """ """
    bl_label = "TearDrop R"
    bl_idname = "object.teardropr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["TearDrop R"])
            delete_obj(bpy.data.objects["TearDrop R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "TearDrop R"

        move_to_collection("Right", bpy.data.objects["TearDrop R"])
        return {'FINISHED'} 


class Hip_OT_FemurCentre_R(Operator):
    """ """
    bl_label = "Femur Centre R"
    bl_idname = "object.femurcentrer"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["FemurCentre R"])
            delete_obj(bpy.data.objects["FemurCentre R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "FemurCentre R"

        move_to_collection("Right", bpy.data.objects["FemurCentre R"])
        return {'FINISHED'} 
 

class Hip_OT_LateralEpicondyle_R(Operator):
    """ """
    bl_label = "LateralEpicondyle R"
    bl_idname = "object.lateralepicondyler"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["LateralEpicondyle R"])
            delete_obj(bpy.data.objects["LateralEpicondyle R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "LateralEpicondyle R"

        move_to_collection("Right", bpy.data.objects["LateralEpicondyle R"])
        return {'FINISHED'}     

class Hip_OT_MedialEpicondyle_R(Operator):
    """ """
    bl_label = "MedialEpicondyle R"
    bl_idname = "object.medialepicondyler"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["MedialEpicondyle R"])
            delete_obj(bpy.data.objects["MedialEpicondyle R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "MedialEpicondyle R"

        move_to_collection("Right", bpy.data.objects["MedialEpicondyle R"])
        return {'FINISHED'} 

class Hip_OT_PosteriorLateralEpicondyle_R(Operator):
    """ """
    bl_label = "Post Lat condyle R"
    bl_idname = "object.posteriorlateralepicondyler"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["PosteriorLateralEpicondyle R"])
            delete_obj(bpy.data.objects["PosteriorLateralEpicondyle R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "PosteriorLateralEpicondyle R"

        move_to_collection("Right", bpy.data.objects["PosteriorLateralEpicondyle R"])
        return {'FINISHED'}

class Hip_OT_PosteriorMedialEpicondyle_R(Operator):
    """ """
    bl_label = "Post Med condyle R"
    bl_idname = "object.posteriormedialepicondyler"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Right"])
        try:
            unhide(bpy.data.objects["PosteriorMedialEpicondyle R"])
            delete_obj(bpy.data.objects["PosteriorMedialEpicondyle R"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "PosteriorMedialEpicondyle R"

        move_to_collection("Right", bpy.data.objects["PosteriorMedialEpicondyle R"])
        return {'FINISHED'} 

class Hip_OT_Submit(Operator):
    """ """
    bl_label = "Submit"
    bl_idname = "object.submit"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        check_create_collection(["Right"])
        unhide_list(["Neck Axis R", 'Hip Centre R', 'Neck centre R'])

        try:
            delete_obj(bpy.data.objects["Neck Axis R"])
        except:
            pass

        check_list = check_obj_list(['Hip Centre R', 'Neck centre R'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre R'], "Hip Centre R for neck Axis R")
            copy_object(bpy.data.objects['Neck centre R'], "Neck centre R for neck Axis R")
            make_axis([bpy.data.objects['Hip Centre R for neck Axis R'], bpy.data.objects['Neck centre R for neck Axis R']],"neck Axis R")

            move_to_collection("Right", bpy.data.objects["neck Axis R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        
        check_create_collection(["Right"])
        unhide_list(["Anatomical Axis R", 'ProxAntPt R', 'DistAntPt R'])

        try:
            delete_obj(bpy.data.objects["Anatomical Axis R"])
        except:
            pass

        check_list = check_obj_list(['ProxAntPt R', 'DistAntPt R'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['ProxAntPt R'], "ProxAntPt R for Anatomical Axis R")
            copy_object(bpy.data.objects['DistAntPt R'], "DistAntPt R for Anatomical Axis R")
            make_axis([bpy.data.objects['ProxAntPt R for Anatomical Axis R'], bpy.data.objects['DistAntPt R for Anatomical Axis R']],"Anatomical Axis R")

            move_to_collection("Right", bpy.data.objects["Anatomical Axis R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        check_create_collection(["Right"])
        unhide_list(["TEA R", 'LateralEpicondyle R', 'MedialEpicondyle R'])

        try:
            delete_obj(bpy.data.objects["TEA R"])
        except:
            pass

        check_list = check_obj_list(['LateralEpicondyle R', 'MedialEpicondyle R'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['LateralEpicondyle R'], "LateralEpicondyle R for TEA R")
            copy_object(bpy.data.objects['MedialEpicondyle R'], "MedialEpicondyle R for TEA R")
            make_axis([bpy.data.objects['LateralEpicondyle R for TEA R'], bpy.data.objects['MedialEpicondyle R for TEA R']],"TEA R")

            move_to_collection("Right", bpy.data.objects["TEA R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        check_create_collection(["Right"])
        unhide_list(["PCA R", 'PosteriorLateralEpicondyle R', 'PosteriorMedialEpicondyle R'])
    

        try:
            delete_obj(bpy.data.objects["PCA R"])
        except:
            pass

        check_list = check_obj_list(['PosteriorLateralEpicondyle R', 'PosteriorMedialEpicondyle R'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['PosteriorLateralEpicondyle R'], "PosteriorLateralEpicondyle R for PCA R")
            copy_object(bpy.data.objects['PosteriorMedialEpicondyle R'], "PosteriorMedialEpicondyle R for PCA R")
            make_axis([bpy.data.objects['PosteriorLateralEpicondyle R for PCA R'], bpy.data.objects['PosteriorMedialEpicondyle R for PCA R']],"PCA R")

            move_to_collection("Right", bpy.data.objects["PCA R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        check_create_collection(["Right"])
        unhide_list(["Mechanical Axis R", 'Hip Centre R', 'Femur Centre R'])
        
        try:
            delete_obj(bpy.data.objects["Mechanical Axis R"])
        except:
            pass
        
        check_list = check_obj_list(['Hip Centre R', 'Femur Centre R'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre R'], "Hip Centre R for Mechanical Axis R")
            copy_object(bpy.data.objects['Femur Centre R'], "Femur Centre R for Mechanical Axis R")
            make_axis([bpy.data.objects['Hip Centre R for Mechanical Axis R'], bpy.data.objects['Femur Centre R for Mechanical Axis R']], "Mechanical Axis R")

            move_to_collection("Right", bpy.data.objects["Mechanical Axis R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
    


    
        check_create_collection(["Right"])
        unhide_list(["Coronal Plane at Pelvis R", 'Coronal Plane', 'Pelvis Centre R'])
        
        try:
            delete_obj(bpy.data.objects["Coronal Plane at Pelvis R"])
        except:
            pass

        check_list = check_obj_list(['Coronal Plane', 'Pelvis Centre R'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Coronal Plane'])
            cursor_to_obj(bpy.data.objects['Pelvis Centre R'])
            add_plane("Coronal Plane at Pelvis R")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Right", bpy.data.objects["Coronal Plane at Pelvis R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        

        
        check_create_collection(["Right"])
        unhide_list(["Sagittal Plane at Pelvis R", 'Sagittal Plane', 'Pelvis Centre R'])
       
        try:
            bpy.data.objects["Sagittal Plane at Pelvis R"]
        except:
            pass
        
        check_list = check_obj_list(['Sagittal Plane', 'Pelvis Centre R'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Sagittal Plane'])
            cursor_to_obj(bpy.data.objects['Pelvis Centre R'])
            add_plane("Sagittal Plane at Pelvis R")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Right", bpy.data.objects["Sagittal Plane at Pelvis R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
      

        check_create_collection(["Right"])
        unhide_list(["Transverse Plane At Pelvis R", 'Transverse Plane', 'Pelvis Centre R'])
       
        try:
            bpy.data.objects["Transverse Plane At Pelvis R"]
        except:
            pass
        
        check_list = check_obj_list(['Transverse Plane', 'Pelvis Centre R'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Transverse Plane'])
            cursor_to_obj(bpy.data.objects['Pelvis Centre R'])
            add_plane("Transverse Plane At Pelvis R")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Right", bpy.data.objects["Transverse Plane At Pelvis R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        

        
        check_create_collection(["Right"])
        unhide_list(["Femur Coronal Plane R", 'Mechanical Axis R', 'TransEpicondylar Axis R', 'Femur Centre R'])
        
        try:
            delete_obj(bpy.data.objects["Femur Coronal Plane R"])
        except:
            pass
        
        check_list = check_obj_list(['Mechanical Axis R', 'TransEpicondylar Axis R', 'Femur Centre R'])
        if len(check_list) == 0:
            save_orientation_InEditMode(bpy.data.objects['Mechanical Axis R'], "EDGE")
            copy_object(bpy.data.objects['TransEpicondylar Axis R'], 'TransEpicondylar Axis R for Femur coronal plane R')
        
            deselect()
            select_activate(bpy.data.objects['TransEpicondylar Axis R for Femur coronal plane R'])
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(type="EDGE")
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, -120, 0), "constraint_axis":(False, True, False)})
            bpy.ops.mesh.select_mode(type="FACE")
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.transform.create_orientation(use=True)
            bpy.ops.object.editmode_toggle()

            cursor_to_obj(bpy.data.objects['Femur Centre R'])
        
            add_plane("Femur Coronal Plane R")
            delete_obj(bpy.data.objects['TransEpicondylar Axis R for Femur coronal plane R'])

            move_to_collection("Right", bpy.data.objects["Femur Coronal Plane R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        



        check_create_collection(["Right"])
        unhide_list(["Femur Sagittal Plane R", 'Femur Coronal Plane R', 'Femur Centre R'])
        
        try:
            delete_obj(bpy.data.objects["Femur Sagittal Plane R"])
        except:
            pass 
        
        check_list = check_obj_list(['Femur Coronal Plane R', 'Femur Centre R'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Femur Coronal Plane R'])
            cursor_to_obj(bpy.data.objects['Femur Centre R'])
            add_plane("Femur Sagittal Plane R")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Y',  constraint_axis=(False, True, False))

            move_to_collection("Right", bpy.data.objects["Femur Sagittal Plane R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        


        check_create_collection(["Right"])
        unhide_list(["Femur Distal Plane R", 'Femur Coronal Plane R', 'Femur Centre R'])

        try:
            delete_obj(bpy.data.objects["Femur Distal Plane R"])
        except:
            pass
        
        check_list = check_obj_list(['Femur Coronal Plane R', 'Femur Centre R'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Femur Coronal Plane R'])
            cursor_to_obj(bpy.data.objects['Femur Centre R'])
            add_plane("Femur Distal Plane R")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='Femur Coronal Plane R', orient_matrix_type='Femur Coronal Plane R', constraint_axis=(False, True, False))

            move_to_collection("Right", bpy.data.objects["Femur Distal Plane R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))




        # check_create_collection(["Right"])
        # unhide_list(["Referance Plane R", 'Hip Centre R', 'ProxAntPt R', 'DistAntPt R'])
        
        # try:
        #     delete_obj(bpy.data.objects["Referance Plane R"])
        # except:
        #     pass
        
        # check_list = check_obj_list(['Hip Centre R', 'ProxAntPt R', 'DistAntPt R'])
        # if len(check_list) == 0:

        #    copy_object(bpy.data.objects['Hip Centre R'], "Hip Centre R for Referance Plane R")
        #    copy_object(bpy.data.objects['ProxAntPt R'], "ProxAntPt R for Referance Plane R")
        #    copy_object(bpy.data.objects['DistAntPt R'], "DistAntPt R for Referance Plane R")
        # #    make_axis([bpy.data.objects['ProxAntPt R'], bpy.data.objects['DistAntPt R']], "Femur Axis R")


        #    join_obj([bpy.data.objects['Hip Centre R for Referance Plane R'], bpy.data.objects['ProxAntPt R for Referance Plane R'],bpy.data.objects['DistAntPt R for Referance Plane R']], "Referance Plane R")

        #    bpy.ops.object.editmode_toggle()
        #    bpy.ops.mesh.edge_face_add()
        #    bpy.ops.transform.create_orientation(use=True)
        #    bpy.ops.object.editmode_toggle()

        #    cursor_to_obj(bpy.data.objects['ProxAntPt R'])

        #    add_plane("Referance Plane R")
        #    bpy.ops.transform.transform(mode = 'ALIGN')
        #    move_to_collection("Right", bpy.data.objects["Referance Plane R"])
           
        # else:
        #     self.report({'ERROR'}, "missing items:" + ", ".join(check_list))




        # check_create_collection(["Right"])
        # unhide_list(["Femur Plane R", 'Referance Plane R'])

        # try:
        #     delete_obj(bpy.data.objects["Femur Plane R"])
        # except:
        #     pass
        
        # check_list = check_obj_list(['Referance Plane R','ProxAntPt R','Anatomical Axis R'])
        # if len(check_list) == 0:
        #     save_orientation_InEditMode(bpy.data.objects['Referance Plane R'], "FACE")
            

        #     cursor_to_obj(bpy.data.objects['ProxAntPt R'])
            

        #     add_plane("Femur Plane R")

        
        #     bpy.ops.transform.transform(mode = 'ALIGN')

        #     save_orientation_InEditMode(bpy.data.objects['Anatomical Axis R'], "EDGE")

        #     bpy.ops.transform.transform(mode = 'ALIGN')
            

           
            

        #     # delete_obj(bpy.data.objects['TransEpicondylar Axis L for Femur coronal plane L'])

        #     move_to_collection("Right", bpy.data.objects["Femur Plane R"])
        # else:
        #     self.report({'ERROR'}, "missing items:" + ", ".join(check_list))




        # check_create_collection(["Right"])
        # unhide_list(["Femur Plane R", 'Anatomical Axis R'])

        # try:
        #     delete_obj(bpy.data.objects["Femur Plane R"])
        # except:
        #     pass
        
        # check_list = check_obj_list(['Anatomical Axis R'])
        # if len(check_list) == 0:
        #     save_orientation_InEditMode(bpy.data.objects['Anatomical Axis R'], "EDGE")
            

        #     # cursor_to_obj(bpy.data.objects['ProxAntPt R'])
            

        #     # add_plane("Femur Plane R")

        
        #     bpy.ops.transform.transform(mode = 'ALIGN')

        #     # delete_obj(bpy.data.objects['TransEpicondylar Axis L for Femur coronal plane L'])

        #     move_to_collection("Right", bpy.data.objects["Femur Plane R"])
        # else:
        #     self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        check_create_collection(["Right"])
        unhide_list(["Referance Plane R", 'Hip Centre R', 'ProxAntPt R', 'DistAntPt R'])
        
        try:
            delete_obj(bpy.data.objects["Referance Plane R"])
        except:
            pass
        
        check_list = check_obj_list(['Hip Centre R', 'ProxAntPt R', 'DistAntPt R'])
        if len(check_list) == 0:

           copy_object(bpy.data.objects['Hip Centre R'], "Hip Centre R for Referance Plane R")
           copy_object(bpy.data.objects['ProxAntPt R'], "ProxAntPt R for Referance Plane R")
           copy_object(bpy.data.objects['DistAntPt R'], "DistAntPt R for Referance Plane R")

           join_obj([bpy.data.objects['Hip Centre R for Referance Plane R'], bpy.data.objects['ProxAntPt R for Referance Plane R'],bpy.data.objects['DistAntPt R for Referance Plane R']], "Referance Plane R")

           bpy.ops.object.editmode_toggle()
           bpy.ops.mesh.edge_face_add()
           bpy.ops.transform.create_orientation(use=True)
           bpy.ops.object.editmode_toggle()

           cursor_to_obj(bpy.data.objects['ProxAntPt R'])

           add_plane("Referance Plane R")
           bpy.ops.transform.transform(mode = 'ALIGN')
           move_to_collection("Right", bpy.data.objects["Referance Plane R"])
           
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))




        check_create_collection(["Right"])
        unhide_list(["Femur Plane R", 'Referance Plane R'])

        try:
            delete_obj(bpy.data.objects["Femur Plane R"])
        except:
            pass
        
        check_list = check_obj_list(['Referance Plane R','ProxAntPt R'])
        if len(check_list) == 0:
            save_orientation_InEditMode(bpy.data.objects['Referance Plane R'], "FACE")
            

            cursor_to_obj(bpy.data.objects['ProxAntPt R'])
            

            add_plane("Femur Plane R")

        
            bpy.ops.transform.transform(mode = 'ALIGN')

            # delete_obj(bpy.data.objects['TransEpicondylar Axis L for Femur coronal plane L'])

            move_to_collection("Right", bpy.data.objects["Femur Plane R"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))




        try:
            delete_obj(bpy.data.objects["Femur Offset Plane R"])
        except:
            pass
        
        check_list = check_obj_list(['Femur Plane R','ProxAntPt R','Anatomical Axis R'])
        if len(check_list) == 0:

             
            
            save_orientation_InEditMode(bpy.data.objects['Anatomical Axis R'], "EDGE")

            cursor_to_obj(bpy.data.objects['ProxAntPt R'])
            # add_plane("Femur Offset Plane R")
            # bpy.ops.transform.transform(mode='ALIGN')
            # copy_object(bpy.data.objects['Femur Plane R'], 'Femur Offset Plane R') 

            copy_object(bpy.data.objects['Femur Plane R'], 'Femur Offset Plane R')

            bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', constraint_axis=(False, True, False))

            move_to_collection("Right", bpy.data.objects["Femur Offset Plane R"])

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        

        return {'FINISHED'}