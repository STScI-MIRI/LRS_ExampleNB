import numpy as np
import matplotlib.pyplot as plt

from jwst.extract_1d import Extract1dStep
from jwst import datamodels
from jwst.associations.lib.rules_level3_base import DMS_Level3_Base
from jwst.associations.asn_from_list import asn_from_list


#

def extract_spectrum(s2dfile, parfile, plot):

    x1d = Extract1dStep()
    x1d.save_results = True
    x1d.output_dir = './'
    x1d.override_extract1d = parfile
    x1d.use_source_posn = False


    sp3 = x1d.run(s2dfile)

    if plot:
        fig = plt.figure(figsize=[10,6])
        plt.plot(sp3.spec[0].spec_table['WAVELENGTH'], sp3.spec[0].spec_table['FLUX'])
        plt.title(sp3.meta.filename)
        plt.xlabel('micron')
        plt.ylabel('Jy')
        outfile = sp3.meta.filename.replace("_extract1dstep.fits", ".png")
        plt.savefig(outfile)




if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Select the files')
    parser.add_argument('--s2dfile', required=True, help='the L3 s2d input file')
    parser.add_argument('--parfile', required=False, default='miri_lrs_demo_extract1d.json', help='the custom extraction file')
    parser.add_argument('--save_plot', required=False, action='store_true', help='flag to save a plot')
    args = parser.parse_args()
    extract_spectrum(s2dfile=args.s2dfile, parfile=args.parfile, plot=args.save_plot)
