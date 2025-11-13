from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Charger_detail:
    charger_id: str
    charger_id: str
    station_id: str
    charger_type: str
    output_kw: float
    method: str
    del_yn: str
    del_detail: str
    stat: int
    stat_upd_dt: Optional[datetime] = None
    last_tsdt: Optional[datetime] = None
    last_tedt: Optional[datetime] = None
    now_tsdt: Optional[datetime] = None
