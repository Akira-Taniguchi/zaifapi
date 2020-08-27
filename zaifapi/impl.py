# Importing from this module is deprecated
# This module will be removed in the future

from zaifapi.exchange_api.public import (
    ZaifPublicStreamApi,
    ZaifPublicApi,
    ZaifFuturesPublicApi,
)
from zaifapi.exchange_api.trade import (
    ZaifTradeApi,
    ZaifLeverageTradeApi,
    ZaifTokenTradeApi,
)

from zaifapi.oauth import ZaifTokenApi

_MAX_COUNT = 1000
_MIN_WAIT_TIME_SEC = 1

__all__ = [
    "ZaifTradeApi",
    "ZaifLeverageTradeApi",
    "ZaifTokenTradeApi",
    "ZaifPublicStreamApi",
    "ZaifPublicApi",
    "ZaifFuturesPublicApi",
    "ZaifTokenApi",
]
