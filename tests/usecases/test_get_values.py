from datetime import date

import pytest
from fastapi import HTTPException

from ctrl import Ctrl
from src.models.fund import Fund
from src.repositories.mock.mock_data import MockData


ctrl = Ctrl().ctrl
basedate = date(2021, 8, 13)


class Test_UCgetValues:
    def test_get_remaining_principal_in_fund_by_id(self):
        remain = ctrl.getFundPrincAfterAmortById(MockData.fund2.dealId, basedate=basedate)

        assert isinstance(remain, float)
        assert remain == 16_000_000.

    def test_get_remaining_principal_in_fund_not_found_by_id(self):
        with pytest.raises(HTTPException):
            ctrl.getFundPrincAfterAmortById(9999)

    def test_get_remaining_principal_in_desemb_by_id(self):
        remain = ctrl.getDesembPrincAfterAmortById(MockData.desemb1.dealId, basedate=basedate)

        assert isinstance(remain, float)
        assert remain == 3_500_000

    def test_get_remaining_principal_in_desemb_not_found_by_id(self):
        with pytest.raises(HTTPException):
            ctrl.getDesembPrincAfterAmortById(9999)

    def test_get_available_funds_for_desemb_by_ccb(self):
        actualFunds = sorted(
            ctrl.getAvailableFundsForDesembByCcb(MockData.desemb2.ccb, basedate=basedate),
            key=lambda fund: fund.venc
        )
        expectedFunds = sorted(
            [MockData.fund1, MockData.fund2],
            key=lambda fund: fund.venc
        )

        assert len(actualFunds) == len(expectedFunds)

        for i in range(len(actualFunds)):
            actualFund = actualFunds[i]
            expectedFund = expectedFunds[i]

            assert isinstance(actualFund, Fund)
            assert actualFund == expectedFund

    def test_get_available_funds_for_desemb_by_ccb(self):
        with pytest.raises(HTTPException):
            ctrl.getAvailableFundsForDesembByCcb('9999')
        