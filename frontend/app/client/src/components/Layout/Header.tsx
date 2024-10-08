import HeroSection from '../Donate/HeroSection';
import NavBar from './NavBar';

const links = [
  { label: '最新消息', href: '#' },
  { label: '最新消息', href: '#' },
  { label: '最新消息', href: '#' },
  { label: '最新消息', href: '#' },
];

const Header: React.FC = () => {
  return (
    <header
      className='bg-cover bg-center h-[693px]'
      style={{
        backgroundImage: `url('https://s3-alpha-sig.figma.com/img/90ac/40b7/8e7f07c3515688a250b9503246027cf5?Expires=1728864000&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=jk~2Jds~r1YSHCiwEUmRifm5-t6qtxzNJWKxseHjZXSEwkqgevqrgQ3MLT6dnkGamDx3iwSrMHrZbqh90FGSgCd54wUMzE9s7GWRpj2cx7hYNioIOu5K5mIqLn~bIloR9wxR~-30RfnztGm15sHlxi972WPaOy-Y3O5Q2lnUeGBlQgxoZJnXoxiz76nWgKM3SLbjnFZUr72JE~XejSLTbwuwJoK9n-Sfhx05ma9pAEplKxbuiO4k-x09WP7Dbh3GCtu8wu~dwsIsHQH~GeGt~nJge-zgTebP1Q18pjPdWR8ydp5k54nosKMW5jXcxJzAWRlL2w1JU9zXCb~odtST9w__')`,
      }}
    >
      <div className='flex justify-center'>
        <div className='fixed bg-white mx-auto flex justify-between items-center rounded-full shadow-md w-[1242px] h-[84px] mt-5 z-50'>
          <div className='flex items-center'>
            <img
              className='w-[304px] h-[44px] my-5 ml-14'
              src='http://i.imgur.com/2URSQrW.gif'
              alt='國立臺北商業大學'
            />
          </div>
          <NavBar links={links} />
        </div>
      </div>

      <HeroSection />
    </header>
  );
};

export default Header;
