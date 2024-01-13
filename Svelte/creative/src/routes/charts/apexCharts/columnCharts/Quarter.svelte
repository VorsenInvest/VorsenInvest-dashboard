<script>
	import {onMount} from 'svelte';

	var optionsQuarter = {
		chart: {
			id: "barQuarter",
			height: 330,
			width: "100%",
			type: "bar",
			stacked: true,
		},
		series: [
			{
				data: [],
			},
		],
		plotOptions: {
			bar: {
				columnWidth: "50%",
				horizontal: false,
			},
		},
		legend: {
			show: false,
		},
		grid: {
			yaxis: {
				lines: {
					show: false,
				},
			},
			xaxis: {
				lines: {
					show: true,
				},
			},
		},
		yaxis: {
			labels: {
				show: false,
			},
		},
		title: {
			text: "Quarterly Results",
			offsetX: 10,
			style: {
				fontWeight: 500,
			},
		},
		tooltip: {
			x: {
				formatter: function (val, opts) {
					return opts.w.globals.seriesNames[opts.seriesIndex];
				},
			},
			y: {
				title: {
					formatter: function (val, opts) {
						return opts.w.globals.labels[opts.dataPointIndex];
					},
				},
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#quarterchart"), optionsQuarter)
  		chart.render()
	})
</script>

<div id="quarterchart" class="apex-charts" dir="ltr"></div>
