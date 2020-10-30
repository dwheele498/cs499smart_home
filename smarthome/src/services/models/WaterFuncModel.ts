import { ChartDataModel } from './ChartDataModel';
import {GraphData} from './GraphDataModel';
import { WaterModel } from './WaterModel';

export interface WaterFuncModel{
    dishWasher: number[],
    clothesWasher: number[],
    shower: number[],
    bath: number[],
    labels: string[],
    value: number[],
    graphData: GraphData,
}