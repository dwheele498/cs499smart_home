import { Api } from "./api";
import { PredictionModel } from "./models";
import { PowerModel } from "./models/PowerModel";

class PowerApi {
  getMonth = (start: string, end: string) =>
    Api.get<PowerModel, [PowerModel]>("/monthlypowerdata", {
      params: {
        start,
        end,
      },
    });

  getPrediction = () => Api.get<[PredictionModel]>("/monthlypowerprediction");

  getScreens = () => Api.get<PredictionModel>("/screenstats");

  sendPower = async (name: string, amt: number) =>
    Api.post("/powerupdate", {
      name,
      amt
    });
}
export const powerApi = new PowerApi();
