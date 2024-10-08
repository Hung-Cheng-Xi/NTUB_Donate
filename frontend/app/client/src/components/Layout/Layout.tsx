import { Outlet } from 'react-router-dom';
import Footer from './Footer';
import Header from './Header';

export const Layout: React.FC = () => {
  return (
    <div className='relative w-full'>
      <Header />
      <div className='flex flex-col min-h-screen items-center'>
        <main className='flex-grow'>
          <Outlet />
        </main>
      </div>
      <Footer />
    </div>
  );
};

export default Layout;
