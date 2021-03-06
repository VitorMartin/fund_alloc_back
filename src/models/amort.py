from datetime import date
from typing import Any

from src.controllers.fastapi.http.models import AmortModel
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *


class Amort:
    amortId: int = None
    data: date
    ccy: CCY
    val: float

    def __init__(self, amortData: date, ccy: CCY, val: float, pk: int = None):
        self.amortId = pk
        self.data = amortData
        self.ccy = ccy
        self.val = val

    def __str__(self):
        return (
            f'{MODEL.AMORT} = {{ '
            f'{AMORT.ID} = {self.amortId},'
            f'\t{AMORT.CCY} = {self.ccy},'
            f'\t{AMORT.VAL} = {self.val},'
            f'\t{AMORT.DATA} = {self.data}'
            f'}}'
        )

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    def toModel(self) -> AmortModel:
        return AmortModel(
            amortId=self.amortId,
            data=self.data,
            ccy=self.ccy,
            val=self.val
        )

    @staticmethod
    def fromDict(d: dict):
        amort = Amort(
            d[AMORT.DATA.value], d[AMORT.CCY.value], d[AMORT.VAL.value], d[AMORT.ID.value]
        )

        return amort

    @staticmethod
    def fromModel(m: AmortModel):
        return Amort(
            pk=m.amortId,
            amortData=m.data,
            ccy=m.ccy,
            val=m.val
        )
