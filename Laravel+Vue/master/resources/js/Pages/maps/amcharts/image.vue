<script>
import * as am5 from "@amcharts/amcharts5";
import * as am5map from "@amcharts/amcharts5/map";
import am5geodata_worldLow from "@amcharts/amcharts5-geodata/worldLow";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";

import logoSm from "@assets/images/logo-sm.png";

export default {
    methods: {
        imageChart() {
            let imageRoot = am5.Root.new("imageChartDiv");

            imageRoot.setThemes([am5themes_Animated.new(imageRoot)]);


            let ImageChart = imageRoot.container.children.push(
                am5map.MapChart.new(imageRoot, {
                    panX: "none",
                    panY: "none",
                    opacity: 1,
                    projection: am5map.geoMercator(),
                })
            );

            ImageChart.series.push(
                am5map.MapPolygonSeries.new(imageRoot, {
                    geoJSON: am5geodata_worldLow,
                    exclude: ["AQ"],
                    fill: am5.color("rgb(222, 226, 232)"),
                    stroke: am5.color("#fff"),
                })
            );

            // Create point series
            var pointSeries = ImageChart.series.push(
                am5map.MapPointSeries.new(imageRoot, {})
            );

            pointSeries.bullets.push(function () {
                return am5.Bullet.new(imageRoot, {
                    sprite: am5.Picture.new(imageRoot, {
                        width: 18,
                        height: 20,
                        src: logoSm,
                    }),
                });
            });

            pointSeries.bullets.push(function () {
                return am5.Bullet.new(imageRoot, {
                    sprite: am5.Label.new(imageRoot, {
                        text: "{name}",
                        populateText: true
                    })
                });
            });

            pointSeries.pushDataItem({ latitude: 31.9474, longitude: 35.2272 });
            pointSeries.pushDataItem({ latitude: 61.524, longitude: 105.3188 });
            pointSeries.pushDataItem({ latitude: 56.1304, longitude: -106.3468 });
            pointSeries.pushDataItem({ latitude: 71.7069, longitude: -42.6043 });


        }
    },
    mounted() {
        this.imageChart();
    }
};
</script>

<template>
    <div id="imageChartDiv" style="height: 420px"></div>
</template>
