#!/bin/sh
# Blender Rendering Commands
#
#   Note: -S Scene360 used for 2nd phase rendering
#

# confiuration parameters to simplify manual render variations
startup_file='/Users/bswift/Downloads/junoDirs/JunocamLibraryPJ26.blend'
startup_file=JunocamLibraryPJ41IoA.blend
common_py=blenderCommon.py
common_py=selectTargetNorthCam.py
common_py=selectP41_02_04Cam.py
common_py=selectP41_05_04Cam.py
render_prefix=''
render_prefix='z5P'
render_suffix=''

'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_01ev.obj.py --python "$common_py" --render-output ${render_prefix}CP41_01ev_03${render_suffix}_#  --render-frame 1 >/tmp/render.log
'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_01od.obj.py --python "$common_py" --render-output ${render_prefix}CP41_01od_03${render_suffix}_#  --render-frame 1 >/tmp/render.log
'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_02ev.obj.py --python "$common_py" --render-output ${render_prefix}CP41_02ev_04${render_suffix}_#  --render-frame 1 >/tmp/render.log
'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_02od.obj.py --python "$common_py" --render-output ${render_prefix}CP41_02od_04${render_suffix}_#  --render-frame 1 >/tmp/render.log
'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_03ev.obj.py --python "$common_py" --render-output ${render_prefix}CP41_03ev_04${render_suffix}_#  --render-frame 1 >/tmp/render.log
'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_03od.obj.py --python "$common_py" --render-output ${render_prefix}CP41_03od_04${render_suffix}_#  --render-frame 1 >/tmp/render.log
'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_04ev.obj.py --python "$common_py" --render-output ${render_prefix}CP41_04ev_03${render_suffix}_#  --render-frame 1 >/tmp/render.log
'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_04od.obj.py --python "$common_py" --render-output ${render_prefix}CP41_04od_03${render_suffix}_#  --render-frame 1 >/tmp/render.log
'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_05ev.obj.py --python "$common_py" --render-output ${render_prefix}CP41_05ev_04${render_suffix}_#  --render-frame 1 >/tmp/render.log
'/Volumes/Macintosh HD/Applications/Blender/blender.app/Contents/MacOS/blender' --background --factory-startup "$startup_file" -S JunoScene  --python P41_05od.obj.py --python "$common_py" --render-output ${render_prefix}CP41_05od_04${render_suffix}_#  --render-frame 1 >/tmp/render.log
# EOF
