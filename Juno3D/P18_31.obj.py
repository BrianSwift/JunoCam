#  Setup Blender for Juno3D rendering
# Requires JunocamLibrary.blend to be loaded before running this
import bpy
from mathutils import Quaternion
# import Juno3D geometry and textures Wavefront OBJ
bpy.ops.import_scene.obj(filepath="/Users/bswift/Downloads/junoDirs/PJ18/P18_31.obj",axis_forward='Y', axis_up='Z')
# Replace materials created by blender obj import with JunoTemplateMaterial from JunocamLibrary.blend
holdMatName=bpy.data.objects['P18_31r'].data.materials[0].name
holdImage=bpy.data.objects['P18_31r'].data.materials[0].node_tree.nodes['Image Texture'].image
bpy.data.objects['P18_31r'].data.materials[0].name='avoidCollision'
bpy.data.objects['P18_31r'].data.materials[0]=bpy.data.materials['JunoTemplateMaterial'].copy()
bpy.data.objects['P18_31r'].data.materials[0].name=holdMatName
bpy.data.objects['P18_31r'].data.materials[0].node_tree.nodes['Image Texture'].image=holdImage
# configure objects layers to match render layer for that objects color
bpy.data.objects['P18_31r'].layers=bpy.data.scenes['JunoScene'].render.layers["rl.r"].layers

holdMatName=bpy.data.objects['P18_31g'].data.materials[0].name
holdImage=bpy.data.objects['P18_31g'].data.materials[0].node_tree.nodes['Image Texture'].image
bpy.data.objects['P18_31g'].data.materials[0].name='avoidCollision'
bpy.data.objects['P18_31g'].data.materials[0]=bpy.data.materials['JunoTemplateMaterial'].copy()
bpy.data.objects['P18_31g'].data.materials[0].name=holdMatName
bpy.data.objects['P18_31g'].data.materials[0].node_tree.nodes['Image Texture'].image=holdImage
# configure objects layers to match render layer for that objects color
bpy.data.objects['P18_31g'].layers=bpy.data.scenes['JunoScene'].render.layers["rl.g"].layers

holdMatName=bpy.data.objects['P18_31b'].data.materials[0].name
holdImage=bpy.data.objects['P18_31b'].data.materials[0].node_tree.nodes['Image Texture'].image
bpy.data.objects['P18_31b'].data.materials[0].name='avoidCollision'
bpy.data.objects['P18_31b'].data.materials[0]=bpy.data.materials['JunoTemplateMaterial'].copy()
bpy.data.objects['P18_31b'].data.materials[0].name=holdMatName
bpy.data.objects['P18_31b'].data.materials[0].node_tree.nodes['Image Texture'].image=holdImage
# configure objects layers to match render layer for that objects color
bpy.data.objects['P18_31b'].layers=bpy.data.scenes['JunoScene'].render.layers["rl.b"].layers

# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_01'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.472529, 2.41311, 0.517286, -1.82715))
newCamera.location=(-41315.3, 40449.7, 51761.2)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_02'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.477429, 2.27042, 0.482263, -1.86182))
newCamera.location=(-41316.6, 40463., 51743.4)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_03'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.479698, 2.12545, 0.44705, -1.88528))
newCamera.location=(-41317.8, 40476.4, 51725.6)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_04'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((0.479322, 1.97906, 0.411858, -1.89742))
newCamera.location=(-41319.1, 40489.8, 51707.7)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_05'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.493456, -1.89813, -0.390473, 1.96649))
newCamera.location=(-41320.3, 40503.2, 51689.9)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_06'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.527018, -1.88743, -0.383383, 2.11343))
newCamera.location=(-41321.6, 40516.5, 51672.1)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_07'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.56003, -1.86538, -0.373639, 2.25907))
newCamera.location=(-41322.8, 40529.9, 51654.3)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_08'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.592293, -1.83211, -0.361302, 2.40254))
newCamera.location=(-41324.1, 40543.3, 51636.4)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_09'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.623612, -1.78781, -0.346445, 2.54297))
newCamera.location=(-41325.3, 40556.6, 51618.6)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_10'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.653798, -1.73276, -0.32916, 2.67951))
newCamera.location=(-41326.5, 40570., 51600.8)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_11'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.682669, -1.66729, -0.30955, 2.81135))
newCamera.location=(-41327.8, 40583.3, 51582.9)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_12'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.710052, -1.59179, -0.287736, 2.93768))
newCamera.location=(-41329., 40596.7, 51565.1)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_13'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.73578, -1.50672, -0.263849, 3.05774))
newCamera.location=(-41330.2, 40610.1, 51547.2)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_14'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.7597, -1.41258, -0.238034, 3.17081))
newCamera.location=(-41331.5, 40623.4, 51529.4)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_15'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.781666, -1.30996, -0.210446, 3.27621))
newCamera.location=(-41332.7, 40636.8, 51511.6)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_16'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.801546, -1.19946, -0.181253, 3.37331))
newCamera.location=(-41333.9, 40650.1, 51493.7)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_17'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.819222, -1.08174, -0.150631, 3.46151))
newCamera.location=(-41335.1, 40663.5, 51475.9)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_18'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.834586, -0.957534, -0.118765, 3.54029))
newCamera.location=(-41336.3, 40676.8, 51458.)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_19'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.847546, -0.827572, -0.0858472, 3.60917))
newCamera.location=(-41337.5, 40690.2, 51440.2)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_20'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.858024, -0.692642, -0.052077, 3.66773))
newCamera.location=(-41338.7, 40703.5, 51422.3)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_21'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.865958, -0.553558, -0.0176582, 3.71563))
newCamera.location=(-41339.9, 40716.9, 51404.5)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_22'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.8713, -0.411158, 0.0172017, 3.75257))
newCamera.location=(-41341.1, 40730.2, 51386.6)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_23'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.874018, -0.266301, 0.0522923, 3.77833))
newCamera.location=(-41342.3, 40743.6, 51368.7)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_24'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.874095, -0.119859, 0.0874019, 3.79275))
newCamera.location=(-41343.5, 40756.9, 51350.9)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_25'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.871533, 0.0272843, 0.122319, 3.79575))
newCamera.location=(-41344.7, 40770.3, 51333.)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_26'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.866346, 0.174242, 0.156832, 3.78731))
newCamera.location=(-41345.9, 40783.6, 51315.1)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_27'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.858566, 0.320128, 0.190735, 3.76748))
newCamera.location=(-41347.1, 40797., 51297.3)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_28'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.848241, 0.464064, 0.223822, 3.73639))
newCamera.location=(-41348.3, 40810.3, 51279.4)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_29'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.835433, 0.605181, 0.255894, 3.6942))
newCamera.location=(-41349.4, 40823.6, 51261.5)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_30'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.82022, 0.742629, 0.286758, 3.64119))
newCamera.location=(-41350.6, 40837., 51243.7)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_31'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.802693, 0.875578, 0.316228, 3.57767))
newCamera.location=(-41351.8, 40850.3, 51225.8)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_32'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.782959, 1.00323, 0.344127, 3.50402))
newCamera.location=(-41352.9, 40863.7, 51207.9)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_33'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.761136, 1.12481, 0.370288, 3.42069))
newCamera.location=(-41354.1, 40877., 51190.)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_34'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.737357, 1.23958, 0.394551, 3.32818))
newCamera.location=(-41355.3, 40890.3, 51172.1)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_35'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.711766, 1.34687, 0.416773, 3.22705))
newCamera.location=(-41356.4, 40903.7, 51154.3)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_36'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.684515, 1.446, 0.436819, 3.1179))
newCamera.location=(-41357.6, 40917., 51136.4)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_37'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.655771, 1.5364, 0.454569, 3.0014))
newCamera.location=(-41358.7, 40930.3, 51118.5)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_38'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.625707, 1.61752, 0.469916, 2.87824))
newCamera.location=(-41359.9, 40943.7, 51100.6)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_39'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.594502, 1.68886, 0.482769, 2.74917))
newCamera.location=(-41361., 40957., 51082.7)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Add image specific camera
newCamera=bpy.data.objects['Camera'].copy()
newCamera.name='CP18_31_40'
newCamera.rotation_mode='QUATERNION'
newCamera.rotation_quaternion=Quaternion((-0.562347, 1.74999, 0.493051, 2.61497))
newCamera.location=(-41362.2, 40970.3, 51064.8)
bpy.data.scenes['JunoScene'].objects.link(newCamera)
# Set Camera for rendering also make that camera the active object
bpy.context.scene.camera=bpy.data.objects['CP18_31_20']
bpy.context.scene.objects.active=bpy.data.objects['CP18_31_20']

# update scene (not sure if needed)
bpy.data.scenes['JunoScene'].update()
# EOF
