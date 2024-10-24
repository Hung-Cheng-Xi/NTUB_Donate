// LoadingErrorHandler.tsx
import React from 'react';

interface LoadingErrorHandlerProps {
  isLoading: boolean;
  isError: boolean;
  children: React.ReactNode;
}

const LoadingErrorHandler: React.FC<LoadingErrorHandlerProps> = ({
  isLoading,
  isError,
  children,
}) => {
  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError) {
    return <div>Error fetching data</div>;
  }

  return <>{children}</>;
};

export default LoadingErrorHandler;
