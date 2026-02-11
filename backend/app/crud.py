from sqlalchemy.orm import Session
from app import models, schemas
from typing import List


def get_medication_records(db: Session, skip: int = 0, limit: int = 100) -> List[models.MedicationRecord]:
    """모든 복약 기록 조회"""
    return db.query(models.MedicationRecord).offset(skip).limit(limit).all()


def get_medication_record(db: Session, record_id: int) -> models.MedicationRecord:
    """특정 복약 기록 조회"""
    return db.query(models.MedicationRecord).filter(models.MedicationRecord.id == record_id).first()


def create_medication_record(db: Session, record: schemas.MedicationRecordCreate) -> models.MedicationRecord:
    """복약 기록 생성"""
    db_record = models.MedicationRecord(**record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def update_medication_record(
    db: Session,
    record_id: int,
    record_update: schemas.MedicationRecordUpdate
) -> models.MedicationRecord:
    """복약 기록 업데이트 (복용 체크)"""
    db_record = get_medication_record(db, record_id)
    if db_record:
        db_record.is_taken = record_update.is_taken
        db.commit()
        db.refresh(db_record)
    return db_record


def delete_medication_record(db: Session, record_id: int) -> bool:
    """복약 기록 삭제"""
    db_record = get_medication_record(db, record_id)
    if db_record:
        db.delete(db_record)
        db.commit()
        return True
    return False
