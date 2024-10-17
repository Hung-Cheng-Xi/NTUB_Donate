import React from 'react';
import GenericPage from '../components/common/pageLayout/genericPage';

interface AnnouncementProps {
  id: number;
  date: string;
  title: string;
  description: string;
  is_show: boolean;
}

const newsPropsData: AnnouncementProps[] = [
  {
    id: 1,
    date: '2024-10-12',
    title: 'Announcement Title 1',
    description: 'This is the description of the first news.',
    is_show: true,
  },
  {
    id: 2,
    date: '2024-10-11',
    title: 'Announcement Title 2',
    description: 'This is the description of the second news.',
    is_show: true,
  },
  {
    id: 3,
    date: '2024-10-10',
    title: 'Announcement Title 3',
    description: 'This is the description of the third news.',
    is_show: false,
  },
  {
    id: 4,
    date: '2024-10-09',
    title: 'Announcement Title 4',
    description: 'This is the description of the fourth news.',
    is_show: true,
  },
  {
    id: 5,
    date: '2024-10-08',
    title: 'Announcement Title 5',
    description: 'This is the description of the fifth news.',
    is_show: false,
  },
];

const AnnouncementPage: React.FC = () => {
  return (
    <GenericPage<AnnouncementProps>
      data={newsPropsData}
      itemTitle="Donate Announcement"
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

export default AnnouncementPage;
