import { createBrowserRouter } from 'react-router-dom';
import { Layout } from './components/Layout/Layout';
import DonateHomePage from './pages/donate.Homepage';

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
