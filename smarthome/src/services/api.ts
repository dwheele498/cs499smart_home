import axios, { AxiosInstance } from "axios";
import { API_KEY, API_KEY_BACKUP } from "../consts";

export const Api: AxiosInstance = axios.create({
  baseURL: "http://localhost:5000",
  timeout: 30000,
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Content-Type':'application/json',
  },
});

export const WeatherAPI: AxiosInstance = axios.create({
  baseURL: "https://api.meteostat.net/v2/",
  headers: {
    "x-api-key": API_KEY,
    'Content-Type':'application/json'
  },


  
});

export interface Result<T> {
  result: T;
  targetUrl?: string;
  error?: {
    message?: string;
    details?: string;
  };
  success: boolean;
  unAuthorizedRequest: boolean;
}
