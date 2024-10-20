import { UnitInfo } from "../../../shared/openapi/types.gen";

export interface ListItemType {
  id: number;
  date?: string;
  unit?: UnitInfo;
  title: string;
  lump_sum?: number;
  memo?: string;
  description?: string;
  category?: string;
  description_link?: string;
  is_show: boolean;
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
