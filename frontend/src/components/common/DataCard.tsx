import React from "react";
import { FormatNumber } from "../../helpers/formatters";
import { ReturnedActivityRecords } from "../../types/client_types";
import { getIconByName } from "../../config/IconMapping";

interface Props {
  data: ReturnedActivityRecords;
}

const DataCard: React.FC<Props> = (props: Props) => {
  const iconData = getIconByName(props.data.iconName)
  return (
    <div className="bg-[#1E1F25] rounded p-4 flex-1 flex items-center">
      <div className="pl-4">
        <div className="flex items-center">
          <strong className="text-3xl text-gray-700 font-semibold">
            {FormatNumber(props.data.value)}
          </strong>
        </div>
        <span className="text-sm text-gray-500 font-light">
          {props.data.record}
        </span>
      </div>
      <div className="rounded-full h-12 w-12 flex items-center justify-center ml-auto bg-shark-925 text-green-500">
        <iconData.icon className="text-3xl" />
      </div>
    </div>
  );
};

export default DataCard;
