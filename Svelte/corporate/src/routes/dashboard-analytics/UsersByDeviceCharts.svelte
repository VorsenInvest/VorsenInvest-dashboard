<script>
    import { onMount } from "svelte";
    export let dataColors;
    import { browser } from "$app/environment";
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

    const dountchartUserDeviceColors = getChartColorsArray(dataColors);

    const options = {
        labels: ["Desktop", "Mobile", "Tablet"],
        chart: {
            type: "donut",
            height: 219,
        },
        series: [78.56, 105.02, 42.89],
        plotOptions: {
            pie: {
                size: 100,
                donut: {
                    size: "76%",
                },
            },
        },
        dataLabels: {
            enabled: false,
        },
        legend: {
            show: false,
            position: "bottom",
            horizontalAlign: "center",
            offsetX: 0,
            offsetY: 0,
            markers: {
                width: 20,
                height: 6,
                radius: 2,
            },
            itemMargin: {
                horizontal: 12,
                vertical: 0,
            },
        },
        stroke: {
            width: 0,
        },
        yaxis: {
            labels: {
                formatter: function (value) {
                    return value + "k Users";
                },
            },
            tickAmount: 4,
            min: 0,
        },
        colors: dountchartUserDeviceColors,
    };
    onMount(() => {
        const chart = new ApexCharts(
            document.querySelector("#userbtdevicechart"),
            options
        );
        chart.render();
    });
</script>

<div id="userbtdevicechart" class="apex-charts" dir="ltr" />
