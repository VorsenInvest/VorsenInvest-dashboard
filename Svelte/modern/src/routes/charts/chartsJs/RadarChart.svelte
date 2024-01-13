<script>
    import { Radar } from 'svelte-chartjs';
    export let dataColors;
    import { browser } from "$app/environment"

    import {
        Chart as ChartJS,
        Title,
        Tooltip,
        Legend,
        PointElement,
        RadialLinearScale,
        LineElement,
    } from 'chart.js';

    ChartJS.register(
        Title,
        Tooltip,
        Legend,
        PointElement,
        RadialLinearScale,
        LineElement
    );

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

    var radarChartColors = getChartColorsArray(dataColors);
    var data={};

    if (radarChartColors) {

        data = {
            labels: [
                "Eating",
                "Drinking",
                "Sleeping",
                "Designing",
                "Coding",
                "Cycling",
                "Running",
            ],
            datasets: [
                {
                    label: "Desktops",
                    backgroundColor: radarChartColors[0],
                    borderColor: radarChartColors[1], //"#2ab57d",
                    pointBackgroundColor: radarChartColors[1], //"#2ab57d",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: radarChartColors[1], //"#2ab57d",
                    data: [65, 59, 90, 81, 56, 55, 40],
                },
                {
                    label: "Tablets",
                    backgroundColor: radarChartColors[2], //"rgba(81, 86, 190, 0.2)",
                    borderColor: radarChartColors[3], //"#5156be",
                    pointBackgroundColor: radarChartColors[3], //"#5156be",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: radarChartColors[3], //"#5156be",
                    data: [28, 48, 40, 19, 96, 27, 100],
                },
            ],
        };
    }
    
</script>

<Radar {data} option={{ responsive: true }} class="chartjs-chart" />
