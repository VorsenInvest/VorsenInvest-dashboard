<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Container,
		Row,
	} from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	// HTML Highlight

	const htmlHighlightCode = `<!DOCTYPE html>
<html>
    <head>
        {document.title ="Velzon - Responsive Admin Dashboard Template"}
    </head>
    <body>
        <div>
            <h1>This is a Heading 1</h1>
            <h2>This is a Heading 2</h2>
            <h3>This is a Heading 3</h3>
            <h4>This is a Heading 4</h4>
        </div>
        <!-- end div content -->
    </body>
</html>
`;

	// CSS Highlight

	const cssHighlightCode = `body {
    color: #212529; 
    background-color: #f3f3f9;
    font-family: "Poppins",sans-serif;
}

.example {
    margin: 0;
    color: #74788d; 
}
`;

	// Javascript Highlight

	const javaScriptCode = `function myFunction() {
    var divElement = document.getElementById("myDIV");
    if (divElement.style.display === "none") {
      divElement.style.display = "block";
    } else {
      divElement.style.display = "none";
    }
}
`;
</script>

<svelte:head>
	<title>Highlight | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Highlight" pageTitle="Advance UI" />

		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader class="align-items-center d-flex">
						<div class="flex-grow-1">
							<h4 class="card-title mb-0">HTML Highlight</h4>
						</div>
					</CardHeader>

					<CardBody>
						<p class="text-muted">
							HTML highlight is used to mark or highlight text
							that is of property, relevance, or special interest
							to an HTML document. here is the example shown
							below.
						</p>

						<div class="live-preview">
							<PrismCode
								code={htmlHighlightCode}
								id="htmlHighlightCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader class="align-items-center d-flex">
						<div class="flex-grow-1">
							<h4 class="card-title mb-0">CSS Highlight</h4>
						</div>
					</CardHeader>

					<CardBody>
						<p class="text-muted">
							CSS highlight is used to mark or highlight text that
							is of property, relevance, or special interest to a
							CSS document. Here is the example shown below.
						</p>
						<div class="live-preview">
							<PrismCode
								code={cssHighlightCode}
								id="cssHighlightCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader class="align-items-center d-flex">
						<div class="flex-grow-1">
							<h4 class="card-title mb-0">
								Javascript Highlight
							</h4>
						</div>
					</CardHeader>

					<CardBody>
						<p class="text-muted">
							Javascript highlight is used to mark or highlight
							text that is of property, relevance, or special
							interest to a Javascript document. Here is the
							example shown below.
						</p>
						<div class="live-preview">
							<PrismCode
								code={javaScriptCode}
								id="javaScriptCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
