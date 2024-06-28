from datetime import date
import requests
from bs4 import BeautifulSoup

class ParserCBRF:
    def __init__(self):
        self.data = {}

    def start(self):
        self._download_data()
        self._parse_data()

    def _download_data(self):
        url_params = "?" \
                     "UniDbQuery.Posted=True&" \
                     "UniDbQuery.From=17.09.2013&" \
                     "UniDbQuery.To={}".format(self._today_human_date())
        url = "https://www.cbr.ru/hd_base/KeyRate/" + url_params
        r = requests.get(url)
        return r.text

    def _parse_data(self, html):
        soup = BeautifulSoup(html, "html.parser")
        raw_data = [i.text for i in soup.find("table", {"class": "data"}).find_all("td")]
        dates = raw_data[::2]
        rates = raw_data[1::2]
        for date, rate in zip(dates, rates):
            self.data[date] = rate

    def _today_human_date(self):
        today = date.today().strftime("%d.%m.%Y")
        return today

    def get_data(self):
        return self.data

if __name__ == "__main__":
    parser = ParserCBRF()
    parser.start()
    print(parser.get_data())
