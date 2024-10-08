import React from 'react';
import styled from 'styled-components';

interface NewsItem {
  date: string;
  title: string;
  description: string;
  imageUrl: string;
}

interface NewsSectionProps {
  item: NewsItem;
}

const NewsContainer = styled.div`
  margin-top: 24px;
  margin-left: 10px;
`;

const NewsTitle = styled.h3`
  font-size: 24px;
  font-weight: bold;
  margin-left: 8px;
  margin-bottom: 24px;
`;

const DetailsButton = styled.button`
  width: 125px;
  height: 40px;
  margin-left: 8px;
  margin-bottom: 31px;
  padding-left: 0.5rem;
  font-size: 20px;
  font-weight: 600;
  border-radius: 10px;
  display: flex;
  align-items: center;
  transition: background-color 0.3s, color 0.3s;

  &:hover {
    background-color: #1e3a8a; /* Tailwind button-darkblue equivalent */
    color: white;
  }

  svg {
    height: 1rem;
    width: 1rem;
    margin-left: 0.5rem;
  }
`;

const NewsSection: React.FC<NewsSectionProps> = ({ item }) => {
  return (
    <NewsContainer>
      <NewsTitle>{item.title}</NewsTitle>
      <DetailsButton>
        更多詳情
        <svg
          xmlns='http://www.w3.org/2000/svg'
          fill='none'
          viewBox='0 0 24 24'
          stroke='currentColor'
        >
          <path
            strokeLinecap='round'
            strokeLinejoin='round'
            strokeWidth='2'
            d='M9 5l7 7-7 7'
          />
        </svg>
      </DetailsButton>
    </NewsContainer>
  );
};

export default NewsSection;
