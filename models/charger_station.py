from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Charger_station:
    station_id: str
    station_name: str
    addr: str
    addr_detail: str
    location: str
    lat: float
    lng: float
    use_time: str
    parking_free: str
    note: str
    limit_yn: str
    limit_detail: str
    del_yn: str
    del_detail: str
    kind: str
    kind_detail: str
    zcode: str
    zscode: str
    traffic_yn: str
    year: str
    floor_num: str
    floor_type: str
    operator_id: str
    update_dt: Optional[datetime] = None
