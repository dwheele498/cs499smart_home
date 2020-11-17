import { ChartDataModel } from "./ChartDataModel";
import { GraphData } from "./GraphDataModel";

export interface PredcitGraphModel{
    value: number[],
    labels: string[],
    chartData: GraphData,
}