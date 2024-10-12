import { Outlet } from 'react-router-dom';
import Footer from './Footer';
import Header from './Header';

export const Layout: React.FC = () => {

  // 首頁的 NavBar 項目
  const links = [
    { label: '最新消息', href: '/admin/news/' },
    { label: '最新消息', href: '#' },
    { label: '最新消息', href: '#' },
    { label: '最新消息', href: '#' },
  ];

  return (
    <div className="relative w-full">
      <Header links={links}/>
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
