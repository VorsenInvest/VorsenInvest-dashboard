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

    var chartRadarBasicColors = getChartColorsArray(dataColors);

    var options = {
        chart: {
            height: 350,
            type: "radar",
            toolbar: {
                show: false,
            },
        },
        series: [
            {
                name: "Series 1",
                data: [80, 50, 30, 40, 100, 20],
            },
        ],
        colors: chartRadarBasicColors,
        xaxis: {
            categories: [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
            ],
        },
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#simpleradarchart"), options)
  		chart.render()
	})
</script>

<div id="simpleradarchart" class="apex-charts" dir="ltr"></div>
