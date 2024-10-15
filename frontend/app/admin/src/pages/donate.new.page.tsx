import React from 'react';
import GenericPage from '../components/common/pageLayout/generic.page';

interface NewsProps {
  id: number;
  date: string;
  title: string;
  description: string;
  is_show: boolean;
}

const newsPropsData: NewsProps[] = [
  {
    id: 1,
    date: '2024-10-12',
    title: 'News Title 1',
    description: 'This is the description of the first news.',
    is_show: true,
  },
  {
    id: 2,
    date: '2024-10-11',
    title: 'News Title 2',
    description: 'This is the description of the second news.',
    is_show: true,
  },
  {
    id: 3,
    date: '2024-10-10',
    title: 'News Title 3',
    description: 'This is the description of the third news.',
    is_show: false,
  },
  {
    id: 4,
    date: '2024-10-09',
    title: 'News Title 4',
    description: 'This is the description of the fourth news.',
    is_show: true,
  },
  {
    id: 5,
    date: '2024-10-08',
    title: 'News Title 5',
    description: 'This is the description of the fifth news.',
    is_show: false,
  },
];

const NewsPage: React.FC = () => {
  return (
    <GenericPage<NewsProps>
      data={newsPropsData}
      itemTitle="Donate News"
      formFields={[
        { name: 'date', label: 'Date', type: 'date' },
        { name: 'title', label: 'Title', type: 'text' },
        { name: 'description', label: 'Description', type: 'textarea' },
        { name: 'is_show', label: 'Show', type: 'checkbox' },
      ]}
      viewMode="list" // Add viewMode property to determine if list or table should be used
    />
  );
};

export default NewsPage;
