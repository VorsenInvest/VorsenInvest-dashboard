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

      var Brazil = pointSeries.pushDataItem({ latitude: -14.2350, longitude: -51.9253, title: "Brazil" });
      var Unitedstates = pointSeries.pushDataItem({ latitude: 37.0902, longitude: -95.7129, title: "United States" });
      var Canada = pointSeries.pushDataItem({ latitude: 56.1304, longitude: -106.3468, title: "Canada" });
      var Greenland = pointSeries.pushDataItem({ latitude: 71.7069, longitude: -42.6043, title: "Greenland" });
      var Norway = pointSeries.pushDataItem({ latitude: 60.4720, longitude: 8.4689, title: "Norway" });
      var Ukraine = pointSeries.pushDataItem({ latitude: 48.3794, longitude: 31.1656, title: "Ukraine" });
      var Egypt = pointSeries.pushDataItem({ latitude: 26.8206, longitude: 30.8025, title: "Egypt" });
      var Russia = pointSeries.pushDataItem({ latitude: 61.5240, longitude: 105.3188, title: "Russia" });
      var China = pointSeries.pushDataItem({ latitude: 35.8617, longitude: 104.1954, title: "China" });


      var lineSeries = chart.series.push(
        am5map.MapLineSeries.new(root, { lineType: "straight", stateAnimationEasing: am5.ease.out(am5.ease.cubic), })
      );


      lineSeries.pushDataItem({
        pointsToConnect: [Greenland, Egypt, China, Egypt, Brazil, Egypt, Unitedstates, Egypt, Norway, Egypt, Ukraine, Egypt, Russia, Egypt, Canada, Egypt]
      });

      lineSeries.mapLines.template.setAll({
        stroke: am5.color('rgb(128, 128, 128)'),
        fill: am5.color('rgb(128, 128, 128)'),
        strokeWidth: 1,
        strokeOpacity: 1,
        strokeDasharray: [6, 3, 6],
      });

      // adding zoom control
      // chart.set("zoomControl", am5map.ZoomControl.new(root, {}));
    },
  },
};
</script>

<template>
  <BCard no-body class="card-height-100">
    <BCardHeader class="align-items-center d-flex">
      <BCardTitle class="mb-0 flex-grow-1">Live Users By Country</BCardTitle>
      <div class="flex-shrink-0">
        <BButton type="button" variant="soft-primary" size="sm" class="material-shadow-none">
          Export Report
        </BButton>
      </div>
    </BCardHeader>

    <BCardBody>
      <!-- <div id="country-map" style="height: 252px;"></div> -->
      <div id="chartDiv" class="chart-container" style="height: 245px; width:auto"></div>
      <div role="progressbar"></div>
      <div class="table-responsive table-card mt-3">
        <table class="table table-borderless table-sm table-centered align-middle table-nowrap mb-1">
          <thead class="text-muted border-dashed border border-start-0 border-end-0 bg-light-subtle">
            <tr>
              <th>Duration (Secs)</th>
              <th style="width: 30%">Sessions</th>
              <th style="width: 30%">Views</th>
            </tr>
          </thead>
          <tbody class="border-0">
            <tr>
              <td>0-30</td>
              <td>2,250</td>
              <td>4,250</td>
            </tr>
            <tr>
              <td>31-60</td>
              <td>1,501</td>
              <td>2,050</td>
            </tr>
            <tr>
              <td>61-120</td>
              <td>750</td>
              <td>1,600</td>
            </tr>
            <tr>
              <td>121-240</td>
              <td>540</td>
              <td>1,040</td>
            </tr>
          </tbody>
        </table>
      </div>
    </BCardBody>
  </BCard>
</template>
