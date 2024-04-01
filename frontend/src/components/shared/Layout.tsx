import React from "react";
import { Outlet } from "react-router-dom";
import VerticalNavigation from "../navigation/VerticalNavigation";
import TopHeader from "../navigation/TopHeader";

interface Props {}

const Layout: React.FC<Props> = (props: Props) => {
  return (
    <div className="bg-neutral-100 h-screen w-screen flex flex-row">
      <VerticalNavigation />
      <div className="flex flex-col flex-1">
        <TopHeader />
        <div className="flex-1 p-4 min-h-0 overflow-auto bg-black text-white">
          <Outlet />
        </div>
      </div>
    </div>
  );
};

export default Layout;
