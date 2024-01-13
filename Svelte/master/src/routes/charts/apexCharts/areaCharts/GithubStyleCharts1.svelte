<script>
	import {onMount} from 'svelte';
	import allseries from "../series";
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

	var BasicAreaChartsColors = getChartColorsArray(dataColors);
    var options = {
        chart: {
            height: 170,
            type: 'area',
            toolbar: {
                autoSelected: 'selection',
            },
            brush: {
                enabled: true,
                target: 'chartyear'
            },
            selection: {
                enabled: true,
                xaxis: {
                    min: new Date('26 Jan 2014').getTime(),
                    max: new Date('29 Mar 2015').getTime()
                }
            },
        },
		series : [{
			name: 'commits',
			data: allseries.githubdata.series
		}],
        colors: BasicAreaChartsColors,
        dataLabels: {
            enabled: false
        },
        stroke: {
            width: 0,
            curve: 'smooth'
        },
        fill: {
            opacity: 1,
            type: 'solid'
        },
        legend: {
            position: 'top',
            horizontalAlign: 'left'
        },
        xaxis: {
            type: 'datetime'
        },
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#githubstylechart1"), options)
  		chart.render()
	})
</script>

<div id="githubstylechart1" class="apex-charts" dir="ltr"></div>
