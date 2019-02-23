# Juno3D - JunoCam raw to textured 3D object processing pipeline

## Files
Juno3D.nb - _Mathematica_ notebook implementing pipeline (contains operating instructions)

juno_kernels.tm - Metakernel template for NASA SPICE
## Sample Output
P00_102.obj - 3D geometry in _Wavefront_ format

P00_102.obj.mtl - Materials specification

P00_102bt3.png - Blue texture image

P00_102gt2.png - Green texture image

P00_102rt1.png - Red texture image

P00_102.obj.py - Blender Python rendering setup commands

Blender command example  `/Applications/Blender/blender.app/Contents/MacOS/blender --factory-startup JunocamLibrary.blend --python P00_102.obj.py`
## Renderer Samples
JunocamLibrary.blend - _Blender_ configuration template

P00_102c.blend - _Blender_ import and configuration of above sample output

P00_102_8k25ptc.png - _Blender Cycles_ rendered equirectangular image (using 8K 25% scale preset)

P00_102.scn - _Apple SceneKit_ import and configuration of above sample output
# Description
**Juno3D**, a JunoCam raw to textured 3D object processing pipeline implemented in Mathematica is available under permissive open source license at https://github.com/BrianSwift/JunoCam/tree/master/Juno3D

## What it does...

Converts Junocam raw image and metadata to 3D object suitable for importing into 3rd party rendering application (such as Blender).

Input is [MissionJuno](https://www.missionjuno.swri.edu) website formatted **-raw.png** or PDS **.IMG** or **.IMG.gz** raw image file, and **.json** or **.LBL** metadata file. 

Output is _Wavefront_ geometry and material file (**.obj, .mtl**) and an image/texture file for each color (**.png**).

Raw image files and metadata are imported, SPICE and the camera model are used to map image pixels to a tessellated representation of the target (Jupiter) surface. Imagery that doesn't intercept the target is projected onto a backstop surface (large sphere centered at a spacecraft location with radius less than the distance to the limb.) Texture mapped geometry is written out.

Information useful for rendering scenes (such as spacecraft position and Blender camera rotation values) is included as comments in the **.obj** file (which is a textual format.)

By default flat field adjustment and linear light to sRGB are performed on generated imagery textures. These sRGB encoded textures provide a close representation of actual Jupiter contrast and may need post-processing in a tool like Photoshop to enhance details in the cloud structures.

Can mark SPICE computed limb locations in texture images.

The current lens model uses Brown-Conrady K1,K2,Xp,Yp plus linear and cubic CA terms.

The output structure of a separate set of geometry for each of the three colors requires non-default shader/material and rendering options described below in Rendering in 3rd party application .

## Rendering in 3rd party application

The 3D object produced by this script has three separate but co-located groups of geometry. Each set of geometry is textured with imagery for a different color channel. Each set of geometry has different triangle vertex locations, so the geometry associated with each color channel consists of triangles that are both inter-penetrating and nearly co-planar with the geometry from the other color channels. Therefore, each set of geometry must effectively be rendered independently to the red/green/blue channels of the final image.

The above organization means there is no spatial resampling of the raw data performed by this script. Thus, lens correction and perspective projection are accomplished in a single resampling done in the renderer.

Step by step instructions to setup this rendering configuration in Blender and Apple XCode SceneKit Viewer are available in the _Mathematica_ notebook. The Blender setup process is also available as a screen recording on YouTube at: https://youtu.be/6Wx--D_OxbI

If you don't have _Mathematica_, the source code can still be viewed with correct formatting using _Wolfram CDF Player_ available at https://www.wolfram.com/cdf-player/

Full resolution Earth flyby image rendered in Blender at 45.51 pixels/deg available on Flickr:
[![Earth](https://farm8.staticflickr.com/7805/46261746184_93ef5c8977_k.jpg)](https://www.flickr.com/photos/bswift/46261746184)
