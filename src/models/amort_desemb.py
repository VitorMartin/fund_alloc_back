from datetime import date

from src.models.amort import Amort
from src.models.desemb import Desemb
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *


class AmortDesemb(Amort):
    desemb: Desemb

    def __init__(self, desemb: Desemb, amortData: date, ccy: CCY, val: float, pk: int = None):
        super().__init__(amortData, ccy, val, pk=pk)
        self.desemb = desemb

    def __str__(self):
        return (
            f'{MODEL.AMORT_DESEMB} = {{ '
            f'{AMORT_DESEMB.ID} = {self.amortId},'
            f'\t{AMORT_DESEMB.CCY} = {self.ccy},'
            f'\t{AMORT_DESEMB.VAL} = {self.val},'
            f'\t{AMORT_DESEMB.DATA} = {self.data},'
            f'\t{MODEL.DESEMB} = {{ '
            f'{DESEMB.ID} = {self.desemb.dealId},'
            f'{DESEMB.CCB} = {self.desemb.ccb},'
            f'\t{DESEMB.CCY} = {self.desemb.ccy},'
            f'\t{DESEMB.PRINC} = {self.desemb.princ}'
            f'\t{DESEMB.INI} = {self.desemb.ini}'
            f'\t{DESEMB.VENC} = {self.desemb.venc},'
            f'\t{MODEL.FUND} = {{ '
            f'{FUND.ID} = {self.desemb.fund.dealId},'
            f'\t{FUND.KOLD} = {self.desemb.fund.kold},'
            f'\t{FUND.CCY} = {self.desemb.fund.ccy},'
            f'\t{FUND.PRINC} = {self.desemb.fund.princ},'
            f'\t{FUND.INI} = {self.desemb.fund.ini},'
            f'\t{FUND.VENC} = {self.desemb.fund.venc} '
            f'}} '
            f'}} '
            f'}}'
        )
