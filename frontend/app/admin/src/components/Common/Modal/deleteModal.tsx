// DeleteModal Component
import React from 'react';
import BaseModal from './baseModal';
import { SubmitHandler } from 'react-hook-form';

interface DeleteModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: SubmitHandler<{
    [key: string]: string | number | boolean | { id: string | number };
  }>;
  fields?: {
    name: string;
    label: string;
    type: string;
    options?: { id: string | number; name: string }[];
  }[];
  defaultValues?: {
    [key: string]: string | number | boolean | { id: string | number };
  };
}

export const DeleteModal: React.FC<DeleteModalProps> = ({
  isOpen,
  onClose,
  onSubmit,
  defaultValues,
}) => {
  return (
    <BaseModal
      isOpen={isOpen}
      onClose={onClose}
      onSubmit={onSubmit}
      fields={[]}
      defaultValues={defaultValues}
      title="Delete Item"
      submitButtonLabel="Delete"
    />
  );
};
