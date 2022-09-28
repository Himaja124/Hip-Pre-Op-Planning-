import bpy
from bpy.types import Operator
from .Hip_functions  import copy_object, join_obj, make_axis, join_obj,save_orientation_InEditMode, save_orientation_obj, select_activate, vertex_group, save_orientation_InEditMode, shrinkwrap_obj, cursor_to_obj, add_plane, delete_obj, move_to_collection, transform_to_orientation, unhide_list, check_obj_list, check_create_collection, remove_doubles, get_coordinates
from .Hip_finding_angle import angle_triangle
from .Hip_finding_distance import distance
from .Hip_measurements_file import Hip_save_to_file

my_measurements = {"Inclination Angle L":None , "Inclination Angle R":None , "Version Angle L":None, "Version Angle R":None, "Acetabular Offset L":None, "Acetabular Offset R":None, "Leg Length L":None, "Leg Length R":None, "Hip Length L":None, "Hip Length R":None, "NeckShaft Angle L":None, "NeckShaft Angle R":None, "FemoralOffset L":None, "FemoralOffset R":None}

class Hip_OT_InclinationAngle_L(Operator):
    """it is the angle between neck axis projected on the coronal plane and the line parallel to the saggital plane"""
    bl_label = "Inclination Angle L"
    bl_idname = "object.inclinationanglel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Left", "Projections", "Measurements"])
        unhide_list(["Inclination Angle L",'Hip Centre L P:CorPL', 'Pelvis Centre L','Neck centre L P:CorPL','Neck centre L P:CorPL.SagPL'])
        
        try:
            delete_obj(bpy.data.objects["Inclination Angle L"])
        except:
            pass

        check_list = check_obj_list(['Pelvis Centre L','Hip Centre L P:CorPL','Neck centre L P:CorPL','Neck centre L P:CorPL.SagPL'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre L P:CorPL'], 'Hip Centre L P:CorPL for Inclination Angle L1')
            copy_object(bpy.data.objects['Neck centre L P:CorPL'], 'Neck centre L P:CorPL for Inclination Angle L1')
            make_axis([bpy.data.objects['Hip Centre L P:CorPL for Inclination Angle L1'], bpy.data.objects['Neck centre L P:CorPL for Inclination Angle L1']], "Inclination Angle Line1")

            copy_object(bpy.data.objects['Pelvis Centre L'], 'Pelvis Centre L for Inclination Angle L2')
            copy_object(bpy.data.objects['Neck centre L P:CorPL.SagPL'], 'Neck centre L P:CorPL.SagPL for Inclination Angle L2')
            make_axis([bpy.data.objects['Pelvis Centre L for Inclination Angle L2'], bpy.data.objects['Neck centre L P:CorPL.SagPL for Inclination Angle L2']], "Inclination Angle Line2")

            join_obj([bpy.data.objects["Inclination Angle Line1"], bpy.data.objects["Inclination Angle Line2"]], 'Inclination Point L')

            vertex_group(bpy.data.objects["Inclination Point L"])
            copy_object(bpy.data.objects["Inclination Point L"], "Inclination Point L copy1")
            copy_object(bpy.data.objects["Inclination Point L"], "Inclination Point L copy2")
            
            copy_object(bpy.data.objects['Neck centre L P:CorPL'], 'Neck centre L P:CorPL for Inclination Angle L')
            copy_object(bpy.data.objects['Neck centre L P:CorPL.SagPL'], 'Neck centre L P:CorPL.SagPL for Inclination Angle L')
            make_axis([bpy.data.objects["Inclination Point L copy1"], bpy.data.objects['Neck centre L P:CorPL for Inclination Angle L']], 'Inclination L1')
            make_axis([bpy.data.objects["Inclination Point L copy2"], bpy.data.objects['Neck centre L P:CorPL.SagPL for Inclination Angle L']], 'Inclination L2')
            join_obj([bpy.data.objects['Inclination L1'], bpy.data.objects['Inclination L2']], 'Inclination Angle L')
            # remove_doubles(bpy.data.objects['NeckShaft Angle L'])

            move_to_collection("Measurements", bpy.data.objects['Inclination Angle L'])

            coord_values = get_coordinates(['Neck centre L P:CorPL',"Inclination Point L",'Neck centre L P:CorPL.SagPL'])
            my_measurements["Inclination Angle L"] =  angle_triangle(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5], coord_values[6], coord_values[7], coord_values[8])

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}



