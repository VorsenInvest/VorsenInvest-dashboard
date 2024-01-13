<script>
	import {
		Card,
		CardHeader,
		Col,
		Nav,
		NavItem,
		NavLink,
		Row,
		TabContent,
		TabPane,
		Label,
		CardBody
	} from 'sveltestrap';
	let activeTab = 1;
</script>

<Col xl={4}>
<Card>
	<CardHeader class="align-items-center border-0 d-flex">
		<h4 class="card-title mb-0 flex-grow-1">Trading</h4>
		<div class="flex-shrink-0">
			<Nav class="nav justify-content-end nav-tabs-custom rounded card-header-tabs border-bottom-0">
				<NavItem>
					<NavLink href={null} on:click={()=> (activeTab = 1)} active={activeTab == 1}>Buy</NavLink>
				</NavItem>
				<NavItem>
					<NavLink href={null} on:click={()=> (activeTab = 2)} active={activeTab == 2}>Sell</NavLink>
				</NavItem>
			</Nav>
		</div>
	</CardHeader>
	<CardBody class="p-0">
		<TabContent class="p-0">
			<TabPane tabId={1} class={activeTab==1 ? 'active' : '' }>
				<div class="p-3 bg-primary-subtle">
					<div class="float-end ms-2">
						<h6 class="text-primary mb-0">
							USD Balance : <span class="text-body">$12,426.07</span>
						</h6>
					</div>
					<h6 class="mb-0 text-success">Buy Coin</h6>
				</div>
				<div class="p-3">
					<Row>
						<Col xs-={6}>
						<div class="mb-3">
							<Label>Currency :</Label>
							<select class="form-select">
								<option>BTC</option>
								<option>ETH</option>
								<option>LTC</option>
							</select>
						</div>
						</Col>
						<Col xs-={6}>
						<div class="mb-3">
							<Label>Payment Method :</Label>
							<select class="form-select">
								<option>Wallet Balance</option>
								<option>Credit / Debit Card</option>
								<option>PayPal</option>
								<option>Payoneer</option>
							</select>
						</div>
						</Col>
					</Row>
					<div>
						<div class="input-group mb-3">
							<Label class="input-group-text">Amount</Label>
							<input type="text" class="form-control" placeholder="0" />
						</div>

						<div class="input-group mb-3">
							<Label class="input-group-text">Price</Label>
							<input type="text" class="form-control" placeholder="2.045585" />
							<Label class="input-group-text">$</Label>
						</div>

						<div class="input-group mb-0">
							<Label class="input-group-text">Total</Label>
							<input type="text" class="form-control" placeholder="2700.16" />
						</div>
					</div>
					<div class="mt-3 pt-2">
						<div class="d-flex mb-2">
							<div class="flex-grow-1">
								<p class="fs-13 mb-0">
									Transaction Fees<span class="text-muted ms-1 fs-11">(0.05%)</span>
								</p>
							</div>
							<div class="flex-shrink-0">
								<h6 class="mb-0">$1.08</h6>
							</div>
						</div>
						<div class="d-flex mb-2">
							<div class="flex-grow-1">
								<p class="fs-13 mb-0">
									Minimum Received<span class="text-muted ms-1 fs-11">(2%)</span>
								</p>
							</div>
							<div class="flex-shrink-0">
								<h6 class="mb-0">$7.85</h6>
							</div>
						</div>
						<div class="d-flex">
							<div class="flex-grow-1">
								<p class="fs-13 mb-0">Estimated Rate</p>
							</div>
							<div class="flex-shrink-0">
								<h6 class="mb-0">1 BTC ~ $34572.00</h6>
							</div>
						</div>
					</div>
					<div class="mt-3 pt-2">
						<button type="button" class="btn btn-success w-100">Buy Coin</button>
					</div>
				</div>
			</TabPane>

			<TabPane tabId={2} class={activeTab==2 ? 'active' : '' }>
				<div class="p-3 bg-primary-subtle">
					<div class="float-end ms-2">
						<h6 class="text-primary mb-0">
							USD Balance : <span class="text-body">$12,426.07</span>
						</h6>
					</div>
					<h6 class="mb-0 text-danger">Sell Coin</h6>
				</div>
				<div class="p-3">
					<Row>
						<Col xs-={6}>
						<div class="mb-3">
							<Label>Currency :</Label>
							<select class="form-select">
								<option>BTC</option>
								<option>ETH</option>
								<option>LTC</option>
							</select>
						</div>
						</Col>
						<Col xs-={6}>
						<div class="mb-3">
							<Label>Email :</Label>
							<input type="email" class="form-control" placeholder="example@email.com" />
						</div>
						</Col>
					</Row>
					<div>
						<div class="input-group mb-3">
							<Label class="input-group-text">Amount</Label>
							<input type="text" class="form-control" placeholder="0" />
						</div>
						<div class="input-group mb-3">
							<Label class="input-group-text">Price</Label>
							<input type="text" class="form-control" placeholder="2.045585" />
							<Label class="input-group-text">$</Label>
						</div>
						<div class="input-group mb-0">
							<Label class="input-group-text">Total</Label>
							<input type="text" class="form-control" placeholder="2700.16" />
						</div>
					</div>
					<div class="mt-3 pt-2">
						<div class="d-flex mb-2">
							<div class="flex-grow-1">
								<p class="fs-13 mb-0">
									Transaction Fees<span class="text-muted ms-1 fs-11">(0.05%)</span>
								</p>
							</div>
							<div class="flex-shrink-0">
								<h6 class="mb-0">$1.08</h6>
							</div>
						</div>
						<div class="d-flex mb-2">
							<div class="flex-grow-1">
								<p class="fs-13 mb-0">
									Minimum Received<span class="text-muted ms-1 fs-11">(2%)</span>
								</p>
							</div>
							<div class="flex-shrink-0">
								<h6 class="mb-0">$7.85</h6>
							</div>
						</div>
						<div class="d-flex">
							<div class="flex-grow-1">
								<p class="fs-13 mb-0">Estimated Rate</p>
							</div>
							<div class="flex-shrink-0">
								<h6 class="mb-0">1 BTC ~ $34572.00</h6>
							</div>
						</div>
					</div>
					<div class="mt-3 pt-2">
						<button type="button" class="btn btn-danger w-100">Sell Coin</button>
					</div>
				</div>
			</TabPane>
		</TabContent>
	</CardBody>
</Card>
</Col>