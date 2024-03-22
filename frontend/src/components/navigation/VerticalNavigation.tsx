import React from "react";
import {
  FaApple,
  FaHouseChimney,
  FaFire,
  FaHeartPulse,
  FaPersonRunning,
  FaBedPulse,
  FaGear,
} from "react-icons/fa6";

const VerticalNavigation: React.FC = () => {
  return (
    <div
      className="fixed top-0 left-0 h-screen w-16 flex flex-col
    bg-shark-950 shadow-lg"
    >
      <SideBarIcon icon={<FaApple size="28" />} text={"Temp Icon"} />
      <Divider />
      <SideBarIcon icon={<FaHouseChimney size="26" />} text={"Home"} />
      <SideBarIcon icon={<FaFire size="26" />} text={"Activity"} />
      <SideBarIcon icon={<FaHeartPulse size="26" />} text={"Vitals"} />
      <SideBarIcon icon={<FaPersonRunning size="26" />} text={"Workouts"} />
      <SideBarIcon icon={<FaBedPulse size="26" />} text={"Sleep"} />
      <div className="mt-auto"></div>
      <Divider />
      <SideBarIcon icon={<FaGear size="22" />} text={"Settings"} />
    </div>
  );
};

interface SidebarIcon {
  icon: any;
  text: string;
}

const SideBarIcon = (props: SidebarIcon) => (
  <div className="sidebar-icon group">
    {props.icon}
    <span className="sidebar-tooltip group-hover:scale-100">{props.text}</span>
  </div>
);

const Divider = () => <hr className="sidebar-hr" />;

export default VerticalNavigation;
