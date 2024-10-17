import React, { useState, useEffect } from 'react';
import NavBarItem from './navBarItem';
import { NavBarProps } from '../../../types/nav';

const HomeNavBar: React.FC<NavBarProps> = ({ links }) => {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 693) {
        setIsScrolled(true);
      } else {
        setIsScrolled(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div className="flex justify-center">
      <div
        className={`fixed bg-white mx-auto flex justify-between items-center shadow-md h-[84px] z-50 transition-all duration-500 ease-in-out ${isScrolled ? 'w-full rounded-none' : 'w-[1242px] mt-5 rounded-full'}`}
      >
        <div className="flex items-center">
          <img
            className="w-[304px] h-[44px] my-5 ml-14"
            src="http://i.imgur.com/2URSQrW.gif"
            alt="國立臺北商業大學"
          />
        </div>
        <NavBarItem links={links} />
      </div>
    </div>
  );
};

export default HomeNavBar;
