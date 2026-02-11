import { useState } from 'react';

function SearchBar({ onSearch }) {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      onSearch(query);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-2xl mx-auto mb-8">
      <div className="flex gap-2">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="약 이름을 검색하세요 (예: 타이레놀, 아빌리파이)"
          className="flex-1 px-6 py-4 text-lg rounded-full border-2 border-purple-200
                   focus:border-purple-400 focus:outline-none focus:ring-4
                   focus:ring-purple-100 shadow-lg transition-all"
        />
        <button
          type="submit"
          className="px-8 py-4 bg-gradient-to-r from-purple-400 to-pink-400
                   text-white font-semibold rounded-full shadow-lg
                   hover:shadow-xl hover:scale-105 transition-all"
        >
          🔍 검색
        </button>
      </div>
    </form>
  );
}

export default SearchBar;
