import React from 'react';
import styled from 'styled-components';
import { NavBarProps } from '../../../types/nav';

const NavContainer = styled.div`
  display: flex;
  align-items: center;
`;

const Nav = styled.nav`
  display: flex;
  margin: 24px 59px 24px 0;
`;

const NavLinkItem = styled.a`
  display: flex;
  justify-content: center;
  align-items: center;
  color: #1f2937; /* Tailwind gray-800 equivalent */
  background-color: transparent;
  border-radius: 0.75rem;
  width: 115px;
  height: 36px;
  margin-left: 22px;
  font-size: 20px;
  font-weight: bold;
  transition:
    background-color 0.3s,
    color 0.3s;

  &:hover {
    background-color: #0c2d65; /* Tailwind button-darkblue equivalent */
    color: white;
  }
`;

const NavBarItem: React.FC<NavBarProps> = ({ links }) => {
  return (
    <NavContainer>
      <Nav>
        {links.map((link, index) => (
          <NavLinkItem key={index} href={link.href}>
            {link.label}
          </NavLinkItem>
        ))}
      </Nav>
    </NavContainer>
  );
};

export default NavBarItem;
