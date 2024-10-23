// CreateModal Component
import React from 'react';
import BaseModal from './baseModal';
import { SubmitHandler } from 'react-hook-form';

interface CreateModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: SubmitHandler<{ [key: string]: string | number | boolean | { id: string | number } }>;
  fields: { name: string; label: string; type: string; options?: { id: string | number; name: string }[] }[];
}

const CreateModal: React.FC<CreateModalProps> = ({
  isOpen,
  onClose,
  onSubmit,
  fields,
}) => {
  return (
    <BaseModal
      isOpen={isOpen}
      onClose={onClose}
      onSubmit={onSubmit}
      fields={fields}
      title="Create Item"
      submitButtonLabel="Create"
    />
  );
};

export default CreateModal;
