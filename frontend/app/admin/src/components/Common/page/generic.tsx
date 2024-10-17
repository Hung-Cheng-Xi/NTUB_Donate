import { useState } from 'react';
import { SubmitHandler } from 'react-hook-form';
import Pagination from '../pagination';
import FormModal from '../modal/modal';
import ListItem from './listItem';
import TableItem from './tableItem';
import { formatListItemType, formatTableItemType } from '../../../utils/format';
import { ListItemType, TableItemType } from '../../../types/item';
import ItemsPerPage from './itemsPer';

interface GenericProps<T> {
  data: T[];
  itemTitle: string;
  formFields: {
    name: string;
    label: string;
    type: string;
    options?: string[];
  }[];
  viewMode: 'list' | 'table';
}

type GenericItemType = ListItemType | TableItemType;

const Generic = <T extends GenericItemType>({
  data,
  itemTitle,
  formFields,
  viewMode,
}: GenericProps<T>) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState<T | null>(null);

  const openModal = (item: T) => {
    setIsOpen(true);
    setSelectedItem(item);
  };

  const closeModal = () => {
    setIsOpen(false);
    setSelectedItem(null);
  };

  const onSubmit: SubmitHandler<Record<string, string>> = (data) => {
    console.log(data);
    closeModal();
  };

  const [currentPage, setCurrentPage] = useState(1);
  const totalPages = 5;

  const handlePageChange = (page: number) => {
    setCurrentPage(page);
  };

  const [itemsPerPage, setItemsPerPage] = useState<number>(10);

  const handleSelect = (value: number) => {
    setItemsPerPage(value);
    console.log(`Selected ${value} items per page`);
    // 這裡可以根據選擇的數量更新資料顯示邏輯
  };

  return (
    <>
      <div className="flex flex-col items-center min-h-screen w-full p-8 rounded">
        <div className="w-full bg-white p-6 rounded-md shadow-md">
          <div className="flex justify-between mb-3">
            <h2 className="text-3xl font-bold text-gray-800">{itemTitle}</h2>
          </div>

          <div className="relative overflow-x-auto sm:rounded-lg">
            <div className="pb-4 bg-white dark:bg-gray-900">
              <div className="flex justify-between my-1">
                <div className="relative">
                  <div className="absolute inset-y-0 start-0">
                    <ItemsPerPage
                      selectedValue={itemsPerPage}
                      onSelect={handleSelect}
                    />
                  </div>
                </div>

                <div className="relative">
                  <div
                    className="absolute inset-y-0 start-0 flex items-center ps-3
                  pointer-events-none"
                  >
                    <svg
                      className="w-4 h-4 text-gray-500 dark:text-gray-400"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 20 20"
                    >
                      <path
                        stroke="currentColor"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                      />
                    </svg>
                  </div>
                  <input
                    type="text"
                    className="block py-2 ps-10 text-sm text-gray-900
                    border border-gray-300 rounded-lg w-80 bg-gray-50
                    focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700
                    dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
                    placeholder="Search for items"
                  />
                </div>
              </div>
            </div>

            {viewMode === 'list' ? (
              <ul className="space-y-4">
                <ListItem
                  item={data as ListItemType[]}
                  openModal={(item) => openModal(item as T)}
                />
              </ul>
            ) : (
              <TableItem
                data={data as TableItemType[]}
                openModal={(item) => openModal(item as T)}
              />
            )}

            <div className="p-8">
              <Pagination
                currentPage={currentPage}
                totalPages={totalPages}
                onPageChange={handlePageChange}
              />
            </div>
          </div>
        </div>
      </div>

      <FormModal
        isOpen={isOpen}
        onClose={closeModal}
        onSubmit={onSubmit}
        fields={selectedItem ? formFields : []}
        viewMode={viewMode}
        defaultValues={
          selectedItem
            ? viewMode === 'list'
              ? formatListItemType(selectedItem as ListItemType)
              : formatTableItemType(selectedItem as TableItemType)
            : undefined
        }
      />
    </>
  );
};

export default Generic;
