import bpy

def Hip_save_to_file(my_measurements):
        scene = bpy.context.scene
        mytool = scene.my_tool
        filedir = mytool.HipMyFileDir
        filename = mytool.HipMyFileName
        
        outputFile = filedir+'/'+filename+'.txt'
        
        f = open( outputFile, 'w' )
        for angle_name, value in my_measurements.items():
            textLine = str(angle_name) + " : " + str(value) + '\n'
            f.writelines( textLine )

        f.close()
        