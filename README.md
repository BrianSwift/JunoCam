# JunoCam
JunoCam Image Processing

Mathematica notebooks for playing with JunoCam images.

Note: These are not "production quality" tools, but I wanted to
make them available.

## Usage
Open notebook in _Mathematica_

If you don't have _Mathematica_, these notebooks can still be viewed with correct formatting using _Wolfram CDF Player_ available at [https://www.wolfram.com/cdf-player/](https://www.wolfram.com/cdf-player/)

Follow instructions at top of notebook.

Outputs typically written to `/tmp` or to same directory as source file.

There are JunoCam raw image processing discussions in [Juno PDS data](http://www.unmannedspaceflight.com/index.php?showtopic=8143) topic on Unmanned Spaceflight forums.

## Descriptions
Juno9 - Enhances `-mapprojected.png` color files.

Juno12 - Gridded contrast enhancements from `-raw.png` files.

Juno14b	 - Ring image from `JNCE_2016346_03R00112_V02-raw.png`

Juno24u - Extract control points, produce and evaluate camera model.

Juno24Matchpoints.csv - Control points extracted by Juno24u.

Juno28g - JunoCam raw data processing pipeline

extendedImageTransformation - development and testing of extension to Mathematica's `ImageTransformation[]`

## Obsolete

Juno15 - Extract flats from _Radiation trend tracking_ `-raw.png` files.

Juno24e - Extract control points from cruise phase star fields to drive *Hugin’s* lens parameter generation

Juno25 - Convert MissionJuno website `-raw.png` files to full CCD frame images which can be processed as a panorama in *Hugin*
