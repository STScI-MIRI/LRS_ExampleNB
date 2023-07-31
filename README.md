# MIRI LRS Example Notebooks and Scripts

This repository contains some demo and helper notebooks for MIRI LRS data processing. We focus especially on cases where the JWST pipeline has bugs or needs improvements; while we work to resolve those, the resources here can hopefully help you work through them.

## Spectral Extraction

Spectral extraction is the step that most often requires some manual reprocessing for LRS data. We include here some notebooks to help understand the capabilities of the pipeline and how to use them.

* miri_lrs_pipeline_extraction.ipynb: this notebook illustrates the spectral extraction capabilities of the JWST calibration pipeline for LRS data, beyond the simple fixed-width aperture method that is used for the automated processing. Test data can be retrieved from [this Box folder](https://stsci.box.com/s/i2xi18jziu1iawpkom0z2r94kvf9n9kb).

Prior to May 2023 (CRDS context < 1089.pmap), the calibration pipeline used a sub-optimal method to locate the target in the aperture for spectral extraction, which often misplaced the extraction aperture. As a result, the extracted products (the x1d files) in MAST were often of poor quality. We produced a notebook and script to demonstrate how to work around this problem. As of CRDS context 1089.pmap, implemented in May 2023, this workaround has become the default method for automated processing, effectively resolving the issue. The following products are still available:

* ``LRS_PointSource_Slit_Reduction.ipynb`` goes through stage 2 and stage 3 pipeline processing, including extraction, for a demo LRS slit observation, to show how to get science-ready extracted products. Test data can be retrieved from [this Box folder](https://stsci.box.com/s/i2xi18jziu1iawpkom0z2r94kvf9n9kb).
* Script ``miri_lrs_extract_L3.py`` is an abbreviated version of the notebook, providing a simple script that takes a Level 3 s2d file as input, and returns an extracted spectrum with appropriate extraction limits set.

Script usage:

``python miri_lrs_extract_L3.py --s2dfile myfile_s2d.fits --parfile miri_lrs_demo_extract1d.json --save_plot``


## Questions or feedback?

If you have questions or would like to see additional notebooks here for MIRI LRS, please contact us [via the Helpdesk](https://jwsthelp.stsci.edu)!

-- the MIRI LRS team, July 2023
