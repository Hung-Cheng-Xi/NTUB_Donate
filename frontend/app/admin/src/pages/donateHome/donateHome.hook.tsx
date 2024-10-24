import { useQuery, keepPreviousData } from '@tanstack/react-query';
import { adminGetDonations, AdminGetDonationsResponse } from '../../../../shared/openapi';

interface UseDonationsParams {
  pageIndex: number;
  pageSize: number;
}

export const useDonations = ({ pageIndex, pageSize }: UseDonationsParams) => {
  return useQuery<AdminGetDonationsResponse, Error>({
    queryKey: ['adminGetDonations', pageIndex, pageSize],
    queryFn: async () => {
      const skip = pageIndex * pageSize;
      const limit = pageSize;
      const response = await adminGetDonations({
        query: {
          skip,
          limit,
        },
      });

      if (!response.data) {
        throw new Error('No data returned from adminGetDonations');
      }

      return response.data;
    },
    placeholderData: keepPreviousData,
  });
};
