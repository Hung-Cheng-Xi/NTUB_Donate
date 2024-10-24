import React, { useState } from 'react';
import { Donation } from '../../../../shared/openapi';
import { Button, CircularProgress } from '@mui/material';
import DonationDetailModal from './donationDetailModal.component';
import DonationTable from './donateHomeTable.component';
import { useDonations } from './donateHome.hook';
import { ColumnDef } from '@tanstack/react-table';

const DonationHome: React.FC = () => {
  const [pagination, setPagination] = React.useState({
    pageIndex: 0,
    pageSize: 10,
  });

  const { data, isPending, error } = useDonations({
    pageIndex: pagination.pageIndex,
    pageSize: pagination.pageSize,
  });

  const tableData = data?.items || [];
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedRow, setSelectedRow] = useState<Donation | null>(null);

  const columns: ColumnDef<Donation>[] = [
    { accessorKey: 'id', header: 'Id' },
    { accessorKey: 'username', header: '使用者名稱' },
    { accessorKey: 'user_birthday', header: '使用者生日' },
    { accessorKey: 'id_card', header: '身分證字號' },
    { accessorKey: 'phone_number', header: '電話號碼' },
    { accessorKey: 'email', header: 'Email' },
    { accessorKey: 'input_date', header: '捐款日期' },
    { accessorKey: 'amount', header: '捐款金額' },
    { accessorKey: 'account', header: '捐款帳號' },
    {
      id: 'detail',
      header: '操作',
      cell: ({ row }) => (
        <Button
          onClick={() => {
            setSelectedRow(row.original);
            setIsModalOpen(true);
          }}
          variant="text"
          color="primary"
        >
          詳細資料
        </Button>
      ),
    },
  ];

  const totalCount = data?.total_count || 0;

  const fieldLabels: { [key: string]: string } = {
    username: '使用者名稱',
    user_birthday: '使用者生日',
    id_card: '身分證字號',
    phone_number: '電話號碼',
    email: 'Email',
    input_date: '捐款日期',
    amount: '捐款金額',
    account: '捐款帳號',
    memo: '備註',
  };

  const handlePaginationChange = (newPagination: {
    pageIndex: number;
    pageSize: number;
  }) => {
    setPagination(newPagination);
  };

  return (
    <>
      {isPending ? (
        <div style={{ textAlign: 'center', marginTop: '20px' }}>
          <CircularProgress />
        </div>
      ) : error ? (
        <div>Error loading donations: {error.message}</div>
      ) : (
        <>
          <DonationTable
            data={tableData}
            columns={columns}
            pagination={pagination}
            totalCount={totalCount}
            onPaginationChange={handlePaginationChange}
            onRowClick={(row) => {
              setSelectedRow(row);
              setIsModalOpen(true);
            }}
          />

          <DonationDetailModal
            open={isModalOpen}
            onClose={() => setIsModalOpen(false)}
            selectedRow={selectedRow}
            fieldLabels={fieldLabels}
          />
        </>
      )}
    </>
  );
};

export default DonationHome;
