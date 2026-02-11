from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MedicationRecordBase(BaseModel):
    """복약 기록 기본 스키마"""
    item_name: str
    item_image: Optional[str] = None
    efcy_qesitm: Optional[str] = None
    use_method_qesitm: Optional[str] = None


class MedicationRecordCreate(MedicationRecordBase):
    """복약 기록 생성 스키마"""
    pass


class MedicationRecordUpdate(BaseModel):
    """복약 기록 업데이트 스키마"""
    is_taken: bool


class MedicationRecord(MedicationRecordBase):
    """복약 기록 응답 스키마"""
    id: int
    is_taken: bool
    created_at: datetime

    class Config:
        from_attributes = True


class DrugSearchResult(BaseModel):
    """약물 검색 결과 스키마"""
    item_name: str
    item_image: Optional[str] = None
    efcy_qesitm: Optional[str] = None
    use_method_qesitm: Optional[str] = None
