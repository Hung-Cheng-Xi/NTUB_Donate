import React, { useEffect, useRef, useState } from 'react';
import styled, { css, keyframes } from 'styled-components';

// 上移文字的動畫效果
const moveUpAnimation = keyframes`
  from {
    transform: translateY(100px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
`;

interface DonationContainerProps {
  isFullWidth: boolean;
}

interface ContentWrapperProps {
  isTextVisible: boolean;
}

const DonationContainer = styled.div<DonationContainerProps>`
  width: ${({ isFullWidth }) => (isFullWidth ? '100%' : '1350px')};
  height: 762px;
  margin: 96px auto 0 auto;
  padding: 96px 48px;
  gap: 10px;
  border-radius: 40px;
  background-color: #f5f5f5; /* 原來的 bg-button-gray */
  transition:
    width 0.5s ease-in-out,
    padding-left 0.5s ease-in-out,
    padding-right 0.5s ease-in-out;

  display: flex;
  justify-content: center;
  align-items: center;

  ${({ isFullWidth }) =>
    isFullWidth &&
    css`
      padding-left: 0;
      padding-right: 0;
      border-radius: 0;
    `}
`;

const ContentWrapper = styled.div<ContentWrapperProps>`
  width: 1199px;
  height: 312px;
  opacity: ${({ isTextVisible }) => (isTextVisible ? 1 : 0)};
  transition: opacity 0.5s ease-in-out;

  ${({ isTextVisible }) =>
    isTextVisible &&
    css`
      animation: ${moveUpAnimation} 1s ease-in-out;
    `}
`;

const Heading = styled.h2`
  font-size: 52px;
  font-weight: bold;
  margin-bottom: 48px;
`;

const Paragraph = styled.p`
  font-size: 32px;
  line-height: 2rem;
  margin-bottom: 16px;
`;

const DonationInfo: React.FC = () => {
  const [isFullWidth, setIsFullWidth] = useState(false);
  const [isTextVisible, setIsTextVisible] = useState(false);
  const containerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setIsFullWidth(true);
            setIsTextVisible(true);
          }
        });
      },
      {
        threshold: 0.5, // 當元素進入 50% 可見區域時觸發
      },
    );

    const currentContainer = containerRef.current;
    if (currentContainer) {
      observer.observe(currentContainer);
    }

    return () => {
      if (currentContainer) {
        observer.unobserve(currentContainer);
      }
    };
  }, []);

  return (
    <DonationContainer ref={containerRef} isFullWidth={isFullWidth}>
      <ContentWrapper isTextVisible={isTextVisible}>
        <Heading>捐款支持北商的好處</Heading>
        <Paragraph>
          捐款支持北商大學不僅有助於培育未來的專業人才，還能提升學校的教學設備與資源，讓學生有更優質的學習環境。您的善款將用於資助學術研究、社會服務以及學生獎學金，造福更多學子。
        </Paragraph>
        <Paragraph>
          每一筆捐款都是對未來的投資，感謝您與我們一起攜手，共創美好明天。
        </Paragraph>
      </ContentWrapper>
    </DonationContainer>
  );
};

export default DonationInfo;
