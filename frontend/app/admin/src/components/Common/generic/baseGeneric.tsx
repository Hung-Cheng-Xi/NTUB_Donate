import { useState } from 'react';
import { SubmitHandler } from 'react-hook-form';
import Pagination from '../page/pagination';
import BaseFormModal from '../modal/baseModal';
import ItemsPerPage from '../page/itemsPer';

export interface BaseGenericProps<T> {
  data: T[];
  itemTitle: string;
  formFields: {
    name: string;
    label: string;
    type: string;
    options?: { id: string | number; name: string }[];
  }[];
  isReadOnly?: boolean;
  itemsPerPage: number;
  currentPage: number;
  onSelect: (value: number) => void;
  onPageChange: (value: number) => void;
  ItemComponent: React.ComponentType<{ data: T[]; openModal: (item: T) => void }>;
}

const BaseGeneric = <T,>({
  data,
  itemTitle,
  formFields,
  itemsPerPage,
  currentPage,
  isReadOnly,
  onSelect,
  onPageChange,
  ItemComponent,
}: BaseGenericProps<T>) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState<T | null>(null);

  const openModal = (item: T) => {
    setIsOpen(true);
    setSelectedItem(item);
    console.log(item);
  };

  const closeModal = () => {
    setIsOpen(false);
    setSelectedItem(null);
  };

  const onSubmit: SubmitHandler<{ [key: string]: string | number | boolean | { id: string | number } }> = (data) => {
    console.log(data);
    closeModal();
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
                      onSelect={onSelect}
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

            <ItemComponent data={data} openModal={openModal} />

            <div className="p-8">
              <Pagination
                currentPage={currentPage}
                onPageChange={onPageChange}
              />
            </div>
          </div>
        </div>
      </div>

      <BaseFormModal
        isOpen={isOpen}
        onClose={closeModal}
        onSubmit={onSubmit}
        fields={formFields ? formFields : []}
        defaultValues={selectedItem ? (selectedItem as { [key: string]: string | number | boolean }) : undefined}
        isReadOnly={isReadOnly ? isReadOnly : false}
      />
    </>
  );
};

export default BaseGeneric;
