import { Api, WeatherAPI } from "./api";
import { WEATHER_STATS } from "../consts";
import { WeatherModel } from "./models/WeatherModel";
import { HourlyWeatherModel } from "./models/HourlyWeatherModel";
import { PredictionModel } from "./models";

class WeatherApi {
  getDay = (start: string, end: string) =>
    WeatherAPI.get<HourlyWeatherModel>("/point/hourly", {
      params: {
        start,
        end,
        lat: WEATHER_STATS.lat,
        lon: WEATHER_STATS.lon,
      },
    });
  getMonth = (start: string, end: string) =>
    Api.get<WeatherModel, [WeatherModel]>("/monthlyweatherdata", {
      params: {
        start,
        end,
      },
    });
  getPrediction = () =>
    Api.get<[PredictionModel]>("/monthlyweatherprediction");
}
export const weatherApi = new WeatherApi();
