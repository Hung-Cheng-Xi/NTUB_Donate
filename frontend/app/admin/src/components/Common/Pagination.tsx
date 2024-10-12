import React from 'react';
import styled from 'styled-components';

interface PaginationButtonProps {
  onClick?: () => void;
}

const PaginationContainer = styled.div`
  display: flex;
  justify-content: flex-end;
  gap: 12px;
`;

const PaginationButton = styled.button<PaginationButtonProps>`
  font-size: 42px;
  width: 45px;
  height: 45px;
  border-radius: 100px;
  border: 1px solid #000; /* You can customize the border color */
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Pagination: React.FC = () => {
  return (
    <PaginationContainer>
      <PaginationButton>
        <span>&#8592;</span> {/* 左箭頭 */}
      </PaginationButton>
      <PaginationButton>
        <span>&#8594;</span> {/* 右箭頭 */}
      </PaginationButton>
    </PaginationContainer>
  );
};

export default Pagination;
