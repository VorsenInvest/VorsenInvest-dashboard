<script>
	import {onMount} from 'svelte';
	export let dataColors;
	import { browser } from "$app/environment"

	import smallImage1 from "../../../../assets/images/small/img-1.jpg";
	import smallImage2 from "../../../../assets/images/small/img-2.jpg";
	import smallImage3 from "../../../../assets/images/small/img-3.jpg";
	import smallImage4 from "../../../../assets/images/small/img-4.jpg";

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

	var chartPieImageColors = getChartColorsArray(dataColors);
	const options = {
		chart: {
			width: 380,
			type: "pie",
		},
		series: [44, 33, 54, 45],
		colors: chartPieImageColors,
		fill: {
			type: "image",
			opacity: 0.85,
			image: {
				src: [smallImage1, smallImage2, smallImage3, smallImage4],
				width: 25,
				imagedHeight: 25,
			},
		},
		stroke: {
			width: 4,
		},
		dataLabels: {
			enabled: true,
			style: {
				colors: ["#111"],
			},
			background: {
				enabled: true,
				foreColor: "#fff",
				borderWidth: 0,
			},
		},
		legend: {
        	position: 'bottom'
    	}
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#imagepiechart"), options)
  		chart.render()
	})
</script>

<div id="imagepiechart" class="apex-charts" dir="ltr"></div>
