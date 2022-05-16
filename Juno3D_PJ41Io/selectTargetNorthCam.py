# Set Camera for rendering and make that camera the active object
import bpy

camTargetNorthName=bpy.data.scenes['JunoScene'].camTargetNorthName

bpy.context.scene.camera=bpy.data.objects[camTargetNorthName]
bpy.context.scene.objects.active=bpy.data.objects[camTargetNorthName]
