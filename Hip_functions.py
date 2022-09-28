import bpy

def deselect():
    bpy.ops.object.select_all(action='DESELECT')


def unhide(obj):
    deselect()
    bpy.context.view_layer.objects.active = obj
    bpy.context.object.hide_set(False)


def unhide_list(myList):
    for obj in myList:
        try:
            unhide(bpy.data.objects[obj])
        except:
            pass

def select_activate(obj):
    deselect()
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def copy_object(obj, name):
    deselect()
    select_activate(obj)
    bpy.ops.object.duplicate_move()  
    bpy.context.object.name = name


def make_axis(obs, name):
    deselect()
    select_activate(obs[0])
    ctx = bpy.context.copy()   
    ctx['active object'] = obs[0]
    ctx['selected_editable_objects'] = obs
    bpy.ops.object.join(ctx)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    bpy.context.object.name = name


def save_orientation_InEditMode(obj, myType):
    deselect()
    select_activate(obj)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_mode(type=myType)
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.transform.create_orientation(use=True)
    bpy.ops.object.editmode_toggle()


def save_orientation_obj(obj):
    deselect()
    select_activate(obj)
    bpy.ops.transform.create_orientation(use=True)


def origin_to_geometry(obj):
    select_activate(obj)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')


def cursor_to_obj(obj):
    origin_to_geometry(obj)
    bpy.ops.view3d.snap_cursor_to_selected()


def add_plane(name):
    bpy.ops.mesh.primitive_plane_add(size=300, enter_editmode=False)
    bpy.ops.transform.transform(mode = 'ALIGN')
    bpy.context.object.name = name


def delete_obj(obj):
    deselect()
    select_activate(obj)
    bpy.ops.object.delete(use_global=False, confirm=False)
    

def shrinkwrap_obj(obj, target):
    bpy.ops.object.modifier_add(type = "SHRINKWRAP")
    obj.modifiers["Shrinkwrap"].target = target
    bpy.ops.object.modifier_apply(modifier="Shrinkwrap")
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
    # bpy.ops.outliner.item_activate(deselect_all=True)
    
    # bpy.ops.object.move_to_collection(collection_index=5)


def join_obj(obs, name):
    deselect()
    select_activate(obs[0])
    ctx = bpy.context.copy()
    ctx['active object'] = obs[0]
    ctx['selected_editable_objects'] = obs
    bpy.ops.object.join(ctx)
    bpy.context.object.name = name

def remove_doubles(obj):
    select_activate(obj)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.remove_doubles()
    bpy.ops.object.editmode_toggle()


def vertex_group(obj):
    select_activate(obj)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.object.vertex_group_add()
    bpy.ops.object.vertex_group_assign()
    bpy.ops.tinycad.vertintersect()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.object.vertex_group_select()
    bpy.ops.mesh.separate(type = "SELECTED")
    bpy.ops.object.editmode_toggle()
    delete_obj(bpy.context.selected_objects[1])


def add_new_collection(name):
    my_collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(my_collection)


def get_collection_pos(coll_name):
    coll_list = list(bpy.data.collections)
    try:
        return coll_list.index(bpy.data.collections[coll_name])
    except:
        return -1
    

def move_to_collection(coll_name, obj):
    try:
        bpy.data.collections[coll_name].objects.link(obj)
    except:
        pass

    coll_list = list(bpy.data.collections)

    for coll in coll_list:
        if coll != bpy.data.collections[coll_name]:
            try:
                coll.objects.unlink(obj)
            except:
                pass


def check_create_collection(myList):
    for name in myList:
        unhide_collection(name)
        if (get_collection_pos(name) == -1):
            add_new_collection(name)


def coll_list():
    my_list = ["APP", "Right", "Left", "Projections", "Measurements"]
    return my_list


def transform_to_orientation():
    bpy.ops.transform.transform(mode = 'ALIGN')


def check_obj_list(obj_list):
    return_list = [] 
    objects_list = [obj.name for obj in list(bpy.data.objects)]
    for obj in obj_list:
        if obj not in objects_list:
            return_list.append(obj)
    return return_list


def unhide_collection(name):
    try:
        vlayer = bpy.context.scene.view_layers['View Layer']
        vlayer.layer_collection.children[name].hide_viewport = False
        unhide_list([name for name in bpy.data.collections[name].objects])   
    except:
        pass

def get_coordinates(points):
    coord_values = []
    for point in points:

        origin_to_geometry(bpy.data.objects[point])

        point_y = bpy.data.objects[point].location[0]
        coord_values.append(point_y)
        point_z = bpy.data.objects[point].location[1]
        coord_values.append(point_z)
        point_x = bpy.data.objects[point].location[2]
        coord_values.append(point_x)
    return coord_values   


def add_single_vert(name):
    bpy.ops.mesh.primitive_vert_add()
    bpy.ops.object.editmode_toggle()
    bpy.context.object.name = name



