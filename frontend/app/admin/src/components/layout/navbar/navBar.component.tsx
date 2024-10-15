import React from 'react';
import NavBarItem from './navBarItem.component';
import { NavBarProps } from '../../../types/nav';

const HomeNavBar: React.FC<NavBarProps> = ({ links }) => {
  return (
    <div className="flex justify-center mb-[24px]">
      <div
        className="bg-white mx-auto flex justify-between items-center shadow-md h-[84px] w-full rounded-none"
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
