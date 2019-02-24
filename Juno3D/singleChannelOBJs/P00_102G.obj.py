#  Setup Blender for Juno3D rendering
# Requires JunocamLibrary.blend to be loaded before running this
import bpy
from mathutils import Quaternion
# import Juno3D geometry and textures Wavefront OBJ
bpy.ops.import_scene.obj(filepath="/Users/bswift/Downloads/PJ0EFB/P00_102G.obj",axis_forward='Y', axis_up='Z')
# Replace materials created by blender obj import with JunoTemplateMaterial from JunocamLibrary.blend
holdMatName=bpy.data.objects['P00_102Gg'].data.materials[0].name
holdImage=bpy.data.objects['P00_102Gg'].data.materials[0].node_tree.nodes['Image Texture'].image
bpy.data.objects['P00_102Gg'].data.materials[0].name='avoidCollision'
bpy.data.objects['P00_102Gg'].data.materials[0]=bpy.data.materials['JunoTemplateMaterial'].copy()
bpy.data.objects['P00_102Gg'].data.materials[0].name=holdMatName
bpy.data.objects['P00_102Gg'].data.materials[0].node_tree.nodes['Image Texture'].image=holdImage
# configure objects layers to match render layer for that objects color
bpy.data.objects['P00_102Gg'].layers=bpy.data.scenes['JunoScene'].render.layers["rl.g"].layers

# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_01'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.926562, 0.624332, 3.65534, 0.107373))
newCamera.location=(5735.47, -3588.02, -6942.99)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_02'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.05525, 0.6229, 3.57853, 0.081692))
newCamera.location=(5734.98, -3583.37, -6941.28)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_03'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.17766, 0.619511, 3.49203, 0.0563261))
newCamera.location=(5734.5, -3578.72, -6939.56)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_04'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.29307, 0.614183, 3.39634, 0.0314266))
newCamera.location=(5734.01, -3574.07, -6937.85)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_05'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.40078, 0.606948, 3.29204, 0.0071418))
newCamera.location=(5733.52, -3569.42, -6936.13)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_06'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.50017, 0.59785, 3.17975, -0.0163842))
newCamera.location=(5733.03, -3564.77, -6934.41)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_07'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.59063, 0.586942, 3.06013, -0.0390111))
newCamera.location=(5732.54, -3560.12, -6932.7)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_08'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.67163, 0.574288, 2.9339, -0.0606045))
newCamera.location=(5732.05, -3555.47, -6930.98)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_09'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.7427, 0.559965, 2.8018, -0.0810358))
newCamera.location=(5731.56, -3550.82, -6929.26)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_10'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.8034, 0.544057, 2.66462, -0.100183))
newCamera.location=(5731.08, -3546.17, -6927.54)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_11'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.85338, 0.526659, 2.52318, -0.117933))
newCamera.location=(5730.59, -3541.51, -6925.82)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_12'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.89234, 0.507873, 2.37831, -0.134179))
newCamera.location=(5730.1, -3536.86, -6924.1)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_13'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.92005, 0.487812, 2.23087, -0.148824))
newCamera.location=(5729.61, -3532.21, -6922.38)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_14'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.93635, 0.466595, 2.08175, -0.161782))
newCamera.location=(5729.12, -3527.56, -6920.66)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_15'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.95048, 0.44649, 1.94113, -0.173808))
newCamera.location=(5728.63, -3522.9, -6918.94)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_16'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((2.09981, 0.457226, 1.93438, -0.197929))
newCamera.location=(5728.14, -3518.25, -6917.22)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_72'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.597518, 0.529884, 3.79818, 0.358814))
newCamera.location=(5700.57, -3257.31, -6820.14)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_73'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.453372, 0.547388, 3.83851, 0.338703))
newCamera.location=(5700.07, -3252.65, -6818.4)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_74'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.306544, 0.563397, 3.86759, 0.31738))
newCamera.location=(5699.58, -3247.98, -6816.65)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_75'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.157906, 0.577814, 3.88526, 0.294973))
newCamera.location=(5699.08, -3243.31, -6814.9)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_76'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.00834232, 0.590555, 3.8914, 0.271614))
newCamera.location=(5698.58, -3238.65, -6813.16)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_77'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.14126, 0.601543, 3.88599, 0.247442))
newCamera.location=(5698.09, -3233.98, -6811.41)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_78'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.290012, 0.610713, 3.86906, 0.222601))
newCamera.location=(5697.59, -3229.31, -6809.66)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_79'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.43703, 0.61801, 3.8407, 0.197238))
newCamera.location=(5697.1, -3224.65, -6807.91)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_80'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.581441, 0.623391, 3.80108, 0.171505))
newCamera.location=(5696.6, -3219.98, -6806.16)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_81'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.722388, 0.626824, 3.75045, 0.145553))
newCamera.location=(5696.1, -3215.31, -6804.41)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP00_102G_82'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.859032, 0.628288, 3.68909, 0.119537))
newCamera.location=(5695.61, -3210.64, -6802.66)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Set Camera for rendering also make that camera the active object
bpy.context.scene.camera=bpy.data.objects['CP00_102G_14']
bpy.context.scene.objects.active=bpy.data.objects['CP00_102G_14']

# update scene (not sure if needed)
bpy.data.scenes['JunoScene'].update()
# EOF
