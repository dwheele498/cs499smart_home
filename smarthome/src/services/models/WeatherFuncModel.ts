import {GraphData} from './GraphDataModel';

export interface WeatherFuncModel{
    value: number[],
    labels: string[],
    highs: number[],
    lows: number[],
    graphData: GraphData,
}