class Hip_OT_InclinationAngle_R(Operator):
    """ """
    bl_label = "Inclination Angle R"
    bl_idname = "object.inclinationangler"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Right", "Projections", "Measurements"])
        unhide_list(["Inclination Angle R", 'Pelvis Centre R','Neck centre R P:CorPR','Neck centre R P:CorPR.SagPR'])
        
        try:
            delete_obj(bpy.data.objects["Inclination Angle R"])
        except:
            pass

        check_list = check_obj_list(['Pelvis Centre R','Hip Centre R P:CorPR','Neck centre R P:CorPR','Neck centre R P:CorPR.SagPR'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre R P:CorPR'], 'Hip Centre R P:CorPR for Inclination Angle R1')
            copy_object(bpy.data.objects['Neck centre R P:CorPR'], 'Neck centre R P:CorPR for Inclination Angle R1')
            make_axis([bpy.data.objects['Hip Centre R P:CorPR for Inclination Angle R1'], bpy.data.objects['Neck centre R P:CorPR for Inclination Angle R1']], "Inclination Angle Rine1")

            copy_object(bpy.data.objects['Pelvis Centre R'], 'Pelvis Centre R for Inclination Angle R2')
            copy_object(bpy.data.objects['Neck centre R P:CorPR.SagPR'], 'Neck centre R P:CorPR.SagPR for Inclination Angle R2')
            make_axis([bpy.data.objects['Pelvis Centre R for Inclination Angle R2'], bpy.data.objects['Neck centre R P:CorPR.SagPR for Inclination Angle R2']], "Inclination Angle Rine2")

            join_obj([bpy.data.objects["Inclination Angle Rine1"], bpy.data.objects["Inclination Angle Rine2"]], 'Inclination Point R')

            vertex_group(bpy.data.objects["Inclination Point R"])
            copy_object(bpy.data.objects["Inclination Point R"], "Inclination Point R copy1")
            copy_object(bpy.data.objects["Inclination Point R"], "Inclination Point R copy2")
            
            copy_object(bpy.data.objects['Neck centre R P:CorPR'], 'Neck centre R P:CorPR for Inclination Angle R')
            copy_object(bpy.data.objects['Neck centre R P:CorPR.SagPR'], 'Neck centre R P:CorPR.SagPR for Inclination Angle R')
            make_axis([bpy.data.objects["Inclination Point R copy1"], bpy.data.objects['Neck centre R P:CorPR for Inclination Angle R']], 'Inclination R1')
            make_axis([bpy.data.objects["Inclination Point R copy2"], bpy.data.objects['Neck centre R P:CorPR.SagPR for Inclination Angle R']], 'Inclination R2')
            join_obj([bpy.data.objects['Inclination R1'], bpy.data.objects['Inclination R2']], 'Inclination Angle R')
            # remove_doubles(bpy.data.objects['NeckShaft Angle L'])

            move_to_collection("Measurements", bpy.data.objects['Inclination Angle R'])

            coord_values = get_coordinates(['Neck centre R P:CorPR',"Inclination Point R",'Neck centre R P:CorPR.SagPR'])
            my_measurements["Inclination Angle R"] =  angle_triangle(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5], coord_values[6], coord_values[7], coord_values[8])
                        


            
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}      




