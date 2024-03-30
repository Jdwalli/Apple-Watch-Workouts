import React from "react";
import { Outlet } from 'react-router-dom'
import VerticalNavigation from "../navigation/VerticalNavigation";
import TopHeader from "../navigation/TopHeader";

interface Props {
    
}
const Layout: React.FC<Props> = (props: Props) => {
		return (
		<div className="bg-neutral-100 h-screen w-screen overflow-hidden">
			<TopHeader />
		</div>
	)
  
};

export default Layout;
