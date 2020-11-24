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

  sendWater = async (name: string, amt: number) =>
    Api.post("/waterupdate", {
      name,
      amt,
    });
}
export const waterApi = new WaterApi();
