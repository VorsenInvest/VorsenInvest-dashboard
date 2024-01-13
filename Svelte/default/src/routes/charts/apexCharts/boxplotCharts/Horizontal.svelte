<script>
    import { onMount } from "svelte";
    import { browser } from "$app/environment"

    export let dataColors;

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

    onMount(() => {
        var chartBoxBasicColors = getChartColorsArray(dataColors);
        var options = {
            chart: {
                type: "boxPlot",
                height: 350,
                toolbar: {
                    show: false,
                },
            },
            series: [
                {
                    type: "boxPlot",
                    data: [
                        {
                            x: "Category A",
                            y: [54, 66, 69, 75, 88],
                        },
                        {
                            x: "Category B",
                            y: [43, 65, 69, 76, 81],
                        },
                        {
                            x: "Category C",
                            y: [31, 39, 45, 51, 59],
                        },
                        {
                            x: "Category D",
                            y: [39, 46, 55, 65, 71],
                        },
                        {
                            x: "Category E",
                            y: [29, 31, 35, 39, 44],
                        },
                        {
                            x: "Category F",
                            y: [41, 49, 58, 61, 67],
                        },
                        {
                            x: "Category G",
                            y: [54, 59, 66, 71, 88],
                        },
                    ],
                },
            ],
            plotOptions: {
                bar: {
                    horizontal: true,
                    barHeight: "50%",
                },
                boxPlot: {
                    colors: {
                        upper: chartBoxBasicColors[0],
                        lower: chartBoxBasicColors[1],
                    },
                },
            },
            stroke: {
                colors: [chartBoxBasicColors[2]],
            },
        };
        const chart = new ApexCharts(
            document.querySelector("#horizontalchart"),
            options
        );
        chart.render();
    });
</script>

<div id="horizontalchart" class="apex-charts" dir="ltr" />
