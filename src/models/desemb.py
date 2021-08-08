from datetime import date

from src.models.deal import Deal
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
from src.models.fund import Fund


class Desemb(Deal):
    fund: Fund
    ccb: str

    def __init__(
            self, fund: Fund, ccb: str, ccy: CCY, princ: float, ini: date, venc: date, pk: int = None
    ):
        super().__init__(ccy, princ, ini, venc, pk=pk)
        self.fund = fund
        self.ccb = ccb

    def __str__(self):
        return (
            f'{MODEL.DESEMB} = {{ '
            f'{DESEMB.ID} = {self.dealId},'
            f'\t{DESEMB.CCB} = {self.ccb},'
            f'\t{DESEMB.CCY} = {self.ccy},'
            f'\t{DESEMB.PRINC} = {self.princ},'
            f'\t{DESEMB.INI} = {self.ini},'
            f'\t{DESEMB.VENC} = {self.venc},'
            f'\t{MODEL.FUND} = {{ '
            f'{FUND.ID} = {self.fund.dealId},'
            f'\t{FUND.KOLD} = {self.fund.kold},'
            f'\t{FUND.CCY} = {self.fund.ccy},'
            f'\t{FUND.PRINC} = {self.fund.princ},'
            f'\t{FUND.INI} = {self.fund.ini},'
            f'\t{FUND.VENC} = {self.fund.venc} '
            f'}} '
            f'}}'
        )

    @staticmethod
    def fromDict(d: dict):
        fund = Fund(
            d[FUND.KOLD.value], d[FUND.CCY.value], d[FUND.PRINC.value], d[FUND.INI.value],
            d[FUND.VENC.value], d[FUND.ID.value]
        )
        desemb = Desemb(
            fund, d[DESEMB.CCB.value], d[DESEMB.CCY.value], d[DESEMB.PRINC.value],
            d[DESEMB.INI.value], d[DESEMB.VENC.value], d[DESEMB.ID.value]
        )

        return desemb
