import NavBar from './navbar/NavBar';
import { NavBarProps } from '../../types/nav';

const Header: React.FC<NavBarProps> = ({ links }) => {
  return (
    <header>
      <NavBar links={links} />
    </header>
  );
};

export default Header;
