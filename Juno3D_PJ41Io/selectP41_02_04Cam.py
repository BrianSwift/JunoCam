#  Setup Blender for Juno3D rendering
# Requires JunocamLibrary.blend to be loaded before running this
import bpy
from mathutils import Quaternion
bpy.context.screen.scene=bpy.data.scenes['JunoScene']

# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP41_02od_04'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.464166, 0.367305, -0.0844439, 3.90854))
newCamera.location=(15222.93309749882, -22206.49752452494, 104974.6050466291)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP41_02od_04TN'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((3.5924, 0.453344, 0.140469, 1.11311))
newCamera.location=(15222.93309749882, -22206.49752452494, 104974.6050466291)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP41_02od_04BN'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((2.65055, 0.253801, 0.178639, 1.8656))
newCamera.location=(15222.93309749882, -22206.49752452494, 104974.6050466291)
bpy.data.scenes['JunoScene'].objects.link(newCamera)

# Set Camera for rendering and make that camera the active object
bpy.context.scene.camera=bpy.data.objects['CP41_02od_04TN']
bpy.context.scene.objects.active=bpy.data.objects['CP41_02od_04TN']

# update scene (not sure if needed)
bpy.data.scenes['JunoScene'].update()

# EOF
