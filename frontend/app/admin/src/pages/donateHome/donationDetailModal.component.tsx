import React from 'react';
import { Donation } from '../../../../shared/openapi';
import { Typography, Grid2 } from '@mui/material';
import DetailModal from '../../components/detailModal';

interface DonationDetailModalProps {
  open: boolean;
  onClose: () => void;
  selectedRow: Donation | null;
  fieldLabels: { [key: string]: string };
}

const DonationDetailModal: React.FC<DonationDetailModalProps> = ({
  open,
  onClose,
  selectedRow,
  fieldLabels,
}) => {
  return (
    <DetailModal open={open} onClose={onClose} title="詳細資料">
      {selectedRow && (
        <div>
          <Grid2 container spacing={2}>
            {Object.entries(selectedRow)
              .filter(
                ([key]) =>
                  key !== 'id' && key !== 'memo' && key !== 'purpose_id',
              )
              .map(([key, value]) => (
                <Grid2 size={6} key={key}>
                  <Typography variant="body1">
                    <strong>{fieldLabels[key] || key}：</strong>{' '}
                    {value ?? '未提供'}
                  </Typography>
                </Grid2>
              ))}
          </Grid2>
          {selectedRow.memo && (
            <Typography
              variant="body1"
              style={{ marginTop: '16px', whiteSpace: 'pre-wrap' }}
            >
              <strong>{fieldLabels['memo'] || '備註'}：</strong>{' '}
              {selectedRow.memo}
            </Typography>
          )}
        </div>
      )}
    </DetailModal>
  );
};

export default DonationDetailModal;
