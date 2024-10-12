import React, { useState } from 'react';
import { SubmitHandler } from 'react-hook-form';
import styled from 'styled-components';
import Pagination from '../components/Common/Pagination';
import FormModal from '../components/Common/Modal/Modal';

interface NewsItem {
  id: number;
  date: string;
  title: string;
  description: string;
  is_show: boolean;
}

const newsData: NewsItem[] = [
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

const Container = styled.div`
  margin: 97.5px 97.5px 10.5px 97.5px;
  width: 1245px;
`;

const NewsPage: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedNews, setSelectedNews] = useState<NewsItem | null>(null);

  const openModal = (news: NewsItem) => {
    setSelectedNews(news);
    setIsOpen(true);
  };

  const closeModal = () => {
    setIsOpen(false);
    setSelectedNews(null);
  };

  const onSubmit: SubmitHandler<Record<string, string>> = (data) => {
    console.log(data);
    closeModal();
  };

  return (
    <Container>
      <div className="flex flex-col items-center min-h-screen bg-gray-100 p-8 rounded">
        <div className="w-full max-w-4xl bg-white p-6 rounded-md shadow-md">
          <div className="flex justify-between mb-3">
            <h2 className="text-3xl font-bold text-gray-800">Latest News</h2>
            <Pagination />
          </div>
          <ul className="space-y-4">
            {newsData.map((news) => (
              <li
                key={news.id}
                className="p-4 border rounded-md shadow-sm bg-gray-50"
              >
                <div className="flex justify-between items-center">
                  <h3 className="text-xl font-semibold text-gray-800">
                    {news.title}
                  </h3>
                  <button
                    className="px-4 py-2 text-sm font-semibold text-white bg-blue-600 rounded-md hover:bg-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-400"
                    onClick={() => openModal(news)}
                  >
                    Edit
                  </button>
                </div>
                <p className="mt-2 text-gray-600">{news.description}</p>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <FormModal
        isOpen={isOpen}
        onClose={closeModal}
        onSubmit={onSubmit}
        fields={
          selectedNews
            ? [
                { name: 'date', label: 'Date', type: 'date' },
                { name: 'title', label: 'Title', type: 'text' },
                { name: 'description', label: 'Description', type: 'text' },
                { name: 'is_show', label: 'Show', type: 'checkbox' },
              ]
            : []
        }
      />
    </Container>
  );
};

export default NewsPage;
