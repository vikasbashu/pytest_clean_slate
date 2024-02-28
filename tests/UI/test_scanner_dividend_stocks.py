import pytest
import allure
from pages.ScannerDividendPage import ScannerDividend

@pytest.mark.usefixtures('setup')
class Test_DIVIDEND_STOCKS:

    @pytest.mark.dividendStocks
    def test_get_top_dividend_stocks(self):
        self.sd = ScannerDividend(self.driver)
        assert self.sd.get_page_title() == "Highest Dividend Yield Shares - Screener"
        assert self.sd.get_welcome_message() == "Highest Dividend Yield Shares"
        self.sd.fetch_headers()
        self.sd.fetch_records()
