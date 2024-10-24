import { useState } from 'react';
import Pagination from '../page/pagination';
import ItemsPerPage from '../page/itemsPer';
import { PaginatedResponse } from '../../../types/item';
import { UpdateModal, CreateModal } from '../modal/';
import SearchInput from '../page/searchQuery';
import { DeleteModal } from '../modal/deleteModal';

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
  ItemComponent: React.ComponentType<{
    data: T[];
    openUpdateModal: (item: T) => void;
    openDeleteModal: (item: T) => void;
  }>;
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
  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
  const [isUpdateModalOpen, setIsUpdateModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState<T | null>(null);
  const totalPages = Math.ceil(data.total_count / itemsPerPage);

  const handleOpenCreateModal = () => setIsCreateModalOpen(true);
  const handleOpenUpdateModal = (item: T) => {
    setSelectedItem(item);
    setIsUpdateModalOpen(true);
  };
  const handleOpenDeleteModal = (item: T) => {
    setSelectedItem(item);
    setIsDeleteModalOpen(true);
  };

  const handleCloseCreateModal = () => setIsCreateModalOpen(false);
  const handleCloseUpdateModal = () => setIsUpdateModalOpen(false);
  const handleCloseDeleteModal = () => setIsDeleteModalOpen(false);

  const handleCreateSubmit = (data: {
    [key: string]: string | number | boolean | { id: string | number };
  }) => {
    console.log('Creating item:', data);
    handleCloseCreateModal();
  };

  const handleUpdateSubmit = (data: {
    [key: string]: string | number | boolean | { id: string | number };
  }) => {
    console.log('Updating item:', data);
    handleCloseUpdateModal();
  };

  const handleDeleteSubmit = (data: {
    [key: string]: string | number | boolean | { id: string | number };
  }) => {
    console.log('Deleting item:', data);
    handleCloseDeleteModal();
  };

  return (
    <>
      <div className="flex flex-col items-center min-h-screen w-full p-8 rounded">
        <div className="w-full bg-white p-6 rounded-md shadow-md">
          <div className="flex justify-between mb-3">
            <h2 className="text-3xl font-bold text-gray-800">{itemTitle}</h2>
            <button
              className="px-4 py-2 text-sm font-semibold text-white bg-green-600 rounded-md hover:bg-green-500 focus:outline-none focus:ring-2 focus:ring-green-400"
              onClick={handleOpenCreateModal}
            >
              Create New Item
            </button>
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

                <SearchInput search={search} onSearch={onSearch} />
              </div>
            </div>

            <ItemComponent
              data={data.items}
              openUpdateModal={handleOpenUpdateModal}
              openDeleteModal={handleOpenDeleteModal}
            />

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

      <CreateModal
        isOpen={isCreateModalOpen}
        onClose={handleCloseCreateModal}
        onSubmit={handleCreateSubmit}
        fields={formFields ? formFields : []}
      />

      {isUpdateModalOpen && selectedItem && (
        <UpdateModal
          isOpen={isUpdateModalOpen}
          onClose={handleCloseUpdateModal}
          onSubmit={handleUpdateSubmit}
          fields={formFields ? formFields : []}
          defaultValues={selectedItem}
          isReadOnly={isReadOnly ? isReadOnly : false}
        />
      )}

      {isDeleteModalOpen && selectedItem && (
        <DeleteModal
          isOpen={isDeleteModalOpen}
          onClose={handleCloseDeleteModal}
          onSubmit={handleDeleteSubmit}
          defaultValues={selectedItem}
        />
      )}
    </>
  );
};

export default BaseGeneric;
