from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base


class MedicationRecord(Base):
    """복약 리스트 모델"""
    __tablename__ = "medication_records"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)  # 약품명
    item_image = Column(String, nullable=True)  # 약 이미지 URL
    efcy_qesitm = Column(String, nullable=True)  # 효능
    use_method_qesitm = Column(String, nullable=True)  # 용법
    is_taken = Column(Boolean, default=False)  # 복용 여부
    created_at = Column(DateTime, default=datetime.utcnow)  # 등록 일시
