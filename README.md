# 💊 Med-Track

귀여운 의약품 복용 관리 웹 애플리케이션

## 📝 프로젝트 소개

Med-Track은 한국 의약품을 검색하고, 상세 정보를 확인하고, 나의 '오늘의 복약 리스트'에 추가할 수 있는 CRUD 웹 애플리케이션입니다. 공공데이터포털의 '식품의약품안전처 e약은요' API를 활용하여 정확한 의약품 정보를 제공합니다.

## ✨ 주요 기능

- 🔍 **약물 검색**: 약 이름으로 검색 (예: 타이레놀, 아빌리파이, 쎄로켈)
- 💊 **약물 카드**: 약 사진, 이름, 효능, 용법을 보기 좋은 카드 UI로 표시
- ✅ **복약 리스트 관리**: 검색한 약을 '오늘의 복약 리스트'에 추가/삭제/체크
- 🎨 **파스텔톤 UI**: 부드럽고 귀여운 파스텔 컬러 테마

## 🛠️ 기술 스택

### 프론트엔드
- **React 18** + **Vite**: 빠른 개발 환경
- **Tailwind CSS**: 유틸리티 우선 CSS 프레임워크
- **파스텔 컬러 테마**: #F3E5F5, #E1F5FE 등

### 백엔드
- **FastAPI**: 고성능 Python 웹 프레임워크
- **SQLAlchemy**: SQL 툴킷 및 ORM
- **PostgreSQL**: 관계형 데이터베이스
- **uv**: 빠른 Python 패키지 관리자

### 외부 API
- **공공데이터포털 API**: 식품의약품안전처 e약은요 API

## 📁 프로젝트 구조

```
med-track/
├── backend/                 # FastAPI 백엔드
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # FastAPI 앱 및 라우터
│   │   ├── database.py     # 데이터베이스 연결
│   │   ├── models.py       # SQLAlchemy 모델
│   │   ├── schemas.py      # Pydantic 스키마
│   │   ├── crud.py         # CRUD 작업
│   │   └── services/
│   │       └── drug_api.py # 공공데이터 API 서비스
│   ├── .env                # 환경 변수
│   └── pyproject.toml      # uv 의존성
│
├── frontend/               # React 프론트엔드
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.jsx
│   │   │   ├── DrugCard.jsx
│   │   │   └── MedicationList.jsx
│   │   ├── App.jsx
│   │   └── index.css
│   ├── tailwind.config.js
│   └── package.json
│
└── README.md
```

## 🚀 시작하기

### 사전 요구사항

- Python 3.8+
- Node.js 18+
- Docker & Docker Compose
- 공공데이터포털 API 키

### 1. 저장소 클론

```bash
cd med-track
```

### 2. 환경 변수 설정

`backend/.env` 파일을 생성하고 다음 내용을 추가하세요:

```env
DRUG_INFO_API_KEY="your_api_key_here"
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/medtrack"
```

### 3. PostgreSQL 실행 (Docker Compose)

```bash
# Docker Compose로 PostgreSQL 실행
docker-compose up -d

# 데이터베이스가 준비될 때까지 잠시 대기 (약 5초)
# 상태 확인
docker-compose ps
```

PostgreSQL이 백그라운드에서 실행되며, `medtrack` 데이터베이스가 자동으로 생성됩니다.

**중지하려면:**
```bash
docker-compose down
```

**데이터까지 완전히 삭제하려면:**
```bash
docker-compose down -v
```

### 4. 백엔드 설정 및 실행

```bash
# backend 디렉토리로 이동
cd backend

# uv로 의존성 설치 (가상환경 자동 생성)
uv sync

# FastAPI 서버 실행
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

백엔드 서버가 http://localhost:8000 에서 실행됩니다.

API 문서는 http://localhost:8000/docs 에서 확인할 수 있습니다.

### 5. 프론트엔드 설정 및 실행

새 터미널을 열고:

```bash
# frontend 디렉토리로 이동
cd frontend

# Node.js 의존성 설치
npm install

# Vite 개발 서버 실행
npm run dev
```

프론트엔드가 http://localhost:5173 에서 실행됩니다.

## 📡 API 엔드포인트

### 약물 검색
- `GET /api/drugs/search?q={query}&limit={limit}`: 약물 검색

### 복약 리스트 CRUD
- `GET /api/medications`: 모든 복약 기록 조회
- `GET /api/medications/{id}`: 특정 복약 기록 조회
- `POST /api/medications`: 복약 기록 생성
- `PATCH /api/medications/{id}`: 복약 기록 업데이트 (복용 체크)
- `DELETE /api/medications/{id}`: 복약 기록 삭제

## 🎨 UI/UX 특징

- **파스텔 그라데이션 배경**: 보라색에서 파란색으로 부드러운 그라데이션
- **둥근 카드 디자인**: 모든 UI 요소가 둥글둥글하고 귀여움
- **호버 효과**: 마우스를 올리면 카드가 살짝 커지는 인터랙티브 효과
- **체크박스 시스템**: 복약 완료 시 시각적 피드백
- **반응형 그리드**: 화면 크기에 따라 자동으로 레이아웃 조정

## 🐛 트러블슈팅

### 백엔드 실행 시 `ModuleNotFoundError`
```bash
# 가상환경 활성화 확인
source .venv/bin/activate  # Linux/Mac
# 또는
.venv\Scripts\activate  # Windows

# 의존성 재설치
uv sync
```

### 프론트엔드 실행 시 API 연결 실패
- 백엔드가 http://localhost:8000 에서 실행 중인지 확인
- CORS 설정이 올바른지 확인
- 브라우저 콘솔에서 에러 메시지 확인

### PostgreSQL 연결 실패
- PostgreSQL 서비스가 실행 중인지 확인
- `DATABASE_URL`이 올바른지 확인
- 데이터베이스가 생성되었는지 확인

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 🙏 감사의 말

- 공공데이터포털의 '식품의약품안전처 e약은요' API
- FastAPI, React, Tailwind CSS 커뮤니티
