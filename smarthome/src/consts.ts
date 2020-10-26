import store from "./store";
import { weatherApi } from "./services/WeatherApi";
import { WeatherModel } from "./services/models/WeatherModel";
import { DateTime } from "luxon";
import * as models from "./services/models";
import { Api } from "./services/api";
import { waterApi } from "./services/WaterApi";
import { ChartDataModel, WaterModel } from "./services/models";

export const API_KEY = "1mXl3ltqbTwYp4w7T9F3VylcJGwfzJRh";
export const WEATHER_STATS = { lat: 33.543682, lon: -86.779633 };
export const ROOMS = [
  "Living Room",
  "Kitchen",
  "Master Bedroom",
  "Child Bedroom",
  "Garage",
  "Bathroom",
];
export enum MONTHS {
  January = 1,
  February = 2,
  March,
  April,
  May,
  June,
  July,
  August,
  September,
  October,
  November,
  December,
}

export async function WeatherCall(
  dates: string[],
  value: number[],
  label: string[],
  highs: number[],
  lows: number[]
): Promise<models.WeatherFuncModel> {
  store.commit("resetIndex");
  const start = dates[0];
  const end = dates[1];
  const weather = {} as models.WeatherFuncModel;
  await weatherApi
    .getMonth(start, end)
    .then((res: any) => {
      res.data.data.forEach((temp: WeatherModel) => {
        if (temp.tavg == null) {
          console.log("");
        } else {
          const inLabel = label.find((d) => {
            d == `${temp.month}-${temp.day}`;
          });
          if (!inLabel) {
            const dt = DateTime.local().set({
              month: Number.parseInt(temp.month),
              day: Number.parseInt(temp.day),
            });
            value.push(temp.tavg);
            label.push(dt.toFormat("M/d"));
            lows.push(temp.tmin);
            highs.push(temp.tmax);
            const i = label.indexOf(`${temp.month}-${temp.day}`);
            value[i] += Math.floor(temp.tavg / 2);
          }
        }
      });
    })
    .catch((err: Error) => console.log(err.message))
    .finally(() => {
      const graphData = {
        labels: label,
        datasets: [
          {
            label: "Avg Temp Per Day",
            data: value,
            backgroundColor: ["#32a852"],
            borderColor: "red",
          },
        ],
      } as models.GraphData;
      weather.labels = label;
      weather.value = value;
      weather.graphData = graphData;
      weather.highs = highs;
      weather.lows = lows;
    });

  return weather;
}
export async function WaterCall(
  dates: string[],
  value: number[],
  label: string[]
): Promise<models.WaterFuncModel> {
  store.commit("resetIndex");
  const start = dates[0];
  const end = dates[1];
  const bath = [] as number[];
  const shower = [] as number[];
  const clothes = [] as number[];
  const dish = [] as number[];
  const waterResult = {} as models.WaterFuncModel;
  await waterApi
    .getMonth(start, end)
    .then((res: any) => {
      res.data.start.forEach((water: models.WaterModel) => {
        const total =
          water.bath + water.clotheswasher + water.dishwasher + water.shower;
        value.push(total);
        dish.push(water.dishwasher);
        clothes.push(water.clotheswasher);
        bath.push(water.bath);
        shower.push(water.shower);
        const dt = DateTime.local()
          .set({ month: water.month, day: water.day })
          .toFormat("M/d");
        label.push(dt);
      });
    })
    .catch((err) => console.log(err))
    .finally(() => {
      const graphData0 = {
        label: "Total Water Usage Per Day",
        data: value,
        backgroundColor: [],
        borderColor: "cyan",
      } as ChartDataModel;
      const graphData1 = {
        label: "Shower Water Usage Per Day",
        data: shower,
        backgroundColor: [],
        borderColor: "teal",
      };
      const graphData2 = {
        label: "Bath Water Usage Per Day",
        data: bath,
        backgroundColor: [],
        borderColor: "navy",
      };
      const graphData3 = {
        label: "Dish Washer Water Usage Per Day",
        data: dish,
        backgroundColor: [],
        borderColor: "green",
      };
      const graphData4 = {
        label: "Washing Machine Water Usage Per Day",
        data: clothes,
        backgroundColor: [],
        borderColor: "orange",
      };
    const graphData = {
        labels: label,
        datasets: [
  
        ],
    };

      waterResult.labels = label;
      waterResult.value = value;
      waterResult.graphData = graphData;
      waterResult.graphData.datasets.push(graphData0);
      waterResult.graphData.datasets.push(graphData1);
      waterResult.graphData.datasets.push(graphData2);
      waterResult.graphData.datasets.push(graphData3);
      waterResult.graphData.datasets.push(graphData4);
      console.log(waterResult);
        waterResult.bath = bath;
        waterResult.shower = shower;
        waterResult.clothesWasher = clothes;
        waterResult.dishWasher = dish;
    });

  return waterResult;
}
