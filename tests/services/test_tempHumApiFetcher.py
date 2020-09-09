import unittest
from src.services.tempHumApiFetcher import TempHumApiFetcher
import datetime as dt
from src.config.appConfig import getConfig


class TestHumTempApiFetcher(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that creates raw outages data using it's api service
        """
        measId = 'Server_Room|Temperature'
        startDt = dt.datetime.now() - dt.timedelta(days=1)
        endDt = dt.datetime.now()

        tokenUrl: str = self.appConfig['tokenUrl']
        apiBaseUrl: str = self.appConfig['apiBaseUrl']
        clientId: str = self.appConfig['clientId']
        clientSecret: str = self.appConfig['clientSecret']

        tempHumFetcher = TempHumApiFetcher(
            tokenUrl, apiBaseUrl, clientId, clientSecret)
        resData = tempHumFetcher.fetchData(measId, startDt, endDt)

        self.assertFalse(len(resData) == 0)
