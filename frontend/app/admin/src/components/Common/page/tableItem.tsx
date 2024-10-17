import React from 'react';
import type { TableItemType } from '../../../types/item';

// TableItem Component
interface TableItemProps {
  data: TableItemType[];
  openModal: (item: TableItemType) => void;
}

const TableItem: React.FC<TableItemProps> = ({ data, openModal }) => {
  return (
    <>
      <div className="shadow-md">
        <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50
           dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th className="px-6 py-3">Name</th>
              <th className="px-6 py-3">Create Date</th>
              <th className="px-6 py-3">Donate Date</th>
              <th className="px-6 py-3">Category</th>
              <th className="px-6 py-3">Amount</th>
              <th className="px-6 py-3">Payment Code</th>
              <th className="px-6 py-3">Actions</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item) => (
              <tr
                key={item.id}
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700
                 hover:bg-gray-50 dark:hover:bg-gray-600"
              >
                <th className="px-6 py-4 font-medium text-gray-900 dark:text-white">
                  {item.name}
                </th>
                <td className="px-6 py-4">{item.createDate}</td>
                <td className="px-6 py-4">{item.donateDate}</td>
                <td className="px-6 py-4">
                  {'category' in item ? item.category : 'N/A'}
                </td>
                <td className="px-6 py-4">{item.amount}</td>
                <td className="px-6 py-4">{item.paymentCode}</td>
                <td className="px-6 py-4">
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
      </div>
    </>
  );
};

export default TableItem;
