<script>
    import { Doughnut } from 'svelte-chartjs';
    export let dataColors;
    import { browser } from "$app/environment"

    import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    ArcElement,
    CategoryScale,
  } from 'chart.js';

  ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);

    function getChartColorsArray(colors) {
        if (browser) {
            return colors.map(function (value) {
                var newValue = value.replace(" ", "");
                if (newValue.indexOf(",") === -1) {
                    var color = getComputedStyle(
                        document.documentElement
                    ).getPropertyValue(newValue);
                    if (color.indexOf("#") !== -1)
                        color = color.replace(" ", "");
                    if (color) return color;
                    else return newValue;
                } else {
                    var val = value.split(",");
                    if (val.length === 2) {
                        var rgbaColor = getComputedStyle(
                            document.documentElement
                        ).getPropertyValue(val[0]);
                        rgbaColor = "rgba(" + rgbaColor + "," + val[1] + ")";
                        return rgbaColor;
                    } else {
                        return newValue;
                    }
                }
            });
        }
    }

    var doughnutChartColors = getChartColorsArray(dataColors);
        var data={};

    if (doughnutChartColors) {

            data = {
            labels: ["Desktops", "Tablets"],
            datasets: [
                {
                    data: [300, 210],
                    backgroundColor: doughnutChartColors,
                    hoverBackgroundColor: doughnutChartColors,
                    hoverBorderColor: "#fff",
                },
            ],
        };
    }
</script>

<Doughnut {data} option={{ responsive: true }} class="chartjs-chart" />
