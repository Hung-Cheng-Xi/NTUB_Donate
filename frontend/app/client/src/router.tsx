import { createBrowserRouter } from 'react-router-dom';
import { Layout } from './components/layout/Layout';
import DonateHomePage from './pages/donateHome';

export const router = createBrowserRouter([
  {
    Component: Layout,
    // loader: RequireAuthService,
    children: [
      {
        path: '/client/',
        index: true,
        async lazy() {
          return { Component: DonateHomePage };
        },
      },
    ],
  },
]);
