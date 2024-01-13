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

    var chartRadialbarBasicColors = getChartColorsArray(dataColors);

    var options = {
        chart: {
            height: 350,
            type: "radialBar",
        },
        series: [70],
        plotOptions: {
            radialBar: {
                hollow: {
                    size: "70%",
                },
            },
        },
        labels: ["Cricket"],
        colors: chartRadialbarBasicColors,
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#simpleradialbarchart"), options)
  		chart.render()
	})
</script>

<div id="simpleradialbarchart" class="apex-charts" dir="ltr"></div>
