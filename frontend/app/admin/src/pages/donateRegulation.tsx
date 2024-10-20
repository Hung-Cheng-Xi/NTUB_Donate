import React from 'react';
import { usePagination } from '../hooks/usePagination';
import ListGeneric from '../components/common/generic/listGeneric';

interface RegulationPurpose {
  id: number;
  title: string;
  category: string;
  description_link: string;
  is_show: boolean;
}

const RegulationData: RegulationPurpose[] = [
  {
    id: 1,
    category: 'ALL',
    title: 'Education Fund',
    description_link: 'Support for educational initiatives.',
    is_show: true,
  },
  {
    id: 2,
    category: 'ALL',
    title: 'Health Fund',
    description_link: 'Support for healthcare projects.',
    is_show: true,
  },
  {
    id: 3,
    category: 'ALL',
    title: 'Community Development',
    description_link: 'Support for community building activities.',
    is_show: true,
  },
  {
    id: 4,
    category: 'ALL',
    title: 'Animal Welfare',
    description_link: 'Support for animal welfare initiatives.',
    is_show: false,
  },
  {
    id: 5,
    category: 'ALL',
    title: 'Environmental Conservation',
    description_link: 'Support for environmental conservation.',
    is_show: true,
  },
];

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
      data={RegulationData}
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
