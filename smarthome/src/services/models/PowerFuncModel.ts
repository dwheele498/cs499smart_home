import { ChartDataModel } from './ChartDataModel';
import {GraphData} from './GraphDataModel';
import { PowerModel } from './PowerModel';

export interface PowerFuncModel{
    oven: number[],
    microwave: number[],
    bedtv: number[],
    livingtv: number[],
    stove: number[],
    dishwasher: number[],
    hvac: number[],
    clotheswasher: number[],
    exhaust: number[],
    labels: string[],
    value: number[]
    graphData: GraphData,
}