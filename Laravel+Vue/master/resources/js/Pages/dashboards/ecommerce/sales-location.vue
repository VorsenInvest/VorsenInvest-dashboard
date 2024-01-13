<script>
import * as am5 from "@amcharts/amcharts5";
import * as am5map from "@amcharts/amcharts5/map";
import am5geodata_worldLow from "@amcharts/amcharts5-geodata/worldLow";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";

export default {
  mounted() {
    this.initialMap();
  },
  methods: {
    initialMap() {
      // Create a chart instance
      const root = am5.Root.new("chartDiv");
      root.setThemes([am5themes_Animated.new(root)]);
      let chart = root.container.children.push(
        am5map.MapChart.new(root, {
          panX: "none",
          panY: "none",
          opacity: 1,
          projection: am5map.geoMercator(),
        })
      );

      chart.series.push(
        am5map.MapPolygonSeries.new(root, {
          geoJSON: am5geodata_worldLow,
          exclude: ["AQ"],
          fill: am5.color("rgb(222, 226, 232)"),
          stroke: am5.color("#fff"),
        })
      );

      let colorset = am5.ColorSet.new(root, {});
      // Create point series
      var pointSeries = chart.series.push(
        am5map.MapPointSeries.new(root, {})
      );

      pointSeries.bullets.push(function () {
        return am5.Bullet.new(root, {
          sprite: am5.Circle.new(root, {
            radius: 4,
            stroke: colorset.next(),
            strokeWidth: 6,
            strokeOpacity: 0.5,
            fill: colorset.next(),
            fillOpacity: 1,
            tooltipText: "{title}",
            cursorOverStyle: 'pointer',
          }),
        });
      });

      pointSeries.pushDataItem({ title: "Greenland", latitude: 71.7069, longitude: -42.6043 });
      pointSeries.pushDataItem({ title: "Russia", latitude: 61.5240, longitude: 105.3188 });
      pointSeries.pushDataItem({ title: "Canada", latitude: 56.1304, longitude: -106.3468 });


      // adding zoom control
      // chart.set("zoomControl", am5map.ZoomControl.new(root, {}));
    },
  },
};
</script>

<template>
  <BCard no-body class="card-height-100">
    <BCardHeader class="align-items-center d-flex">
      <BCardTitle class="mb-0 flex-grow-1">Sales by Locations</BCardTitle>
      <div class="flex-shrink-0">
        <BButton type="button" variant="soft-primary" size="sm" class="material-shadow-none">
          Export Report
        </BButton>
      </div>
    </BCardHeader>
    <div id="chartDiv" class="chart-container" style="height: 245px; width:auto"></div>
    <BCardBody>
      <div class="px-2 py-2 mt-1">
        <p class="mb-1">Canada <span class="float-end">75%</span></p>
        <BProgress striped :value="75" class="mt-2" variant="primary" style="height: 6px;" />

        <p class="mt-3 mb-1">Greenland <span class="float-end">47%</span></p>
        <BProgress striped :value="47" class="mt-2" variant="primary" style="height: 6px;" />

        <p class="mt-3 mb-1">Russia <span class="float-end">82%</span></p>
        <BProgress striped :value="82" class="mt-2" variant="primary" style="height: 6px;" />
      </div>
    </BCardBody>
  </BCard>
</template>