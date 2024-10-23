import React from 'react';
import type { TableItemType } from '../../../types/item';

// TableItem Component
interface TableItemProps {
  data: TableItemType[];
  openUpdateModal: (item: TableItemType) => void;
  openDeleteModal: (item: TableItemType) => void;
}

const TableItem: React.FC<TableItemProps> = ({
  data,
  openUpdateModal,
  openDeleteModal,
}) => {
  return (
    <>
      <div className="shadow-md">
        <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
          <thead
            className="text-xs text-gray-700 uppercase bg-gray-50
           dark:bg-gray-700 dark:text-gray-400"
          >
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
                  <div>
                    <button
                      className="px-4 py-2 text-sm font-semibold
            text-white bg-blue-600 rounded-md hover:bg-blue-500
            focus:outline-none focus:ring-2 focus:ring-blue-400"
                      onClick={() => openUpdateModal(item)}
                    >
                      View
                    </button>
                    <button
                      className="px-4 py-2 ml-2 text-sm font-semibold
            text-white bg-red-600 rounded-md hover:bg-red-500
            focus:outline-none focus:ring-2 focus:ring-red-400"
                      onClick={() => openDeleteModal(item)}
                    >
                      Delete
                    </button>
                  </div>
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
