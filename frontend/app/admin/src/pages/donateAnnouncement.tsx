import React, { useState } from 'react';
import LoadingErrorHandler from '../components/common/api/loadingErrorHandler';
import { usePagination } from '../hooks/usePagination';
import { useQuery } from '@tanstack/react-query';
import { getAnnouncementsApiAdminAnnouncementGet } from '../../../shared/openapi/services.gen';
import {
  GetAnnouncementsApiAdminAnnouncementGetResponse,
} from '../../../shared/openapi/types.gen';
import { useUnitsQuery } from '../hooks/useUnits';
import ListGeneric from '../components/common/generic/listGeneric';

// TODO: 添加上傳 image 功能
const AnnouncementPage: React.FC = () => {
  // 搜尋相關的 state
  const [search, setSearch] = useState<string>('');

  const {
    itemsPerPage,
    currentPage,
    skip,
    limit,
    handlePageChange,
    handleSelect,
  } = usePagination();

  // 使用 useUnits Hook 獲取 unit 資料
  const {
    data: isUnitsData,
    isLoading: isUnitsLoading,
    isError: isUnitsError,
  } = useUnitsQuery();

  // 使用 React Query 來處理資料獲取
  const {
    data: isAnnouncementsData,
    isLoading: isAnnouncementsLoading,
    isError: isAnnouncementsError,
    refetch,
  } = useQuery<GetAnnouncementsApiAdminAnnouncementGetResponse, Error>({
    queryKey: ['announcements', skip, limit, search],
    queryFn: async () => {
      const response = await getAnnouncementsApiAdminAnnouncementGet({
        query: { skip, limit, search },
      });
      return response.data as GetAnnouncementsApiAdminAnnouncementGetResponse;
    },
  });

  // 搜尋按鈕點擊處理
  const handleSearch = (value: string) => {
    setSearch(value);
    refetch();
  };


  return (
    <LoadingErrorHandler
      isLoading={isUnitsLoading || isAnnouncementsLoading}
      isError={isUnitsError || isAnnouncementsError}
    >
      <ListGeneric
        data={isAnnouncementsData ?? { total_count: 0, items: [] }}
        itemTitle="Donate Announcement"
        formFields={[
          { name: 'date', label: 'Date', type: 'date' },
          { name: 'title', label: 'Title', type: 'text' },
          {
            name: 'unit_id',
            label: 'Unit',
            type: 'select',
            options: isUnitsData?.map(unit => ({ ...unit, id: unit.id ?? '' })),
          },
          { name: 'description', label: 'Description', type: 'textarea' },
          { name: 'image_url', label: 'imageURL', type: 'text' },
          { name: 'is_show', label: 'Show', type: 'checkbox' },
        ]}
        itemsPerPage={itemsPerPage}
        currentPage={currentPage}
        search={search}
        onSelect={handleSelect}
        onPageChange={handlePageChange}
        onSearch={handleSearch}
      />
    </LoadingErrorHandler>
  );
};

export default AnnouncementPage;
