<script>
    import { Polar } from 'svelte-chartjs';
    export let dataColors;
    import { browser } from "$app/environment"

    import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    ArcElement,
    RadialLinearScale,
  } from 'chart.js';

  ChartJS.register(Title, Tooltip, Legend, ArcElement, RadialLinearScale);

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

    var polarAreaChartColors = getChartColorsArray(dataColors);
    var data={};

    if (polarAreaChartColors) {

        data = {
        labels: ["Series 1", "Series 2", "Series 3", "Series 4"],
        datasets: [
            {
                data: [11, 16, 7, 18],
                backgroundColor: polarAreaChartColors,
                label: "My dataset", // for legend
                hoverBorderColor: "#fff",
            },
        ],
    };
}
</script>

<Polar {data} option={{ responsive: true }} class="chartjs-chart" />
