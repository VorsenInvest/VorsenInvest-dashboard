<script>
	import { Card, CardBody, Col, Container, Row } from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";

	// Ratio Video 16:9

	const ratio169Code = `
<!-- Ratio Video 16:9 -->
<div class="ratio ratio-16x9">
    <iframe src="//www.youtube.com/embed/1y_kfWUCFDQ" title="YouTube video" allowfullscreen></iframe>
</div>
`;

	// Ratio Video 21:9

	const ratio219Code = `
<!-- Ratio Video 21:9 -->
<div class="ratio ratio-21x9">
    <iframe src="//www.youtube.com/embed/Z-fV2lGKnnU" title="YouTube video" allowfullscreen></iframe>
</div>
`;

	// Ratio Video 4:3

	const ratio43Code = `
<!-- Ratio Video 4:3 -->
<div class="ratio ratio-4x3">
    <iframe src="//www.youtube.com/embed/1y_kfWUCFDQ" title="YouTube video" allowfullscreen></iframe>
</div>
`;

	// Ratio Video 1:1

	const ratio11Code = `
<!-- Ratio Video 1:1 -->
<div class="ratio ratio-1x1">
    <iframe src="//www.youtube.com/embed/GfSZtaoc5bw" title="YouTube video" allowfullscreen></iframe>
</div>

`;

	// Custom Ratio Video

	const customRationCode = `
<!-- Custom Ratio Video -->
<div class="ratio ratio-16x9">
    <iframe src="//www.youtube.com/embed/2RZQN_ko0iU" title="YouTube video" allowfullscreen></iframe>
</div>

`;
</script>

<svelte:head>
	<title>Embed Video | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Embed Video" pageTitle="Base UI" />
		<Row>
			<Col xl={6}>
				<Card>
					<PreviewCardHeader title="Ratio Video 16:9" />
					<CardBody>
						<p class="text-muted">
							Wrap any embed in<code>&lt;iframe&gt;</code> tag, in
							a parent element, use
							<code>ratio-16x9</code> class to set aspect ratio 16:9.
						</p>
						<div class="live-preview">
							<div class="ratio ratio-16x9">
								<iframe
									class="rounded"
									src="//www.youtube.com/embed/1y_kfWUCFDQ"
									title="YouTube video"
									allowFullScreen
								/>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={ratio169Code}
								id="ratio169Code"
							/>
						</div>
					</CardBody>
				</Card>

				<Card>
					<PreviewCardHeader title="Ratio Video 4:3" />
					<CardBody>
						<p class="text-muted">
							Use <code>ratio-4x3</code> class to set aspect ratio
							4:3.
						</p>
						<div class="live-preview">
							<div class="ratio ratio-4x3">
								<iframe
									class="rounded"
									src="//www.youtube.com/embed/PHcgN1GTjdU"
									title="YouTube video"
									allowFullScreen
								/>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={ratio43Code}
								id="ratio43Code"
							/>
						</div>

						<div class="d-none code-view">
							<pre class="language-markup">
                                <code
									>&lt;!-- Ratio Video 4:3 --&gt;
                                    &lt;div class=&quot;ratio ratio-4x3&quot;&gt;
                                    &lt;iframe src=&quot;//www.youtube.com/embed/1y_kfWUCFDQ&quot; title=&quot;YouTube video&quot; allowFullScreen&gt;&lt;/iframe&gt;
                                    &lt;/div&gt;</code
								></pre>
						</div>
					</CardBody>
				</Card>

				<Card>
					<PreviewCardHeader title="Custom Ratios" />
					<CardBody>
						<p class="text-muted">
							Use <code>--vz-aspect-ratio: 50%</code> to style element
							to set aspect ratio 2:1.
						</p>
						<div class="live-preview">
							<div class="ratio ratio-16x9">
								<iframe
									class="rounded"
									src="//www.youtube.com/embed/2RZQN_ko0iU"
									title="YouTube video"
									allowFullScreen
								/>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={customRationCode}
								id="customRationCode"
							/>
						</div>

						<div class="d-none code-view">
							<pre class="language-markup">
                                <code
									>&lt;!-- Custom Ratio Video --&gt;
                                    &lt;div class=&quot;ratio&quot; style=&quot;--vz-aspect-ratio: 50%;&quot;&gt;
                                    &lt;iframe src=&quot;//www.youtube.com/embed/2RZQN_ko0iU&quot; title=&quot;YouTube video&quot; allowFullScreen&gt;&lt;/iframe&gt;
                                    &lt;/div&gt;</code
								></pre>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<PreviewCardHeader title="Ratio Video 21:9" />
					<CardBody>
						<p class="text-muted">
							Use <code>ratio-21x9</code> class to set aspect ratio
							21:9.
						</p>
						<div class="live-preview">
							<div class="ratio ratio-21x9">
								<iframe
									class="rounded"
									src="//www.youtube.com/embed/Z-fV2lGKnnU"
									title="YouTube video"
									allowFullScreen
								/>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={ratio219Code}
								id="ratio219Code"
							/>
						</div>

						<div class="d-none code-view">
							<pre class="language-markup">
                                <code
									>&lt;!-- Ratio Video 21:9 --&gt;
                                    &lt;div class=&quot;ratio ratio-21x9&quot;&gt;
                                    &lt;iframe src=&quot;//www.youtube.com/embed/Z-fV2lGKnnU&quot; title=&quot;YouTube video&quot; allowFullScreen&gt;&lt;/iframe&gt;
                                    &lt;/div&gt;</code
								></pre>
						</div>
					</CardBody>
				</Card>

				<Card>
					<PreviewCardHeader title="Ratio Video 1:1" />
					<CardBody>
						<p class="text-muted">
							Use <code>ratio-1x1</code> class to set aspect ratio
							1:1.
						</p>
						<div class="live-preview">
							<div class="ratio ratio-1x1">
								<iframe
									class="rounded"
									src="//www.youtube.com/embed/GfSZtaoc5bw"
									title="YouTube video"
									allowFullScreen
								/>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={ratio11Code}
								id="ratio11Code"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
