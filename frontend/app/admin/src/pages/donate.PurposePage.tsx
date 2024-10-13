import React from 'react';
import GenericPage from '../components/Common/PageLayout/GenericPage';

interface DonationPurpose {
  id: number;
  title: string;
  lump_sum: number;
  description: string;
  memo: string;
  is_show: boolean;
}

const donationPurposeData: DonationPurpose[] = [
  {
    id: 1,
    title: 'Education Fund',
    lump_sum: 10000,
    description: 'Support for educational initiatives.',
    memo: 'This fund is used for school facilities and scholarships.',
    is_show: true,
  },
  {
    id: 2,
    title: 'Health Fund',
    lump_sum: 20000,
    description: 'Support for healthcare projects.',
    memo: 'This fund helps in providing medical aid to those in need.',
    is_show: true,
  },
  {
    id: 3,
    title: 'Community Development',
    lump_sum: 15000,
    description: 'Support for community building activities.',
    memo: 'This fund is used for infrastructure and social projects.',
    is_show: true,
  },
  {
    id: 4,
    title: 'Animal Welfare',
    lump_sum: 8000,
    description: 'Support for animal welfare initiatives.',
    memo: 'This fund helps in rescuing and caring for stray animals.',
    is_show: false,
  },
  {
    id: 5,
    title: 'Environmental Conservation',
    lump_sum: 12000,
    description: 'Support for environmental conservation.',
    memo: 'This fund is used for tree planting and waste management projects.',
    is_show: true,
  },
];

// Usage example
const PurposePage: React.FC = () => {
  return (
    <GenericPage<DonationPurpose>
      data={donationPurposeData}
      itemTitle="Donate Purpose"
      formFields={[
        { name: 'title', label: 'Title', type: 'text' },
        { name: 'lump_sum', label: 'Lump Sum', type: 'number' },
        { name: 'description', label: 'Description', type: 'textarea' },
        { name: 'memo', label: 'Memo', type: 'textarea' },
        { name: 'is_show', label: 'Show', type: 'checkbox' },
      ]}
      viewMode="list" // Add viewMode property to determine if list or table should be used
    />
  );
};

export default PurposePage;
