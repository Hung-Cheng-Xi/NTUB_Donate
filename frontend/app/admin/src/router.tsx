import { createBrowserRouter } from 'react-router-dom';
import { Layout } from './components/Layout/Layout';
import DonateLoginPage from './pages/donate.LoginPage';
import DonateHomePage from './pages/donate.HomePage';

export const router = createBrowserRouter([
  {
    path: '/admin/login/',
    async lazy() {
      return { Component: DonateLoginPage };
    },
  },
  {
    Component: Layout,
    // loader: RequireAuthService,
    children: [
      {
        path: '/admin/',
        async lazy() {
          return { Component: DonateHomePage };
        },
      },
    ],
  },
]);
