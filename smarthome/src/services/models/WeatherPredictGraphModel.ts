import { ChartDataModel } from "./ChartDataModel";
import { GraphData } from "./GraphDataModel";

export interface WeatherPredcitGraphModel{
    value: number[],
    labels: string[],
    chartData: GraphData,
}