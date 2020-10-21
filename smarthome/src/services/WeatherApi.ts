import { WeatherAPI } from "./api";
import { WEATHER_STATS } from "../consts";

class WeatherApi {
    getDay = (start: string, end: string) =>
        WeatherAPI.get("/point/daily", {
            params: {
                lat: WEATHER_STATS.lat,
                lon: WEATHER_STATS.lon,
                start,
                end,
            },
        });
}
export const weatherApi = new WeatherApi();
