import {Api} from './api';
import {PowerModel} from './models/PowerModel';

class PowerApi{
getMonth = (start: string, end: string)=>
    Api.get<PowerModel,[PowerModel]>('/monthlypowerdata',{
        params:{
            start,
            end
        }
    })
}
export const powerApi = new PowerApi();