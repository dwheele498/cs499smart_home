import {Api} from './api';
import { PredictionModel } from './models';
import {PowerModel} from './models/PowerModel';

class PowerApi{
getMonth = (start: string, end: string)=>
    Api.get<PowerModel,[PowerModel]>('/monthlypowerdata',{
        params:{
            start,
            end
        }
    })

    getPrediction = ()=>
    Api.get<[PredictionModel]>('/monthlypowerprediction')

    getScreens=()=> Api.get<PredictionModel>('/screenstats');
}
export const powerApi = new PowerApi();