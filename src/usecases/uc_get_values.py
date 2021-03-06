from datetime import date
from typing import List

from src.interfaces.i_storage import IStorage
from src.models.fund import Fund


class UCGetFundPrincAfterAmortById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int, basedate: date = date.today()) -> float:
        return self.storage.getFundPrincAfterAmortById(dealId, basedate=basedate)


class UCGetDesembPrincAfterAmortById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int, basedate: date = date.today()) -> float:
        return self.storage.getDesembPrincAfterAmortById(dealId, basedate=basedate)


class UCGetAvailableFundsForDesembByCcb:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, ccb: str, basedate: date = date.today()) -> List[Fund]:
        return self.storage.getAvailableFundsForDesembByCcb(ccb, basedate=basedate)
