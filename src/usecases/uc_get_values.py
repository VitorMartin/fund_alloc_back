from datetime import date

from src.interfaces.i_storage import IStorage
from src.models.fund import Fund


class UCgetRemainPrincInFundById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int, basedate: date = date.today()) -> float:
        return self.storage.getRemainPrincInFundById(dealId, basedate=basedate)


class UCgetRemainPrincInDesembById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int, basedate: date = date.today()) -> float:
        return self.storage.getRemainPrincInDesembById(dealId, basedate=basedate)
