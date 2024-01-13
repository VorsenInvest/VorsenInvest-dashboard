<script>
	import {onMount} from 'svelte';
	export let dataColors;
	import { browser } from "$app/environment"
    import logosm from "../../../assets/images/logo-sm.png"
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
                selector: document.querySelector("#ImageMarkersVectorChart"),
                map: 'world',
                zoomOnScroll: false,
                zoomButtons: false, 
                showTooltip: false,
                selectedMarkers: [0, 2],
                regionStyle: {
                    initial: {
                        stroke: "#9599ad",
                        strokeWidth: 0.25,
                        fill: MarkersColors,
                        fillOpacity: 1,
                    },
                },
                markers: [{
                name: "Palestine",
                coords: [31.9474, 35.2272]
            },
            {
                name: "Russia",
                coords: [61.524, 105.3188]
            },
            {
                name: "Canada",
                coords: [56.1304, -106.3468]
            },
            {
                name: "Greenland",
                coords: [71.7069, -42.6043]
            },
                ],
                markerStyle: {
            initial: {
                fill: "#038edc"
            },
            selected: {
                fill: "red"
            }
        },
        labels: {
            markers: {
                render: function (marker) {
                    return marker.name
                }
            }
        },
        markerStyle: {
            initial: {
                image: logosm
            }
        },
                
            })
		})
</script>

<div id="ImageMarkersVectorChart" class="apex-charts" dir="ltr"></div>
<style>
    .apex-charts {
        width: 100%;
        height: 100%;
    }
</style>
