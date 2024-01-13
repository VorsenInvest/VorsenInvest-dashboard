<script>
	import {
		Card,
		CardBody,
		Container,
		Col,
		Row,
		CardHeader,
	} from "sveltestrap";
	import Dropzone from "svelte-file-dropzone";
	import Link from "svelte-link";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import FilePond, { registerPlugin, supported } from "svelte-filepond";
	import "filepond/dist/filepond.min.css";
	import FilePondPluginImageExifOrientation from "filepond-plugin-image-exif-orientation";
	import FilePondPluginImagePreview from "filepond-plugin-image-preview";
	import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css";

	let files = {
		accepted: [],
		rejected: [],
		preview: [],
	};

	function handleFilesSelect(e) {
		const { acceptedFiles, fileRejections } = e.detail;
		files.accepted = [...files.accepted, ...acceptedFiles];
		files.rejected = [...files.rejected, ...fileRejections];

		const uploadedfiles = event.target.files;

		for (var i = 0; i < uploadedfiles.length; i++) {
			const file = uploadedfiles[i];
			if (file) {
				const reader = new FileReader();

				reader.onload = (e) => {
					files.preview = [...files.preview, e.target.result];
				};

				reader.readAsDataURL(file);
			}
		}
	}

	function handleRemoveFile(e, index) {
		if (confirm("Are sure want to cancel upload file?")) {
			files.accepted.splice(index, 1);
			files.preview.splice(index, 1);
			files.accepted = [...files.accepted];
		}
	}

	// Register the plugins
	registerPlugin(
		FilePondPluginImageExifOrientation,
		FilePondPluginImagePreview
	);

	// a reference to the component, used to call FilePond methods
	let pond;

	// pond.getFiles() will return the active files

	// the name to use for the internal file input
	let name = "filepond";

	// handle filepond events
	function handleInit() {
		console.log("FilePond has initialised");
	}

	function handleAddFile(err, fileItem) {
		console.log("A file has been added", fileItem);
	}

</script>

<svelte:head>
	<title>File Upload | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="File Upload" pageTitle="Forms" />
		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader class="card-header">
						<h4 class="card-title mb-0">Dropzone</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							DropzoneJS is an open source library that provides
							drag’n’drop file uploads with image previews.
						</p>

						<Dropzone on:drop={handleFilesSelect}>
							<div>
								<div class="dz-message needsclick">
									<div class="dz-message needsclick">
										<div class="mb-3">
											<i
												class="display-4 text-muted ri-upload-cloud-2-fill"
											/>
										</div>
										<h4>
											Drop files here or click to upload.
										</h4>
									</div>
								</div>
							</div>
						</Dropzone>

						<ul class="list-unstyled mb-0" id="dropzone-preview">
							{#each files.accepted as item, index}
								<li class="mt-2" id="dropzone-preview-list">
									<!-- This is used as the file preview template -->
									<div class="border rounded">
										<div class="d-flex p-2">
											<div class="flex-shrink-0 me-3">
												<div
													class="avatar-sm bg-light rounded"
												>
													<img
														class="img-fluid rounded d-block"
														src={files.preview[
															index
														]}
														alt="Product-Image"
														style="height: 100%;"
													/>
												</div>
											</div>
											<div class="flex-grow-1">
												<div class="pt-1">
													<h5 class="fs-14 mb-1">
														{item.name}
													</h5>
													<p
														class="fs-13 text-muted mb-0"
													>
														{item.size}
													</p>
													<strong
														class="error text-danger"
													/>
												</div>
											</div>
											<div class="flex-shrink-0 ms-3">
												<button
													class="btn btn-sm btn-danger"
													on:click={(e) =>
														handleRemoveFile(
															e,
															index
														)}>Delete</button
												>
											</div>
										</div>
									</div>
								</li>
							{/each}
						</ul>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<div class="justify-content-between d-flex align-items-center mb-3">
				<h5 class="mb-0 pb-1 text-decoration-underline">Filepond</h5>
			</div>
			<Col lg={6}>
				<Card>
					<CardHeader class="card-header">
						<h4 class="card-title mb-0">Multiple File Upload</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							FilePond is a JavaScript library that optimizes
							multiple images for faster uploads and offers a
							great, accessible, silky smooth user experience.
						</p>

						<FilePond
							bind:this={pond}
							{name}
							allowMultiple={true}
							oninit={handleInit}
							onaddfile={handleAddFile}
						/>
					</CardBody>
				</Card>
			</Col>
			<Col lg={6}>
				<Card>
					<CardHeader class="card-header">
						<h4 class="card-title mb-0">
							Profile Picture Selection
						</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							FilePond is a JavaScript library with profile
							picture-shaped file upload variation.
						</p>
						<div class="avatar-xl mx-auto">
						<FilePond
							bind:this={pond}
							{name}
							className={'filepond-input-circle'}
							allowMultiple={false}
							oninit={handleInit}
							onaddfile={handleAddFile}
						/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
