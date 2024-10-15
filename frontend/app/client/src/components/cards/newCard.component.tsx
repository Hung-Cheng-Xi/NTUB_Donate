import React from 'react';
import styled from 'styled-components';
import NewsSection from '../new/newsSection.component';

interface DonationItem {
  date: string;
  title: string;
  description: string;
  imageUrl: string;
}

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: 1fr;
  gap: 22px;

  @media (min-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(3, 1fr);
  }
`;

const Card = styled.div`
  background-color: #f5f5f5; /* 原來的 bg-button-gray */
  border-radius: 40px;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  width: 400px;
  margin-top: 10px;
  margin-bottom: 48px;
`;

const ImageContainer = styled.div`
  position: relative;

  img {
    width: 400px;
    height: 237px;
    object-fit: cover;
  }
`;

const DateLabel = styled.div`
  position: absolute;
  top: 15px;
  left: 23px;
  background-color: #1e3a8a; /* 原來的 bg-button-darkblue */
  width: 100px;
  height: 40px;
  color: white;
  font-size: 24px;
  padding: 2px 20px;
  border-radius: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export const NewsCard: React.FC = () => {
  const donationItems: DonationItem[] = [
    {
      date: '10/20',
      title: '捐款項目抓拉抓拉抓拉-活動',
      description: '這是捐款活動的描述文字。',
      imageUrl: 'https://via.placeholder.com/400x237',
    },
    {
      date: '10/20',
      title: '捐款項目抓拉抓拉抓拉-活動',
      description: '這是捐款活動的描述文字。',
      imageUrl: 'https://via.placeholder.com/400x237',
    },
    {
      date: '10/20',
      title: '捐款項目抓拉抓拉抓拉-活動',
      description: '這是捐款活動的描述文字。',
      imageUrl: 'https://via.placeholder.com/400x237',
    },
  ];

  return (
    <GridContainer>
      {donationItems.map((item, index) => (
        <Card key={index}>
          {/* 圖片區域 */}
          <ImageContainer>
            <img src={item.imageUrl} alt={item.title} />
            <DateLabel>{item.date}</DateLabel>
          </ImageContainer>

          {/* 內容區域 */}
          <NewsSection item={item} />
        </Card>
      ))}
    </GridContainer>
  );
};
