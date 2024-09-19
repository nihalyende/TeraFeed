<template>
  <div class="container">
    <form @submit.prevent="handleSubmit">
      <label for="population">Population:</label>
      <input type="range" v-model="population" id="population" min="1378946751" max="1601689794" /><br />

      <label for="unemployment_between_15_24">Unemployment between age 15-24:</label>
      <input type="range" v-model="unemployment_between_15_24" id="unemployment_between_15_24" min="18.3771323529412" max="18.8077389390507" step="0.0001"/><br />

      <label for="unemployment_above_25">Unemployment Above age 25+:</label>
      <input type="range" v-model="unemployment_above_25" id="unemployment_above_25" min="7.814632353" max="8.11818838389546" step="0.0001"/><br />

      <input type="range" v-model="share_of_agricultural_land" style="display: none!important;" id="share_of_agricultural_land" min="78.92050154" max="79.42" step="0.0001" />

      <label for="people_employed_in_agriculture">People employed in agricultural sector in millions:</label>
      <input type="range" v-model="people_employed_in_agriculture" id="people_employed_in_agriculture" min="230" max="248" step="1" /><br />

      <input type="range" style="display: none!important;" v-model="total_employment_in_africa" id="total_employment_in_africa" min="470" max="541.781704552942" />

      <label for="import_us_thousand">Imports Africa:</label>
      <input type="range" v-model="import_us_thousand" id="import_us_thousand" min="58033618.41" max="66199586.45" /><br />

      <label for="export_us_thousand">Exports Africa:</label>
      <input type="range" v-model="export_us_thousand" id="export_us_thousand" min="71067999.24" max="76370336.17" /><br />

      <label for="net_official_development_assistance_and_aid">Net official Development Assistance And Aid:</label>
      <input type="range" v-model="net_official_development_assistance_and_aid" id="net_official_development_assistance_and_aid" min="63" max="69.6493821827028" /><br />

      <label for="credit_received_from_other_countries_in_billions">Credit Received From Other Countries in Billions:</label>
      <input type="range" v-model="credit_received_from_other_countries_in_billions" id="credit_received_from_other_countries_in_billions" min="76987.40485" max="104182.7117" /><br />

      <label for="gasoline">Price of Gasoline:</label>
      <input type="range" v-model="gasoline" id="gasoline" min="1.37" max="1.599835498" step="0.001" /><br />

      <input type="hidden" v-model="storing_data" />

      <button type="submit">Submit</button>
      <div>{{ predictionResult }}</div>
    </form>
    <canvas id="myChart" width="400" height="300"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
let predictedData= [315000000];
let predictedDataLabels= [0];

export default {
  data() {
    return {
      population: 1601689794,
      unemployment_between_15_24: 18.8077389390507,
      unemployment_above_25: 8.11818838389546,
      share_of_agricultural_land: 78.92050154,
      people_employed_in_agriculture: 230,
      total_employment_in_africa: 470,
      import_us_thousand: 58033618.41,
      export_us_thousand: 71067999.24,
      net_official_development_assistance_and_aid: 63,
      credit_received_from_other_countries_in_billions: 76987.40485,
      gasoline: 1.599835498,
      storing_data: 26,
      predictionResult: '',
    };
  },
  mounted() {
    this.renderChart();
  },
  methods: {
    renderChart() {
      const ctx = document.getElementById("myChart").getContext("2d");
      const myChart = new Chart(ctx, {
        type: "line",
        data: {
          labels: predictedDataLabels,
          datasets: [
            {
              label: "Predicted Value",
              data: predictedData,
              fill: true,
              borderColor: "rgb(182,88,91)",
              tension: 0.1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              ticks: {
                color: 'white'
              },
              grid: {
                color: 'rgba(200, 200, 200, 0.5)'
              }
            },
            x: {
              ticks: {
                color: 'white'
              },
              grid: {
                color: 'rgba(200, 200, 200, 0.5)'
              }
            }
          },
          plugins: {
            legend: {
              labels: {
                color: 'white'
              }
            }
          }
        }
      });

      this.$data.myChart = myChart;
    },
    updateChartData() {
      let myChart = this.$data.myChart;
      predictedData.push(this.storing_data);
      predictedDataLabels.push(predictedDataLabels[predictedDataLabels.length - 1] + 1);
      console.log( myChart.data.datasets[0].data);
      myChart.destroy();
      const ctx = document.getElementById("myChart").getContext("2d");
      myChart = new Chart(ctx, {
        type: "line",
        data: {
          labels: predictedDataLabels,
          datasets: [
            {
              label: "Predicted Value",
              data: predictedData,
              fill: true,
              borderColor: "rgb(182,88,91)",
              tension: 0.1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              ticks: {
                color: 'white'
              },
              grid: {
                color: 'rgba(200, 200, 200, 0.5)'
              }
            },
            x: {
              ticks: {
                color: 'white'
              },
              grid: {
                color: 'rgba(200, 200, 200, 0.5)'
              }
            }
          },
          plugins: {
            legend: {
              labels: {
                color: 'white'
              }
            }
          }
        }
      });

      this.$data.myChart = myChart;
    },
    handleSubmit() {
      fetch("http://localhost:5000/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          population: this.population,
          unemployment_between_15_24: this.unemployment_between_15_24,
          unemployment_above_25: this.unemployment_above_25,
          share_of_agricultural_land: this.share_of_agricultural_land,
          people_employed_in_agriculture: this.people_employed_in_agriculture,
          total_employment_in_africa: this.total_employment_in_africa,
          import_us_thousand: this.import_us_thousand,
          export_us_thousand: this.export_us_thousand,
          net_official_development_assistance_and_aid: this.net_official_development_assistance_and_aid,
          credit_received_from_other_countries_in_billions: this.credit_received_from_other_countries_in_billions,
          gasoline: this.gasoline,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          this.predictionResult = `Predicted Output: ${data.prediction}`;
          this.storing_data = data.prediction;
          this.updateChartData();
        });
    }
  }
};
</script>
