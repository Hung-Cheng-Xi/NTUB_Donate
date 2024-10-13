import React from 'react';
import type { TableItemType } from '../../../types/ItemType';

// TableItem Component
interface TableItemProps {
  data: TableItemType[];
  openModal: (item: TableItemType) => void;
}

const TableItem: React.FC<TableItemProps> = ({ data, openModal }) => (
  <table className="min-w-full bg-white border border-gray-200">
    <thead>
      <tr className="bg-blue-600 text-white">
        <th className="py-2 px-4 border">ID</th>
        <th className="py-2 px-4 border">Create Date</th>
        <th className="py-2 px-4 border">Donate Date</th>
        <th className="py-2 px-4 border">Title</th>
        <th className="py-2 px-4 border">Category</th>
        <th className="py-2 px-4 border">Amount</th>
        <th className="py-2 px-4 border">Payment Code</th>
        <th className="py-2 px-4 border">Actions</th>
      </tr>
    </thead>
    <tbody>
      {data.map((item) => (
        <tr key={item.id} className="odd:bg-white even:bg-gray-100">
          <td className="py-2 px-4 border text-center">{item.id}</td>
          <td className="py-2 px-4 border text-center">{item.createDate}</td>
          <td className="py-2 px-4 border text-center">{item.donateDate}</td>
          <td className="py-2 px-4 border text-center">{item.name}</td>
          <td className="py-2 px-4 border text-center">
            {'category' in item ? item.category : 'N/A'}
          </td>
          <td className="py-2 px-4 border text-center">{item.amount}</td>
          <td className="py-2 px-4 border text-center">{item.paymentCode}</td>
          <td className="py-2 px-4 border text-center">
            <button
              className="bg-blue-500 text-white py-1 px-2 rounded hover:bg-blue-700"
              onClick={() => openModal(item)}
            >
              View
            </button>
          </td>
        </tr>
      ))}
    </tbody>
  </table>
);

export default TableItem;
