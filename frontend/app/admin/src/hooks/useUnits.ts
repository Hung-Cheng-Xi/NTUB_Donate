// useUnits.ts
import { useQuery, UseQueryResult } from '@tanstack/react-query';
import { getUnitsApiAdminUnitGet } from '../../../shared/openapi/services.gen';
import { GetUnitsApiAdminUnitGetResponse } from '../../../shared/openapi/types.gen';

export const useUnitsQuery = (): UseQueryResult<GetUnitsApiAdminUnitGetResponse, Error> => {
  return useQuery<GetUnitsApiAdminUnitGetResponse, Error>({
    queryKey: ['units'],
    queryFn: async () => {
      const response = await getUnitsApiAdminUnitGet();
      return response.data as GetUnitsApiAdminUnitGetResponse;
    },
  });
};
