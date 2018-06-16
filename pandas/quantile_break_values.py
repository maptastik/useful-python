def quantileBreakValues(series, quantiles):
    """Define quantile breaks for a pandas series

    Args:
        series (pandas Series): A pandas Series containing numeric values 
                                for which to calculate quantile break values
        quantiles (int): Number of quantiles the Series should be split into
    
    Returns:
        qValuesList: A list of quantile break values for a pandas Series
    
    """
    qValuesList = []
    qInterval = 1/quantiles
    qBreak = 0
    while len(qValuesList) < (quantiles - 1):
        qBreak += qInterval
        qValue = series.quantile(qBreak)
        qValuesList.append(qValue)
    return qValuesList