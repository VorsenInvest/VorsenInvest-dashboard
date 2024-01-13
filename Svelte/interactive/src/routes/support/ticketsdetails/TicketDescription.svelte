<script>
	import { Card, CardBody, Col, Label, Row, Form } from 'sveltestrap';
	import Link from 'svelte-link';
	import TicketsDetailsCode from './TicketsDetailsCode.svelte';

	import avatar6 from '../../../assets/images/users/avatar-6.jpg';
	import avatar8 from '../../../assets/images/users/avatar-8.jpg';
	import avatar10 from '../../../assets/images/users/avatar-10.jpg';
	import img4 from '../../../assets/images/small/img-4.jpg';
	import img5 from '../../../assets/images/small/img-5.jpg';
</script>

<Col xxl={9}>
	<Card>
		<CardBody class="p-4">
			<h6 class="fw-semibold text-uppercase mb-3">Ticket Description</h6>
			<p class="text-muted">
				It would also help to know what the errors are - it could be something simple like a message
				saying delivery is not available which could be a problem with your shipping templates. Too
				much or too little spacing, as in the example below, can make things unpleasant for the
				reader. The goal is to make your text as comfortable to read as possible. On the note of
				consistency, color consistency is a MUST. If you’re not trying to create crazy contrast in
				your design, then a great idea would be for you to use a color palette throughout your
				entire design. It will subconsciously interest viewers and also is very pleasing to look at. <Link
					href="{null}"
					class="link-secondary text-decoration-underline">Example</Link>
			</p>
			<h6 class="fw-semibold text-uppercase mb-3">Create an Excellent UI for a Dashboard</h6>
			<ul class="text-muted vstack gap-2 mb-4">
				<li>Pick a Dashboard Type</li>
				<li>Categorize information when needed</li>
				<li>Provide Context</li>
				<li>On using colors</li>
				<li>On using the right graphs</li>
			</ul>
			<div class="mt-4">
				<h6 class="fw-semibold text-uppercase mb-3">Here is the code you've requested</h6>
				<div>
					<TicketsDetailsCode />
				</div>
			</div>
		</CardBody>
		<!--end card-body-->
		<CardBody class="p-4">
			<h5 class="card-title mb-4">Comments</h5>

			<div data-simplebar style="height: 300px;" class="px-3 mx-n3">
				<div class="d-flex mb-4">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h5 class="fs-14">
							Joseph Parker <small class="text-muted">20 Dec 2021 - 05:47AM</small>
						</h5>
						<p class="text-muted">
							I am getting message from customers that when they place order always get error
							message .
						</p>
						<Link href="{null}" class="badge text-muted bg-light"><i class="mdi mdi-reply" /> Reply</Link
						>
						<div class="d-flex mt-4">
							<div class="flex-shrink-0">
								<img
									src={avatar10}
									alt=""
									class="avatar-xs rounded-circle"
								/>
							</div>
							<div class="flex-grow-1 ms-3">
								<h5 class="fs-14">
									Alexis Clarke <small class="text-muted">22 Dec 2021 - 02:32PM</small>
								</h5>
								<p class="text-muted">
									Please be sure to check your Spam mailbox to see if your email filters have
									identified the email from Dell as spam.
								</p>
								<Link href="{null}" class="badge text-muted bg-light"
									><i class="mdi mdi-reply" /> Reply</Link
								>
							</div>
						</div>
					</div>
				</div>
				<div class="d-flex mb-4">
					<div class="flex-shrink-0">
						<img
							src={avatar6}
							alt=""
							class="avatar-xs rounded-circle"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h5 class="fs-14">
							Donald Palmer <small class="text-muted">24 Dec 2021 - 05:20PM</small>
						</h5>
						<p class="text-muted">
							If you have further questions, please contact Customer Support from the “Action Menu”
							on your <a href="{null}" class="text-decoration-underline">Online Order Support</a>.
						</p>
						<Link href="{null}" class="badge text-muted bg-light"><i class="mdi mdi-reply" /> Reply</Link
						>
					</div>
				</div>
				<div class="d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar10}
							alt=""
							class="avatar-xs rounded-circle"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h5 class="fs-14">Alexis Clarke <small class="text-muted">26 min ago</small></h5>
						<p class="text-muted">
							Your <Link href="{null}" class="text-decoration-underline">Online Order Support</Link>
							provides you with the most current status of your order. To help manage your order refer
							to the “Action Menu” to initiate return, contact Customer Support and more.
						</p>
						<div class="row g-2 mb-3">
							<Col lg={1} sm={2} xs={6}>
								<img src={img4} alt="" class="img-fluid rounded" />
							</Col>
							<Col lg={1} sm={2} xs={6}>
								<img src={img5} alt="" class="img-fluid rounded" />
							</Col>
						</div>
						<Link href="{null}" class="badge text-muted bg-light"><i class="mdi mdi-reply" /> Reply</Link
						>
						<div class="d-flex mt-4">
							<div class="flex-shrink-0">
								<img
									src={avatar6}
									alt=""
									class="avatar-xs rounded-circle"
								/>
							</div>
							<div class="flex-grow-1 ms-3">
								<h5 class="fs-14">Donald Palmer <small class="text-muted">8 sec ago</small></h5>
								<p class="text-muted">
									Other shipping methods are available at checkout if you want your purchase
									delivered faster.
								</p>
								<Link href="{null}" class="badge text-muted bg-light"
									><i class="mdi mdi-reply" /> Reply</Link
								>
							</div>
						</div>
					</div>
				</div>
			</div>
			<Form action="/#" class="mt-3">
				<Row class="g-3">
					<Col lg={12}>
						<Label for="exampleFormControlTextarea1" class="form-label">Leave a Comments</Label>
						<textarea
							class="form-control bg-light border-light"
							id="exampleFormControlTextarea1"
							rows="3"
							placeholder="Enter comments"
						/>
					</Col>
					<Col lg={12} class="text-end">
						<Link href="{null}" class="btn btn-success">Post Comments</Link>
					</Col>
				</Row>
			</Form>
		</CardBody>
		<!-- end card body -->
	</Card>
	<!--end card-->
</Col>
