from datetime import date
from typing import Any

from src.controllers.fastapi.http.models import FundModel
from src.models.deal import Deal
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *


class Fund(Deal):
    kold: str

    def __init__(self, kold: str, ccy: CCY, princ: float, ini: date, venc: date, pk: int = None):
        super().__init__(ccy, princ, ini, venc, pk=pk)
        self.kold = kold

    def __str__(self):
        return (
            f'{MODEL.FUND} = {{ '
            f'{FUND.ID} = {self.dealId},'
            f'\t{FUND.KOLD} = {self.kold},'
            f'\t{FUND.CCY} = {self.ccy},'
            f'\t{FUND.PRINC} = {self.princ},'
            f'\t{FUND.INI} = {self.ini},'
            f'\t{FUND.VENC} = {self.venc}'
            f'}}'
        )

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    def toModel(self) -> FundModel:
        return FundModel(
            dealId=self.dealId,
            ccy=self.ccy,
            princ=self.princ,
            ini=self.ini,
            venc=self.venc,
            kold=self.kold
        )

    def toDict(self):
        return {
            FUND.ID: self.dealId,
            FUND.KOLD: self.kold,
            FUND.CCY: self.ccy,
            FUND.PRINC: self.princ,
            FUND.INI: self.ini,
            FUND.VENC: self.venc
        }

    @staticmethod
    def fromDict(d: dict):
        fund = Fund(
            d[FUND.KOLD.value], d[FUND.CCY.value], d[FUND.PRINC.value], d[FUND.INI.value],
            d[FUND.VENC.value], d[FUND.ID.value]
        )

        return fund

    @staticmethod
    def fromModel(m: FundModel):
        if m is None:
            return None
        else:
            return Fund(
                pk=m.dealId,
                ccy=m.ccy,
                princ=m.princ,
                ini=m.ini,
                venc=m.venc,
                kold=m.kold
            )
