from cellpose import models, plot

def _cellpose(image, diameter = None, GPU = False):
    """
    Run cellpose for nuclear segmentation

    Parameters
    ----------
    image : array
        Image to segment as array.
    diameter : integer, optional
        Aproximate average diameter. The default is None.
    GPU : bool, optional
        Use GPU if available. The default is None.

    Returns
    -------
    masks : array
        Masks obtained.
    flows : TYPE
        DESCRIPTION.

    """

    model = models.Cellpose(gpu = GPU, model_type = 'nuclei')
    channels = [0, 0]
    masks, flows, _, _ = model.eval(image, diameter = diameter, channels = channels, resample = True)

    return masks, flows
