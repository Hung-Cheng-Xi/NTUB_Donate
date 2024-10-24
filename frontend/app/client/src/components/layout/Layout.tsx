import { Outlet, useLocation } from 'react-router-dom';
import NavBar from './navbar/navBar';
import Header from './header';
import Footer from './footer';

export const Layout: React.FC = () => {
  const location = useLocation();

  // 判斷是否為首頁路由
  const isHomePage = location.pathname === '/client/';

  // 首頁的 NavBar 項目
  const links = [
    { label: '最新消息', href: '#' },
    { label: '最新消息', href: '#' },
    { label: '最新消息', href: '#' },
    { label: '最新消息', href: '#' },
  ];

  return (
    <div className="relative w-full">
      {isHomePage ? <Header links={links} /> : <NavBar links={links} />}
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
