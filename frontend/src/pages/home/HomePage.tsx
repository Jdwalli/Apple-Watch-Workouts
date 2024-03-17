import React from "react";
import DateTime from "../../components/common/DateTime";

interface Props {}

const HomePage: React.FC<Props> = (props: Props) => {
  return (
    <div className="p-3 flex w-full">
      <h1 className="text-xl font-semibold tracking-wide"> Apple Watch Health Data </h1>
      <div className="ml-auto">
      <DateTime timestamp={"2024-02-21 01:43:05 -0500"} />
      </div>
      
    </div>
  );
};

export default HomePage;