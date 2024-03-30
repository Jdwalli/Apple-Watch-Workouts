import { IconType } from "react-icons/lib";

import {
  FaHouseChimney,
  FaFire,
  FaHeartPulse,
  FaPersonRunning,
  FaBedPulse,
  FaGear,
  FaCircleQuestion,
  FaChartLine
} from "react-icons/fa6";

export interface SidebarNavigationData {
  title: string;
  path: string;
  icon: IconType;
}

export const SidebarMainLinks: SidebarNavigationData[] = [
  {
    title: "Home",
    path: "/",
    icon: FaHouseChimney,
  },
  {
    title: "Activity",
    path: "/activity",
    icon: FaFire,
  },
  {
    title: "Vitals",
    path: "/vitals",
    icon: FaHeartPulse,
  },
  {
    title: "Workouts",
    path: "/workouts",
    icon: FaPersonRunning,
  },
  {
    title: "Sleep",
    path: "/sleep",
    icon: FaBedPulse,
  },
  {
    title: "Reports",
    path: "/reports",
    icon: FaChartLine,
  },
];

export const SidebarBottomLinks: SidebarNavigationData[] = [
  {
    title: "Settings",
    path: "/settings",
    icon: FaGear,
  },
  {
    title: "Help & Support",
    path: "/support",
    icon: FaCircleQuestion,
  },
];
