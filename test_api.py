import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# backend/.env 파일 명시적으로 로드
env_path = Path(__file__).parent / 'backend' / '.env'
load_dotenv(env_path)

print(f"Loading .env from: {env_path}")
print(f"API Key loaded: {'Yes' if os.getenv('DRUG_INFO_API_KEY') else 'No'}")
if os.getenv('DRUG_INFO_API_KEY'):
    print(f"API Key (first 10 chars): {os.getenv('DRUG_INFO_API_KEY')[:10]}...")
print()

def test_api():
    api_key = os.getenv('DRUG_INFO_API_KEY')
    base_url = 'http://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList'

    # 테스트할 약물 이름들
    test_drugs = [
        # 일반의약품 (OTC) - 작동할 것으로 예상
        '타이레놀',           # ✓ 해열진통제
        '게보린',             # 해열진통제
        '판피린',             # 해열진통제
        '부루펜',             # 소염진통제
        '베아제',             # 소화제

        # 정신과 전문의약품 - 작동하지 않을 것으로 예상
        '아빌리파이',         # 항정신병약
        '플루옥세틴',         # 항우울제
        '쎄로켈',             # 항정신병약
    ]

    for drug_name in test_drugs:
        print(f"\n{'='*60}")
        print(f"검색어: {drug_name}")
        print('='*60)

        params = {
            'serviceKey': api_key,
            'type': 'json',
            'itemName': drug_name,
            'numOfRows': 5,
            'pageNo': 1
        }

        try:
            response = requests.get(base_url, params=params, timeout=10)

            print(f"Status Code: {response.status_code}")

            if response.status_code == 200:
                try:
                    data = response.json()

                    # 결과 개수 확인
                    if 'body' in data and 'items' in data['body']:
                        items = data['body']['items']
                        if isinstance(items, list):
                            print(f"✅ 검색 결과: {len(items)}개")
                            for i, item in enumerate(items[:3], 1):
                                print(f"  {i}. {item.get('itemName', 'N/A')}")
                        elif isinstance(items, dict):
                            print(f"✅ 검색 결과: 1개")
                            print(f"  1. {items.get('itemName', 'N/A')}")
                        else:
                            print("❌ 검색 결과 없음")
                    else:
                        print("❌ 검색 결과 없음")
                        import json
                        print("API 응답:")
                        print(json.dumps(data, indent=2, ensure_ascii=False))

                except Exception as e:
                    print(f"JSON 파싱 실패: {e}")
                    print("Raw Response:")
                    print(response.text[:500])
            else:
                print(f"❌ API Error: {response.text[:500]}")

        except Exception as e:
            print(f"❌ 요청 실패: {e}")

if __name__ == "__main__":
    test_api()
