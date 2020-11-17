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
}
export const powerApi = new PowerApi();