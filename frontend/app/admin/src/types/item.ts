export interface ListItemType {
  id: number;
  date?: string;
  title: string;
  lump_sum?: number;
  memo?: string;
  description?: string;
  category?: string;
  description_link?: string;
}

export interface TableItemType {
  id: number;
  createDate: string;
  donateDate: string;
  idCard: string;
  name: string;
  category: string;
  type: string;
  amount: number;
  paymentCode: string;
  phoneNumber: string;
  email: string;
  memo: string;
}
