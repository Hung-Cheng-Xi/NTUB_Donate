import { HomeNavBar } from './navbar';
import { NavBarProps } from '../../types/nav';

const Header: React.FC<NavBarProps> = ({ links }) => {
  return (
    <header>
      <HomeNavBar links={links} />
    </header>
  );
};

export default Header;
