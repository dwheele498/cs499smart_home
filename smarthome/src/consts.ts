import store from "./store";
import { weatherApi } from "./services/WeatherApi";
import { WeatherModel } from "./services/models/WeatherModel";
import { DateTime } from "luxon";
import * as models from "./services/models";
import { Api } from "./services/api";
import { waterApi } from "./services/WaterApi";
import { ChartDataModel, PredictionModel, WaterModel } from "./services/models";
import { powerApi } from "./services/PowerApi";

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
export const  POWER_DEVICES = ['LiveTv','BedTv','HVAC','Refrigerator','Microwave','Stove','Oven',
'DishWasher','ClothesWasher', 'Dryer','BathExhaust']
export const WATER_DEVICES = ['Bath','Shower','DishWasher','ClothesWasher',]
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
  const start = new Date(dates[0]).toISOString();
  const end = new Date(dates[1]).toISOString();
  const weather = {} as models.WeatherFuncModel;
  await weatherApi
    .getMonth(start, end)
    .then((res: any) => {
      res.data.data.forEach((temp: WeatherModel) => {
        console.log(temp);
        console.log(temp.selectedDate);
        if (temp.tavg == null) {
          console.log("");
        } else {
          const inLabel = label.find((d) => {
            d == `${temp.selectedDate}`;
          });
          if (!inLabel) {
            const dt = DateTime.fromISO(temp.selectedDate);
            value.push(temp.tavg);
            label.push(dt.toFormat("M/d"));
            lows.push(temp.tmin);
            highs.push(temp.tmax);
            const i = label.indexOf(`${temp.selectedDate}`);
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
        const dt = DateTime.fromISO(water.date)
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

export async function PowerCall(
  dates: string[],
  value: number[],
  label: string[]
): Promise<models.PowerFuncModel> {
  store.commit("resetIndex");
  const start = dates[0];
  const end = dates[1];
   const oven =[] as number[];
  const microwave = [] as number[]
   const bedtv=[] as number[]
  const livingtv = [] as number[]
  const stove = [] as number[]
  const dishwasher = [] as number[]
 const hvac = [] as number[]
  const clotheswasher = [] as number[]
 const exhaust = [] as number[]
  const powerResult = {} as models.PowerFuncModel;
  await powerApi
    .getMonth(start, end)
    .then((res: any) => {
      res.data.start.forEach((power: models.PowerModel) => {
        const total =
          power.livingtv + power.bedtv + power.clotheswasher + power.dishwasher + power.exhaust + power.hvac + power.microwave + power.oven + power.stove;
        value.push(total);
        dishwasher.push(power.dishwasher);
        clotheswasher.push(power.clotheswasher);
        exhaust.push(power.exhaust);
        livingtv.push(power.livingtv);
        hvac.push(power.hvac);
        stove.push(power.stove);
        bedtv.push(power.bedtv);
        oven.push(power.oven);
        microwave.push(power.microwave);
        console.log(power.powerdate);
        const dt = DateTime.fromISO(power.powerdate).toFormat("M/d");
        label.push(dt);
      });
    })
    .catch((err) => console.log(err))
    .finally(() => {
      const graphData0 = {
        label: "Total Power Usage Per Day",
        data: value,
        backgroundColor: [],
        borderColor: "cyan",
      } as ChartDataModel;
      const graphData1 = {
        label: "Living Room Tv Power Usage Per Day",
        data: livingtv,
        backgroundColor: [],
        borderColor: "teal",
      };
      const graphData2 = {
        label: "Bedroom Tv Power Usage Per Day",
        data: bedtv,
        backgroundColor: [],
        borderColor: "navy",
      };
      const graphData3 = {
        label: "Dish Washer Power Usage Per Day",
        data: dishwasher,
        backgroundColor: [],
        borderColor: "green",
      };
      const graphData4 = {
        label: "Washing Machine Power Usage Per Day",
        data: clotheswasher,
        backgroundColor: [],
        borderColor: "orange",
      };
      const graphData5 = {
        label: "Bathroom Exhaust Power Usage Per Day",
        data: exhaust,
        backgroundColor: [],
        borderColor: "purple",
      };
      const graphData6 = {
        label: "HVAC Power Usage Per Day",
        data: hvac,
        backgroundColor: [],
        borderColor: "pink",
      };
      const graphData7 = {
        label: "Stove Power Usage Per Day",
        data: stove,
        backgroundColor: [],
        borderColor: "yellow",
      };
      const graphData8 = {
        label: "Oven Power Usage Per Day",
        data: oven,
        backgroundColor: [],
        borderColor: "white",
      };
      const graphData9 = {
        label: "Microwave Power Usage Per Day",
        data: microwave,
        backgroundColor: [],
        borderColor: "grey",
      };
    const graphData = {
        labels: label,
        datasets: [
  
        ],
    };

      powerResult.labels = label;
      powerResult.value = value;
      powerResult.graphData = graphData;
      powerResult.graphData.datasets.push(graphData0);
      powerResult.graphData.datasets.push(graphData1);
      powerResult.graphData.datasets.push(graphData2);
      powerResult.graphData.datasets.push(graphData3);
      powerResult.graphData.datasets.push(graphData4);
      powerResult.graphData.datasets.push(graphData5);
      powerResult.graphData.datasets.push(graphData6);
      powerResult.graphData.datasets.push(graphData7);
      powerResult.graphData.datasets.push(graphData8);
      powerResult.graphData.datasets.push(graphData9);
      console.log(powerResult);
        powerResult.exhaust = exhaust;
        powerResult.stove = stove;
        powerResult.clotheswasher = clotheswasher;
        powerResult.dishwasher = dishwasher;
        powerResult.bedtv = bedtv;
        powerResult.hvac = hvac;
        powerResult.livingtv = livingtv;
        powerResult.microwave = microwave;
        powerResult.oven = oven;
    });
  

  return powerResult;
}

export async function ScreenCall(
  value: number[],
  label: string[]
){
  const wpModel = {} as models.PredcitGraphModel
  await powerApi.getScreens().then((screen: any)=>{
    screen.data.data.forEach((s: models.PredictionModel) => {
        label.push(s[0]);
        value.push(s[1]*1000/636/.12)
    });
  }).finally(()=>{
    const graphData = {
      labels: label,
      datasets: [
        {
          label: "Total Screen Time Per Day",
          data: value,
          backgroundColor: ["#32a852"],
          borderColor: "purple",
        },
      ],
    } as models.GraphData;
    wpModel.labels = label;
    wpModel.value = value;
    wpModel.chartData = graphData;

  })
  return wpModel;
}
