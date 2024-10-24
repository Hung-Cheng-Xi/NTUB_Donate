import React, { useState, useRef, useEffect } from 'react';

// types.ts
export interface ItemsPerPageProps {
  selectedValue: number;
  onSelect: (value: number) => void;
}

// ItemsPerPage.tsx
const ItemsPerPage: React.FC<ItemsPerPageProps> = ({
  selectedValue,
  onSelect,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  const toggleDropdown = () => setIsOpen(!isOpen);

  const handleSelect = (value: number) => {
    onSelect(value);
    setIsOpen(false); // 關閉下拉選單
  };

  // 處理點擊外部區域時關閉選單
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node)
      ) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  return (
    <div ref={dropdownRef}>
      <button
        id="dropdownActionButton"
        onClick={toggleDropdown}
        className="w-44 inline-flex items-center text-gray-500 bg-white
        border border-gray-300 focus:outline-none hover:bg-gray-100
        focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-base px-3 py-1.5
        dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600
        dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700"
        type="button"
      >
        {selectedValue} 筆資料
        <svg
          className="w-2.5 h-2.5 ml-auto"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 10 6"
        >
          <path
            stroke="currentColor"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="m1 1 4 4 4-4"
          />
        </svg>
      </button>

      {isOpen && (
        <div
          id="dropdownAction"
          className="z-10 bg-white divide-y divide-gray-100
           rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600"
        >
          <ul
            className="py-1 text-sm text-gray-700 dark:text-gray-200"
            aria-labelledby="dropdownActionButton"
          >
            {[2, 5, 10, 25, 50, 100].map((value) => (
              <li key={value}>
                <button
                  onClick={() => handleSelect(value)}
                  className="block w-full text-left px-4 py-2 hover:bg-gray-100
                   dark:hover:bg-gray-600 dark:hover:text-white"
                >
                  {value} 筆資料
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ItemsPerPage;
