import React from 'react';
import { NewsCard } from '../components/Cards/NewsCard';
import FAQList from '../components/FQA/FQAList';
import InfoCard from '../components/Cards/InfoCard';
import DonateInfoBanner from '../components/Donate/DonateInfoBanner';
import DonateSection from '../components/Donate/DonateSection';
import styled from 'styled-components';

const Container = styled.div`
  margin-left: 97.5px;
  margin-right: 97.5px;
  width: 1245px;
`;

const DonatePage: React.FC = () => {
  return (
    <>
      <Container>
        {/* 標題 */}
        <DonateSection />

        {/* 捐款相關訊息 */}
        <DonateInfoBanner />

        {/* 最新消息 */}
        <NewsCard />
      </Container>
      {/* 捐款相關訊息 */}
      <InfoCard />

      {/* 常見問題 */}
      <Container>
        <FAQList />
      </Container>
    </>
  );
};

export default DonatePage;
