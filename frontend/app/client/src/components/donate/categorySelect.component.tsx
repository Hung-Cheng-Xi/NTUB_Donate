import React, { useState } from 'react';
import styled from 'styled-components';
import Pagination from '../common/pagination.component';

interface CategorySelectBoxProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
}

const CategoryContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 12px;
`;

const CategorySelectBox = styled.select<CategorySelectBoxProps>`
  padding-left: 10px;
  padding-right: 10px;
  font-size: 32px;
  font-weight: bold;
  width: 361px;
  height: 62px;
  border: 1px solid #000; /* Customize the border color if needed */
  border-radius: 100px;
`;

const CategorySelect: React.FC = () => {
  const categories: string[] = ['資管系', '商學院', '法學院']; // 模擬選單項目
  const [selectedCategory, setSelectedCategory] = useState<string>('資管系');

  return (
    <CategoryContainer>
      <CategorySelectBox
        value={selectedCategory}
        onChange={(e: React.ChangeEvent<HTMLSelectElement>) => setSelectedCategory(e.target.value)}
      >
        {categories.map((category) => (
          <option key={category} value={category}>
            {category}
          </option>
        ))}
      </CategorySelectBox>

      {/* 分頁 */}
      <Pagination />
    </CategoryContainer>
  );
};

export default CategorySelect;
