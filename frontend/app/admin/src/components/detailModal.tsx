import React from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
} from '@mui/material';

interface DetailModalProps {
  open: boolean;
  onClose: () => void;
  title: string;
  buttons?: {
    label: string;
    onClick: () => void;
    color?:
      | 'primary'
      | 'secondary'
      | 'error'
      | 'inherit'
      | 'success'
      | 'warning';
  }[];
  children: React.ReactNode;
}

function DetailModal({
  open,
  onClose,
  title,
  buttons,
  children,
}: DetailModalProps) {
  return (
    <Dialog open={open} onClose={onClose} fullWidth maxWidth="sm">
      <DialogTitle>{title}</DialogTitle>
      <DialogContent dividers>{children}</DialogContent>
      <DialogActions>
        {buttons &&
          buttons.map((button, index) => (
            <Button
              key={index}
              onClick={button.onClick}
              color={button.color || 'primary'}
            >
              {button.label}
            </Button>
          ))}
        <Button onClick={onClose} color="secondary">
          關閉
        </Button>
      </DialogActions>
    </Dialog>
  );
}

export default DetailModal;
