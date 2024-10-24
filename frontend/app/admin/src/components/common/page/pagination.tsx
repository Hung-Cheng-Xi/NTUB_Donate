import React from 'react';

export interface PaginationProps {
  totalItems: number;
  currentPage: number;
  onPageChange: (page: number) => void;
}

const Pagination: React.FC<PaginationProps> = ({
  totalItems,
  currentPage,
  onPageChange,
}) => {
  const handlePageClick = (page: number) => {
    if (page >= 1 && page <= totalItems) {
      onPageChange(page);
    }
  };

  return (
    <nav aria-label="Page navigation example" className="flex justify-end">
      <ul className="list-style-none flex">
        <li>
          <button
            className="relative block rounded bg-transparent px-3 py-1.5 text-sm text-surface
            transition duration-300 hover:bg-neutral-100
            focus:bg-neutral-100 focus:text-primary-700 focus:outline-none
            active:bg-neutral-100 active:text-primary-700
            dark:text-white dark:hover:bg-neutral-700 dark:focus:bg-neutral-700
            dark:focus:text-primary-500 dark:active:bg-neutral-700
            dark:active:text-primary-500"
            onClick={() => handlePageClick(currentPage - 1)}
            disabled={currentPage === 1}
            aria-label="Previous"
          >
            <span aria-hidden="true">&laquo;</span>
          </button>
        </li>

        {Array.from({ length: totalItems }, (_, index) => (
          <li
            key={index}
            aria-current={currentPage === index + 1 ? 'page' : undefined}
          >
            <button
              className={`relative block rounded bg-transparent px-3 py-1.5
                text-sm text-surface transition duration-300 hover:bg-neutral-100
                focus:bg-neutral-100 focus:text-primary-700 focus:outline-none
                active:bg-neutral-100 active:text-primary-700 dark:text-white
                dark:hover:bg-neutral-700 dark:focus:bg-neutral-700
                dark:focus:text-primary-500 dark:active:bg-neutral-700
                dark:active:text-primary-500 ${
                  currentPage === index + 1 ? 'font-bold underline' : ''
                }`}
              onClick={() => handlePageClick(index + 1)}
            >
              {index + 1}
            </button>
          </li>
        ))}

        <li>
          <button
            className="relative block rounded bg-transparent px-3 py-1.5
            text-sm text-surface transition duration-300 hover:bg-neutral-100
            focus:bg-neutral-100 focus:text-primary-700 focus:outline-none
            active:bg-neutral-100 active:text-primary-700 dark:text-white
            dark:hover:bg-neutral-700 dark:focus:bg-neutral-700
            dark:focus:text-primary-500 dark:active:bg-neutral-700
            dark:active:text-primary-500"
            onClick={() => handlePageClick(currentPage + 1)}
            disabled={currentPage === totalItems}
            aria-label="Next"
          >
            <span aria-hidden="true">&raquo;</span>
          </button>
        </li>
      </ul>
    </nav>
  );
};

export default Pagination;
