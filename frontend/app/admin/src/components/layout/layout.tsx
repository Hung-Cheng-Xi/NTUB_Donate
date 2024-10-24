import { Outlet } from 'react-router-dom';
import Footer from './footer';
import Header from './header';

export const Layout: React.FC = () => {
  // 首頁的 NavBar 項目

  const links = [
    { label: '捐款清單', href: '/admin/' },
    { label: '最新公告', href: '/admin/announcement/' },
    { label: '捐款名目', href: '/admin/purpose/' },
    { label: '相關法規', href: '/admin/regulation/' },
  ];

  return (
    <div className="relative w-full">
      <Header links={links} />
      <div className="flex flex-col min-h-screen items-center">
        <main className="flex-grow">
          <Outlet />
        </main>
      </div>
      <Footer />
    </div>
  );
};

export default Layout;
