import schedule
import time

from scripts.get_charger_data import EVChargerAPI


def job():
    getAPI = EVChargerAPI()
    # TODO: 각 list for 돌려서 insert 로직 추가
    charger_info = getAPI.get_charger_info()
    charger_status = getAPI.get_charger_status()

schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
