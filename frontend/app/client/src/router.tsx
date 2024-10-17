import { createBrowserRouter } from 'react-router-dom';
import { Layout } from './components/layout/layout';
import DonateHomePage from './pages/donate.home';

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
