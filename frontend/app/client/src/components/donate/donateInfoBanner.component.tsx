import React from 'react';
import styled from 'styled-components';

const BannerContainer = styled.div`
  margin-bottom: 24px;
`;

const BannerTitle = styled.h1`
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 24px;
`;

const BannerContent = styled.div`
  background-color: #f5f5f5; /* 原來的 bg-button-gray */
  width: 1244px;
  height: 364px;
  padding: 1.5rem;
  border-radius: 40px;
  display: flex;
  align-items: center;
  gap: 52px;
`;

const ImageContainer = styled.div`
  flex-shrink: 0;

  img {
    width: 222.27px;
    height: 304px;
    margin: 30px 0 30px 58px;
    object-fit: contain;
  }
`;

const TextContent = styled.div`
  width: 693px;
  height: 229px;
`;

const TextTitle = styled.h2`
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 18px;
`;

const TextDescription = styled.p`
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 52px;
`;

const DetailsButton = styled.button`
  background-color: #1e3a8a; /* 原來的 bg-button-darkblue */
  color: white;
  font-size: 24px;
  width: 152px;
  height: 48px;
  gap: 4px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 8px;
`;

const DonateInfoBanner: React.FC = () => {
  return (
    <BannerContainer>
      <BannerTitle>捐款相關訊息</BannerTitle>

      <BannerContent>
        {/* 左側圖片 */}
        <ImageContainer>
          <img
            src='https://sec.ntub.edu.tw/var/file/3/1003/img/850587955.png' // 替換為實際圖片路徑
            alt='Donation Info'
          />
        </ImageContainer>

        {/* 右側文字內容 */}
        <TextContent>
          <TextTitle>捐款政策與保障</TextTitle>
          <TextDescription>
            我們致力於保障您的隱私，提供透明的捐款用途，並依照法律規處理捐款退款與稅務扣除。點擊查看完整政策說明。
          </TextDescription>
          <DetailsButton>
            <span>更多詳情</span>
            {/* 這裡使用 SVG 來表示箭頭 */}
            <svg
              xmlns='http://www.w3.org/2000/svg'
              className='h-5 w-5'
              viewBox='0 0 20 20'
              fill='currentColor'
            >
              <path
                fillRule='evenodd'
                d='M10.293 15.293a1 1 0 010-1.414L13.586 10l-3.293-3.293a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z'
                clipRule='evenodd'
              />
            </svg>
          </DetailsButton>
        </TextContent>
      </BannerContent>
    </BannerContainer>
  );
};

export default DonateInfoBanner;
