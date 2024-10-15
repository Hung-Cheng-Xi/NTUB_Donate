import React from 'react';
import GenericPage from '../components/common/pageLayout/generic.page';

interface DocumentPurpose {
  id: number;
  title: string;
  category: string;
  description_link: string;
  is_show: boolean;
}

const documentData: DocumentPurpose[] = [
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
  return (
    <GenericPage<DocumentPurpose>
      data={documentData}
      itemTitle="Donate Document"
      formFields={[
        { name: 'title', label: 'Title', type: 'text' },
        {
          name: 'category',
          label: 'Category',
          type: 'select',
          options: [
            'ALL',
            'Education',
            'Health',
            'Community Development',
            'Animal Welfare',
            'Environmental Conservation',
          ],
        },
        { name: 'description_link', label: 'Description Link', type: 'text' },
        { name: 'is_show', label: 'Show', type: 'checkbox' },
      ]}
      viewMode="list" // Add viewMode property to determine if list or table should be used
    />
  );
};

export default DocumentPage;
