import React, { useState } from 'react';
import styled from 'styled-components';

interface FAQItemProps {
  question: string;
  answer: string;
}

interface ButtonProps {
  isOpen: boolean;
}

interface AnswerContainerProps {
  isOpen: boolean;
}

const Button = styled.button<ButtonProps>`
  transform: ${({ isOpen }) => (isOpen ? 'rotate(0deg)' : 'rotate(-90deg)')};
  transition: transform 0.3s;
  color: white;
  background-color: black;
  border-radius: 9999px;
  padding: 0.5rem;
`;

const AnswerContainer = styled.div<AnswerContainerProps>`
  padding-left: 1.25rem;
  color: #4a5568;
  height: ${({ isOpen }) => (isOpen ? 'auto' : '0')};
  opacity: ${({ isOpen }) => (isOpen ? 1 : 0)};
  overflow: hidden;
  transition: height 0.5s ease-in-out, opacity 0.5s ease-in-out, padding-bottom 0.3s ease-in-out, margin-bottom 0.3s ease-in-out;
  padding-bottom: ${({ isOpen }) => (isOpen ? '1rem' : '0')};
  margin-bottom: ${({ isOpen }) => (isOpen ? '1rem' : '0')}; /* 確保下方有適當的空間 */
`;

const AnswerText = styled.p`
  font-size: 2rem;
  font-weight: bold;
`;

const FAQItemContainer = styled.div`
  width: 1245px;
  padding-top: 38px;
  padding-left: 20px;
  padding-right: 20px;
  gap: 12px;
`;

const QuestionContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1rem;
  padding-bottom: 12px;
  cursor: pointer;
  border-bottom: 1px solid #e2e8f0; /* Tailwind border color equivalent */
`;

const QuestionTitle = styled.h3`
  font-size: 40px;
  line-height: 1.25;
  letter-spacing: 0.1px;
  font-weight: bold;
`;

const FAQListContainer = styled.div`
  width: 1244px;
  padding: 40px 0;
  gap: 24px;
`;

const FAQTitle = styled.h2`
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 24px;
`;

const FAQItem: React.FC<FAQItemProps> = ({ question, answer }) => {
  const [isOpen, setIsOpen] = useState<boolean>(false);

  const toggleOpen = () => {
    setIsOpen(!isOpen);
  };

  return (
    <FAQItemContainer>
      {/* 問題區域 */}
      <QuestionContainer onClick={toggleOpen}>
        <QuestionTitle>{question}</QuestionTitle>
        <Button isOpen={isOpen}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fillRule="evenodd"
              d="M5.293 9.293a1 1 0 011.414 0L10 12.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clipRule="evenodd"
            />
          </svg>
        </Button>
      </QuestionContainer>

      {/* 答案區域 */}
      <AnswerContainer isOpen={isOpen}>
        <AnswerText>{answer}</AnswerText>
      </AnswerContainer>
    </FAQItemContainer>
  );
};

const FAQList: React.FC = () => {
  const faqs: FAQItemProps[] = [
    {
      question: '我可以設定每月自動捐款嗎？',
      answer: '不可以，您可以選擇設定定期捐款計畫，讓您的支持持續幫助學校發展。不可以，您可以選擇設定定期捐款計畫，讓您的支持持續幫助學校發展。',
    },
    {
      question: '我可以設定每月自動捐款嗎？',
      answer: '不可以，您可以選擇設定定期捐款計畫，讓您的支持持續幫助學校發展。',
    },
    {
      question: '我可以設定每月自動捐款嗎？',
      answer: '不可以，您可以選擇設定定期捐款計畫，讓您的支持持續幫助學校發展。',
    },
  ];

  return (
    <FAQListContainer>
      {/* 標題 */}
      <FAQTitle>常見問題</FAQTitle>

      {/* FAQ 列表 */}
      {faqs.map((faq, index) => (
        <FAQItem key={index} question={faq.question} answer={faq.answer} />
      ))}
    </FAQListContainer>
  );
};

export default FAQList;
