from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from app import crud, models, schemas
from app.database import engine, get_db
from app.services.drug_api import drug_api_service

# 데이터베이스 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Med-Track API",
    description="의약품 복용 관리 API",
    version="1.0.0"
)

# CORS 설정 (프론트엔드에서 접근 가능하도록)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 특정 origin만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    """API 루트 엔드포인트"""
    return {
        "message": "Med-Track API에 오신 것을 환영합니다!",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/api/drugs/search", response_model=List[schemas.DrugSearchResult])
def search_drugs(q: str, limit: int = 10):
    """
    약물 검색

    Args:
        q: 검색할 약물명
        limit: 결과 개수 (기본 10개)

    Returns:
        검색된 약물 정보 리스트
    """
    if not q:
        raise HTTPException(status_code=400, detail="검색어를 입력해주세요")

    results = drug_api_service.search_drugs(q, num_of_rows=limit)

    # API 응답을 스키마에 맞게 변환
    formatted_results = []
    for item in results:
        formatted_results.append({
            "item_name": item.get("itemName", ""),
            "item_image": item.get("itemImage"),
            "efcy_qesitm": item.get("efcyQesitm"),
            "use_method_qesitm": item.get("useMethodQesitm")
        })

    return formatted_results


@app.get("/api/medications", response_model=List[schemas.MedicationRecord])
def get_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    모든 복약 기록 조회

    Args:
        skip: 건너뛸 개수
        limit: 조회할 최대 개수
        db: 데이터베이스 세션

    Returns:
        복약 기록 리스트
    """
    records = crud.get_medication_records(db, skip=skip, limit=limit)
    return records


@app.get("/api/medications/{record_id}", response_model=schemas.MedicationRecord)
def get_medication(record_id: int, db: Session = Depends(get_db)):
    """
    특정 복약 기록 조회

    Args:
        record_id: 기록 ID
        db: 데이터베이스 세션

    Returns:
        복약 기록
    """
    record = crud.get_medication_record(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="복약 기록을 찾을 수 없습니다")
    return record


@app.post("/api/medications", response_model=schemas.MedicationRecord, status_code=201)
def create_medication(
    record: schemas.MedicationRecordCreate,
    db: Session = Depends(get_db)
):
    """
    복약 기록 생성

    Args:
        record: 생성할 복약 기록 정보
        db: 데이터베이스 세션

    Returns:
        생성된 복약 기록
    """
    return crud.create_medication_record(db, record)


@app.patch("/api/medications/{record_id}", response_model=schemas.MedicationRecord)
def update_medication(
    record_id: int,
    record_update: schemas.MedicationRecordUpdate,
    db: Session = Depends(get_db)
):
    """
    복약 기록 업데이트 (복용 체크)

    Args:
        record_id: 기록 ID
        record_update: 업데이트할 정보
        db: 데이터베이스 세션

    Returns:
        업데이트된 복약 기록
    """
    record = crud.update_medication_record(db, record_id, record_update)
    if not record:
        raise HTTPException(status_code=404, detail="복약 기록을 찾을 수 없습니다")
    return record


@app.delete("/api/medications/{record_id}", status_code=204)
def delete_medication(record_id: int, db: Session = Depends(get_db)):
    """
    복약 기록 삭제

    Args:
        record_id: 기록 ID
        db: 데이터베이스 세션
    """
    success = crud.delete_medication_record(db, record_id)
    if not success:
        raise HTTPException(status_code=404, detail="복약 기록을 찾을 수 없습니다")
    return None
