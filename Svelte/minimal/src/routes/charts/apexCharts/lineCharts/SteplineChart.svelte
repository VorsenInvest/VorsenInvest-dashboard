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

    var SteplineChartColors = getChartColorsArray(dataColors);

    const options = {
        chart: {
            height: 350,
            type: "line",
            toolbar: {
				show: false,
			},
        },
        stroke: {
            curve: "stepline",
        },
        
        series: [
            {
                data: [34, 44, 54, 21, 12, 43, 33, 23, 66, 66, 58],
            },
        ],
        dataLabels: {
            enabled: !1,
        },
        title: {
            text: "Stepline Chart",
            align: "left",
            style: {
                fontWeight: 500,
            },
        },
        markers: {
            hover: {
                sizeOffset: 4,
            },
        },
        colors: SteplineChartColors,
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#SteplineChart"), options)
  		chart.render()
	})
</script>

<div id="SteplineChart" class="apex-charts" dir="ltr"></div>
