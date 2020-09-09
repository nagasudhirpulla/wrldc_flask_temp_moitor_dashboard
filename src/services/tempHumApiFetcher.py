import requests
import json
import datetime as dt
from typing import List, Tuple
from src.utils.timeUtils import convertEpochMsToDt


class TempHumApiFetcher():
    tokenUrl: str = ''
    apiBaseUrl: str = ''
    clientId: str = ''
    clientSecret: str = ''

    def __init__(self, tokenUrl, apiBaseUrl, clientId, clientSecret):
        self.tokenUrl = tokenUrl
        self.apiBaseUrl = apiBaseUrl
        self.clientId = clientId
        self.clientSecret = clientSecret

    def fetchData(self, measId: str, startDt: dt.datetime, endDt: dt.datetime) -> List[Tuple[float, float]]:
        """fetches data from temperature humidity archive api

        Args:
            measId (str): measurement Id
            startDt (dt.datetime): start date
            endDt (dt.datetime): end date

        Returns:
            List[Tuple[dt.datetime, float]]: data from temperature humidity archive api
        """
        apiUrl: str = '{0}/api/TempMointor/{1}/{2}/{3}'.format(self.apiBaseUrl, measId, dt.datetime.strftime(
            startDt, '%Y-%m-%d-%H-%M-%S'), dt.datetime.strftime(endDt, '%Y-%m-%d-%H-%M-%S'))

        # step A, B - single call with client credentials as the basic auth header - will return access_token
        data = {'grant_type': 'client_credentials'}

        access_token_response = requests.post(
            self.tokenUrl, data=data, verify=False, allow_redirects=False, auth=(self.clientId, self.clientSecret))

        tokens = json.loads(access_token_response.text)

        api_call_headers = {
            'Authorization': 'Bearer ' + tokens['access_token']}
        respSegs = (requests.get(
            apiUrl, headers=api_call_headers, verify=False)).text[1:-1].split(',')
        apiData: List[Tuple[float, float]] = []
        try:
            for samplInd in range(0, int(len(respSegs)/2)):
                # ts = convertEpochMsToDt(float(respSegs[2*samplInd]))
                ts = float(respSegs[2*samplInd])
                val = float(respSegs[2*samplInd+1])
                apiData.append((ts, val))
            return apiData
        except Exception as inst:
            print(inst)
            return[]
