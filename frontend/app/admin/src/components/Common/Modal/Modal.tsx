import React from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import renderInputField from './renderInputField';

interface FormModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: SubmitHandler<{ [key: string]: string }>;
  fields: { name: string; label: string; type: string }[];
}

const FormModal: React.FC<FormModalProps> = ({
  isOpen,
  onClose,
  onSubmit,
  fields,
}) => {
  const { register, handleSubmit } = useForm();

  return (
    <div
      className={`fixed inset-0 flex items-center justify-center ${isOpen ? 'block' : 'hidden'}`}
    >
      <div
        className="fixed inset-0 bg-black bg-opacity-50"
        onClick={onClose}
      ></div>
      <div className="bg-white rounded-lg p-6 z-50 w-full max-w-md mx-auto">
        <h3 className="text-lg font-medium leading-6 text-gray-900 mb-4">
          Form Modal
        </h3>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          {fields.map((field) =>
            field.type === 'checkbox' ? (
              <div key={field.name} className="flex items-center">
                {renderInputField(field, register)}
                <label
                  className="ml-2 block text-sm font-medium text-gray-700"
                  htmlFor={field.name}
                >
                  {field.label}
                </label>
              </div>
            ) : (
              <div key={field.name}>
                <label
                  className="block text-sm font-medium text-gray-700"
                  htmlFor={field.name}
                >
                  {field.label}
                </label>
                {renderInputField(field, register)}
              </div>
            ),
          )}
          <div className="flex justify-end mt-4">
            <button
              type="button"
              className="mr-2 inline-flex justify-center rounded-md border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-500 focus-visible:ring-offset-2"
              onClick={onClose}
            >
              Cancel
            </button>
            <button
              type="submit"
              className="inline-flex justify-center rounded-md border border-transparent bg-blue-500 px-4 py-2 text-sm font-medium text-white hover:bg-blue-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default FormModal;