class Hip_OT_VersionAngle_L(Operator):
    """ """
    bl_label = "Version Angle L"
    bl_idname = "object.versionanglel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Left", "Projections","Measurements"])
        unhide_list(["Version Angle L",'Hip Centre L P:TranPL', 'Pelvis Centre L','Neck centre L P:TranPL','Neck centre L P:TranPL.CorPL'])
        
        try:
            delete_obj(bpy.data.objects["Version Angle L"])
        except:
            pass

        check_list = check_obj_list(['Pelvis Centre L','Hip Centre L P:TranPL','Neck centre L P:TranPL','Neck centre L P:TranPL.CorPL'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre L P:TranPL'], 'Hip Centre L P:TranPL for Version Angle L1')
            copy_object(bpy.data.objects['Neck centre L P:TranPL'], 'NCL P:TranPL for Version Angle L1')
            make_axis([bpy.data.objects['Hip Centre L P:TranPL for Version Angle L1'], bpy.data.objects['NCL P:TranPL for Version Angle L1']], "Version Angle Line1")

            copy_object(bpy.data.objects['Pelvis Centre L'], 'Pelvis Centre L for Version Angle L2')
            copy_object(bpy.data.objects['Neck centre L P:TranPL.CorPL'], 'NCL P:TranPL.CorPL for Version Angle L2')
            make_axis([bpy.data.objects['Pelvis Centre L for Version Angle L2'], bpy.data.objects['NCL P:TranPL.CorPL for Version Angle L2']], "Version Angle Line2")

            join_obj([bpy.data.objects["Version Angle Line1"], bpy.data.objects["Version Angle Line2"]], 'Version Point L')
            
            vertex_group(bpy.data.objects["Version Point L"])
            copy_object(bpy.data.objects["Version Point L"], "Version Point L copy1")
            copy_object(bpy.data.objects["Version Point L"], "Version Point L copy2")
        
            copy_object(bpy.data.objects['Neck centre L P:TranPL'], 'Neck centre L P:TranPL for Version Angle L')
            copy_object(bpy.data.objects['Neck centre L P:TranPL.CorPL'], 'Neck centre L P:TranPL.CorPL for Version Angle L')
            make_axis([bpy.data.objects["Version Point L copy1"], bpy.data.objects['Neck centre L P:TranPL for Version Angle L']], 'Version L1')
            make_axis([bpy.data.objects["Version Point L copy2"], bpy.data.objects['Neck centre L P:TranPL.CorPL for Version Angle L']], 'Version L2')
            join_obj([bpy.data.objects['Version L1'], bpy.data.objects['Version L2']], 'Version Angle L')
            # remove_doubles(bpy.data.objects['NeckShaft Angle L'])

            move_to_collection("Measurements", bpy.data.objects['Version Angle L'])

            coord_values = get_coordinates(['Neck centre L P:TranPL',"Version Point L",'Neck centre L P:TranPL.CorPL'])
            my_measurements["Version Angle L"] =  angle_triangle(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5], coord_values[6], coord_values[7], coord_values[8])

        
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}




