import React from 'react';
import { NewsCard } from '../components/cards/newCard.component';
import FAQList from '../components/FQA/FQAList.component';
import InfoCard from '../components/cards/infoCard.component';
import DonateInfoBanner from '../components/donate/donateInfoBanner.component';
import DonateSection from '../components/donate/donateSection.component';
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
