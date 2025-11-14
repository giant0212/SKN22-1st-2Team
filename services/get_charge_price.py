import requests

url = "https://ev.or.kr/nportal/evcarInfo/selectEvcarStationPriceSearch.ajax"

payload = {
    "spageId": "statsList",
    "srecordCountPerPage": 1000,
    "spageNo": 1,
    "spageSize": 10,
    "excelPage": "",
    "excelCnt": "",
    "bid": "",
    "type": "",
    "selExcelCnt": 1000
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://ev.or.kr/nportal/evcarInfo/initEvcarChargeInfoAction.do"
}

res = requests.post(url, data=payload, headers=headers)
data = res.json()
charge_datas=data['list']