class Hip_OT_VersionAngle_R(Operator):
    """ """
    bl_label = "Version Angle R"
    bl_idname = "object.versionangler"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Right", "Projections","Measurements"])
        unhide_list(["Version Angle R",'Hip Centre R P:TranPR','Pelvis Centre R','Neck centre R P:TranPR','Neck centre R P:TranPR.CorPR'])
        
        try:
            delete_obj(bpy.data.objects["Version Angle R"])
        except:
            pass

        check_list = check_obj_list(['Pelvis Centre R','Hip Centre R P:TranPR','Neck centre R P:TranPR','Neck centre R P:TranPR.CorPR'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre R P:TranPR'], 'Hip Centre R P:TranPR for Version Angle R1')
            copy_object(bpy.data.objects['Neck centre R P:TranPR'], 'NCR P:TranPR for Version Angle R1')
            make_axis([bpy.data.objects['Hip Centre R P:TranPR for Version Angle R1'], bpy.data.objects['NCR P:TranPR for Version Angle R1']], "Version Angle Rine1")

            copy_object(bpy.data.objects['Pelvis Centre R'], 'Pelvis Centre R for Version Angle R2')
            copy_object(bpy.data.objects['Neck centre R P:TranPR.CorPR'], 'NCR P:TranPR.CorPR for Version Angle R2')
            make_axis([bpy.data.objects['Pelvis Centre R for Version Angle R2'], bpy.data.objects['NCR P:TranPR.CorPR for Version Angle R2']], "Version Angle Rine2")

            join_obj([bpy.data.objects["Version Angle Rine1"], bpy.data.objects["Version Angle Rine2"]], 'Version Point R')
            
            vertex_group(bpy.data.objects["Version Point R"])
            copy_object(bpy.data.objects["Version Point R"], "Version Point R copy1")
            copy_object(bpy.data.objects["Version Point R"], "Version Point R copy2")
        
            copy_object(bpy.data.objects['Neck centre R P:TranPR'], 'Neck centre R P:TranPR for Version Angle R')
            copy_object(bpy.data.objects['Neck centre R P:TranPR.CorPR'], 'Neck centre R P:TranPR.CorPR for Version Angle R')
            make_axis([bpy.data.objects["Version Point R copy1"], bpy.data.objects['Neck centre R P:TranPR for Version Angle R']], 'Version R1')
            make_axis([bpy.data.objects["Version Point R copy2"], bpy.data.objects['Neck centre R P:TranPR.CorPR for Version Angle R']], 'Version R2')
            join_obj([bpy.data.objects['Version R1'], bpy.data.objects['Version R2']], 'Version Angle R')
            # remove_doubles(bpy.data.objects['NeckShaft Angle L'])

            move_to_collection("Measurements", bpy.data.objects['Version Angle R'])

            coord_values = get_coordinates(['Neck centre R P:TranPR',"Version Point R",'Neck centre R P:TranPR.CorPR'])
            my_measurements["Version Angle R"] =  angle_triangle(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5], coord_values[6], coord_values[7], coord_values[8])



        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}




class Hip_OT_AcetabularOffset_L(Operator):
    """ """
    bl_label = "Acetabular Offset L"
    bl_idname = "object.acetabularoffsetl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["APP", "Left", "Projections","Measurements"])
        unhide_list(["Acetabular Offset L",'TearDrop L P:CorPL.TranPL','Pelvis Centre L P:CorPL.TranPL'])
        
        try:
            delete_obj(bpy.data.objects["Acetabular Offset L"])
        except:
            pass

        check_list = check_obj_list(['TearDrop L P:CorPL.TranPL','Pelvis Centre L P:CorPL.TranPL'])
        if len(check_list) == 0:

            copy_object(bpy.data.objects['TearDrop L P:CorPL.TranPL'], 'TDL P:CorPL.TranPL for AOffset L1')
            copy_object(bpy.data.objects['Pelvis Centre L P:CorPL.TranPL'], 'PelvisC L P:CorPL.TranPL for AOffset L2')
            make_axis([bpy.data.objects['TDL P:CorPL.TranPL for AOffset L1'], bpy.data.objects['PelvisC L P:CorPL.TranPL for AOffset L2']], "Acetabular Offset L")

    
            move_to_collection("Measurements", bpy.data.objects["Acetabular Offset L"])

            coord_values = get_coordinates(["TearDrop L P:CorPL.TranPL","Pelvis Centre L P:CorPL.TranPL"])
            my_measurements["Acetabular Offset L"] = distance(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5])
            
        

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}



