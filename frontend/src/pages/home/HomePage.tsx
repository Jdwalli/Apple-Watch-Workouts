import React from "react";
import TopHeader from "../../components/navigation/TopHeader";

interface Props {}

const HomePage: React.FC<Props> = (props: Props) => {
  return (
    <div>
      <TopHeader />
    </div>
  );
};

export default HomePage;