// Updated TableGeneric Component
import BaseGeneric from './baseGeneric';
import type {BaseGenericProps} from './baseGeneric';
import TableItem from '../page/tableItem';
import { TableItemType } from '../../../types/item';

const TableGeneric = ({
  data,
  itemTitle,
  formFields,
  itemsPerPage,
  currentPage,
  onSelect,
  onPageChange,
}: Omit<BaseGenericProps<TableItemType>, 'ItemComponent'>) => { // Omit 作用是排除 renderItems 屬性
  return (
    <BaseGeneric
      data={data}
      itemTitle={itemTitle}
      formFields={formFields}
      isReadOnly={true}
      itemsPerPage={itemsPerPage}
      currentPage={currentPage}
      onSelect={onSelect}
      onPageChange={onPageChange}
      ItemComponent={TableItem}
    />
  );
};

export default TableGeneric;
