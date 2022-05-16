#
# configure camera for EQR map rendering
import bpy;
bpy.context.scene.camera=bpy.data.objects['CameraEQRMap'];
bpy.context.scene.objects.active=bpy.data.objects['CameraEQRMap'];
