import * as models from './services/models';
import {weatherApi} from './services/WeatherApi';
import {waterApi} from './services/WaterApi';
import { powerApi } from './services/PowerApi';

export async function WeatherPrediction(
    value: number[],
    label: string[],
  
  ): Promise<models.PredcitGraphModel>{
    const wpModel = {} as models.PredcitGraphModel;
    await weatherApi.getPrediction().then((result: any)=>{
      result.data.forEach((prediction: models.PredictionModel) => {
        label.push(prediction[0]);
        value.push(Math.floor(prediction[1]));
      });
    }).finally(()=>{
      const graphData = {
        labels: label,
        datasets: [
          {
            label: "Predicted Avg Temp Per Day",
            data: value,
            backgroundColor: ["#32a852"],
            borderColor: "red",
          },
        ],
      } as models.GraphData;
      wpModel.labels = label;
      wpModel.value = value;
      wpModel.chartData = graphData;
  
    })
    return wpModel;
  
  }

  export async function WaterPrediction(
    value: number[],
    label: string[],
  
  ): Promise<models.PredcitGraphModel>{
    const wpModel = {} as models.PredcitGraphModel;
    await waterApi.getPrediction().then((result: any)=>{
      result.data.forEach((prediction: models.PredictionModel) => {
        
        label.push(prediction[0]);
        value.push(Math.floor(prediction[1]));
      });
    }).finally(()=>{
      const graphData = {
        labels: label,
        datasets: [
          {
            label: "Predicted Total Water Usage Per Day",
            data: value,
            backgroundColor: ["#32a852"],
            borderColor: "blue",
          },
        ],
      } as models.GraphData;
      wpModel.labels = label;
      wpModel.value = value;
      wpModel.chartData = graphData;
  
    })
    return wpModel;
  
  }

  export async function PowerPrediction(
    value: number[],
    label: string[],
  
  ): Promise<models.PredcitGraphModel>{
    const wpModel = {} as models.PredcitGraphModel;
    await powerApi.getPrediction().then((result: any)=>{
      result.data.forEach((prediction: models.PredictionModel) => {
        label.push(prediction[0]);
        value.push((prediction[1]));
      });
    }).finally(()=>{
      const graphData = {
        labels: label,
        datasets: [
          {
            label: "Predicted Total Power Usage Per Day",
            data: value,
            backgroundColor: ["#32a852"],
            borderColor: "orange",
          },
        ],
      } as models.GraphData;
      wpModel.labels = label;
      wpModel.value = value;
      wpModel.chartData = graphData;
  
    })
    return wpModel;
  
  }