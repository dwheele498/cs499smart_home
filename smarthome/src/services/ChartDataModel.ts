export interface ChartDataModel{
        labels: string[],
        datasets: [
          {
            label: string,
            data: number[],
            backgroundColor: CanvasGradient
          },
        ],
}