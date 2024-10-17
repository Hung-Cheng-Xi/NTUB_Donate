import { createBrowserRouter } from 'react-router-dom';
import { Layout } from './components/layout/layout';
import DonateLoginPage from './pages/donateLogin';
import DonateHomePage from './pages/donateHome';
import AnnouncementPage from './pages/donateAnnouncement';
import PurposePage from './pages/donatePurpose';
import RegulationPage from './pages/donateRegulation';

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
