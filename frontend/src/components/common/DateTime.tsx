import React from "react";
import { format } from 'date-fns';
import { convertTimestamp } from "../../helpers/date";


interface Props {
    timestamp: string
}


const DateTime: React.FC<Props> = (props: Props) => {
    const timestampObject = convertTimestamp(props.timestamp)
    const date = format(timestampObject, "MMM dd, yyyy");
    const time = format(timestampObject, "HH:mm:ss");

  return (
      <div className="w-full">
          <div className="flex bg-shark-950 justify-center items-center pr-1 pl-1 pt-0.5 pb-0.5 rounded">
              <div className="mr-1">
                  <span className="text-md text-white font-bold"> {date} </span>
              </div>
              <div className="bg-shark-925 rounded">
                  <span className="text-md text-amber-400 font-bold p-1"> {time} </span>
              </div>
          </div>
      </div>
  );
};

export default DateTime;