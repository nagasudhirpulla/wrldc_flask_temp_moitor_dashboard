from typing import TypedDict


class IAppConfig(TypedDict):
    flaskSecret: str
    flaskPort: str
    tokenUrl: str
    apiBaseUrl: str
    clientId: str
    clientSecret: str
