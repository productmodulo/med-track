import os
import requests
from typing import List, Dict, Optional
from dotenv import load_dotenv

load_dotenv()


class DrugAPIService:
    """공공데이터포털 의약품 API 서비스"""

    def __init__(self):
        self.api_key = os.getenv('DRUG_INFO_API_KEY')
        self.base_url = 'http://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList'

    def search_drugs(self, item_name: str, num_of_rows: int = 10) -> List[Dict]:
        """
        약물 검색

        Args:
            item_name: 검색할 약물명
            num_of_rows: 결과 개수 (기본 10개)

        Returns:
            검색된 약물 정보 리스트
        """
        params = {
            'serviceKey': self.api_key,
            'type': 'json',
            'itemName': item_name,
            'numOfRows': num_of_rows,
            'pageNo': 1
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()

                # API 응답 구조 확인
                if 'body' in data and 'items' in data['body']:
                    items = data['body']['items']

                    # items가 리스트인지 확인
                    if isinstance(items, list):
                        return items
                    elif isinstance(items, dict):
                        # 단일 결과인 경우 리스트로 변환
                        return [items]

                return []
            else:
                print(f"API Error: {response.status_code} - {response.text}")
                return []

        except Exception as e:
            print(f"Exception occurred: {e}")
            return []

    def get_drug_detail(self, item_name: str) -> Optional[Dict]:
        """
        특정 약물의 상세 정보 조회

        Args:
            item_name: 약물명

        Returns:
            약물 상세 정보 또는 None
        """
        results = self.search_drugs(item_name, num_of_rows=1)
        return results[0] if results else None


# 싱글톤 인스턴스
drug_api_service = DrugAPIService()
