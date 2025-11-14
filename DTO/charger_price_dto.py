from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class ChargePriceDto:
    operator_code: str          # 운영기관 코드 (BID)
    operator_name: Optional[str]=None          # 운영기관명 (BNM)
    price_type_code: str        # 급속/완속 코드(01/02)
    price_type_name: Optional[str]=None        # 급속/완속 명칭 (PRICE_TYPE_NM)
    member_price: Optional[str]=None         # 회원요금
    guest_price: float          # 비회원요금
    update_dt: Optional[str]=None             # 업데이트 날짜
