import React from 'react';
import styled from 'styled-components';
import CategorySelect from './categorySelect.component';
import { DonationCards } from '../cards/donationCards.component';

const SectionTitle = styled.h1`
  font-size: 48px;
  font-weight: bold;
  width: 193px;
  height: 68px;
  margin-top: 48px;
  margin-bottom: 32px;
`;

const DonateSection: React.FC = () => {
  return (
    <>
      {/* 標題 */}
      <SectionTitle id="donation-section">捐款項目</SectionTitle>

      {/* 下拉選單 */}
      <CategorySelect />

      {/* 捐款項目卡片區域 */}
      <DonationCards />
    </>
  );
};

export default DonateSection;