class Hip_OT_AcetabularOffset_R(Operator):
    """ """
    bl_label = "Acetabular Offset R"
    bl_idname = "object.acetabularoffsetr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Right", "Projections","Measurements"])
        unhide_list(["Acetabular Offset R",'TearDrop R P:CorPR.TranPR','Pelvis Centre R P:CorPR.TranPR'])
        
        try:
            delete_obj(bpy.data.objects["Acetabular Offset R"])
        except:
            pass

        check_list = check_obj_list(['TearDrop R P:CorPR.TranPR','Pelvis Centre R P:CorPR.TranPR'])
        if len(check_list) == 0:

            copy_object(bpy.data.objects['TearDrop R P:CorPR.TranPR'], 'TDR P:CorPR.TranPR for AOffset R1')
            copy_object(bpy.data.objects['Pelvis Centre R P:CorPR.TranPR'], 'PelvisC R P:CorPR.TranPR for AOffset R2')
            make_axis([bpy.data.objects['TDR P:CorPR.TranPR for AOffset R1'], bpy.data.objects['PelvisC R P:CorPR.TranPR for AOffset R2']], "Acetabular Offset R")

    
            move_to_collection("Measurements", bpy.data.objects["Acetabular Offset R"])

            coord_values = get_coordinates(["TearDrop R P:CorPR.TranPR","Pelvis Centre R P:CorPR.TranPR"])
            my_measurements["Acetabular Offset R"] = distance(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5])
            

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class Hip_OT_LegLength_L(Operator):
    """ """
    bl_label = "Leg Length L"
    bl_idname = "object.leglengthl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Left", "Projections","Measurements"])
        unhide_list(["Leg Length L", 'TearDrop L P:CorPL.SagPL','LesserTrochanter L P:CorPL.SagPL'])
        
        try:
            delete_obj(bpy.data.objects["Leg Length L"])
        except:
            pass

        check_list = check_obj_list(['TearDrop L P:CorPL.SagPL','LesserTrochanter L P:CorPL.SagPL'])
        if len(check_list) == 0:

            copy_object(bpy.data.objects['TearDrop L P:CorPL.SagPL'], 'TDL P:CorPL.SagPL for Lgth L1')
            copy_object(bpy.data.objects['LesserTrochanter L P:CorPL.SagPL'], 'LTrocht L P:CorPL.SagPL for Lgth L2')
            make_axis([bpy.data.objects['TDL P:CorPL.SagPL for Lgth L1'], bpy.data.objects['LTrocht L P:CorPL.SagPL for Lgth L2']], "Leg Length L")

        
            move_to_collection("Measurements", bpy.data.objects["Leg Length L"])

            coord_values = get_coordinates(["TearDrop L P:CorPL.SagPL","LesserTrochanter L P:CorPL.SagPL"])
            my_measurements["Leg Length L"] = distance(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5])
            

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}



class Hip_OT_LegLength_R(Operator):
    """ """
    bl_label = "Leg Length R"
    bl_idname = "object.leglengthr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Right", "Projections","Measurements"])
        unhide_list(["Leg Length R", 'TearDrop R P:CorPR.SagPR','LesserTrochanter R P:CorPR.SagPR'])
        
        try:
            delete_obj(bpy.data.objects["Leg Length R"])
        except:
            pass

        check_list = check_obj_list(['TearDrop R P:CorPR.SagPR','LesserTrochanter R P:CorPR.SagPR'])
        if len(check_list) == 0:

            copy_object(bpy.data.objects['TearDrop R P:CorPR.SagPR'], 'TDR P:CorPR.SagPR for Lgth R1')
            copy_object(bpy.data.objects['LesserTrochanter R P:CorPR.SagPR'], 'LTrocht R P:CorRR.SagPR for Lgth R2')
            make_axis([bpy.data.objects['TDR P:CorPR.SagPR for Lgth R1'], bpy.data.objects['LTrocht R P:CorRR.SagPR for Lgth R2']], "Leg Length R")

        
            move_to_collection("Measurements", bpy.data.objects["Leg Length R"])

            coord_values = get_coordinates(["TearDrop R P:CorPR.SagPR","LesserTrochanter R P:CorPR.SagPR"])
            my_measurements["Leg Length R"] = distance(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5])
            
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class Hip_OT_HipLength_L(Operator):
    """ """
    bl_label = "Hip Length L"
    bl_idname = "object.hiplengthl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Left", "Projections","Measurements"])
        unhide_list(["Hip Length L",'Hip Centre L P:CorPL.SagPL','LesserTrochanter L P:CorPL.SagPL'])
        
        try:
            delete_obj(bpy.data.objects["Hip Length L"])
        except:
            pass

        check_list = check_obj_list(['Hip Centre L P:CorPL.SagPL','LesserTrochanter L P:CorPL.SagPL'])
        if len(check_list) == 0:

            copy_object(bpy.data.objects['Hip Centre L P:CorPL.SagPL'], 'Hip Centre L P:CorPL.SagPL for Hp L1')
            copy_object(bpy.data.objects['LesserTrochanter L P:CorPL.SagPL'], 'LTrocht L P:CorPL.SagPL for Hp L2')
            make_axis([bpy.data.objects['Hip Centre L P:CorPL.SagPL for Hp L1'], bpy.data.objects['LTrocht L P:CorPL.SagPL for Hp L2']], "Hip Length L")

            # join_obj([bpy.data.objects[ Hip Length L1"], bpy.data.objects[ Hip Length L2"]],  Hip Length L') 
            # remove_doubles(bpy.data.objects[ Hip Length L"])
            move_to_collection("Measurements", bpy.data.objects["Hip Length L"])

            coord_values = get_coordinates(["Hip Centre L P:CorPL.SagPL","LesserTrochanter L P:CorPL.SagPL"])
            my_measurements["Hip Length L"] = distance(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5])
            

        

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}



