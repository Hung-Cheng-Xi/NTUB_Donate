// src/pages/donation/DonationTableComponent.tsx

import React from 'react';
import {
  useReactTable,
  getCoreRowModel,
  ColumnDef,
  flexRender,
} from '@tanstack/react-table';
import { Donation } from '../../../../shared/openapi';
import { TablePagination } from '@mui/material';

interface DonationTableProps {
  data: Donation[];
  columns: ColumnDef<Donation>[];
  pagination: {
    pageIndex: number;
    pageSize: number;
  };
  totalCount: number;
  onPaginationChange: (pagination: {
    pageIndex: number;
    pageSize: number;
  }) => void;
  onRowClick: (row: Donation) => void;
}

const DonationTable: React.FC<DonationTableProps> = ({
  data,
  columns,
  pagination,
  totalCount,
  onPaginationChange,
}) => {
  const tableInstance = useReactTable<Donation>({
    columns,
    data,
    getCoreRowModel: getCoreRowModel(),
    manualPagination: true,
    pageCount: Math.ceil(totalCount / pagination.pageSize),
    state: {
      pagination: pagination,
    },
    onPaginationChange: (updaterOrValue) => {
      const newPagination =
        typeof updaterOrValue === 'function'
          ? updaterOrValue(pagination)
          : updaterOrValue;
      onPaginationChange(newPagination);
    },
  });

  const handleChangePage = (
    event: React.MouseEvent<HTMLButtonElement> | null,
    newPage: number,
  ) => {
    onPaginationChange({
      ...pagination,
      pageIndex: newPage,
    });
  };

  const handleChangeRowsPerPage = (
    event: React.ChangeEvent<HTMLInputElement>,
  ) => {
    const newPageSize = parseInt(event.target.value, 10);
    onPaginationChange({
      pageIndex: 0,
      pageSize: newPageSize,
    });
  };

  return (
    <>
      <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
        <table className="w-full text-base text-left rtl:text-right text-gray-500 dark:text-gray-400">
          <thead className="text-base text-gray-700 uppercase dark:text-gray-400">
            {tableInstance.getHeaderGroups().map((headerGroup) => (
              <tr key={headerGroup.id}>
                {headerGroup.headers.map((header, index) => {
                  const isBackgroundHeader = index % 2 === 0;
                  const className = `px-6 py-3 ${
                    isBackgroundHeader ? 'bg-gray-50 dark:bg-gray-800' : ''
                  }`;
                  return (
                    <th key={header.id} scope="col" className={className}>
                      {header.isPlaceholder
                        ? null
                        : flexRender(
                            header.column.columnDef.header,
                            header.getContext(),
                          )}
                    </th>
                  );
                })}
              </tr>
            ))}
          </thead>
          <tbody>
            {tableInstance.getRowModel().rows.length > 0 ? (
              tableInstance.getRowModel().rows.map((row) => (
                <tr
                  key={row.id}
                  className="border-b border-gray-200 dark:border-gray-700"
                >
                  {row.getVisibleCells().map((cell, index) => {
                    const isFirstCell = index === 0;
                    const isBackgroundCell = index % 2 === 0;
                    const CellTag = isFirstCell ? 'th' : 'td';
                    const scope = isFirstCell ? 'row' : undefined;
                    let className = 'px-6 py-4 text-base';
                    if (isFirstCell) {
                      className +=
                        ' font-medium text-gray-900 whitespace-nowrap';
                      if (isBackgroundCell) {
                        className +=
                          ' bg-gray-50 dark:text-white dark:bg-gray-800';
                      }
                    } else {
                      if (isBackgroundCell) {
                        className += ' bg-gray-50 dark:bg-gray-800';
                      }
                    }
                    return (
                      <CellTag
                        key={cell.id}
                        scope={scope}
                        className={className}
                      >
                        {flexRender(
                          cell.column.columnDef.cell,
                          cell.getContext(),
                        )}
                      </CellTag>
                    );
                  })}
                </tr>
              ))
            ) : (
              <tr>
                <td
                  colSpan={columns.length}
                  className="text-center px-6 py-4 text-base"
                >
                  No data available
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      <TablePagination
        component="div"
        count={totalCount}
        page={pagination.pageIndex}
        onPageChange={handleChangePage}
        rowsPerPage={pagination.pageSize}
        onRowsPerPageChange={handleChangeRowsPerPage}
        labelRowsPerPage="每頁顯示："
        labelDisplayedRows={({ from, to, count }) =>
          `第 ${from}-${to} 項，共 ${count} 項`
        }
      />
    </>
  );
};

export default DonationTable;
