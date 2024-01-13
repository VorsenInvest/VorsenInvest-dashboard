<script>
    import { onMount } from "svelte";
    import comingSoon from "../../../../assets/images/comingsoon.png";
    import Img4 from "../../../../assets/images/small/img-4.jpg";

    onMount(() => {
        var options = {
            chart: {
                height: 315,
                type: "radialBar",
            },
            series: [67],
            plotOptions: {
                radialBar: {
                    hollow: {
                        margin: 15,
                        size: "65%",
                        image: comingSoon,
                        imageWidth: 56,
                        imageHeight: 56,
                        imageClipped: false,
                    },
                    dataLabels: {
                        name: {
                            show: false,
                            color: "#fff",
                        },
                        value: {
                            show: true,
                            color: "#333",
                            offsetY: 65,
                            fontSize: "22px",
                        },
                    },
                },
            },
            fill: {
                type: "image",
                image: {
                    src: [Img4],
                },
            },
            stroke: {
                lineCap: "round",
            },
            labels: ["Volatility"],
        };
        const chart = new ApexCharts(
            document.querySelector("#imageradialchart"),
            options
        );
        chart.render();
    });
</script>

<div id="imageradialchart" class="apex-charts" dir="ltr" />