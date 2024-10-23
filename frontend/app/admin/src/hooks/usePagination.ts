// usePagination.ts
import { useState } from 'react';

export const usePagination = (initialItemsPerPage = 10) => {
  const [itemsPerPage, setItemsPerPage] = useState<number>(initialItemsPerPage);
  const [currentPage, setCurrentPage] = useState<number>(1);

  const skip = (currentPage - 1) * itemsPerPage;
  const limit = itemsPerPage;

  const handlePageChange = (page: number) => {
    setCurrentPage(page);
  };

  const handleSelect = (value: number) => {
    setItemsPerPage(value);
  };



  return { itemsPerPage, currentPage, skip, limit, handlePageChange, handleSelect };
};
