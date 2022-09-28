import bpy 
from bpy.types import Operator
from .Hip_functions import make_axis, save_orientation_InEditMode,join_obj,move_to_collection,deselect, select_activate, cursor_to_obj, add_plane, copy_object, delete_obj, save_orientation_obj, unhide, unhide_collection, unhide_list, move_to_collection, check_obj_list, check_create_collection, copy_object, make_axis, unhide_list, unhide, move_to_collection, delete_obj, check_obj_list, check_create_collection


class Hip_OT_PelvisCentre_L(Operator):
    """ """
    bl_label = "Pelvis Centre L"
    bl_idname = "object.pelviscentrel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["Pelvis Centre L"])
            delete_obj(bpy.data.objects["Pelvis Centre L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Pelvis Centre L"

        move_to_collection("Left", bpy.data.objects["Pelvis Centre L"])
        return {'FINISHED'}


class Hip_OT_Neckcentre_L(Operator):
    """ """
    bl_label = "Neck centre L"
    bl_idname = "object.neckcentrel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["Neck centre L"])
            delete_obj(bpy.data.objects["Neck centre L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Neck centre L"

        move_to_collection("Left", bpy.data.objects["Neck centre L"])
        return {'FINISHED'}


class Hip_OT_HipCentre_L(Operator):
    """ """
    bl_label = "Hip Centre L"
    bl_idname = "object.hipcentrel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["Hip Centre L"])
            delete_obj(bpy.data.objects["Hip Centre L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Hip Centre L"

        move_to_collection("Left", bpy.data.objects["Hip Centre L"])
        return {'FINISHED'}


class Hip_OT_ProxAntPt_L(Operator):
    """ """
    bl_label = "Prox Ant Pt L"
    bl_idname = "object.proxantptl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["ProxAntPt L"])
            delete_obj(bpy.data.objects["ProxAntPt L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "ProxAntPt L"

        move_to_collection("Left", bpy.data.objects["ProxAntPt L"])
        return {'FINISHED'}    


class Hip_OT_DistAntPt_L(Operator):
    """ """
    bl_label = "Dist Ant Pt L"
    bl_idname = "object.disantptl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["DistAntPt L"])
            delete_obj(bpy.data.objects["DistAntPt L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "DistAntPt L"

        move_to_collection("Left", bpy.data.objects["DistAntPt L"])
        return {'FINISHED'} 


class Hip_OT_GreaterTrochanter_L(Operator):
    """ """
    bl_label = "GreaterTrochanter L"
    bl_idname = "object.greatertrochanterl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["GreaterTrochanter L"])
            delete_obj(bpy.data.objects["GreaterTrochanter L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "GreaterTrochanter L"

        move_to_collection("Left", bpy.data.objects["GreaterTrochanter L"])
        return {'FINISHED'}        

class Hip_OT_LesserTrochanter_L(Operator):
    """ """
    bl_label = "LesserTrochanter L"
    bl_idname = "object.lessertrochanterl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["LesserTrochanter L"])
            delete_obj(bpy.data.objects["LesserTrochanter L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "LesserTrochanter L"

        move_to_collection("Left", bpy.data.objects["LesserTrochanter L"])
        return {'FINISHED'}   

class Hip_OT_TearDrop_L(Operator):
    """ """
    bl_label = "TearDrop L"
    bl_idname = "object.teardropl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["TearDrop L"])
            delete_obj(bpy.data.objects["TearDrop L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "TearDrop L"

        move_to_collection("Left", bpy.data.objects["TearDrop L"])
        return {'FINISHED'} 

class Hip_OT_FemurCentre_L(Operator):
    """ """
    bl_label = "Femur Centre L"
    bl_idname = "object.femurcentrel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["Femur Centre L"])
            delete_obj(bpy.data.objects["Femur Centre L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Femur Centre L"

        move_to_collection("Left", bpy.data.objects["Femur Centre L"])
        return {'FINISHED'}  

class Hip_OT_LateralEpicondyle_L(Operator):
    """ """
    bl_label = "Lateral Epicondyle L"
    bl_idname = "object.lateralepicondylel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["LateralEpicondyle L"])
            delete_obj(bpy.data.objects["LateralEpicondyle L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "LateralEpicondyle L"

        move_to_collection("Left", bpy.data.objects["LateralEpicondyle L"])
        return {'FINISHED'} 

class Hip_OT_MedialEpicondyle_L(Operator):
    """ """
    bl_label = "Medial Epicondyle L"
    bl_idname = "object.medialepicondylel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["MedialEpicondyle L"])
            delete_obj(bpy.data.objects["MedialEpicondyle L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "MedialEpicondyle L"

        move_to_collection("Left", bpy.data.objects["MedialEpicondyle L"])
        return {'FINISHED'} 

class Hip_OT_PosteriorLateralEpicondyle_L(Operator):
    """ """
    bl_label = "Post Lat condyle L"
    bl_idname = "object.posteriorlateralepicondylel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["PosteriorLateralEpicondyle L"])
            delete_obj(bpy.data.objects["PosteriorLateralEpicondyle L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "PosteriorLateralEpicondyle L"

        move_to_collection("Left", bpy.data.objects["PosteriorLateralEpicondyle L"])
        return {'FINISHED'} 


class Hip_OT_PosteriorMedialEpicondyle_L(Operator):
    """ """
    bl_label = "Post Med condyle L"
    bl_idname = "object.posteriormedialepicondylel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Left"])
        try:
            unhide(bpy.data.objects["PosteriorMedialEpicondyle L"])
            delete_obj(bpy.data.objects["PosteriorMedialEpicondyle L"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "PosteriorMedialEpicondyle L"

        move_to_collection("Left", bpy.data.objects["PosteriorMedialEpicondyle L"])
        return {'FINISHED'} 


class Hip_OT_Submitt(Operator):
    """ """
    bl_label = "Submitt"
    bl_idname = "object.submitt"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        check_create_collection(["Left"])
        unhide_list(["Neck Axis L", 'Hip Centre L', 'Neck centre L'])

        try:
            delete_obj(bpy.data.objects["Neck Axis L"])
        except:
            pass

        check_list = check_obj_list(['Hip Centre L', 'Neck centre L'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre L'], "Hip Centre L for neck Axis L")
            copy_object(bpy.data.objects['Neck centre L'], "Neck centre L for neck Axis L")
            make_axis([bpy.data.objects['Hip Centre L for neck Axis L'], bpy.data.objects['Neck centre L for neck Axis L']],"neck Axis L")

            move_to_collection("Left", bpy.data.objects["neck Axis L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        
        check_create_collection(["Left"])
        unhide_list(["Anatomical Axis L", 'ProxAntPt L', 'DistAntPt L'])

        try:
            delete_obj(bpy.data.objects["Anatomical Axis L"])
        except:
            pass

        check_list = check_obj_list(['ProxAntPt L', 'DistAntPt L'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['ProxAntPt L'], "ProxAntPt L for Anatomical Axis L")
            copy_object(bpy.data.objects['DistAntPt L'], "DistAntPt L for Anatomical Axis L")
            make_axis([bpy.data.objects['ProxAntPt L for Anatomical Axis L'], bpy.data.objects['DistAntPt L for Anatomical Axis L']],"Anatomical Axis L")

            move_to_collection("Left", bpy.data.objects["Anatomical Axis L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        check_create_collection(["Left"])
        unhide_list(["TEA L", 'LateralEpicondyle L', 'MedialEpicondyle L'])

        try:
            delete_obj(bpy.data.objects["TEA L"])
        except:
            pass

        check_list = check_obj_list(['LateralEpicondyle L', 'MedialEpicondyle L'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['LateralEpicondyle L'], "LateralEpicondyle L for TEA L")
            copy_object(bpy.data.objects['MedialEpicondyle L'], "MedialEpicondyle L for TEA L")
            make_axis([bpy.data.objects['LateralEpicondyle L for TEA L'], bpy.data.objects['MedialEpicondyle L for TEA L']],"TEA L")

            move_to_collection("Left", bpy.data.objects["TEA L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        check_create_collection(["Left"])
        unhide_list(["PCA L", 'PosteriorLateralEpicondyle L', 'PosteriorMedialEpicondyle L'])
    

        try:
            delete_obj(bpy.data.objects["PCA L"])
        except:
            pass

        check_list = check_obj_list(['PosteriorLateralEpicondyle L', 'PosteriorMedialEpicondyle L'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['PosteriorLateralEpicondyle L'], "PosteriorLateralEpicondyle L for PCA L")
            copy_object(bpy.data.objects['PosteriorMedialEpicondyle L'], "PosteriorMedialEpicondyle L for PCA L")
            make_axis([bpy.data.objects['PosteriorLateralEpicondyle L for PCA L'], bpy.data.objects['PosteriorMedialEpicondyle L for PCA L']],"PCA L")

            move_to_collection("Left", bpy.data.objects["PCA L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))



        check_create_collection(["Left"])
        unhide_list(["Mechanical Axis L", 'Hip Centre L', 'Femur Centre L'])
        
        try:
            delete_obj(bpy.data.objects["Mechanical Axis L"])
        except:
            pass
        
        check_list = check_obj_list(['Hip Centre L', 'Femur Centre L'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre L'], "Hip Centre L for Mechanical Axis L")
            copy_object(bpy.data.objects['Femur Centre L'], "Femur Centre L for Mechanical Axis L")
            make_axis([bpy.data.objects['Hip Centre L for Mechanical Axis L'], bpy.data.objects['Femur Centre L for Mechanical Axis L']], "Mechanical Axis L")

            move_to_collection("Left", bpy.data.objects["Mechanical Axis L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))



        check_create_collection(["Left"])
        unhide_list(["Coronal Plane at Pelvis L", 'Coronal Plane', 'Pelvis Centre L'])
        
        try:
            delete_obj(bpy.data.objects["Coronal Plane at Pelvis L"])
        except:
            pass

        check_list = check_obj_list(['Coronal Plane', 'Pelvis Centre L'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Coronal Plane'])
            cursor_to_obj(bpy.data.objects['Pelvis Centre L'])
            add_plane("Coronal Plane at Pelvis L")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Left", bpy.data.objects["Coronal Plane at Pelvis L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        

        
        check_create_collection(["Left"])
        unhide_list(["Sagittal Plane at Pelvis L", 'Sagittal Plane', 'Pelvis Centre L'])
       
        try:
            bpy.data.objects["Sagittal Plane at Pelvis L"]
        except:
            pass
        
        check_list = check_obj_list(['Sagittal Plane', 'Pelvis Centre L'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Sagittal Plane'])
            cursor_to_obj(bpy.data.objects['Pelvis Centre L'])
            add_plane("Sagittal Plane at Pelvis L")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Left", bpy.data.objects["Sagittal Plane at Pelvis L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
      

        check_create_collection(["Left"])
        unhide_list(["Transverse Plane At Pelvis L", 'Transverse Plane', 'Pelvis Centre L'])
       
        try:
            bpy.data.objects["Transverse Plane At Pelvis L"]
        except:
            pass
        
        check_list = check_obj_list(['Transverse Plane', 'Pelvis Centre L'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Transverse Plane'])
            cursor_to_obj(bpy.data.objects['Pelvis Centre L'])
            add_plane("Transverse Plane At Pelvis L")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Left", bpy.data.objects["Transverse Plane At Pelvis L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        

        
        check_create_collection(["Left"])
        unhide_list(["Femur Coronal Plane L", 'Mechanical Axis L', 'TransEpicondylar Axis L', 'Femur Centre L'])
        
        try:
            delete_obj(bpy.data.objects["Femur Coronal Plane L"])
        except:
            pass
        
        check_list = check_obj_list(['Mechanical Axis L', 'TransEpicondylar Axis L', 'Femur Centre L'])
        if len(check_list) == 0:
            save_orientation_InEditMode(bpy.data.objects['Mechanical Axis L'], "EDGE")
            copy_object(bpy.data.objects['TransEpicondylar Axis L'], 'TransEpicondylar Axis L for Femur coronal plane L')
        
            deselect()
            select_activate(bpy.data.objects['TransEpicondylar Axis L for Femur coronal plane L'])
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(type="EDGE")
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, -120, 0), "constraint_axis":(False, True, False)})
            bpy.ops.mesh.select_mode(type="FACE")
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.transform.create_orientation(use=True)
            bpy.ops.object.editmode_toggle()

            cursor_to_obj(bpy.data.objects['Femur Centre L'])
        
            add_plane("Femur Coronal Plane L")
            delete_obj(bpy.data.objects['TransEpicondylar Axis L for Femur coronal plane L'])

            move_to_collection("Left", bpy.data.objects["Femur Coronal Plane L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        



        check_create_collection(["Left"])
        unhide_list(["Femur Sagittal Plane L", 'Femur Coronal Plane L', 'Femur Centre L'])
        
        try:
            delete_obj(bpy.data.objects["Femur Sagittal Plane L"])
        except:
            pass 
        
        check_list = check_obj_list(['Femur Coronal Plane L', 'Femur Centre L'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Femur Coronal Plane L'])
            cursor_to_obj(bpy.data.objects['Femur Centre L'])
            add_plane("Femur Sagittal Plane L")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Y',  constraint_axis=(False, True, False))

            move_to_collection("Left", bpy.data.objects["Femur Sagittal Plane L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        


        check_create_collection(["Left"])
        unhide_list(["Femur Distal Plane L", 'Femur Coronal Plane L', 'Femur Centre L'])

        try:
            delete_obj(bpy.data.objects["Femur Distal Plane L"])
        except:
            pass
        
        check_list = check_obj_list(['Femur Coronal Plane L', 'Femur Centre L'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Femur Coronal Plane L'])
            cursor_to_obj(bpy.data.objects['Femur Centre L'])
            add_plane("Femur Distal Plane L")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='Femur Coronal Plane L', orient_matrix_type='Femur Coronal Plane L', constraint_axis=(False, True, False))

            move_to_collection("Left", bpy.data.objects["Femur Distal Plane L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        



        
        # check_create_collection(["Left"])
        # unhide_list(["Referance Plane L", 'Hip Centre L', 'ProxAntPt L', 'DistAntPt L'])
        
        # try:
        #     delete_obj(bpy.data.objects["Referance Plane L"])
        # except:
        #     pass
        
        # check_list = check_obj_list(['Hip Centre L', 'ProxAntPt L', 'DistAntPt L'])
        # if len(check_list) == 0:

        #    copy_object(bpy.data.objects['Hip Centre L'], "Hip Centre L for Referance Plane L")
        #    copy_object(bpy.data.objects['ProxAntPt L'], "ProxAntPt L for Referance Plane L")
        #    copy_object(bpy.data.objects['DistAntPt L'], "DistAntPt L for Referance Plane L")

        #    join_obj([bpy.data.objects['Hip Centre L for Referance Plane L'], bpy.data.objects['ProxAntPt L for Referance Plane L'],bpy.data.objects['DistAntPt L for Referance Plane L']], "Referance Plane L")

        #    bpy.ops.object.editmode_toggle()
        #    bpy.ops.mesh.edge_face_add()
        #    bpy.ops.transform.create_orientation(use=True)
        #    bpy.ops.object.editmode_toggle()

        # #    cursor_to_obj(bpy.data.objects['Pubic'])

        # # #    add_plane("Referance Plane")
        # #    bpy.ops.transform.transform(mode = 'ALIGN')
        #    move_to_collection("Left", bpy.data.objects["Referance Plane L"])
           
        # else:
        #     self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        # check_create_collection(["Left"])
        # unhide_list(["Femur Plane L", 'Referance Plane L'])

        # try:
        #     delete_obj(bpy.data.objects["Femur Plane L"])
        # except:
        #     pass
        
        # check_list = check_obj_list(['Referance Plane L','ProxAntPt L'])
        # if len(check_list) == 0:
        #     save_orientation_InEditMode(bpy.data.objects['Referance Plane L'], "FACE")
            

        #     cursor_to_obj(bpy.data.objects['ProxAntPt L'])
            

        #     add_plane("Femur Plane L")

        
        #     bpy.ops.transform.transform(mode = 'ALIGN')

        #     # delete_obj(bpy.data.objects['TransEpicondylar Axis L for Femur coronal plane L'])

        #     move_to_collection("Left", bpy.data.objects["Femur Plane L"])
        # else:
        #     self.report({'ERROR'}, "missing items:" + ", ".join(check_list))



        # check_create_collection(["Left"])
        # unhide_list(["Helping Axis L",'Femur Plane L', 'ProxAntPt L', 'DistAntPt L'])

        # try:
        #     delete_obj(bpy.data.objects["Helping Axis L"])
        # except:
        #     pass

        # check_list = check_obj_list(['ProxAntPt L', 'DistAntPt L'])
        # if len(check_list) == 0:
        #     copy_object(bpy.data.objects['ProxAntPt L'], "ProxAntPt L for Helping Axis L")
        #     copy_object(bpy.data.objects['DistAntPt L'], "DistAntPt L for Helping Axis L")
        #     make_axis([bpy.data.objects['ProxAntPt L for Helping Axis L'], bpy.data.objects['DistAntPt L for Helping Axis L']],"Helping Axis L")

        #     move_to_collection("Left", bpy.data.objects["Helping Axis L"])
        #     save_orientation_InEditMode(bpy.data.objects['Helping Axis L'], "EDGE")
        #     # select_activate(bpy.data.objects['Femur Plane L for Helping Axis L'])
        #     bpy.ops.transform.transform(mode = 'ALIGN')


        # else:
        #     self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


        # check_create_collection(["Left"])
        # unhide_list(["Femural Plane L", 'ProxAntPt L'])
        
        # try:
        #     delete_obj(bpy.data.objects["Femural Plane L"])
        # except:
        #     pass 
        
        # check_list = check_obj_list(['Femur Plane L','ProxAntPt L'])
        # if len(check_list) == 0:
        #     save_orientation_obj(bpy.data.objects['Femur Plane L'])
        #     cursor_to_obj(bpy.data.objects['ProxAntPt L'])
        #     add_plane("Femural Plane L")
        #     bpy.ops.transform.transform(mode='ALIGN')
        #     bpy.ops.transform.rotate(value=1.5708, orient_axis='Y',  constraint_axis=(False, True, False))

        #     move_to_collection("Left", bpy.data.objects["Femural Plane L"])
        # else:
        #     self.report({'ERROR'}, "missing items:" + ", ".join(check_list))



        check_create_collection(["Left"])
        unhide_list(["Referance Plane L", 'Hip Centre L', 'ProxAntPt L', 'DistAntPt L'])
        
        try:
            delete_obj(bpy.data.objects["Referance Plane L"])
        except:
            pass
        
        check_list = check_obj_list(['Hip Centre L', 'ProxAntPt L', 'DistAntPt L'])
        if len(check_list) == 0:

           copy_object(bpy.data.objects['Hip Centre L'], "Hip Centre L for Referance Plane L")
           copy_object(bpy.data.objects['ProxAntPt L'], "ProxAntPt L for Referance Plane L")
           copy_object(bpy.data.objects['DistAntPt L'], "DistAntPt L for Referance Plane L")

           join_obj([bpy.data.objects['Hip Centre L for Referance Plane L'], bpy.data.objects['ProxAntPt L for Referance Plane L'],bpy.data.objects['DistAntPt L for Referance Plane L']], "Referance Plane L")

           bpy.ops.object.editmode_toggle()
           bpy.ops.mesh.edge_face_add()
           bpy.ops.transform.create_orientation(use=True)
           bpy.ops.object.editmode_toggle()

           cursor_to_obj(bpy.data.objects['ProxAntPt L'])

           add_plane("Referance Plane L")
           bpy.ops.transform.transform(mode = 'ALIGN')
           move_to_collection("Left", bpy.data.objects["Referance Plane L"])
           
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))






        check_create_collection(["Left"])
        unhide_list(["Femur Plane L", 'Referance Plane L'])

        try:
            delete_obj(bpy.data.objects["Femur Plane L"])
        except:
            pass
        
        check_list = check_obj_list(['Referance Plane L','ProxAntPt L'])
        if len(check_list) == 0:
            save_orientation_InEditMode(bpy.data.objects['Referance Plane L'], "FACE")
            

            cursor_to_obj(bpy.data.objects['ProxAntPt L'])
            

            add_plane("Femur Plane L")

        
            bpy.ops.transform.transform(mode = 'ALIGN')

            # delete_obj(bpy.data.objects['TransEpicondylar Axis L for Femur coronal plane L'])

            move_to_collection("Left", bpy.data.objects["Femur Plane L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))





        # check_create_collection(["Left"])
        # unhide_list(["Helping Axis L",'Femur Plane L', 'ProxAntPt L', 'DistAntPt L'])

        # try:
        #     delete_obj(bpy.data.objects["Helping Axis L"])
        # except:
        #     pass

        # check_list = check_obj_list(['ProxAntPt L', 'DistAntPt L'])
        # if len(check_list) == 0:
        #     copy_object(bpy.data.objects['ProxAntPt L'], "ProxAntPt L for Helping Axis L")
        #     copy_object(bpy.data.objects['DistAntPt L'], "DistAntPt L for Helping Axis L")
        #     make_axis([bpy.data.objects['ProxAntPt L for Helping Axis L'], bpy.data.objects['DistAntPt L for Helping Axis L']],"Helping Axis L")

        #     move_to_collection("Left", bpy.data.objects["Helping Axis L"])
            
        # else:
        #     self.report({'ERROR'}, "missing items:" + ", ".join(check_list))


            


        # check_create_collection(["Left"])
        # unhide_list(["Helping Axis L",'Femur Plane L1'])

        # try:
        #     delete_obj(bpy.data.objects["Femur Plane L1"])
        # except:
        #     pass

        # check_list = check_obj_list(['ProxAntPt L','Helping Axis L'])
        # if len(check_list) == 0:
        #     save_orientation_InEditMode(bpy.data.objects['Helping Axis L'], "EDGE")
            
            
        #     cursor_to_obj(bpy.data.objects['ProxAntPt L'])
            

        #     add_plane("Femur Plane L1")

        
        #     bpy.ops.transform.transform(mode = 'ALIGN')

        #     # delete_obj(bpy.data.objects['TransEpicondylar Axis L for Femur coronal plane L'])

        #     move_to_collection("Left", bpy.data.objects["Femur Plane L1"])
            

            
        # else:
        #     self.report({'ERROR'}, "missing items:" + ", ".join(check_list))



        try:
            delete_obj(bpy.data.objects["Femur Offset Plane L"])
        except:
            pass
        
        check_list = check_obj_list(['Femur Plane L','ProxAntPt L','Anatomical Axis L'])
        if len(check_list) == 0:

            
            
            save_orientation_InEditMode(bpy.data.objects['Anatomical Axis L'], "EDGE")
            cursor_to_obj(bpy.data.objects['ProxAntPt L'])

            # add_plane("Femur Offset Plane R")
            # bpy.ops.transform.transform(mode='ALIGN')
            copy_object(bpy.data.objects['Femur Plane L'], 'Femur Offset Plane L') 

            bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', constraint_axis=(False, True, False))

            move_to_collection("Left", bpy.data.objects["Femur Offset Plane L"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
     

        return {'FINISHED'}