<script>
    import { onMount } from "svelte";
    import { browser } from "$app/environment";
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

    var PopularityChartColors = getChartColorsArray(dataColors);

    const options = {
        chart: {
            type: "bar",
            height: 260,
            stacked: true,
            toolbar: {
                show: false,
            },
        },
        series: [
            {
                name: "Like",
                data: [12.45, 16.2, 8.9, 11.42, 12.6, 18.1, 18.2, 14.16],
            },
            {
                name: "Share",
                data: [
                    -11.45, -15.42, -7.9, -12.42, -12.6, -18.1, -18.2, -14.16,
                ],
            },
        ],
        plotOptions: {
            bar: {
                columnWidth: "20%",
                borderRadius: [4, 4],
            },
        },
        dataLabels: {
            enabled: false,
            textAnchor: "top",
        },
        colors: PopularityChartColors,

        fill: {
            opacity: 1,
        },
        legend: {
            position: "top",
            horizontalAlign: "right",
        },
        yaxis: {
            labels: {
                show: false,
                formatter: function (y) {
                    return y.toFixed(0) + "%";
                },
            },
        },
        xaxis: {
            categories: [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
            ],
            labels: {
                rotate: -90,
            },
        },
    };

    onMount(() => {
        const chart = new ApexCharts(
            document.querySelector("#populariychartcharts"),
            options
        );
        chart.render();
    });
</script>

<div id="populariychartcharts" class="apex-charts mt-n4" dir="ltr" />
