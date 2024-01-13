<script>
	import { Card, CardBody, Col, Container, Row } from "sveltestrap";

	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";

	import avatar1 from '../../../assets/images/users/avatar-1.jpg';
	import avatar2 from '../../../assets/images/users/avatar-2.jpg';
	import avatar3 from '../../../assets/images/users/avatar-3.jpg';
	import avatar4 from '../../../assets/images/users/avatar-4.jpg';
	import avatar5 from '../../../assets/images/users/avatar-5.jpg';
	import avatar6 from '../../../assets/images/users/avatar-6.jpg';
	import avatar7 from '../../../assets/images/users/avatar-7.jpg';
	import avatar8 from '../../../assets/images/users/avatar-8.jpg';
	import avatar9 from '../../../assets/images/users/avatar-9.jpg';
	import avatar10 from '../../../assets/images/users/avatar-10.jpg';

	// Examples

	const defultCode = `
<div class="d-flex align-items-start text-muted mb-4">
    <div class="flex-shrink-0 me-3">
        <img src={avatar2} class="avatar-sm rounded shadow" alt="...">
    </div>
    
    <div class="flex-grow-1">
        <h5 class="fs-14">Media heading</h5>
        This is some content from a media component. You can replace this with any content and adjust it as needed.
    </div>
</div>

<div class="d-flex align-items-start text-muted mb-4">
    <div class="flex-grow-1">
        <h5 class="fs-14">Media heading</h5>
        This is some content from a media component. You can replace this with any content and adjust it as needed.
    </div>
    <div class="flex-shrink-0 ms-3">
        <img src={avatar3} class="avatar-sm rounded shadow" alt="...">
    </div>
</div>

<div class="d-flex align-items-start text-muted">
    <div class="flex-shrink-0 me-3">
        <img src={avatar2} class="avatar-sm rounded shadow" alt="...">
    </div>
    <div class="flex-grow-1">
        <h5 class="fs-14">Media heading</h5>
        This is some content from a media component. You can replace this with any content and adjust it as needed.
    </div>
</div>
`;

	// Nesting Example

	const nestingCode = `
<!-- Nesting Example -->
<div class="d-flex align-items-start text-muted mb-4">
    <div class="flex-shrink-0 me-3">
        <img src={avatar2} class="avatar-sm rounded shadow" alt="...">
    </div>
    <div class="flex-grow-1">
        <h5 class="fs-14">Media heading</h5>
        This is some content from a media component. You can replace this with any content and adjust it as needed.
        <div class="d-flex align-items-start text-muted mt-3">
            <div class="flex-shrink-0 me-3">
                <img src={avatar3} class="avatar-sm rounded shadow" alt="...">
            </div>
            <div class="flex-grow-1">
                <h5 class="fs-14">Media heading</h5>
                This is some content from a media component. You can replace this with any content and adjust it as needed.
            </div>
        </div>
    </div>
</div>

<div class="d-flex align-items-start text-muted">
    <div class="flex-shrink-0 me-3">
        <img src={avatar4} class="avatar-sm rounded shadow" alt="...">
    </div>
    <div class="flex-grow-1">
        <h5 class="fs-14">Media heading</h5>
        This is some content from a media component. You can replace this with any content and adjust it as needed.
    </div>
</div>

`;

	// Media Alignment

	const mediaCode = `
<!-- Media Alignment -->
<div class="d-flex align-items-start text-muted mb-4">
    <div class="flex-shrink-0 me-3">
    <img src={avatar2} class="avatar-sm rounded shadow" alt="...">
    </div>
    <div class="flex-grow-1">
    <h5 class="fs-14">Top Aligned media</h5>
    <p class="mb-1">Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
    <p class="mb-0">Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
    </div>
</div>

<div class="d-flex align-items-center text-muted mb-4">
    <div class="flex-shrink-0 me-3">
    <img src={avatar6} class="avatar-sm rounded shadow" alt="...">
    </div>
    <div class="flex-grow-1">
    <h5 class="fs-14">Center Aligned media</h5>
    <p class="mb-1">Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
    <p class="mb-0">Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
    </div>
</div>

<div class="d-flex align-items-end text-muted">
    <div class="flex-shrink-0 me-3">
    <img src={avatar8} class="avatar-sm rounded shadow" alt="...">
    </div>
    <div class="flex-grow-1">
    <h5 class="fs-14">Bottom Aligned media</h5>
    <p class="mb-1">Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
    <p class="mb-0">Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
    </div>
</div>
`;

</script>

