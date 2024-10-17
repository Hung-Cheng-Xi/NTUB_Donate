import { createBrowserRouter } from 'react-router-dom';
import { Layout } from './components/layout/layout';
import DonateLoginPage from './pages/donate.login';
import DonateHomePage from './pages/donate.home';
import AnnouncementPage from './pages/donate.announcement';
import PurposePage from './pages/donate.purpose';
import RegulationPage from './pages/donate.regulation';

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
        path: '/admin/announcement/',
        async lazy() {
          return { Component: AnnouncementPage };
        },
      },
      {
        path: '/admin/purpose/',
        async lazy() {
          return { Component: PurposePage };
        },
      },
      {
        path: '/admin/regulation/',
        async lazy() {
          return { Component: RegulationPage };
        },
      },
    ],
  },
]);
