import { Outlet } from 'react-router-dom';
import Footer from './footer.component';
import Header from './header.component';

export const Layout: React.FC = () => {

  // 首頁的 NavBar 項目
  const links = [
    { label: '捐款清單', href: '/admin/' },
    { label: '最新消息', href: '/admin/news/' },
    { label: '捐款名目', href: '/admin/purpose/' },
    { label: '相關文件', href: '/admin/document/' },
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
