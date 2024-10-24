import React from 'react';
import styled from 'styled-components';

const DonateButton = styled.button`
  font-size: 32px;
  font-weight: bold;
  color: black;
  background-color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 246px;
  height: 76px;
  border-radius: 20px;
`;

const HeroSectionContainer = styled.div`
  background-size: cover;
  background-position: center;
  margin-top: 268px;
`;

const HeroContent = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
`;

const HeroTitle = styled.h2`
  font-size: 40px;
  font-weight: bold;
  color: white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
`;

const HeroSection: React.FC = () => {
  const handleDonateClick = () => {
    const donationSection = document.getElementById('donation-section');
    if (donationSection) {
      donationSection.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <HeroSectionContainer>
      <HeroContent>
        <HeroTitle>攜手北商</HeroTitle>
        <HeroTitle>共創教育未來</HeroTitle>
        <DonateButton onClick={handleDonateClick}>捐款</DonateButton>
      </HeroContent>
    </HeroSectionContainer>
  );
};

export default HeroSection;
