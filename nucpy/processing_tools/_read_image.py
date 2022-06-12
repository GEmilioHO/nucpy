import czifile as zis
import tifffile

from matplotlib import image
from .. import logging as logg


def get_array_czi(filename):
    """
    Read image in CZI format as array
    """

    fn = filename.replace(".czi", "").split("/")[-1]
    logg.info(f"Reading CZI file '{fn}'...")

    czi = zis.CziFile(filename)
    cziarray = czi.asarray()
    czi.close()

    return cziarray


def get_array_common(filename):
    """
    Read image in common image format (png, jpeg, jpg)
    """

    fn = filename.replace(".png", "").replace(".jpeg", "").replace(".jpg", "").split("/")[-1]
    logg.info(f"Reading image file '{fn}'...")

    imgarray = image.imread(filename)

    return imgarray


def get_array_tiff(filename):
    """
    Read image in TIFF/TIF format as array
    """

    fn = filename.replace(".tiff", "").replace(".tif", "").split("/")[-1]
    logg.info(f"Reading image file '{fn}'...")

    tiffarray = tifffile.imread(filename)

    return tiffarray
