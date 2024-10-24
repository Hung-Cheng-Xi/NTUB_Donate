import React from 'react';
import type { ListItemType } from '../../../types/item';

interface ListItemProps {
  data: ListItemType[];
  openUpdateModal: (item: ListItemType) => void;
  openDeleteModal: (item: ListItemType) => void;
}

const ListItem: React.FC<ListItemProps> = ({
  data,
  openUpdateModal,
  openDeleteModal,
}) => (
  <ul>
    {data.map((item) => (
      <li
        key={item.id}
        className="p-4 mb-3 border rounded-md shadow-sm bg-gray-50"
      >
        <div className="flex justify-between items-center">
          <h3 className="text-xl font-semibold text-gray-800">
            {'category' in item ? item.category : item.title}
          </h3>
          <div>
            <button
              className="px-4 py-2 text-sm font-semibold
            text-white bg-blue-600 rounded-md hover:bg-blue-500
            focus:outline-none focus:ring-2 focus:ring-blue-400"
              onClick={() => openUpdateModal(item)}
            >
              Edit
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
        </div>
        <p className="mt-2 text-gray-600">
          {'description' in item ? item.description : item.description_link}
        </p>
      </li>
    ))}
  </ul>
);

export default ListItem;
