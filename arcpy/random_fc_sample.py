import arcpy
import numpy as np

def randomFCSample(fc, fd='sample_fd', sample_field='OBJECTID', sample_pct=10):
    """Generate a random sample of a feature class from a field with a unique numeric ID

    Args:
        fc (Feature Class): A GIS feature class
        fd (string): Name of resulting sample feature layer
        sample_field (string): Name of numeric field with unique values
        sample_pct (int, float): Sample size

    Returns:
        A feature layer that is a random sample of the input feature class
    """
    count_class = arcpy.GetCount_management(fc)
    count = int(count_class[0])
    random_vals = np.random.choice(count, int(count*(sample_pct/100)))
    arcpy.MakeFeatureLayer_management(fc,
                                      fd + "_" + str(sample_pct) + 'pct',
                                      sample_field + ' IN ' + str(tuple(random_vals)))