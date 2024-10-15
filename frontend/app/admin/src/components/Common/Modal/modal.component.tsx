import React from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import renderInputField from './renderInputField';

interface FormModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: SubmitHandler<{ [key: string]: string }>;
  fields: { name: string; label: string; type: string; options?: string[]; }[];
  viewMode: 'list' | 'table';
  defaultValues?: { [key: string]: string };
}

const FormModal: React.FC<FormModalProps> = ({
  isOpen,
  onClose,
  onSubmit,
  fields,
  viewMode,
  defaultValues,
}) => {
  const { register, handleSubmit, setValue } = useForm({ defaultValues });

  // 如果是 table 模式，則所有字段都是只讀的
  const isReadOnly = viewMode === 'table';

  // 當表單打開時，設置默認值
  React.useEffect(() => {
    if (defaultValues) {
      Object.entries(defaultValues).forEach(([key, value]) => {
        setValue(key, value);
      });
    }
  }, [defaultValues, setValue]);

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

export default FormModal;
