import React from 'react';
import { AnnouncementCard } from '../components/cards/announcementCard';
import FAQList from '../components/FQA/FQAList';
import styled from 'styled-components';
import InfoCard from '../components/cards/infoCard';
import DonateSection from '../components/donate/donateSection';
import DonateInfoBanner from '../components/donate/donateInfoBanner';

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
        <AnnouncementCard />
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
