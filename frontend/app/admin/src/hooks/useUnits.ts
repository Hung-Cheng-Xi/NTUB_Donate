// useUnits.ts
import { useQuery, UseQueryResult } from '@tanstack/react-query';
import { adminGetUnits } from '../../../shared/openapi/services.gen';
import { AdminGetUnitsResponse } from '../../../shared/openapi/types.gen';

export const useUnitsQuery = (): UseQueryResult<AdminGetUnitsResponse, Error> => {
  return useQuery<AdminGetUnitsResponse, Error>({
    queryKey: ['units'],
    queryFn: async () => {
      const response = await adminGetUnits();
      return response.data as AdminGetUnitsResponse;
    },
  });
};
