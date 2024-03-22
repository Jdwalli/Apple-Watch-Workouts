import React from "react";
import Button from "../common/Button";

const TopHeader: React.FC = () => {
  return (
    <div className="ml-16 flex items-center bg-shark-950 h-16 px-6">
      <div>
      <span className="text-lg font-semibold tracking-wide ">Apple Watch Dashboard </span>
      </div>
      <div className="ml-auto">
        <Button text={'Upload'} variant="primary" onClick={() => alert("Button clicked!")} />
      </div>
    </div>
  );
};

export default TopHeader;
