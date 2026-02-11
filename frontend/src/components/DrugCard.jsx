function DrugCard({ drug, onAdd }) {
  return (
    <div className="bg-white rounded-3xl shadow-xl p-6 hover:shadow-2xl
                    transition-all duration-300 hover:scale-105">
      <div className="flex flex-col items-center">
        {drug.item_image ? (
          <img
            src={drug.item_image}
            alt={drug.item_name}
            className="w-32 h-32 object-contain mb-4 rounded-xl"
            onError={(e) => {
              e.target.style.display = 'none';
            }}
          />
        ) : (
          <div className="w-32 h-32 bg-gradient-to-br from-pastel-purple to-pastel-pink
                        rounded-xl flex items-center justify-center mb-4">
            <span className="text-5xl">💊</span>
          </div>
        )}

        <h3 className="text-xl font-bold text-purple-800 mb-3 text-center">
          {drug.item_name}
        </h3>

        {drug.efcy_qesitm && (
          <div className="mb-3 w-full">
            <p className="text-sm font-semibold text-purple-600 mb-1">효능</p>
            <p className="text-sm text-gray-700 line-clamp-3">
              {drug.efcy_qesitm}
            </p>
          </div>
        )}

        {drug.use_method_qesitm && (
          <div className="mb-4 w-full">
            <p className="text-sm font-semibold text-purple-600 mb-1">용법</p>
            <p className="text-sm text-gray-700 line-clamp-2">
              {drug.use_method_qesitm}
            </p>
          </div>
        )}

        <button
          onClick={() => onAdd(drug)}
          className="w-full px-6 py-3 bg-gradient-to-r from-purple-400 to-pink-400
                   text-white font-semibold rounded-full shadow-lg
                   hover:shadow-xl hover:scale-105 transition-all"
        >
          ➕ 복약 리스트에 추가
        </button>
      </div>
    </div>
  );
}

export default DrugCard;
