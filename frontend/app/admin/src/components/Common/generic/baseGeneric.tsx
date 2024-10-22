import { useState } from 'react';
import { SubmitHandler } from 'react-hook-form';
import Pagination from '../page/pagination';
import BaseFormModal from '../modal/baseModal';
import ItemsPerPage from '../page/itemsPer';
import { PaginatedResponse } from '../../../types/item';
import SearchInput from '../page/searchQuery';

export interface BaseGenericProps<T> {
  data: PaginatedResponse<T>;
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
  search: string;
  onSelect: (value: number) => void;
  onPageChange: (value: number) => void;
  onSearch: (value: string) => void;
  ItemComponent: React.ComponentType<{ data: T[]; openModal: (item: T) => void }>;
}

const BaseGeneric = <T,>({
  data,
  itemTitle,
  formFields,
  itemsPerPage,
  currentPage,
  search,
  isReadOnly,
  onSelect,
  onPageChange,
  onSearch,
  ItemComponent,
}: BaseGenericProps<T>) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState<T | null>(null);
  const totalPages = Math.ceil(data.total_count / itemsPerPage);

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

                <SearchInput
                  search={search}
                  onSearch={onSearch}
                />
              </div>
            </div>

            <ItemComponent data={data.items} openModal={openModal} />

            <div className="p-8">
              <Pagination
                totalItems={totalPages}
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
