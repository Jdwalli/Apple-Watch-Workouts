import ApiClient from "./api_client";
import { GetActivitySummaryParameters, GetActivitySummaryResponse, GetActivitySummariesResponse } from "../types/client_types";

export class ActivitySummaryApiClient {
  apiClient = new ApiClient();
  HEADERS = {
    "Content-Type": "application/json"
  }

  async getActivitySummary(params: GetActivitySummaryParameters): Promise<GetActivitySummaryResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'POST',
        path: '/api/activity-summary',
        headers: this.HEADERS,
        body: params
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

  async getActivitySummaries(): Promise<GetActivitySummariesResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'GET',
        path: '/api/activity-summaries',
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

}