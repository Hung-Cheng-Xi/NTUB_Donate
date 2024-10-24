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
  search,
  onSelect,
  onPageChange,
  onSearch,
}: Omit<BaseGenericProps<TableItemType>, 'ItemComponent'>) => {
  return (
    <BaseGeneric
      data={data}
      itemTitle={itemTitle}
      formFields={formFields}
      isReadOnly={true}
      itemsPerPage={itemsPerPage}
      currentPage={currentPage}
      search={search}
      onSelect={onSelect}
      onPageChange={onPageChange}
      onSearch={(onSearch)}
      ItemComponent={TableItem}
    />
  );
};

export default TableGeneric;
