import { createBrowserRouter } from 'react-router-dom';
import DonateHomePage from './pages/donateHome';
import Layout from './components/layout/layout';

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
