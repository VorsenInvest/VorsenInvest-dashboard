<script>
	export let color, data,id;
	import {onMount} from 'svelte'; 

	const options = {
		chart: {
			type: 'area',
			height: '50',
			sparkline: {
				enabled: true
			}
		},
		series: [
			{
				data: data
			}
		],
		fill: {
			type: 'gradient',
			gradient: {
				shadeIntensity: 1,
				inverseColors: false,
				opacityFrom: 0.45,
				opacityTo: 0.05,
				stops: [20, 100, 100, 100]
			}
		},
		stroke: {
			curve: 'smooth',
			width: 2
		},
		colors: [color],
		tooltip: {
			fixed: {
				enabled: false
			},
			x: {
				show: false
			},
			y: {
				title: {
					formatter: function (seriesName) {
						return '';
					}
				}
			},
			marker: {
				show: false
			}
		}
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#sellercharts"+id), options)
  		chart.render()
	})
</script>

<div id={"sellercharts"+id} class="apex-charts" dir="ltr"></div>
