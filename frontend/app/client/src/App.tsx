import { RouterProvider } from 'react-router-dom';
import { router } from './router';
import React from 'react';

function App() {
  return (
    <React.Suspense fallback={<div>Loading...</div>}>
      <RouterProvider router={router} />
    </React.Suspense>
  );
}

export default App;
