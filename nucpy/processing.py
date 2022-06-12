from . import processing_tools as pt

class NucpyProcessing(object):

    def __init__(self, indir, outdir = None):
        """
        Start Nucpy Processing.
        Parameters
        ----------
        indir : string
            Is the path to the folder where all the microscope images that will be analysed
            are found.

        Returns
        -------
        None.

        """

        self.directory = indir

        
