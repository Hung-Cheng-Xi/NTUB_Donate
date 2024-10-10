// 定義 NavLink 的屬性類型
export type NavLink = {
  label: string;
  href: string;
};

// 定義 NavBar 的屬性類型
export type NavBarProps = {
  links: NavLink[];
};
