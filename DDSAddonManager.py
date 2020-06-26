#list of add-ons to show. 
AO = [
    "node_wrangler",
    "DDSName",
    "mesh_auto_mirror",
    "mesh_looptools",
    "DDSAnimeTools",
    "object_collection_manager",
    "rigify", 
    "object_edit_linked",
    "camera_dolly_crane_rigs",
    "add_camera_rigs",
    "magic_uv", 
    "import_runtime_mhx2",
    "power_sequencer", 
    "ant_landscape",
    "add_mesh_extra_objects",
    "add_mesh_BoltFactory",
    "add_curve_extra_objects",
]
#list of names to use for add-on on panel
AN = [
    "Node Wrangler",
    "DDS Name",
    "Auto Mirror",
    "Loop Tools",
    "DDS Animation Tools",
    "Collection Manager",
    "Rigify", 
    "Edit Link library",
    "Camera Rigs",
    "Camera Rigs",
    "Magic UV", 
    "Make Human MHX2",
    "Power Sequencer", 
    "ANT Landscape",
    "Mesh Extras",
    "Bolt Factory",
    "Curve Extras",
]

bl_info = {
    "name": "DDS Add-on Manager",
    "author": "Dwayne Savage",
    "version": (0, 2),
    "blender": (2, 83, 0),
    "location": "3D View->sidebar->Tools /n Properties editor Active Tools & Workspace tab",
    "description": "A way to turn on/off add-ons as they are needed.",
    "warning": "",
    "wiki_url": "http://blenderclassroom.com",
    "category": "3D View",
    }


import bpy
from bpy.types import Panel
import addon_utils

#sets up the animation panel
class DDSAddMan(Panel):
    bl_idname = "DDS_PT_addman"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    bl_label = "Add-on Manager"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        #Add-on Settings
        addons = [(mod, addon_utils.module_bl_info(mod)) for mod in addon_utils.modules(refresh=False)]
        col = self.layout.column(align=True)
        AC = -1
        for Mod_Name in AO:
            AC=AC+1
            #Go through list of all add-ons 
            for Mod, info in addons:
                #Check to see if Addon exist
                if (Mod.__name__ == Mod_Name):
                    is_enabled = context.preferences.addons.find(Mod_Name)
                    
                    if is_enabled>-1:
                        col.operator("preferences.addon_disable", icon='CHECKBOX_HLT', text=AN[AC], emboss=True).module = Mod_Name
                    else:
                        col.operator("preferences.addon_enable", icon='CHECKBOX_DEHLT', text=AN[AC], emboss=True).module = Mod_Name

                    break


def register():
    bpy.utils.register_class(DDSAddMan)
    
def unregister():
    bpy.utils.unregister_class(DDSAddMan)

if __name__ == "__main__": 
    register()    