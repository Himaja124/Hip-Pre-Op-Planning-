import bpy
from bpy.types import Operator
from .Hip_functions import copy_object, shrinkwrap_obj, unhide_list, move_to_collection, delete_obj, check_create_collection, check_obj_list

class HIP_OT_Projections(Operator):
    """ """
    bl_label = "Projections"
    bl_idname = "object.projections"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["APP", "Right", "Left", "Projections"])
        unhide_list(['Pelvis Centre L','Hip Centre L','Hip Centre R','Neck centre L','Pelvis Centre R','Neck centre R','TearDrop L','TearDrop R','LesserTrochanter L','LesserTrochanter R'])
        unhide_list(['Hip Centre L P:CorPL','Hip Centre R P:FemAR','Hip Centre L P:FemAL','Neck centre L P:FemurAL','Neck centre R P:FemurAR','Hip Centre L P:TranPL','Hip Centre R P:TranPR','Hip Centre R P:CorPR','Hip Centre L P:CorPL.SagPL','Hip Centre R P:CorPR.SagPR','Neck centre L P:CorPL','DistAntPt L P:CorPL','ProxAntPt L P:CorPL','Neck centre L P:CorPL.SagPL','Neck centre R P:CorPR','Neck centre R P:TranPR','Neck centre R P:TranPR.CorPR','Pelvis Centre R P:CorPR','Neck centre R P:CorPR.SagPR','TearDrop L P:CorPL','TearDrop L P:CorPL.TranPL','Pelvis Centre L P:CorPL','Pelvis Centre L P:CorPL.TranPL','TearDrop R P:CorPR','TearDrop R P:CorPR.TranPR','Pelvis Centre R P:CorPR','Pelvis Centre R P:CorPR.TranPR','LesserTrochanter L P:CorPL','LesserTrochanter L P:CorPL.SagPL','LesserTrochanter R P:CorPR','LesserTrochanter R P:CorPR.SagPR','TearDrop L P:CorPR.SagPR','TearDrop R P:CorPR.SagPR','TearDrop L P:CorPL.TranPL'])
     

        try:
            delete_obj(bpy.data.objects["Neck centre L P:CorPL"])
        except:
            pass

        if (len(check_obj_list(['Neck centre L',"Coronal Plane at Pelvis L"])) == 0):

            try:

                copy_object(bpy.data.objects['Neck centre L'], "Neck centre L P:CorPL")
                shrinkwrap_obj(bpy.data.objects["Neck centre L P:CorPL"], bpy.data.objects["Coronal Plane at Pelvis L"])
                # bpy.ops.outliner.item_activate(deselect_all=True)
                # bpy.ops.object.modifier_apply(modifier="Shrinkwrap")
                # bpy.ops.object.move_to_collection(collection_index=5)
                move_to_collection("Projections", bpy.data.objects["Neck centre L P:CorPL"])   
            except:
                pass

        try:
            delete_obj(bpy.data.objects["Neck centre L P:FemurAL"])

        except:
            pass

        if (len(check_obj_list(['Neck centre L',"Femur Plane L"])) == 0):
            try:
                copy_object(bpy.data.objects['Neck centre L'], "Neck centre L P:FemurAL")
                shrinkwrap_obj(bpy.data.objects["Neck centre L P:FemurAL"], bpy.data.objects["Femur Plane L"])
                move_to_collection("Projections", bpy.data.objects["Neck centre L P:FemurAL"])   
            except:
                pass




        
        try:
            delete_obj(bpy.data.objects["Hip Centre L P:FemAL"])
        except:
            pass

        if (len(check_obj_list(['Hip Centre L',"Femur Offset Plane L"])) == 0):
            try:
                copy_object(bpy.data.objects['Hip Centre L'], "Hip Centre L P:FemAL")
                shrinkwrap_obj(bpy.data.objects["Hip Centre L P:FemAL"], bpy.data.objects["Femur Offset Plane L"])
                move_to_collection("Projections", bpy.data.objects["Hip Centre L P:FemAL"])   
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Hip Centre R P:FemAR"])
        except:
            pass

        if (len(check_obj_list(['Hip Centre R',"Femur Offset Plane R"])) == 0):
            try:
                copy_object(bpy.data.objects['Hip Centre R'], "Hip Centre R P:FemAR")
                shrinkwrap_obj(bpy.data.objects["Hip Centre R P:FemAR"], bpy.data.objects["Femur Offset Plane R"])
                move_to_collection("Projections", bpy.data.objects["Hip Centre R P:FemAR"])   
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Neck centre R P:FemurAR"])
        except:
            pass

        if (len(check_obj_list(['Neck centre R',"Femur Plane R"])) == 0):
            try:
                copy_object(bpy.data.objects['Neck centre R'], "Neck centre R P:FemurAR")
                shrinkwrap_obj(bpy.data.objects["Neck centre R P:FemurAR"], bpy.data.objects["Femur Plane R"])
                move_to_collection("Projections", bpy.data.objects["Neck centre R P:FemurAR"])   
            except:
                pass






        try:
            delete_obj(bpy.data.objects["ProxAntPt L P:CorPL"])
        except:
            pass

        if (len(check_obj_list(['ProxAntPt L',"Coronal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['ProxAntPt L'], "ProxAntPt L P:CorPL")
                shrinkwrap_obj(bpy.data.objects["ProxAntPt L P:CorPL"], bpy.data.objects["Coronal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["ProxAntPt L P:CorPL"])   
            except:
                pass

            

        try:
            delete_obj(bpy.data.objects["DistAntPt L P:CorPL"])
        except:
            pass

        if (len(check_obj_list(['DistAntPt L',"Coronal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['DistAntPt L'], "DistAntPt L P:CorPL")
                shrinkwrap_obj(bpy.data.objects["DistAntPt L P:CorPL"], bpy.data.objects["Coronal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["DistAntPt L P:CorPL"])   
            except:
                pass


        try:
            delete_obj(bpy.data.objects["ProxAntPt R P:CorPR"])
        except:
            pass

        if (len(check_obj_list(['ProxAntPt R',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['ProxAntPt R'], "ProxAntPt R P:CorPR")
                shrinkwrap_obj(bpy.data.objects["ProxAntPt R P:CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["ProxAntPt R P:CorPR"])   
            except:
                pass

            

        try:
            delete_obj(bpy.data.objects["DistAntPt R P:CorPR"])
        except:
            pass

        if (len(check_obj_list(['DistAntPt R',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['DistAntPt R'], "DistAntPt R P:CorPR")
                shrinkwrap_obj(bpy.data.objects["DistAntPt R P:CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["DistAntPt R P:CorPR"])   
            except:
                pass

            

        try:
            delete_obj(bpy.data.objects["Neck centre L P:CorPL.SagPL"])
        except:
            pass

        if (len(check_obj_list(['Neck centre L P:CorPL',"Sagittal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['Neck centre L P:CorPL'], "Neck centre L P:CorPL.SagPL")
                shrinkwrap_obj(bpy.data.objects["Neck centre L P:CorPL.SagPL"], bpy.data.objects["Sagittal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["Neck centre L P:CorPL.SagPL"])   
            except:
                pass

        

        try:
            delete_obj(bpy.data.objects["Neck centre R P:CorPR"])
        except:
            pass

        if (len(check_obj_list(['Neck centre R',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['Neck centre R'], "Neck centre R P:CorPR")
                shrinkwrap_obj(bpy.data.objects["Neck centre R P:CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["Neck centre R P:CorPR"])   
            except:
                pass   


        try:
            delete_obj(bpy.data.objects["Neck centre R P:CorPR.SagPR"])
        except:
            pass

        if (len(check_obj_list(['Neck centre R P:CorPR',"Sagittal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['Neck centre R P:CorPR'], "Neck centre R P:CorPR.SagPR")
                shrinkwrap_obj(bpy.data.objects["Neck centre R P:CorPR.SagPR"], bpy.data.objects["Sagittal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["Neck centre R P:CorPR.SagPR"])   
            except:
                pass

        

        
        try:
            delete_obj(bpy.data.objects["Neck centre R P:TranPR"])
        except:
            pass

        if (len(check_obj_list(['Neck centre R',"Transverse Plane At Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['Neck centre R'], "Neck centre R P:TranPR")
                shrinkwrap_obj(bpy.data.objects["Neck centre R P:TranPR"], bpy.data.objects["Transverse Plane At Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["Neck centre R P:TranPR"])   
            except:
                pass   


        try:
            delete_obj(bpy.data.objects["Neck centre R P:TranPR.CorPR"])
        except:
            pass

        if (len(check_obj_list(['Neck centre R P:TranPR',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['Neck centre R P:TranPR'], "Neck centre R P:TranPR.CorPR")
                shrinkwrap_obj(bpy.data.objects["Neck centre R P:TranPR.CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["Neck centre R P:CorPR.SagPR"])   
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Neck centre L P:TranPL"])
        except:
            pass

        if (len(check_obj_list(['Neck centre L',"Transverse Plane At Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['Neck centre L'], "Neck centre L P:TranPL")
                shrinkwrap_obj(bpy.data.objects["Neck centre L P:TranPL"], bpy.data.objects["Transverse Plane At Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["Neck centre L P:TranPL"])   
            except:
                pass   


        try:
            delete_obj(bpy.data.objects["Neck centre L P:TranPL.CorPL"])
        except:
            pass

        if (len(check_obj_list(['Neck centre L P:TranPL',"Coronal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['Neck centre L P:TranPL'], "Neck centre L P:TranPL.CorPL")
                shrinkwrap_obj(bpy.data.objects["Neck centre L P:TranPL.CorPL"], bpy.data.objects["Coronal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["Neck centre L P:CorPL.SagPL"])   
            except:
                pass

 


        try:
            delete_obj(bpy.data.objects["Pelvis Centre L P:CorPL"])
        except:
            pass

        if (len(check_obj_list(['Pelvis Centre L',"Coronal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['Pelvis Centre L'], "Pelvis Centre L P:CorPL")
                shrinkwrap_obj(bpy.data.objects["Pelvis Centre L P:CorPL"], bpy.data.objects["Coronal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["Pelvis Centre L P:CorPL"])   
            except:
                pass


        
        try:
            delete_obj(bpy.data.objects["Pelvis Centre L P:CorPL.TranPL"])
        except:
            pass

        if (len(check_obj_list(['Pelvis Centre L P:CorPL',"Transverse Plane At Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['Pelvis Centre L P:CorPL'], "Pelvis Centre L P:CorPL.TranPL")
                shrinkwrap_obj(bpy.data.objects["Pelvis Centre L P:CorPL.TranPL"], bpy.data.objects["Transverse Plane At Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["Pelvis Centre L P:CorPR.TranPL"])   
            except:
                pass


 

        try:
            delete_obj(bpy.data.objects["Pelvis Centre R P:CorPR"])
        except:
            pass

        if (len(check_obj_list(['Pelvis Centre R',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['Pelvis Centre R'], "Pelvis Centre R P:CorPR")
                shrinkwrap_obj(bpy.data.objects["Pelvis Centre R P:CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["Pelvis Centre R P:CorPR"])   
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Pelvis Centre R P:CorPR.TranPR"])
        except:
            pass

        if (len(check_obj_list(['Pelvis Centre R P:CorPR',"Transverse Plane At Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['Pelvis Centre R P:CorPR'], "Pelvis Centre R P:CorPR.TranPR")
                shrinkwrap_obj(bpy.data.objects["Pelvis Centre R P:CorPR.TranPR"], bpy.data.objects["Transverse Plane At Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["Pelvis Centre R P:CorPR.TranPR"])   
            except:
                pass



        try:
            delete_obj(bpy.data.objects["LesserTrochanter L P:CorPL"])
        except:
            pass

        if (len(check_obj_list(['LesserTrochanter L',"Coronal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['LesserTrochanter L'], "LesserTrochanter L P:CorPL")
                shrinkwrap_obj(bpy.data.objects["LesserTrochanter L P:CorPL"], bpy.data.objects["Coronal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["LesserTrochanter L P:CorPL"])   
            except:
                pass  



        try:
            delete_obj(bpy.data.objects["LesserTrochanter L P:CorPL.SagPL"])
        except:
            pass

        if (len(check_obj_list(['LesserTrochanter L P:CorPL',"Sagittal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['LesserTrochanter L P:CorPL'], "LesserTrochanter L P:CorPL.SagPL")
                shrinkwrap_obj(bpy.data.objects["LesserTrochanter L P:CorPL.SagPL"], bpy.data.objects["Sagittal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["LesserTrochanter L P:CorPL.SagPL"])   
            except:
                pass  
     
        try:
            delete_obj(bpy.data.objects["Hip Centre L P:Cor"])
        except:
            pass

        if (len(check_obj_list(['Hip Centre L',"Coronal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Hip Centre L'], "Hip Centre L P:Cor")
                shrinkwrap_obj(bpy.data.objects["Hip Centre L P:Cor"], bpy.data.objects["Coronal Plane"])
                move_to_collection("Projections", bpy.data.objects["Hip Centre L P:Cor"])   
            except:
                pass

    
        try:
            delete_obj(bpy.data.objects["Hip Centre L P:CorPL"])
        except:
            pass

        if (len(check_obj_list(['Hip Centre L',"Coronal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['Hip Centre L'], "Hip Centre L P:CorPL")
                shrinkwrap_obj(bpy.data.objects["Hip Centre L P:CorPL"], bpy.data.objects["Coronal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["Hip Centre L P:CorPL"])   
            except:
                pass  



        try:
            delete_obj(bpy.data.objects["Hip Centre L P:TranPL"])
        except:
            pass

        if (len(check_obj_list(['Hip Centre L',"Transverse Plane At Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['Hip Centre L'], "Hip Centre L P:TranPL")
                shrinkwrap_obj(bpy.data.objects["Hip Centre L P:TranPL"], bpy.data.objects["Transverse Plane At Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["Hip Centre L P:TranPL"])   
            except:
                pass 


        try:
            delete_obj(bpy.data.objects["Hip Centre R P:TranPR"])
        except:
            pass

        if (len(check_obj_list(['Hip Centre R',"Transverse Plane At Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['Hip Centre R'], "Hip Centre R P:TranPR")
                shrinkwrap_obj(bpy.data.objects["Hip Centre R P:TranPR"], bpy.data.objects["Transverse Plane At Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["Hip Centre R P:TranPR"])   
            except:
                pass 




        try:
            delete_obj(bpy.data.objects["Hip Centre L P:CorPL.SagPL"])
        except:
            pass

        if (len(check_obj_list(['Hip Centre L P:CorPL',"Sagittal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['Hip Centre L P:CorPL'], "Hip Centre L P:CorPL.SagPL")
                shrinkwrap_obj(bpy.data.objects["Hip Centre L P:CorPL.SagPL"], bpy.data.objects["Sagittal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["Hip Centre L P:CorPL.SagPL"])   
            except:
                pass 

        try:
            delete_obj(bpy.data.objects["LesserTrochanter R P:CorPR"])
        except:
            pass

        if (len(check_obj_list(['LesserTrochanter R',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['LesserTrochanter R'], "LesserTrochanter R P:CorPR")
                shrinkwrap_obj(bpy.data.objects["LesserTrochanter R P:CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["LesserTrochanter R P:CorPR"])   
            except:
                pass  



        try:
            delete_obj(bpy.data.objects["LesserTrochanter R P:CorPR.SagPR"])
        except:
            pass

        if (len(check_obj_list(['LesserTrochanter R P:CorPR',"Sagittal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['LesserTrochanter R P:CorPR'], "LesserTrochanter R P:CorPR.SagPR")
                shrinkwrap_obj(bpy.data.objects["LesserTrochanter R P:CorPR.SagPR"], bpy.data.objects["Sagittal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["LesserTrochanter R P:CorPR.SagPR"])   
            except:
                pass  
     

    
        try:
            delete_obj(bpy.data.objects["Hip Centre R P:CorPR"])
        except:
            pass

        if (len(check_obj_list(['Hip Centre R',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['Hip Centre R'], "Hip Centre R P:CorPR")
                shrinkwrap_obj(bpy.data.objects["Hip Centre R P:CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["Hip Centre R P:CorPR"])   
            except:
                pass  



        try:
            delete_obj(bpy.data.objects["Hip Centre R P:CorPR.SagPR"])
        except:
            pass

        if (len(check_obj_list(['Hip Centre R P:CorPR',"Sagittal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['Hip Centre R P:CorPR'], "Hip Centre R P:CorPR.SagPR")
                shrinkwrap_obj(bpy.data.objects["Hip Centre R P:CorPR.SagPR"], bpy.data.objects["Sagittal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["Hip Centre R P:CorPR.SagPR"])   
            except:
                pass 


        
        
        
        try:
            delete_obj(bpy.data.objects["LesserTrochanter R P:CorPR"])
        except:
            pass

        if (len(check_obj_list(['LesserTrochanter R',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['LesserTrochanter R'], "LesserTrochanter R P:CorPR")
                shrinkwrap_obj(bpy.data.objects["LesserTrochanter R P:CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["LesserTrochanter R P:CorPR"])   
            except:
                pass  



        try:
            delete_obj(bpy.data.objects["LesserTrochanter R P:CorPR.SagPR"])
        except:
            pass

        if (len(check_obj_list(['LesserTrochanter R P:CorPR',"Sagittal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['LesserTrochanter R P:CorPR'], "LesserTrochanter R P:CorPR.SagPR")
                shrinkwrap_obj(bpy.data.objects["LesserTrochanter R P:CorPR.SagPR"], bpy.data.objects["Sagittal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["LesserTrochanter R P:CorPR.SagPR"])   
            except:
                pass  


        try:
            delete_obj(bpy.data.objects["TearDrop R P:CorPR"])
        except:
            pass

        if (len(check_obj_list(['TearDrop R',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['TearDrop R'], "TearDrop R P:CorPR")
                shrinkwrap_obj(bpy.data.objects["TearDrop R P:CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["TearDrop R P:CorPR"])   
            except:
                pass


        try:
            delete_obj(bpy.data.objects["TearDrop R P:CorPR.SagPR"])
        except:
            pass

        if (len(check_obj_list(['TearDrop R P:CorPR',"Sagittal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['TearDrop R P:CorPR'], "TearDrop R P:CorPR.SagPR")
                shrinkwrap_obj(bpy.data.objects["TearDrop R P:CorPR.SagPR"], bpy.data.objects["Sagittal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["TearDrop R P:CorPR.SagPR"])   
            except:
                pass


        try:
            delete_obj(bpy.data.objects["TearDrop R P:CorPR"])
        except:
            pass

        if (len(check_obj_list(['TearDrop R',"Coronal Plane at Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['TearDrop R'], "TearDrop R P:CorPR")
                shrinkwrap_obj(bpy.data.objects["TearDrop R P:CorPR"], bpy.data.objects["Coronal Plane at Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["TearDrop R P:CorPR"])   
            except:
                pass


        try:
            delete_obj(bpy.data.objects["TearDrop R P:CorPR.TranPR"])
        except:
            pass

        if (len(check_obj_list(['TearDrop R P:CorPR',"Transverse Plane At Pelvis R"])) == 0):
            try:
                copy_object(bpy.data.objects['TearDrop R P:CorPR'], "TearDrop R P:CorPR.TranPR")
                shrinkwrap_obj(bpy.data.objects["TearDrop R P:CorPR.TranPR"], bpy.data.objects["Transverse Plane At Pelvis R"])
                move_to_collection("Projections", bpy.data.objects["TearDrop R P:CorPR.TranPR"])   
            except:
                pass





        try:
            delete_obj(bpy.data.objects["TearDrop L P:CorPL"])
        except:
            pass

        if (len(check_obj_list(['TearDrop L',"Coronal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['TearDrop L'], "TearDrop L P:CorPL")
                shrinkwrap_obj(bpy.data.objects["TearDrop L P:CorPL"], bpy.data.objects["Coronal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["TearDrop L P:CorPL"])   
            except:
                pass


        try:
            delete_obj(bpy.data.objects["TearDrop L P:CorPL.SagPL"])
        except:
            pass

        if (len(check_obj_list(['TearDrop L P:CorPL',"Sagittal Plane at Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['TearDrop L P:CorPL'], "TearDrop L P:CorPL.SagPL")
                shrinkwrap_obj(bpy.data.objects["TearDrop L P:CorPL.SagPL"], bpy.data.objects["Sagittal Plane at Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["TearDrop L P:CorPL.SagPL"])   
            except:
                pass



        try:
            delete_obj(bpy.data.objects["TearDrop L P:CorPL.TranPL"])
        except:
            pass

        if (len(check_obj_list(['TearDrop L P:CorPL',"Transverse Plane At Pelvis L"])) == 0):
            try:
                copy_object(bpy.data.objects['TearDrop L P:CorPL'], "TearDrop L P:CorPL.TranPL")
                shrinkwrap_obj(bpy.data.objects["TearDrop L P:CorPL.TranPL"], bpy.data.objects["Transverse Plane At Pelvis L"])
                move_to_collection("Projections", bpy.data.objects["TearDrop L P:CorPL.TranPL"])   
            except:
                pass




        
        return {'FINISHED'}



    
  