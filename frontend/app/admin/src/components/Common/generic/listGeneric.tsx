// Updated ListItem Component
import BaseGeneric from './baseGeneric';
import type {BaseGenericProps} from './baseGeneric';
import ListItem from '../page/listItem';
import { ListItemType } from '../../../types/item';

const ListGeneric = ({
  data,
  itemTitle,
  formFields,
  itemsPerPage,
  currentPage,
  search,
  onSelect,
  onPageChange,
  onSearch,
}: Omit<BaseGenericProps<ListItemType>, 'ItemComponent'>) => {
  return (
    <BaseGeneric
      data={data}
      itemTitle={itemTitle}
      formFields={formFields}
      itemsPerPage={itemsPerPage}
      currentPage={currentPage}
      search={search}
      onSelect={onSelect}
      onPageChange={onPageChange}
      onSearch={onSearch}
      ItemComponent={ListItem}
    />
  );
};

export default ListGeneric;