class Hip_OT_HipLength_R(Operator):
    """ """
    bl_label = "Hip Length R"
    bl_idname = "object.hiplengthr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Right", "Projections","Measurements"])
        unhide_list(["Hip Length R", 'Hip Centre R P:CorPR.SagPR','LesserTrochanter R P:CorPR.SagPR'])
        
        try:
            delete_obj(bpy.data.objects["Hip Length R"])
        except:
            pass

        check_list = check_obj_list(['Hip Centre R P:CorPR.SagPR','LesserTrochanter R P:CorPR.SagPR'])
        if len(check_list) == 0:

            copy_object(bpy.data.objects['Hip Centre R P:CorPR.SagPR'], 'Hip Centre R P:CorPR.SagPR for Hip Length R1')
            copy_object(bpy.data.objects['LesserTrochanter R P:CorPR.SagPR'], 'LTrocht R P:CorPR.SagPR for Hip Length R2')
            make_axis([bpy.data.objects['Hip Centre R P:CorPR.SagPR for Hip Length R1'], bpy.data.objects['LTrocht R P:CorPR.SagPR for Hip Length R2']], "Hip Length R")  
            move_to_collection("Measurements", bpy.data.objects["Hip Length R"])

            coord_values = get_coordinates(["Hip Centre R P:CorPR.SagPR","LesserTrochanter R P:CorPR.SagPR"])
            my_measurements["Hip Length R"] =  distance(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5])
           

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}





        




