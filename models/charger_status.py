from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Charger_status:
    busi_id: str
    station_id: str
    charger_id: str
    stat: int
    stat_upd_dt: Optional[datetime] = None
    last_tsdt: Optional[datetime] = None
    last_tedt: Optional[datetime] = None
    now_tsdt: Optional[datetime] = None
    reg_dt: Optional[datetime] = datetime.now()
    upd_dt: Optional[datetime] = None
