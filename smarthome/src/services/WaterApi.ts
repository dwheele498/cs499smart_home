import {Api} from './api';
import {WaterModel} from './models/WaterModel';

class WaterApi{
getMonth = (start: string, end: string)=>
    Api.get<WaterModel,[WaterModel]>('/monthlywaterdata',{
        params:{
            start,
            end
        }
    })
}
export const waterApi = new WaterApi();