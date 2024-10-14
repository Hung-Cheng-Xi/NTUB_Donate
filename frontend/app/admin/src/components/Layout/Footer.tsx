import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-button-darkblue text-white py-4 mt-[120px]">
      <div className="max-w-7xl mx-auto flex justify-center text-sm">
        <p className="text-center">
          Copyright ©2020 國立臺北商業大學 ALL RIGHTS RESERVED.
          <a href="#" className="ml-4 underline hover:text-gray-300">
            隱私權政策 PRIVACY POLICY
          </a>
        </p>
      </div>
    </footer>
  );
};

export default Footer;
