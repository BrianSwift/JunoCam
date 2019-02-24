#!/bin/sh
# Blender Rendering Commands
#

/Applications/Blender/blender.app/Contents/MacOS/blender --background --factory-startup /Users/bswift/Downloads/Juno3D/JunocamLibrary.blend --python P00_102B.obj.py --render-output CP00_102B_14_#  --render-frame 1 >/tmp/render.log
# EOF
