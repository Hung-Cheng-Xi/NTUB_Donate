import React from 'react';
import ListGeneric from '../components/common/generic/listGeneric';
import { usePagination } from '../hooks/usePagination';

// Usage example
const PurposePage: React.FC = () => {
  const {
    itemsPerPage,
    currentPage,
    skip,
    limit,
    handlePageChange,
    handleSelect,
  } = usePagination();

  console.log(skip, limit);

  return (
    <ListGeneric
      data={{ total_count: 0, items: [] }}
      itemTitle="Donate Purpose"
      formFields={[
        { name: 'title', label: 'Title', type: 'text' },
        { name: 'lump_sum', label: 'Lump Sum', type: 'number' },
        { name: 'description', label: 'Description', type: 'textarea' },
        { name: 'memo', label: 'Memo', type: 'textarea' },
        { name: 'is_show', label: 'Show', type: 'checkbox' },
      ]}
      itemsPerPage={itemsPerPage}
      currentPage={currentPage}
      onSelect={handlePageChange}
      onPageChange={handleSelect}
    />
  );
};

export default PurposePage;
