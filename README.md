# LRS_ExampleNB

This repository contains some demo and helper notebooks for MIRI LRS data processing. We focus especially on cases where the JWST pipeline has bugs or needs improvements; while we work to resolve those, the resources here can hopefully help you work through them.

## Spectral Extraction

Extracted data products in MAST are sometimes of poor quality due to sensitivity of the pipeline algorithm to coordinate regisration issues. The following can help you work around this:

* Notebook ``LRS_PointSource_Slit_Reduction.ipynb`` goes through stage 2 and stage 3 pipeline processing, including extraction, for a demo LRS slit observation, to show how to get science-ready extracted products.
* Script ``miri_lrs_extract_L3.py`` is an abbreviated version of the notebook, providing a simple script that takes a Level 3 s2d file as input, and returns an extracted spectrum with appropriate extraction limits set.

The repository contains the parameter reference file that is passed to the ``extract_1d`` step in both th enotebook and the script. This can be edited to suit your needs in any text editor.

Script usage:

``python miri_lrs_extract_L3.py --s2dfile myfile_s2d.fits --parfile miri_lrs_demo_extract1d.json --save_plot``



-- S. Kendrew, March 2023
