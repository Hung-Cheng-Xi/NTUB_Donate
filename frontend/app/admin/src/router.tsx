import { createBrowserRouter } from 'react-router-dom';
import { Layout } from './components/Layout/Layout';
import DonateLoginPage from './pages/donate.LoginPage';
import DonateHomePage from './pages/donate.HomePage';
import DonateNewsPage from './pages/donate.NewsPage';

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
      {
        path: '/admin/news/',
        async lazy() {
          return { Component: DonateNewsPage };
        },
      },
    ],
  },
]);