class Hip_OT_NeckShaftAngle_R(Operator):
    """ """
    bl_label = "NeckShaft Angle R"
    bl_idname = "object.neckshaftangler"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Right", "Projections", "Measurements"])
        unhide_list(["NeckShaft Angle R", 'Hip Centre R','Neck centre R P:FemurAR','ProxAntPt R','DistAntPt R'])


        try:
            delete_obj(bpy.data.objects["NeckShaft Angle R"])
        except:
            pass

        check_list = check_obj_list(['Hip Centre R','Neck centre R P:FemurAR','ProxAntPt R','DistAntPt R'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre R'], 'Hip Centre R for NeckShaft Angle R1')
            copy_object(bpy.data.objects['Neck centre R P:FemurAR'], 'Neck centre R P:FemurAR for NeckShaft Angle R1')
            make_axis([bpy.data.objects['Hip Centre R for NeckShaft Angle R1'], bpy.data.objects['Neck centre R P:FemurAR for NeckShaft Angle R1']], "NeckShaft Angle Rine1")

            copy_object(bpy.data.objects['ProxAntPt R'], 'ProxAntPt R for NeckShaft Angle R2')
            copy_object(bpy.data.objects['DistAntPt R'], 'DistAntPt R for NeckShaft Angle R2')
            make_axis([bpy.data.objects['ProxAntPt R for NeckShaft Angle R2'], bpy.data.objects['DistAntPt R for NeckShaft Angle R2']], "NeckShaft Angle Rine2")
            
            join_obj([bpy.data.objects["NeckShaft Angle Rine1"], bpy.data.objects["NeckShaft Angle Rine2"]], 'NeckShaft Point R') 
            vertex_group(bpy.data.objects["NeckShaft Point R"])
            copy_object(bpy.data.objects["NeckShaft Point R"], "NeckShaft Point R copy1")
            copy_object(bpy.data.objects["NeckShaft Point R"], "NeckShaft Point R copy2")
        
            copy_object(bpy.data.objects['Hip Centre R'], 'Hip Centre R for NeckShaft Angle R')
            copy_object(bpy.data.objects['DistAntPt R'], 'DistAntPt R for NeckShaft Angle R')
            make_axis([bpy.data.objects["NeckShaft Point R copy1"], bpy.data.objects['Hip Centre R for NeckShaft Angle R']], 'NeckShaft R1')
            make_axis([bpy.data.objects["NeckShaft Point R copy2"], bpy.data.objects['DistAntPt R for NeckShaft Angle R']], 'NeckShaft R2')
            join_obj([bpy.data.objects['NeckShaft R1'], bpy.data.objects['NeckShaft R2']], 'NeckShaft Angle R')
            # remove_doubles(bpy.data.objects['NeckShaft Angle R'])

            move_to_collection("Measurements", bpy.data.objects['NeckShaft Angle R'])

            coord_values = get_coordinates(['DistAntPt R',"NeckShaft Point R",'Hip Centre R'])
            my_measurements["NeckShaft Angle R"] =  angle_triangle(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5], coord_values[6], coord_values[7], coord_values[8])

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}




class Hip_OT_NeckShaftAngle_L(Operator):
    """ """
    bl_label = "NeckShaft Angle L"
    bl_idname = "object.neckshaftanglel"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Left", "Projections", "Measurements"])
        unhide_list(["NeckShaft Angle L", 'Hip Centre L','Neck centre L P:FemurAL','ProxAntPt L','DistAntPt L'])


        try:
            delete_obj(bpy.data.objects["NeckShaft Angle L"])
        except:
            pass

        check_list = check_obj_list(['Hip Centre L','Neck centre L P:FemurAL','ProxAntPt L','DistAntPt L'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Centre L'], 'Hip Centre L for NeckShaft Angle L1')
            copy_object(bpy.data.objects['Neck centre L P:FemurAL'], 'Neck centre L P:FemurAL for NeckShaft Angle L1')
            make_axis([bpy.data.objects['Hip Centre L for NeckShaft Angle L1'], bpy.data.objects['Neck centre L P:FemurAL for NeckShaft Angle L1']], "NeckShaft Angle Line1")

            copy_object(bpy.data.objects['ProxAntPt L'], 'ProxAntPt L for NeckShaft Angle L2')
            copy_object(bpy.data.objects['DistAntPt L'], 'DistAntPt L for NeckShaft Angle L2')
            make_axis([bpy.data.objects['ProxAntPt L for NeckShaft Angle L2'], bpy.data.objects['DistAntPt L for NeckShaft Angle L2']], "NeckShaft Angle Line2")
            
            join_obj([bpy.data.objects["NeckShaft Angle Line1"], bpy.data.objects["NeckShaft Angle Line2"]], 'NeckShaft Point L') 
            vertex_group(bpy.data.objects["NeckShaft Point L"])
            copy_object(bpy.data.objects["NeckShaft Point L"], "NeckShaft Point L copy1")
            copy_object(bpy.data.objects["NeckShaft Point L"], "NeckShaft Point L copy2")
        
            copy_object(bpy.data.objects['Hip Centre L'], 'Hip Centre L for NeckShaft Angle L')
            copy_object(bpy.data.objects['DistAntPt L'], 'DistAntPt L for NeckShaft Angle L')
            make_axis([bpy.data.objects["NeckShaft Point L copy1"], bpy.data.objects['Hip Centre L for NeckShaft Angle L']], 'NeckShaft L1')
            make_axis([bpy.data.objects["NeckShaft Point L copy2"], bpy.data.objects['DistAntPt L for NeckShaft Angle L']], 'NeckShaft L2')
            join_obj([bpy.data.objects['NeckShaft L1'], bpy.data.objects['NeckShaft L2']], 'NeckShaft Angle L')
            # remove_doubles(bpy.data.objects['NeckShaft Angle R'])

            move_to_collection("Measurements", bpy.data.objects['NeckShaft Angle L'])

            coord_values = get_coordinates(['DistAntPt L',"NeckShaft Point L",'Hip Centre L'])
            my_measurements["NeckShaft Angle L"] =  angle_triangle(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5], coord_values[6], coord_values[7], coord_values[8])

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}




