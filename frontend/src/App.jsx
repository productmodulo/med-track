import { useState, useEffect } from 'react';
import SearchBar from './components/SearchBar';
import DrugCard from './components/DrugCard';
import MedicationList from './components/MedicationList';

const API_BASE_URL = 'http://localhost:8000';

function App() {
  const [searchResults, setSearchResults] = useState([]);
  const [medications, setMedications] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // 복약 리스트 불러오기
  const fetchMedications = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/medications`);
      if (response.ok) {
        const data = await response.json();
        setMedications(data);
      }
    } catch (err) {
      console.error('복약 리스트 로딩 실패:', err);
    }
  };

  useEffect(() => {
    fetchMedications();
  }, []);

  // 약물 검색
  const handleSearch = async (query) => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(
        `${API_BASE_URL}/api/drugs/search?q=${encodeURIComponent(query)}&limit=10`
      );

      if (response.ok) {
        const data = await response.json();
        setSearchResults(data);
      } else {
        setError('검색 중 오류가 발생했습니다.');
      }
    } catch (err) {
      setError('서버에 연결할 수 없습니다. 백엔드가 실행 중인지 확인해주세요.');
      console.error('검색 실패:', err);
    } finally {
      setLoading(false);
    }
  };

  // 복약 리스트에 추가
  const handleAddToList = async (drug) => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/medications`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(drug),
      });

      if (response.ok) {
        await fetchMedications();
        alert(`${drug.item_name}이(가) 복약 리스트에 추가되었습니다! ✨`);
      }
    } catch (err) {
      alert('추가 중 오류가 발생했습니다.');
      console.error('추가 실패:', err);
    }
  };

  // 복용 체크 토글
  const handleToggle = async (id, isTaken) => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/medications/${id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ is_taken: isTaken }),
      });

      if (response.ok) {
        await fetchMedications();
      }
    } catch (err) {
      console.error('업데이트 실패:', err);
    }
  };

  // 복약 기록 삭제
  const handleDelete = async (id) => {
    if (!confirm('정말로 삭제하시겠습니까?')) return;

    try {
      const response = await fetch(`${API_BASE_URL}/api/medications/${id}`, {
        method: 'DELETE',
      });

      if (response.status === 204) {
        await fetchMedications();
      }
    } catch (err) {
      alert('삭제 중 오류가 발생했습니다.');
      console.error('삭제 실패:', err);
    }
  };

  return (
    <div className="min-h-screen py-8 px-4">
      <div className="max-w-7xl mx-auto">
        {/* 헤더 */}
        <header className="text-center mb-12">
          <h1 className="text-5xl font-bold text-purple-800 mb-4">
            💊 Med-Track
          </h1>
          <p className="text-xl text-purple-600">
            나의 귀여운 복약 관리 도우미
          </p>
        </header>

        {/* 검색 바 */}
        <SearchBar onSearch={handleSearch} />

        {/* 로딩 상태 */}
        {loading && (
          <div className="text-center text-purple-600 text-xl mb-8">
            검색 중... 🔍
          </div>
        )}

        {/* 에러 메시지 */}
        {error && (
          <div className="bg-red-100 border-2 border-red-300 text-red-700
                        rounded-3xl p-4 mb-8 text-center">
            {error}
          </div>
        )}

        {/* 검색 결과 */}
        {searchResults.length > 0 && (
          <div className="mb-12">
            <h2 className="text-2xl font-bold text-purple-800 mb-6 text-center">
              검색 결과 🔍
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {searchResults.map((drug, index) => (
                <DrugCard
                  key={index}
                  drug={drug}
                  onAdd={handleAddToList}
                />
              ))}
            </div>
          </div>
        )}

        {/* 복약 리스트 */}
        <MedicationList
          medications={medications}
          onToggle={handleToggle}
          onDelete={handleDelete}
          onRefresh={fetchMedications}
        />
      </div>
    </div>
  );
}

export default App;
