KPL/MK
   Juno meta-kernel

   Modify the PATH_VALUES directory name to point to the actual
   location of the JUNO SPICE data set's ``data'' directory on your
   system. Replacing ``/'' with ``\'' and converting line terminators
   to the format native to your system may also be required if
   this meta-kernel is to be used on a non-UNIX workstation.

   This template has CK entries for earth flyby and perijove 16 and 17.
   Add additional CK files to cover the time span of the
   data you will process.

   Also, check for the latest versions of various files.
   Note: these two files get updated regularly, but
   do not have a version number or date in their filename.
      '$JK/spk/juno_pred_orbit.bsp 
      '$JK/spk/juno_rec_orbit.bsp'

   Also Note: these files may need to be renamed to remove ".txt" extension
   added by the browser download.
   	./lsk/naif0012.tls
   	./spk/juno_pred_orbit.orb
	./fk/juno_v12.tf
	./sclk/JNO_SCLKSCET.00082.tsc
	./pck/pck00010.tpc
	./ik/juno_junocam_v02.ti

  spk_rec_131005_131014_131101.bsp is for the earth flyby, because
  juno_rec_orbit.bsp coverage starts 2016 JUL 05.

   \begindata

PATH_VALUES  = ( '/Users/bswift/Downloads/junospice/kernels' )

      PATH_SYMBOLS    = ( 'JK' )

      KERNELS_TO_LOAD = (

                       '$JK/lsk/naif0012.tls'

                       '$JK/pck/pck00010.tpc'

		       '$JK/sclk/JNO_SCLKSCET.00082.tsc'

                       '$JK/fk/juno_v12.tf'

                       '$JK/ik/juno_junocam_v02.ti'

                       '$JK/spk/de438s.bsp'
                       '$JK/spk/jup310.bsp'
                       '$JK/spk/juno_struct_v04.bsp'

		       '$JK/spk/juno_pred_orbit.bsp 
		       '$JK/spk/spk_rec_131005_131014_131101.bsp'
		       '$JK/spk/juno_rec_orbit.bsp'

		       '$JK/ck/juno_sc_rec_131006_131012_v03.bc'
		       '$JK/ck/juno_sc_rec_181028_181103_v01.bc'
		       '$JK/ck/juno_sc_rec_181216_181222_v01.bc'


                        )
   \begintext


End of MK.
