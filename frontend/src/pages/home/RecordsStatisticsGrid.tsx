import React from "react";
import { ReturnedActivityRecords } from "../../types/client_types";
import DataCard from "../../components/common/DataCard";

interface Props {
    recordsData: ReturnedActivityRecords[]
}

const RecordsStatisticsGrid: React.FC<Props> = (props: Props) => {
  return (
    <div className="flex gap-4">
      {props.recordsData.map((record: ReturnedActivityRecords) => {
        if (record.display === false) {
          return null;
        }
        return (
          <DataCard data={record} />
        );
      })}
    </div>
  );
};

export default RecordsStatisticsGrid;