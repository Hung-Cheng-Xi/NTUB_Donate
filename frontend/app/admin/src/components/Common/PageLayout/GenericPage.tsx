import { useState } from 'react';
import { SubmitHandler } from 'react-hook-form';
import styled from 'styled-components';
import Pagination from '../pagination';
import FormModal from '../modal/modal';
import ListItem from './listItem';
import TableItem from './tableItem';
import { formatListItemType, formatTableItemType } from '../../../utils/format';
import { ListItemType, TableItemType } from '../../../types/ItemType';

const Container = styled.div`
  margin: 97.5px 97.5px 10.5px 97.5px;
  width: 1245px;
`;

interface GenericPageProps<T> {
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

const GenericPage = <T extends GenericItemType>({
  data,
  itemTitle,
  formFields,
  viewMode,
}: GenericPageProps<T>) => {
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

  return (
    <Container>
      <div className="flex flex-col items-center min-h-screen bg-gray-100 p-8 rounded">
        <div className="w-full max-w-4xl bg-white p-6 rounded-md shadow-md">
          <div className="flex justify-between mb-3">
            <h2 className="text-3xl font-bold text-gray-800">{itemTitle}</h2>
            <Pagination />
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
    </Container>
  );
};

export default GenericPage;
