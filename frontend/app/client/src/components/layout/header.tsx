import HomeNavBar from './navbar/homeNavBar';
import { NavBarProps } from '../../types/nav';
import HeroSection from '../donate/heroSection';

const Header: React.FC<NavBarProps> = ({ links }) => {
  return (
    <header
      className="bg-cover bg-center h-[693px]"
      style={{
        backgroundImage: `url('https://s3-alpha-sig.figma.com/img/90ac/40b7/8e7f07c3515688a250b9503246027cf5?Expires=1728864000&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=jk~2Jds~r1YSHCiwEUmRifm5-t6qtxzNJWKxseHjZXSEwkqgevqrgQ3MLT6dnkGamDx3iwSrMHrZbqh90FGSgCd54wUMzE9s7GWRpj2cx7hYNioIOu5K5mIqLn~bIloR9wxR~-30RfnztGm15sHlxi972WPaOy-Y3O5Q2lnUeGBlQgxoZJnXoxiz76nWgKM3SLbjnFZUr72JE~XejSLTbwuwJoK9n-Sfhx05ma9pAEplKxbuiO4k-x09WP7Dbh3GCtu8wu~dwsIsHQH~GeGt~nJge-zgTebP1Q18pjPdWR8ydp5k54nosKMW5jXcxJzAWRlL2w1JU9zXCb~odtST9w__')`,
      }}
    >
      <HomeNavBar links={links} />
      <HeroSection />
    </header>
  );
};

export default Header;
