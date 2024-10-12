import { useForm } from 'react-hook-form';

const renderInputField = (
    field: { name: string; label: string; type: string },
    register: ReturnType<typeof useForm>['register'],
  ) => {
    switch (field.type) {
      case 'text':
      case 'date':
        return (
          <input
            id={field.name}
            {...register(field.name)}
            type={field.type}
            className="mt-1 block w-full rounded-md p-3 border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          />
        );
      case 'checkbox':
        return (
          <input
            id={field.name}
            {...register(field.name)}
            type="checkbox"
            className="h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
          />
        );
      case 'select':
        return (
          <select
            id={field.name}
            {...register(field.name)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          >
            <option value="">Please select</option>
            {/* Add options here as needed */}
          </select>
        );
      default:
        return null;
    }
  };

export default renderInputField;
