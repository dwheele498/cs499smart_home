import { Api,WeatherAPI } from "./api";
import { WEATHER_STATS } from "../consts";
import { WeatherModel } from "./models/WeatherModel";

class WeatherApi {
  getDay = (start: string, end: string) =>
    WeatherAPI.get<WeatherModel>("/point/daily", {
      params: {
        start,
        end,
        lat: WEATHER_STATS.lat,
        lon: WEATHER_STATS.lon
      },
    });
  getMonth = (start: string, end: string) =>
    Api.get<WeatherModel,[WeatherModel]>("/monthlyweatherdata", {
        params: {
        start,
        end
      },
    });
}
export const weatherApi = new WeatherApi();
