import { WorkoutLocationTypes } from "./health_types";

/* ====== Apple Health Records Attributes ====== */
interface AppleHealthRecord {
  type: string;
  unit: string;
  value: string | number;
  sourceName: string;
  sourceVersion: string;
  device: string;
  creationDate: string;
  startDate: string;
  endDate: string;
}

interface AppleHealthHeartRateRecord extends AppleHealthRecord {
  motionContext: string;
}

interface AppleHealthAudioEventRecord extends AppleHealthRecord {
  exposureLevel: string;
  exposureLevelUnit: string;
}

/* ====== Workout Statistics ====== */
interface HeartRateWorkoutStatistics {
  maxHeartRate: number;
  minHeartRate: number;
  averageHeartRate: number;
  heartRateUnit: string;
}

interface EnergyBurnedInfo {
  basalEnergyBurned: number;
  basalEnergyBurnedUnit: string;
  activeEnergyBurned: number;
  activeEnergyBurnedUnit: string;
}

interface DistanceInfo {
  distanceTraveled: number;
  distanceTraveledUnit: string;
  lapLength: number;
  lapLengthUnit: string;
}

interface ElevationInfo {
  elevationAscended: number;
  elevationDescended: number;
  elevationUnit: string;
}

interface SpeedInfo {
  maximumSpeed: number;
  averageSpeed: number;
  speedUnit: string;
}

interface EnvironmentInfo {
  humidity: number;
  humidityUnit: string;
  temperature: number;
  temperatureUnit: string;
}

interface WorkoutRunningMetrics {
  averageRunningGroundContactTime: number;
  averageRunningGroundContact: number;
  runningGroundContactUnit: string;
  averageRunningPower: number;
  averageRunningSpeed: number;
  averageRunningStrideLength: number;
  averageRunningVerticalOscillation: number;
  runningPowerUnit: string;
  runningSpeedUnit: string;
  runningStrideLengthUnit: string;
  runningVerticalOscillationUnit: string;
  maximumRunningGroundContact: number;
  maximumRunningPower: number;
  maximumRunningSpeed: number;
  maximumRunningStrideLength: number;
  maximumRunningVerticalOscillation: number;
  minimumRunningGroundContact: number;
  minimumRunningPower: number;
  minimumRunningSpeed: number;
  minimumRunningStrideLength: number;
  minimumRunningVerticalOscillation: number;
}

export interface Workout
  extends HeartRateWorkoutStatistics,
    WorkoutRunningMetrics,
    EnergyBurnedInfo,
    DistanceInfo,
    ElevationInfo,
    SpeedInfo,
    EnvironmentInfo {
  stepCount: number;
  workoutType: string;
  workoutLocation: string;
  duration: number;
  durationUnit: string;
  startDate: string;
  endDate: string;
  swimmingLocationType: string;
  timeZone: string;
  averageMETS: number;
  averageMETSUnit: string;
  swolfScore: number;
  fileReference: string;
  workoutEvents: WorkoutEvents[] | undefined;
  workoutGPX: WorkoutGPX | undefined;
  workoutVitals: WorkoutVitals | undefined;
  workoutAdditionalMetrics: AdditionalWorkoutMetrics | undefined;
}

export interface WorkoutEvents {
  date: string | number | undefined;
  duration: string | number | undefined;
  durationUnit: string | number | undefined;
  type: string | number | undefined;
  metadata?: WorkoutEventsMetadata[];
}

interface WorkoutEventsMetadata {
  key: string;
  value: string | number;
}

export interface CommonGraphData {
  time: string[];
  unit: string;
  value: number;
}

export interface WorkoutGPX {
  course: [number];
  elevation: [number];
  hAcc: [number];
  longitude: [number];
  latitude: [number];
  speed: [number];
  time: [string];
  vAcc: [number];
}

export interface WorkoutVitals {
  heartRate: CommonGraphData | undefined;
}

export interface AdditionalWorkoutMetrics {
  groundContactTime: CommonGraphData | undefined;
  runningPower: CommonGraphData | undefined;
  runningSpeed: CommonGraphData | undefined;
  strideLength: CommonGraphData | undefined;
  verticalOscillation: CommonGraphData | undefined;
}

interface ActivitySummary {
  activeEnergyBurned: number;
  activeEnergyBurnedGoal: number;
  activeEnergyBurnedUnit: string;
  date: string;
  exerciseTime: number;
  exerciseTimeGoal: number;
  moveTime: number;
  moveTimeGoal: number;
  standHours: number;
  standHoursGoal: number;
}

