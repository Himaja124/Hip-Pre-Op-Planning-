
bl_info = {
    "name" : "Hip preop-planning",
    "author" : "Himaja Chopade",
    "description" : "",
    "blender" : (3, 1, 2),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy


from .Hip_APP import HIP_OT_ASIS_L, HIP_OT_ASIS_R, HIP_OT_PubicSymphysis_L, HIP_OT_PubicSymphysis_R,Hip_OT_PubicSymphysis_Axis,Hip_OT_Pubic,Hip_OT_Plane
from .Hip_Right import Hip_OT_PelvisCentre_R,Hip_OT_Neckcentre_R,Hip_OT_HipCentre_R,Hip_OT_ProxAntPt_R,Hip_OT_DistAntPt_R,Hip_OT_GreaterTrochanter_R,Hip_OT_LesserTrochanter_R,Hip_OT_TearDrop_R,Hip_OT_FemurCentre_R,Hip_OT_LateralEpicondyle_R,Hip_OT_MedialEpicondyle_R,Hip_OT_PosteriorLateralEpicondyle_R,Hip_OT_PosteriorMedialEpicondyle_R,Hip_OT_Submit
from .Hip_Left import Hip_OT_PelvisCentre_L,Hip_OT_Neckcentre_L,Hip_OT_HipCentre_L,Hip_OT_ProxAntPt_L,Hip_OT_DistAntPt_L,Hip_OT_GreaterTrochanter_L,Hip_OT_LesserTrochanter_L,Hip_OT_TearDrop_L,Hip_OT_FemurCentre_L,Hip_OT_LateralEpicondyle_L,Hip_OT_MedialEpicondyle_L,Hip_OT_PosteriorLateralEpicondyle_L,Hip_OT_PosteriorMedialEpicondyle_L,Hip_OT_Submitt
from .Hip_Projections import HIP_OT_Projections
from .Hip_Measurements import Hip_OT_InclinationAngle_L,Hip_OT_InclinationAngle_R,Hip_OT_AcetabularOffset_L,Hip_OT_AcetabularOffset_R,Hip_OT_VersionAngle_L,Hip_OT_VersionAngle_R,Hip_OT_LegLength_L,Hip_OT_LegLength_R,Hip_OT_HipLength_L,Hip_OT_HipLength_R,Hip_OT_NeckShaftAngle_L,Hip_OT_NeckShaftAngle_R,Hip_OT_FemoralOffset_L,Hip_OT_FemoralOffset_R,Hip_OT_savetofile
from .Hip_measureIt_panel import HIP_PT_MeasureIt, MyPropertyHip

# from .HIP_Axes import HIP_OT_PubicSymphysis_Axis, HIP_OT_NeckLine_L, HIP_OT_MechanicalAxis_L, HIP_OT_AnatomicalAxis_L, HIP_OT_TransEpicondylarAxis_L, HIP_OT_PosteriorCondylarAxis_L, HIP_OT_NeckLine_R, HIP_OT_MechanicalAxis_R, HIP_OT_AnatomicalAxis_R, HIP_OT_TransEpicondylarAxis_R, HIP_OT_PosteriorCondylarAxis_R
# from .HIP_Plane import HIP_OT_ReferancePlane, HIP_OT_CoronalPlane, HIP_OT_SagittalPlane, HIP_OT_TransversePlane, HIP_OT_CoronalAtHipL, HIP_OT_SagittalAtHipL, HIP_OT_TransverseAtHipL, HIP_OT_FemurCoronalPlane_L, HIP_OT_FemurSagittalPlane_L, HIP_OT_FemurDistalPlane_L, HIP_OT_CoronalAtHipR, HIP_OT_SagittalAtHipR, HIP_OT_TransverseAtHipR, HIP_OT_FemurCoronalPlane_R, HIP_OT_FemurSagittalPlane_R, HIP_OT_FemurDistalPlane_R




from.Hip_APP_Panel import HIP_PT_APP_assignment
from.Hip_Right_Panel import HIP_PT_Right_assignment
from.Hip_Left_Panel import HIP_PT_Left_assignment 
from.Hip_Projections_Panel import HIP_PT_Projections
from.Hip_Measurements_Panel import HIP_PT_Measurements
from.Hip_measureIt import HIP_OT_EnableOrDisableMeasureIt
from.Hip_txt_save_panel import HIP_coordinates_export



classes = (MyPropertyHip,HIP_OT_ASIS_L, HIP_OT_ASIS_R, HIP_OT_PubicSymphysis_L, HIP_OT_PubicSymphysis_R,HIP_PT_APP_assignment,Hip_OT_PubicSymphysis_Axis,Hip_OT_Pubic,Hip_OT_Plane,Hip_OT_PelvisCentre_R,Hip_OT_Neckcentre_R, Hip_OT_HipCentre_R,Hip_OT_ProxAntPt_R,Hip_OT_DistAntPt_R,Hip_OT_GreaterTrochanter_R,Hip_OT_LesserTrochanter_R,Hip_OT_TearDrop_R,Hip_OT_FemurCentre_R,Hip_OT_LateralEpicondyle_R,Hip_OT_MedialEpicondyle_R,Hip_OT_PosteriorLateralEpicondyle_R,Hip_OT_PosteriorMedialEpicondyle_R,Hip_OT_Submit,Hip_OT_PelvisCentre_L, Hip_OT_Neckcentre_L, Hip_OT_HipCentre_L,Hip_OT_ProxAntPt_L,Hip_OT_DistAntPt_L,Hip_OT_GreaterTrochanter_L,Hip_OT_LesserTrochanter_L,Hip_OT_TearDrop_L,Hip_OT_FemurCentre_L,Hip_OT_LateralEpicondyle_L,Hip_OT_MedialEpicondyle_L,Hip_OT_PosteriorLateralEpicondyle_L,Hip_OT_PosteriorMedialEpicondyle_L,Hip_OT_Submitt,HIP_PT_Right_assignment,HIP_PT_Left_assignment,HIP_OT_Projections,HIP_PT_Projections,HIP_PT_Measurements,Hip_OT_InclinationAngle_L,Hip_OT_InclinationAngle_R,Hip_OT_VersionAngle_L,Hip_OT_VersionAngle_R,Hip_OT_AcetabularOffset_L,Hip_OT_AcetabularOffset_R,Hip_OT_LegLength_L,Hip_OT_LegLength_R,Hip_OT_HipLength_L,Hip_OT_HipLength_R, Hip_OT_NeckShaftAngle_L,Hip_OT_NeckShaftAngle_R,Hip_OT_FemoralOffset_L,Hip_OT_FemoralOffset_R,HIP_OT_EnableOrDisableMeasureIt,HIP_PT_MeasureIt,HIP_coordinates_export,Hip_OT_savetofile)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyPropertyHip)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool
   

if __name__ == "__main__":
    register()