<svelte:head>
	<title>Media Object | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Media object" pageTitle="Base UI" />
		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Examples" />

					<CardBody>
						<p class="text-muted mb-4">
							Use few flex utilities that allow even more
							flexibility and customization than before.
						</p>

						<div class="live-preview">
							<div class="d-flex align-items-start text-muted mb-4">
								<div class="flex-shrink-0 me-3">
									<img
										src={avatar2}
										class="avatar-sm rounded shadow"
										alt="..."
									/>
								</div>

								<div class="flex-grow-1">
									<h5 class="fs-14">Media heading</h5>
									This is some content from a media component.
									You can replace this with any content and adjust
									it as needed.
								</div>
							</div>

							<div class="d-flex align-items-start text-muted mb-4">
								<div class="flex-grow-1">
									<h5 class="fs-14">Media heading</h5>
									This is some content from a media component.
									You can replace this with any content and adjust
									it as needed.
								</div>
								<div class="flex-shrink-0 ms-3">
									<img
										src={avatar3}
										class="avatar-sm rounded shadow"
										alt="..."
									/>
								</div>
							</div>

							<div class="d-flex align-items-start text-muted">
								<div class="flex-shrink-0 me-3">
									<img
										src={avatar2}
										class="avatar-sm rounded shadow"
										alt="..."
									/>
								</div>
								<div class="flex-grow-1">
									<h5 class="fs-14">Media heading</h5>
									This is some content from a media component.
									You can replace this with any content and adjust
									it as needed.
								</div>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={defultCode}
								id="defultCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Nesting Example" />

					<CardBody>
						<p class="text-muted mb-4">
							Media objects can be infinitely nested, though we
							suggest you stop at some point. Place nested <code
								>d-flex align-items-start</code>
							within the <code>flex-grow-1</code>
							of a parent media object.
						</p>
						<div class="live-preview">
							<div class="d-flex align-items-start text-muted mb-4">
								<div class="flex-shrink-0 me-3">
									<img
										src={avatar2}
										class="avatar-sm rounded shadow"
										alt="..."
									/>
								</div>
								<div class="flex-grow-1">
									<h5 class="fs-14">Media heading</h5>
									This is some content from a media component.
									You can replace this with any content and adjust
									it as needed.
									<div class="d-flex align-items-start text-muted mt-3"
									>
										<div class="flex-shrink-0 me-3">
											<img
												src={avatar3}
												class="avatar-sm rounded shadow"
												alt="..."
											/>
										</div>
										<div class="flex-grow-1">
											<h5 class="fs-14">Media heading</h5>
											This is some content from a media component.
											You can replace this with any content
											and adjust it as needed.
										</div>
									</div>
								</div>
							</div>

							<div class="d-flex align-items-start text-muted">
								<div class="flex-shrink-0 me-3">
									<img
										src={avatar4}
										class="avatar-sm rounded shadow"
										alt="..."
									/>
								</div>
								<div class="flex-grow-1">
									<h5 class="fs-14">Media heading</h5>
									This is some content from a media component.
									You can replace this with any content and adjust
									it as needed.
								</div>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={nestingCode}
								id="nestingCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Media Alignment" />

					<CardBody>
						<p class="text-muted mb-4">
							The images or other media can be aligned top,
							middle, or bottom. The default is top aligned.
						</p>

						<div class="live-preview">
							<div class="d-flex align-items-start text-muted mb-4">
								<div class="flex-shrink-0 me-3">
									<img
										src={avatar2}
										class="avatar-sm rounded shadow"
										alt="..."
									/>
								</div>

								<div class="flex-grow-1">
									<h5 class="fs-14">Top Aligned media</h5>
									<p class="mb-1">
										Cras sit amet nibh libero, in gravida
										nulla. Nulla vel metus scelerisque ante
										sollicitudin. Cras purus odio,
										vestibulum in vulputate at, tempus
										viverra turpis. Fusce condimentum nunc
										ac nisi vulputate fringilla. Donec
										lacinia congue felis in faucibus.
									</p>
									<p class="mb-0">
										Donec sed odio dui. Nullam quis risus
										eget urna mollis ornare vel eu leo. Cum
										sociis natoque penatibus et magnis dis
										parturient montes, nascetur ridiculus
										mus.
									</p>
								</div>
							</div>

							<div class="d-flex align-items-center text-muted mb-4">
								<div class="flex-shrink-0 me-3">
									<img
										src={avatar6}
										class="avatar-sm rounded shadow"
										alt="..."
									/>
								</div>

								<div class="flex-grow-1">
									<h5 class="fs-14">Center Aligned media</h5>
									<p class="mb-1">
										Cras sit amet nibh libero, in gravida
										nulla. Nulla vel metus scelerisque ante
										sollicitudin. Cras purus odio,
										vestibulum in vulputate at, tempus
										viverra turpis. Fusce condimentum nunc
										ac nisi vulputate fringilla. Donec
										lacinia congue felis in faucibus.
									</p>
									<p class="mb-0">
										Donec sed odio dui. Nullam quis risus
										eget urna mollis ornare vel eu leo. Cum
										sociis natoque penatibus et magnis dis
										parturient montes, nascetur ridiculus
										mus.
									</p>
								</div>
							</div>

							<div class="d-flex align-items-end text-muted">
								<div class="flex-shrink-0 me-3">
									<img
										src={avatar8}
										class="avatar-sm rounded shadow"
										alt="..."
									/>
								</div>

								<div class="flex-grow-1">
									<h5 class="fs-14">Bottom Aligned media</h5>
									<p class="mb-1">
										Cras sit amet nibh libero, in gravida
										nulla. Nulla vel metus scelerisque ante
										sollicitudin. Cras purus odio,
										vestibulum in vulputate at, tempus
										viverra turpis. Fusce condimentum nunc
										ac nisi vulputate fringilla. Donec
										lacinia congue felis in faucibus.
									</p>
									<p class="mb-0">
										Donec sed odio dui. Nullam quis risus
										eget urna mollis ornare vel eu leo. Cum
										sociis natoque penatibus et magnis dis
										parturient montes, nascetur ridiculus
										mus.
									</p>
								</div>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={mediaCode}
								id="mediaCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