interface BreakdownByWorkoutStatistics {
  averageActiveEnergyBurned: number;
  averageAverageSpeed: number | null;
  averageBasalEnergyBurned: number;
  averageDistanceTraveled: number | null;
  averageDuration: number;
  averageElevationAscended: number | null;
  averageElevationDescended: number | null;
  averageHeartRate: number;
  averageLapLength: number | null;
  averageMaximumSpeed: number | null;
  maximumActiveEnergyBurned: number;
  maximumBasalEnergyBurned: number;
  maximumDistanceTraveled: number | null;
  maximumDuration: number;
  maximumElevationAscended: number | null;
  maximumElevationDescended: number | null;
  maximumHeartRate: number;
  maximumLapLength: number | null;
  maximumMaximumSpeed: number | null;
  workoutName: string;
}

/* ====== Activity Summary ====== */
interface ActivitySummary {
  activeEnergyBurned: number;
  activeEnergyBurnedGoal: number;
  activeEnergyBurnedUnit: string;
  date: string;
  exerciseTime: number;
  exerciseTimeGoal: number;
  moveTime: number;
  moveTimeGoal: number;
  standHours: number;
  standHoursGoal: number;
}

/* ====== API Client ====== */
export interface ApiClientRequest {
  httpMethod: "GET" | "POST";
  path: string;
  body?: any;
  queryParams?: any;
  headers?: any;
}

/* ====== API Parameters ====== */
export interface GetRecordByDatesParameters {
  type: string;
  startDate: string;
  endDate: string;
}

export interface GetWorkoutDetailsParameters {
  workoutName: string;
  workoutStartDate: string;
}

export interface GetActivitySummaryParameters {
  date: string;
}

export interface GetRecordByDatesResponse {}

export interface GetRecordByTypeParameters {
  type: string;
}

export interface ReturnedUserData {
  locale?: string;
  exportDate?: string;
  dateOfBirth?: string;
  sex?: string;
  bloodType?: string;
  skinType?: string;
}

export interface ReturnedActivityRecords {
  record: string
  value: number
  unit: string
  display: boolean
  iconName: string
}

export interface ReturnedVitalsRecords {
  heartRateUnit: string;
  maxHeartRate: number;
  maxRespiratoryRate: number;
  minHeartRate: number;
  minRespiratoryRate: number;
  respiratoryRateUnit: string;
}

export interface WorkoutBreakdownData {
  id: string,
  label: string,
  value: number,
  color: string
}

export interface ReturnedWorkoutRecords {
  totalWorkouts: number,
  workoutBreakdown: WorkoutBreakdownData[]
}

/* ====== API Responses ====== */
export interface GetUserRecordResponse {
  userData: ReturnedUserData;
  activityRecords: ReturnedActivityRecords[];
  vitalRecords: ReturnedVitalsRecords;
  workoutRecords: ReturnedWorkoutRecords;
}

export interface GetRecordTypesResponse {
  recordTypes: [string];
}

export interface GetDataStatusResponse {
  dataPresent: boolean;
}

export interface GetActivitySummaryResponse {
  activity: ActivitySummary;
  activityDate: string;
}

export interface GetActivitySummariesResponse {
  activities: ActivitySummary[];
}

export interface GetWorkoutTypesResponse {
  workoutTypes: [string];
}

export interface ApiClientRequest {
  httpMethod: "GET" | "POST";
  path: string;
  body?: any;
  queryParams?: any;
  headers?: any;
}

export interface GetWorkoutDetailsParameters {
  workoutName: string;
  workoutStartDate: string;
}

export interface GetActivitySummaryParameters {
  date: string;
}

export interface GetWorkoutDetailsResponse {
  workoutStartDate: string | undefined;
  workoutType: string | undefined;
  workout: Workout | undefined;
}

export interface GetRecordByTypeResponse {
  type: string;
  record:
    | AppleHealthHeartRateRecord[]
    | AppleHealthAudioEventRecord[]
    | AppleHealthRecord[]
    | undefined;
}

export interface GetWorkoutStatisticsResponse {
  activeEnergyBurnedUnit: string;
  averageMETSUnit: string;
  basalEnergyBurnedUnit: string;
  distanceTraveledUnit: string;
  durationUnit: string;
  heartRateUnit: string;
  highestActiveEnergyBurned: number;
  highestAverageMETS: number;
  highestBasalEnergyBurned: number;
  highestDistanceTraveled: number;
  highestHeartRate: number;
  highestMaximumSpeed: number;
  longestDuration: number;
  lowestActiveEnergyBurned: number;
  lowestBasalEnergyBurned: number;
  lowestDistanceTraveled: number;
  lowestHeartRate: number;
  shortedDuration: number;
  speedUnit: string;
  totalWorkouts: number;
  workoutsByLocation: {
    [key in WorkoutLocationTypes]?: number;
  };
}

export interface GetBreakdownByWorkoutStatistics {
  workoutBreakdowns: BreakdownByWorkoutStatistics[];
}

export interface WorkoutBreakdown {
  index: number;
  workoutType: string;
  workoutLocation: string;
  duration: number;
  durationUnit: string;
  startTime: string;
  fileReference: boolean;
}

export interface GetAllWorkoutDetailsResponse {
  workouts: WorkoutBreakdown[];
}