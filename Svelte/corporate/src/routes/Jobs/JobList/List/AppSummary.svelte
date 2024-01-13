<script>
    import {onMount} from 'svelte';
    export let dataColors;
    import { browser } from "$app/environment"

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
    var chartDonutBasicColors = getChartColorsArray(dataColors);

    var series = [98, 63, 35];
    var options = {
        labels: ["New Application", "Approved", "Rejected"],
        chart: {
        height: 300,
        type: "donut",
        },
        series: series,
        legend: {
        position: "bottom",
        },
        dataLabels: {
        dropShadow: {
            enabled: false,
        },
        },
        colors: chartDonutBasicColors,
    };
    onMount(() => {
		const chart = new ApexCharts(document.querySelector("#appsummarychart"), options)
  		chart.render()
	})
</script>
<div id="appsummarychart" class="apex-charts" dir="ltr"></div>