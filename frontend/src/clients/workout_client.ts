import ApiClient from "./api_client";
import { GetWorkoutDetailsParameters, GetWorkoutDetailsResponse, GetWorkoutTypesResponse, GetWorkoutStatisticsResponse, GetBreakdownByWorkoutStatistics, GetAllWorkoutDetailsResponse } from "../types/client_types";

export class WorkoutApiClient {
  apiClient = new ApiClient();
  HEADERS = {
    "Content-Type": "application/json"
  }

  async getWorkoutDetails(params: GetWorkoutDetailsParameters): Promise<GetWorkoutDetailsResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'POST',
        path: '/api/workout',
        headers: this.HEADERS,
        body: params
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

  async getWorkoutTypes(): Promise<GetWorkoutTypesResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'GET',
        path: '/api/workout-types',
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

  async getWorkoutStatistics(): Promise<GetWorkoutStatisticsResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'GET',
        path: '/api/workouts-statistics',
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

  async getBreakdownByWorkoutStatistics(): Promise<GetBreakdownByWorkoutStatistics> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'GET',
        path: '/api/workouts-breakdown-statistics',
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

  async getAllWorkoutDetails(): Promise<GetAllWorkoutDetailsResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'GET',
        path: '/api/all-workout-details',
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

}