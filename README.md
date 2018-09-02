MCGPUFI
========

A multithreaded CPU & GPU-based facet imager

Authors: Baoqiang Lao, Tao An

Copyright (C) 2018-2020 SHAO, China


Dependencies:
  1. Python 3 (version > = 3.5)
     ./configure --prefix=/install_path --enable-shared
     make -j 4
     make install
  2. casacore (version >= 2.3.0), https://github.com/casacore/casacore, need to build python3: cmake add --DBUILD-PYTHON3=ON
  mkdir build
  cd build
  cmake .. -DCMAKE_INSTALL_PREFIX=/BIGDATA1/ac_shao_tan_1/mcgpufi_lib -DDATA_DIR=/BIGDATA1/ac_shao_tan_1/mcgpufi_soft/casacore-data -DENABLE_TABLELOCKING=OFF -DCMAKE_INCLUDE_PATH=/BIGDATA1/ac_shao_tan_1/mcgpufi_lib/include -DCMAKE_LIBRARY_PATH=/BIGDATA1/ac_shao_tan_1/mcgpufi_lib/lib -DBUILD_PYTHON3=ON -DBUILD_PYTHON=OFF -DBoost_NO_BOOST_CMAKE=True
  make -j 10
  make install
  3. numpy
  4. pyrap, https://github.com/casacore/python-casacore (python ./setup.py build_ext -I/casacore_include_path -L/casacore_lib_path)
  5. matplotlib
  6. pyfits
  7. gtk3.0 with engines and python dev packages and pycairo (and maybe any cairo-dev packages). Important: install package python-gi-cairo, otherwise the gtk drawing area's on draw is never called for some truely bizare reason.
  8. (to edit gui: glade for gtk 3.0 is needed)
  9. cmake
  10. The GNU C++ compiler >= 4.8
  11. OpenMP
  12. CUDA toolkit (nvcc,nvprof) >=5.0
  13. CfitsIO, https://heasarc.gsfc.nasa.gov/fitsio/fitsio.html
      ./configure --prefix=/install_path
      make -j 4
      make install
  14. WcsLib, http://www.atnf.csiro.au/people/mcalabre/WCS/
      ./configure --prefix=/install_path
      make -j 4
      make install
  15. astropy >=3.0.1
  16. photutils
  17. boost, build with python3.5, libboost-all and libboost-dev
      ./bootstrap.sh --prefix=/install_path --with-python=/your_python3_exe --with-libraries=all 
      ./b2 install
      ln -s libboost_python3.so libboost_python-py35.so
      change include/boost/config/compiler/gcc.hpp line 156 to #if defined(_GLIBCXX_USE_FLOAT128) && !defined(__STRICT_ANSI__) && !defined(__CUDACC__)
  18. SWarp, http://www.astromatic.net/software/swarp
  19. FFTW3
      ./configure --prefix=/BIGDATA1/ac_shao_tan_1/mcgpufi_lib --enable-shared --enable-single

Build instructions (outputs CPU and GPU single and double precision libraries and a python wrapper for these)
- change setup.py 
- run: python3 setup.py install --user (this will install into the python user directory)

Run instructions
- Navigate to the mcgpufi/mcgpufi directory
- "python3 mcgpufi.py --help" or "./mcgpufi.py --help"to display a full list of options
- Enjoy

Toy GUI is available (proof of concept demonstrator for targeted faceting)
- "python3 mcgpufi_frontend.py" or "./mcgpufi_frontend.py"

Openmp Example:
python3 /home/lbq/work/facet/MCGPUFI/mcgpufi/mcgpufi.py G55.7+3.4.calib.ms --output_prefix /home/lbq/work/facet/data_test/img --npix_l 512 --npix_m 512 --cell_l 8 --cell_m 8 --pol I --conv_sup 4 --conv_oversamp 63 --output_format fits --field_id 0 --data_column "DATA" --use_back_end CPU --n_facets_l 2 --n_facets_m 2 --average_all 1 --log_dir=/home/lbq/work/facet/data_test --output_psf 1 --stitch_facets 1

CUDA Example(Tianhe-2):
yhrun -N 1 -n 1 -p gpu python3 /BIGDATA1/ac_shao_tan_1/MCGPUFI/mcgpufi/mcgpufi.py G55.7+3.4.calib.ms --output_prefix /BIGDATA1/ac_shao_tan_1/data/img --npix_l 512 --npix_m 512 --cell_l 8 --cell_m 8 --pol I --conv_sup 4 --conv_oversamp 63 --output_format fits --field_id 0 --data_column "DATA" --use_back_end GPU --n_facets_l 2 --n_facets_m 2 --average_all 1 --log_dir=/BIGDATA1/ac_shao_tan_1/data --run_time_output=/BIGDATA1/ac_shao_tan_1/data/time.txt 

MPI+Openmp (Tianhe-2):
yhrun -N 5 -n 5 -c 20 -p gpu  python3 ~/MCGPUFI/mcgpufi/mcgpufi_mpi_cpu.py G55.7+3.4.calib.ms --output_prefix ~/data/img --npix_l 512 --npix_m 512 --cell_l 8 --cell_m 8 --pol I --conv_sup 4 --conv_oversamp 63 --output_format fits --field_id 0 --data_column "DATA" --use_back_end GPU --n_facets_l 2 --n_facets_m 2 --average_all 1 --stitch_facets 1  --log_dir=/BIGDATA1/ac_shao_tan_1/data --run_time_output ~/data/time_chunks.txt --no_chunks 1

MPI+cuda (Tianhe-2):
yhrun -N 10 -n 10 -p gpu  python3 ~/MCGPUFI/mcgpufi/mcgpufi_mpi_gpu.py data_0.ms,data_1.ms,data_2.ms,data_3.ms,data_4.ms,data_5.ms,data_6.ms,data_7.ms,data_8.ms,data_9.ms --output_prefix ~/data/split_data/img --npix_l 512 --npix_m 512 --cell_l 8 --cell_m 8 --pol I --conv_sup 4 --conv_oversamp 63 --output_format fits --field_id 0 --data_column "DATA" --use_back_end GPU --n_facets_l 2 --n_facets_m 2 --average_all 1 --stitch_facets 1  --log_dir=/BIGDATA1/ac_shao_tan_1/data/split_data --run_time_output ~/data/time_chunks.txt --no_chunks 1 
