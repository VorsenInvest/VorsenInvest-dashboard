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

    var MarketplaceChartColors = getChartColorsArray(dataColors);

    var options = {
        chart: {
            id:"dashboardnftcharts",
            height: 350,
            type: "line",
            zoom: {
                enabled: false,
            },
            toolbar: {
                show: false,
            },
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            curve: "smooth",
            width: 3,
        },
        series: [{
            name: "Artwork",
            data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
        },
        {
            name: "Auction",
            data: [40, 120, 83, 45, 31, 74, 35, 34, 78]
        },
        {
            name: "Creators",
            data: [95, 35, 20, 130, 64, 22, 43, 45, 31]
        }],
        colors: MarketplaceChartColors,
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
                "Sep",
            ],
        },
    };

    onMount(() => {
        const chart = new ApexCharts(document.querySelector("#dashboardnftcharts"),options);
        chart.render();
    });
</script>

<div id="dashboardnftcharts" class="apex-charts" dir="ltr" />
