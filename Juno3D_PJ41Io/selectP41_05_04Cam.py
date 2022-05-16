#  Setup Blender for Juno3D rendering
# Requires JunocamLibrary.blend to be loaded before running this
import bpy
from mathutils import Quaternion
bpy.context.screen.scene=bpy.data.scenes['JunoScene']

# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP41_05od_04'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.598413, 0.985947, -0.204844, 3.62106))
newCamera.location=(72880.68076189901, 18313.78056574255, 114846.7402410477)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP41_05od_04TN'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((1.78141, 0.531018, 0.680963, 2.28443))
newCamera.location=(72880.68076189901, 18313.78056574255, 114846.7402410477)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP41_05od_04BN'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((2.5302, 0.694222, 0.476048, 1.73503))
newCamera.location=(72880.68076189901, 18313.78056574255, 114846.7402410477)
bpy.data.scenes['JunoScene'].objects.link(newCamera)

# Set Camera for rendering and make that camera the active object
bpy.context.scene.camera=bpy.data.objects['CP41_05od_04TN']
bpy.context.scene.objects.active=bpy.data.objects['CP41_05od_04TN']

# update scene (not sure if needed)
bpy.data.scenes['JunoScene'].update()

# EOF