class Hip_OT_FemoralOffset_R(Operator):
    """ """
    bl_label = "FemoralOffset R"
    bl_idname = "object.femoraloffsetr"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Right", "Projections","Measurements"])
        unhide_list(["FemoralOffset R",'Hip Centre R','Hip Centre R P:FemAR'])
        
        try:
            delete_obj(bpy.data.objects["FemoralOffset R"])
        except:
            pass

        check_list = check_obj_list(['Hip Centre R','Hip Centre R P:FemAR'])
        if len(check_list) == 0:

            copy_object(bpy.data.objects['Hip Centre R'], 'Hip Centre R for FemoralOffset R1')
            copy_object(bpy.data.objects['Hip Centre R P:FemAR'], 'Hip Centre R P:FemAR for FemoralOffset R2')
            make_axis([bpy.data.objects['Hip Centre R for FemoralOffset R1'], bpy.data.objects['Hip Centre R P:FemAR for FemoralOffset R2']], "FemoralOffset R")  
            move_to_collection("Measurements", bpy.data.objects["FemoralOffset R"])

            coord_values = get_coordinates(["Hip Centre R","Hip Centre R P:FemAR"])
            my_measurements["FemoralOffset R"] =  distance(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5])
           

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class Hip_OT_FemoralOffset_L(Operator):
    """ """
    bl_label = "FemoralOffset L"
    bl_idname = "object.femoraloffsetl"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Left", "Projections","Measurements"])
        unhide_list(["FemoralOffset L",'Hip Centre L','Hip Centre L P:FemAL'])
        
        try:
            delete_obj(bpy.data.objects["FemoralOffset L"])
        except:
            pass

        check_list = check_obj_list(['Hip Centre L','Hip Centre L P:FemAL'])
        if len(check_list) == 0:

            copy_object(bpy.data.objects['Hip Centre L'], 'Hip Centre L for FemoralOffset L1')
            copy_object(bpy.data.objects['Hip Centre L P:FemAL'], 'Hip Centre L P:FemAL for FemoralOffset L2')
            make_axis([bpy.data.objects['Hip Centre L for FemoralOffset L1'], bpy.data.objects['Hip Centre L P:FemAL for FemoralOffset L2']], "FemoralOffset L")  
            move_to_collection("Measurements", bpy.data.objects["FemoralOffset L"])

            coord_values = get_coordinates(["Hip Centre L","Hip Centre L P:FemAL"])
            my_measurements["FemoralOffset L"] =  distance(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5])
           

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}
        

        
class Hip_OT_savetofile(Operator):
    """ """
    bl_label = "Save to file"
    bl_idname = "object.hipsavetofile"
    bl_options = {"REGISTER", "UNDO"}
    
    
    def execute(self, context):
        Hip_save_to_file(my_measurements)
        return {'FINISHED'}  