import requests

from first.models import USD


def get_course():
    data_from_bank = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    rate_usr_rub = data_from_bank['rates']['USD']
    usd = USD.objects.last()
    usd.usd_now = rate_usr_rub
    usd.save()