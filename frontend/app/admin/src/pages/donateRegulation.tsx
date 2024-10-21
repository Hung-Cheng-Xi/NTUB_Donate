import React from 'react';
import { usePagination } from '../hooks/usePagination';
import ListGeneric from '../components/common/generic/listGeneric';

// Usage example
const DocumentPage: React.FC = () => {
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
      itemTitle="Donate Regulation"
      formFields={[
        { name: 'title', label: 'Title', type: 'text' },
        {
          name: 'category',
          label: 'Category',
          type: 'select',
          options: [
            { id: 1, name: 'ALL' },
            { id: 2, name: 'Education' },
            { id: 3, name: 'Health' },
            { id: 4, name: 'Community Development' },
            { id: 5, name: 'Animal Welfare' },
            { id: 6, name: 'Environmental Conservation' },
          ],
        },
        { name: 'description_link', label: 'Description Link', type: 'text' },
        { name: 'is_show', label: 'Show', type: 'checkbox' },
      ]}
      itemsPerPage={itemsPerPage}
      currentPage={currentPage}
      onSelect={handlePageChange}
      onPageChange={handleSelect}
    />
  );
};

export default DocumentPage;
