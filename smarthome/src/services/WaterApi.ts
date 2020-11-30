import { Api } from "./api";
import { WaterModel } from "./models/WaterModel";
import { PredictionModel } from "./models";

class WaterApi {
  getMonth = (start: string, end: string) =>
    Api.get<WaterModel, [WaterModel]>("/monthlywaterdata", {
      params: {
        start,
        end,
      },
    });

  getPrediction = () => Api.get<[PredictionModel]>("/monthlywaterprediction");

  sendWater = async (water: [string,number]) =>
    Api.post("/monthlywaterdata", {
      water
    });
}
export const waterApi = new WaterApi();
