import { ListItemType, TableItemType } from '../types/item';

// Formatting functions for TableItemType
export const formatListItemType = (
  item: ListItemType,
): { [key: string]: string } => ({
  id: String(item.id),
  date: item.date || '',
  title: item.title,
  lump_sum: String(item.lump_sum || 0),
  memo: item.memo || '',
  description: item.description || '',
  category: item.category || '',
  description_link: item.description_link || '',
});

// Formatting functions for TableItemType
export const formatTableItemType = (
  item: TableItemType,
): { [key: string]: string } => ({
  id: String(item.id),
  createDate: item.createDate,
  donateDate: item.donateDate,
  idCard: item.idCard,
  name: item.name,
  category: item.category,
  type: item.type,
  amount: String(item.amount),
  paymentCode: item.paymentCode,
  phoneNumber: item.phoneNumber,
  email: item.email,
  memo: item.memo,
});
