import czifile as zis
import tifffile

from matplotlib import image
from .. import logging as logg


def get_array_czi(filename):
    """
    Read image in CZI format as array
    """

    czi = zis.CziFile(filename)
    cziarray = czi.asarray()
    czi.close()

    return cziarray


def get_array_common(filename):
    """
    Read image in common image format (png, jpeg, jpg)
    """

    imgarray = image.imread(filename)

    return imgarray


def get_array_tiff(filename):
    """
    Read image in TIFF/TIF format as array
    """

    tiffarray = tifffile.imread(filename)

    return tiffarray
