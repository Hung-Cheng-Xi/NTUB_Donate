import React, { useMemo } from 'react';
import Generic from '../components/common/page/generic';
import LoadingErrorHandler from '../components/common/page/LoadingErrorHandler';
import { usePagination } from '../hooks/usePagination';
import { useQuery } from '@tanstack/react-query';
import {
  getAnnouncementsApiAdminAnnouncementGet,
} from '../../../shared/openapi/services.gen';
import {
  AnnouncementInfo,
  GetAnnouncementsApiAdminAnnouncementGetResponse,
} from '../../../shared/openapi/types.gen';
import  { useUnitsQuery } from '../hooks/useUnits';

const AnnouncementPage: React.FC = () => {
  const { itemsPerPage, currentPage, skip, limit, handlePageChange, handleSelect } = usePagination();

  // 使用 useUnits Hook 獲取 unit 資料
  const { data: isUnitsData, isLoading: isUnitsLoading, isError: isUnitsError } = useUnitsQuery();

  // 使用 React Query 來處理資料獲取
  const { data: isAnnouncementsData, isLoading: isAnnouncementsLoading, isError: isAnnouncementsError } = useQuery<
    GetAnnouncementsApiAdminAnnouncementGetResponse,
    Error
  >({
    queryKey: ['announcements', skip, limit],
    queryFn: async () => {
      const response = await getAnnouncementsApiAdminAnnouncementGet({query: {skip, limit}});
      return response.data as GetAnnouncementsApiAdminAnnouncementGetResponse;
    },
  });

  // 提取單位選項（去重處理）
  const unitOptions = useMemo(() => {
    if (!isUnitsData) return [];
    const units = isUnitsData.map((item) => item.name).filter(Boolean);
    return Array.from(new Set(units)); // 去重並轉換為陣列
  }, [isUnitsData]);

  return (
    <LoadingErrorHandler
    isLoading={isUnitsLoading || isAnnouncementsLoading}
    isError={isUnitsError || isAnnouncementsError}>

    <Generic<AnnouncementInfo>
      data={isAnnouncementsData ?? []}
      itemTitle="Donate Announcement"
      formFields={[
        { name: 'date', label: 'Date', type: 'date' },
        { name: 'title', label: 'Title', type: 'text' },
        {
          name: 'unit',
          label: 'Unit',
          type: 'select',
          options: unitOptions,
        },
        { name: 'description', label: 'Description', type: 'textarea' },
        { name: 'is_show', label: 'Show', type: 'checkbox' },
      ]}
      viewMode="list" // Add viewMode property to determine if list or table should be used
      itemsPerPage={itemsPerPage}
      currentPage={currentPage}
      onSelect={handleSelect}
      onPageChange={handlePageChange}
    />
    </LoadingErrorHandler>
  );
};

export default AnnouncementPage;
