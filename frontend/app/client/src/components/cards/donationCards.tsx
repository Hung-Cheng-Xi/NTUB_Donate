import styled from 'styled-components';
import React from 'react';

interface DonationItem {
  id: number;
  title: string;
  amount: string;
  progress: number;
}

interface CardProps {
  primary?: boolean;
}

interface ProgressBarProps {
  progress: number;
}

const CardWrapper = styled.div`
  width: 1244px;
  height: 760px;
  padding: 10px;
  gap: 22px;
  margin-bottom: 48px;
`;

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;

  @media (min-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(3, 1fr);
  }
`;

const Card = styled.div<CardProps>`
  background-color: white;
  border-radius: 40px;
  display: flex;
  flex-direction: column;
  padding: 10px 8px;
  gap: 8px;
  transition: background-color 0.3s;

  &:hover {
    background-color: #f0f0f0; // Use hover color for button-gray equivalent
  }

  ${(props) =>
    props.primary
      ? `
          grid-row: span 2;
          width: 400px;
          height: 740px;
        `
      : `
          width: 400px;
          height: 360px;
        `}
`;

const ImageContainer = styled.div`
  flex-grow: 1;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 40px;
  }
`;

const Content = styled.div`
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
`;

const Title = styled.h2`
  font-size: 1.25rem;
  font-weight: bold;
`;

const ProgressBarContainer = styled.div`
  margin-top: 0.5rem;
  background-color: #d1d5db; // Tailwind gray-300 equivalent
  height: 0.75rem;
  border-radius: 9999px;
`;

const ProgressBar = styled.div<ProgressBarProps>`
  background-color: #3b82f6; // Tailwind blue-500 equivalent
  height: 100%;
  border-radius: 9999px;
  width: ${(props) => props.progress}%;
`;

const Amount = styled.p`
  margin-top: 0.5rem;
  font-size: 1.125rem;
  font-weight: bold;
  color: #1f2937; // Tailwind gray-800 equivalent
`;

export const DonationCards: React.FC = () => {
  // 模擬捐款項目資料
  const donationItems: DonationItem[] = [
    { id: 1, title: '捐款項目 1', amount: '100,000,0000 元', progress: 50 },
    { id: 2, title: '捐款項目 2', amount: '100,000,0000 元', progress: 60 },
    { id: 3, title: '捐款項目 3', amount: '100,000,0000 元', progress: 40 },
    { id: 4, title: '捐款項目 4', amount: '100,000,0000 元', progress: 75 },
    { id: 5, title: '捐款項目 5', amount: '100,000,0000 元', progress: 75 },
  ];

  return (
    <CardWrapper>
      {/* 網格布局 */}
      <GridContainer>
        {donationItems.map((item, index) => (
          <Card key={item.id} primary={index === 0}>
            {/* 圖片 */}
            <ImageContainer>
              <img
                src={
                  index === 0
                    ? 'https://via.placeholder.com/384x598'
                    : 'https://via.placeholder.com/384x220'
                }
                alt={item.title}
              />
            </ImageContainer>

            {/* 內容區域 */}
            <Content>
              {/* 標題 */}
              <Title>{item.title}</Title>

              {/* 進度條 */}
              <ProgressBarContainer>
                <ProgressBar progress={item.progress} />
              </ProgressBarContainer>

              {/* 金額 */}
              <Amount>
                （元）{item.amount}
              </Amount>
            </Content>
          </Card>
        ))}
      </GridContainer>
    </CardWrapper>
  );
};
