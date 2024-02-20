import ApiClient from "./api_client";
import { GetRecordByTypeParameters, GetRecordByTypeResponse, GetRecordByDatesParameters, GetRecordByDatesResponse, GetUserRecordResponse, GetRecordTypesResponse } from "../types/client_types";


export class HealthRecordApiClient {
  apiClient = new ApiClient();
  HEADERS = {
    "Content-Type": "application/json"
  }

  async getUserRecord(): Promise<GetUserRecordResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'GET',
        path: '/api/user-record',
        headers: this.HEADERS,
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }
  
  async getRecordTypes(): Promise<GetRecordTypesResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'GET',
        path: '/api/records',
        headers: this.HEADERS,
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

  async getRecordByType(params: GetRecordByTypeParameters): Promise<GetRecordByTypeResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'POST',
        path: '/api/record-by-type',
        headers: this.HEADERS,
        body: params
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

  async getRecordByDates(params: GetRecordByDatesParameters): Promise<GetRecordByDatesResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'POST',
        headers: this.HEADERS,
        path: '/api/record-by-dates',
        body: params
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

}