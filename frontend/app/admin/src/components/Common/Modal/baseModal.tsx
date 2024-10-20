// BaseFormModal Component
import React from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import renderInputField from './renderInputField';

interface BaseFormModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: SubmitHandler<{ [key: string]: string | number | boolean | { id: string | number } }>;
  fields: { name: string; label: string; type: string; options?: { id: string | number; name: string }[]}[];
  defaultValues?: { [key: string]: string | number | boolean | { id: string | number } };
  isReadOnly?: boolean;
}

const BaseFormModal: React.FC<BaseFormModalProps> = ({
  isOpen,
  onClose,
  onSubmit,
  fields,
  defaultValues,
  isReadOnly = false,
}) => {
  const { register, handleSubmit, reset } = useForm({ defaultValues });

  React.useEffect(() => {
    if (defaultValues) {
      // Extract `unit` ID from `defaultValues` if it's an object
      const processedDefaultValues = { ...defaultValues };
      if (defaultValues.unit && typeof defaultValues.unit === 'object') {
        processedDefaultValues.unit = defaultValues.unit.id;
      }
      if (defaultValues.category && typeof defaultValues.category === 'object') {
        processedDefaultValues.category = defaultValues.category.id;
      }
      reset(processedDefaultValues);
    }
  }, [defaultValues, reset]);

  return (
    <div
      className={`fixed inset-0 z-50 flex items-center justify-center overflow-auto ${isOpen ? 'block' : 'hidden'}`}
    >
      <div
        className="fixed inset-0 bg-black bg-opacity-50"
        onClick={onClose}
      ></div>
      <div className="relative bg-white rounded-lg p-6 w-full max-w-md mx-auto my-8 overflow-y-auto max-h-[80vh]">
        <h3 className="text-lg font-medium leading-6 text-gray-900 mb-4">
          Form Modal
        </h3>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          {fields.map((field) =>
            field.type === 'checkbox' ? (
              <div key={field.name} className="flex items-center">
                {renderInputField(field, register, isReadOnly)}
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
                {renderInputField(field, register, isReadOnly)}
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
            {!isReadOnly ? (
              <button
                type="submit"
                className="inline-flex justify-center rounded-md border border-transparent bg-blue-500 px-4 py-2 text-sm font-medium text-white hover:bg-blue-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
              >
                Submit
              </button>
            ) : (
              <button
                type="button"
                className="inline-flex justify-center rounded-md border border-transparent bg-blue-500 px-4 py-2 text-sm font-medium text-white hover:bg-blue-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
              >
                列印
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
};

export default BaseFormModal;
