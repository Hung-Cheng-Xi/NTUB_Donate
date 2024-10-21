import React from 'react';
import TableGeneric from '../components/common/generic/tableGeneric';
import { usePagination } from '../hooks/usePagination';


const DonationTable: React.FC = () => {
  const {
    itemsPerPage,
    currentPage,
    skip,
    limit,
    handlePageChange,
    handleSelect,
  } = usePagination();

  console.log(skip, limit);

  return (
    <TableGeneric
      data={{ total_count: 0, items: [] }}
      itemTitle="Donate List"
      formFields={[
        { name: 'createDate', label: 'Create Date', type: 'text' },
        { name: 'donateDate', label: 'Donate Date', type: 'text' },
        { name: 'idCard', label: 'ID Card', type: 'text' },
        { name: 'name', label: 'Name', type: 'text' },
        {
          name: 'category',
          label: 'Category',
          type: 'select',
          options: [
            {id: 1, name: 'Education'},
            {id: 2, name: 'Health'},
            {id: 3, name: 'Community Development'},
            {id: 4, name: 'Animal Welfare'},
            {id: 5, name: 'Environmental Conservation'},
          ],
        },
        { name: 'type', label: 'Type', type: 'text' },
        { name: 'amount', label: 'Amount', type: 'number' },
        { name: 'paymentCode', label: 'Payment Code', type: 'text' },
        { name: 'phoneNumber', label: 'Phone Number', type: 'number' },
        { name: 'email', label: 'Email', type: 'text' },
        { name: 'memo', label: 'Memo', type: 'textarea' },
      ]}
      itemsPerPage={itemsPerPage}
      currentPage={currentPage}
      onSelect={handlePageChange}
      onPageChange={handleSelect}
    />
  );
};

export default DonationTable;
