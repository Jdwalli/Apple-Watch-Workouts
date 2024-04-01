import React from "react";
import DateTime from "../../components/common/DateTime";
import { HealthRecordApiClient } from "../../clients/health_record_client";
import { ReturnedActivityRecords } from "../../types/client_types";


// Home Page should have 
// Top Bar: Steps Taken, Walking + Running distance, Stand Minutes, Exercise Minutes, Flights Climed
// Pie Chart (Total Workouts)
// Vitals
// Highest HR, Lowest HR, Heart Rate Variabilitu, Wallimg Hr, Average, Cardio Fitness, ECGs taken, Notifications given, Resp Rate, Blood 02


interface Props {}

const HomePage: React.FC<Props> = (props: Props) => {
  const healthRecordClient = new HealthRecordApiClient();
  const [exportDate, setExportDate] = React.useState<string>('1970-01-01 00:00:00')

  // React.useEffect(() => {
  //   healthRecordClient.getUserRecord().then((data) => {
  //     setExportDate(data.userData.exportDate ?? '1970-01-01 00:00:00')
  //   });

  // }, []);

  return (
    <div>
      
    </div>
    // <div className="p-3 flex w-full">
    //   <h1 className="text-xl font-semibold tracking-wide"> Apple Watch Health Data </h1>
    //   <div className="ml-auto">
    //   <DateTime timestamp={exportDate} />
    //   </div>
      
    // </div>
  );
};

export default HomePage;