// UpdateModal Component
import React from 'react';
import BaseModal from './baseModal';
import { SubmitHandler } from 'react-hook-form';

interface UpdateModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: SubmitHandler<{ [key: string]: string | number | boolean | { id: string | number } }>;
  fields: { name: string; label: string; type: string; options?: { id: string | number; name: string }[] }[];
  defaultValues?: { [key: string]: string | number | boolean | { id: string | number } };
  isReadOnly?: boolean;
}

const UpdateModal: React.FC<UpdateModalProps> = ({
  isOpen,
  onClose,
  onSubmit,
  fields,
  defaultValues,
  isReadOnly = false,
}) => {
  return (
    <BaseModal
      isOpen={isOpen}
      onClose={onClose}
      onSubmit={onSubmit}
      fields={fields}
      defaultValues={defaultValues}
      title="Update Item"
      submitButtonLabel="Update"
      isReadOnly={isReadOnly}
    />
  );
};

export default UpdateModal;
