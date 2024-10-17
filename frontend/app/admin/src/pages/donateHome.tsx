import React from 'react';
import Generic from '../components/common/page/generic';

interface DonationPurpose {
  id: number;
  createDate: string;
  donateDate: string;
  idCard: string;
  name: string;
  category: string;
  type: string;
  amount: number;
  paymentCode: string;
  phoneNumber: string;
  email: string;
  memo: string;
}

const donatePurposeData: DonationPurpose[] = [
  {
    id: 1,
    createDate: '1061013',
    donateDate: '1061015',
    idCard: 'A123456789',
    name: 'John Doe',
    category: 'Education',
    type: 'One-Time',
    amount: 1000,
    paymentCode: 'PAY123456',
    phoneNumber: '0987654321',
    email: 'johndoe@example.com',
    memo: 'For school supplies',
  },
  {
    id: 2,
    createDate: '1061013',
    donateDate: '1061015',
    idCard: 'B234567890',
    name: 'Jane Smith',
    category: 'Health',
    type: 'Monthly',
    amount: 500,
    paymentCode: 'PAY234567',
    phoneNumber: '0987654322',
    email: 'janesmith@example.com',
    memo: 'For medical support',
  },
  {
    id: 3,
    createDate: '1061013',
    donateDate: '1061015',
    idCard: 'C345678901',
    name: 'Alice Johnson',
    category: 'Animal Welfare',
    type: 'One-Time',
    amount: 300,
    paymentCode: 'PAY345678',
    phoneNumber: '0987654323',
    email: 'alicejohnson@example.com',
    memo: 'For animal shelter',
  },
  {
    id: 4,
    createDate: '1061013',
    donateDate: '1061015',
    idCard: 'D456789012',
    name: 'Bob Brown',
    category: 'Environment',
    type: 'One-Time',
    amount: 700,
    paymentCode: 'PAY456789',
    phoneNumber: '0987654324',
    email: 'bobbrown@example.com',
    memo: 'For tree planting',
  },
  {
    id: 5,
    createDate: '1061013',
    donateDate: '1061015',
    idCard: 'E567890123',
    name: 'Charlie Davis',
    category: 'Arts',
    type: 'Monthly',
    amount: 200,
    paymentCode: 'PAY567890',
    phoneNumber: '0987654325',
    email: 'charliedavis@example.com',
    memo: 'For art supplies',
  },
];

const DonationTable: React.FC = () => {
  return (
    <Generic<DonationPurpose>
      data={donatePurposeData}
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
            'Education',
            'Health',
            'Community Development',
            'Animal Welfare',
            'Environmental Conservation',
          ],
        },
        { name: 'type', label: 'Type', type: 'text' },
        { name: 'amount', label: 'Amount', type: 'number' },
        { name: 'paymentCode', label: 'Payment Code', type: 'text' },
        { name: 'phoneNumber', label: 'Phone Number', type: 'number' },
        { name: 'email', label: 'Email', type: 'text' },
        { name: 'memo', label: 'Memo', type: 'textarea' },
      ]}
      viewMode="table"
    />
  );
};

export default DonationTable;
