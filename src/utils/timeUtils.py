import datetime as dt
def convertEpochMsToDt(epochMs: float) -> dt.datetime:
    """convert epoch ms to datetime (time zone not present)

    Args:
        epochMs (float): UNIX epoch milliseconds

    Returns:
        dt.datetime: datetime object
    """    
    timeObj = dt.datetime.fromtimestamp(epochMs/1000)
    return timeObj
