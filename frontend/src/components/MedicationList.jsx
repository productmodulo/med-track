function MedicationList({ medications, onToggle, onDelete, onRefresh }) {
  if (medications.length === 0) {
    return (
      <div className="bg-white rounded-3xl shadow-xl p-8 text-center">
        <p className="text-gray-500 text-lg">
          아직 복약 리스트가 비어있어요 😊
        </p>
        <p className="text-gray-400 mt-2">
          약을 검색해서 추가해보세요!
        </p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-3xl shadow-xl p-6">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-purple-800">
          오늘의 복약 리스트 💊
        </h2>
        <button
          onClick={onRefresh}
          className="px-4 py-2 bg-pastel-blue rounded-full text-purple-700
                   hover:bg-blue-200 transition-all"
        >
          🔄 새로고침
        </button>
      </div>

      <div className="space-y-3">
        {medications.map((med) => (
          <div
            key={med.id}
            className={`flex items-center gap-4 p-4 rounded-2xl transition-all
                     ${med.is_taken
                       ? 'bg-pastel-green border-2 border-green-300'
                       : 'bg-pastel-purple border-2 border-purple-200'
                     }`}
          >
            <input
              type="checkbox"
              checked={med.is_taken}
              onChange={() => onToggle(med.id, !med.is_taken)}
              className="w-6 h-6 rounded-full cursor-pointer accent-purple-500"
            />

            <div className="flex-1">
              <h3 className={`font-bold text-lg ${
                med.is_taken ? 'line-through text-gray-500' : 'text-purple-800'
              }`}>
                {med.item_name}
              </h3>

              {med.efcy_qesitm && (
                <p className="text-sm text-gray-600 mt-1 line-clamp-1">
                  {med.efcy_qesitm}
                </p>
              )}
            </div>

            <button
              onClick={() => onDelete(med.id)}
              className="px-4 py-2 bg-red-100 text-red-600 rounded-full
                       hover:bg-red-200 hover:scale-105 transition-all"
            >
              🗑️ 삭제
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MedicationList;
