import { createBrowserRouter } from 'react-router-dom';
import { Layout } from './components/layout/layout.component';
import DonateLoginPage from './pages/donate.login.page';
import DonateHomePage from './pages/donate.home.page';
import DonateNewsPage from './pages/donate.new.page';
import PurposePage from './pages/donate.purpose.page';
import DocumentPage from './pages/donate.document.page';
import { RequireAuthService } from './libs/services/requireAuth.service';

export const router = createBrowserRouter([
  {
    path: '/admin/login/',
    async lazy() {
      return { Component: DonateLoginPage };
    },
  },
  {
    Component: Layout,
    loader: RequireAuthService,
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
      {
        path: '/admin/purpose/',
        async lazy() {
          return { Component: PurposePage };
        },
      },
      {
        path: '/admin/document/',
        async lazy() {
          return { Component: DocumentPage };
        },
      },
    ],
  },
]);
