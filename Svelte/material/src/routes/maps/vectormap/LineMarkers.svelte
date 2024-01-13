<script>
	import {onMount} from 'svelte';
	export let dataColors;
	import { browser } from "$app/environment"
	let map;

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

	var MarkersColors = getChartColorsArray(dataColors);

	
	onMount(() => {
		map = new jsVectorMap({
                selector: document.querySelector("#LineMarkersVectorChart"),
                map: 'world',
                zoomOnScroll: false,
                zoomButtons: false, 
                showTooltip: false,
                regionStyle: {
                    initial: {
                        stroke: "#9599ad",
                        strokeWidth: 0.25,
                        fill: MarkersColors[0],
                        fillOpacity: 1,
                    },
                },
                markers: [{
                    name: "Greenland",
                    coords: [72, -42]
                },
                {
                    name: "Canada",
                    coords: [56.1304, -106.3468]
                },
                {
                    name: "Brazil",
                    coords: [-14.2350, -51.9253]
                },
                {
                    name: "Egypt",
                    coords: [26.8206, 30.8025]
                },
                {
                    name: "Russia",
                    coords: [61, 105]
                },
                {
                    name: "China",
                    coords: [35.8617, 104.1954]
                },
                {
                    name: "United States",
                    coords: [37.0902, -95.7129]
                },
                {
                    name: "Norway",
                    coords: [60.472024, 8.468946]
                },
                {
                    name: "Ukraine",
                    coords: [48.379433, 31.16558]
                },
                ],
                lines: [{
                    from: "Canada",
                    to: "Egypt"
                },
                {
                    from: "Russia",
                    to: "Egypt"
                },
                {
                    from: "Greenland",
                    to: "Egypt"
                },
                {
                    from: "Brazil",
                    to: "Egypt"
                },
                {
                    from: "United States",
                    to: "Egypt"
                },
                {
                    from: "China",
                    to: "Egypt"
                },
                {
                    from: "Norway",
                    to: "Egypt"
                },
                {
                    from: "Ukraine",
                    to: "Egypt"
                },
                ],
                lineStyle: {
                    animation: true,
                    strokeDasharray: "6 3 6",
                },
            })
		})
</script>

<div id="LineMarkersVectorChart" class="apex-charts" dir="ltr"></div>
<style>
    .apex-charts {
        width: 100%;
        height: 100%;
    }
</style>
