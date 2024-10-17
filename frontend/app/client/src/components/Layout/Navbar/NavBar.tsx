import React from 'react';
import NavBarItem from './navBarItem';
import { NavBarProps } from '../../../types/nav';

const HomeNavBar: React.FC<NavBarProps> = ({ links }) => {
  return (
    <div className="flex justify-center">
      <div className="fixed bg-white mx-auto flex justify-between items-center shadow-md h-[84px] z-50 w-full rounded-none">
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
