import { useForm } from 'react-hook-form';

const renderInputField = (
  field: {
    name: string;
    label: string;
    type: string;
    options?: string[];
  },
  register: ReturnType<typeof useForm>['register'],
  disabled: boolean = false,
) => {
  switch (field.type) {
    case 'checkbox':
      return (
        <input
          id={field.name}
          {...register(field.name)}
          type="checkbox"
          disabled={disabled}
          className="h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
        />
      );
    case 'select':
      return (
        <select
          {...register(field.name)}
          id={field.name}
          disabled={disabled}
          className="mt-1 block w-full rounded-md p-3 border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50"
        >
          {field.options?.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      );
    case 'textarea':
      return (
        <textarea
          id={field.name}
          {...register(field.name)}
          disabled={disabled}
          className="mt-1 block w-full rounded-md p-3 border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
        ></textarea>
      );
    default:
      return (
        <input
          id={field.name}
          {...register(field.name)}
          type={field.type}
          disabled={disabled}
          className="mt-1 block w-full rounded-md p-3 border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
        />
      );
  }
};

export default renderInputField;
