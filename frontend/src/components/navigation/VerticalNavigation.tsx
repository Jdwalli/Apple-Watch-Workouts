import React from "react";
import classNames from "classnames";
import { Link, useLocation } from "react-router-dom";
import {
  SidebarMainLinks,
  SidebarBottomLinks,
  SidebarNavigationData,
} from "../../config/SidebarConfig";

const linkClass =
  "flex items-center gap-2 font-light px-3 py-2 hover:bg-neutral-700 hover:no-underline active:bg-neutral-600 rounded text-base";

const VerticalNavigation: React.FC = () => {
  return (
    <div className="bg-[#1E1F25] w-60 flex flex-col h-full">
      <div className="h-16 w-full px-4 flex items-center">
      <div className="relative">
				<span className="font-bold text-white text-lg">
					Apple Watch Dashboard
				</span>
			</div>
      </div>
      <div className="mt-2 py-4 p-3 flex flex-1 flex-col gap-1.5">
        {SidebarMainLinks.map((link) => (
          <SidebarLink key={link.title} link={link} />
        ))}
      </div>
    </div>
  );
};

interface SidebarLinkProps {
  link: SidebarNavigationData;
}

const SidebarLink = (props: SidebarLinkProps) => {
  const { pathname } = useLocation();

  return (
    <Link
      to={props.link.path}
      className={classNames(
        pathname === props.link.path
          ? "bg-[#262626] text-white"
          : "text-white",
        linkClass
      )}
    >
      <span className="text-xl">
        <props.link.icon className="text-[#C3FA00]" />
      </span>
      <span className="font-normal text-white">
        {props.link.title}
      </span>
    </Link>
  );
};

export default VerticalNavigation;
