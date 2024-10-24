import React, { useState } from 'react';

type SearchInputProps = {
  search: string;
  onSearch: (value: string) => void;
  placeholder?: string;
};

const SearchInput: React.FC<SearchInputProps> = ({
  search,
  onSearch,
  placeholder = 'Search for items',
}) => {
  const [inputValue, setInputValue] = useState(search);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      onSearch(inputValue);
    }
  };

  return (
    <div className="relative">
      <div
        className="absolute inset-y-0 start-0 flex items-center ps-3
                  pointer-events-none"
      >
        <svg
          className="w-4 h-4 text-gray-500 dark:text-gray-400"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 20 20"
        >
          <path
            stroke="currentColor"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
          />
        </svg>
      </div>
      <input
        type="text"
        className="block py-2 ps-10 text-sm text-gray-900
                    border border-gray-300 rounded-lg w-80 bg-gray-50
                    focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700
                    dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
        placeholder={placeholder}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        value={inputValue}
      />
    </div>
  );
};

export default SearchInput;
