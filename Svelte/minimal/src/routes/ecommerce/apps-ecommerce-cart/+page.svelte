<svelte:head>
	<title>Cart | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import {
		Card,
		CardBody,
		Col,
		Container,
		Input,
		Row,
		Button,
		Alert,
		CardHeader
	} from 'sveltestrap';
	import Link from 'svelte-link';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import ecommerceData from '../../../common/data/ecommerce';

	let taxRate = 0.125;
	let shippingRate = 65.00;
	let discountRate = 0.15;
	let subtotal = 239.97;
	let tax = 30;
	let discount = 36;
	let shipping = 65;
	let total = 298.97;

	const plusItem = (product) => {
		for (let item of ecommerceData.shoppingCart) {
			if (item.id === product.id) {
				product.data_attr += 1;
				product.total = (product.data_attr * parseFloat(product.price)).toFixed(2)
				ecommerceData.shoppingCart = ecommerceData.shoppingCart;
				calculateCart()
				return;
			}
		}
	};

	const minusItem = (product) => {
		for (let item of ecommerceData.shoppingCart) {
			if (item.id === product.id) {
				if (product.data_attr > 0) {
					product.data_attr -= 1;
					product.total = (product.data_attr * parseFloat(product.price)).toFixed(2)
					ecommerceData.shoppingCart = ecommerceData.shoppingCart;
				}
				calculateCart()
				return;
			}
		}
	};

	const calculateCart = () => {
		subtotal = 0;
		for (let item of ecommerceData.shoppingCart) {
			subtotal += parseFloat(item.total)
		}
		subtotal = subtotal.toFixed(2)
		/* Calculate totals */
		tax = (subtotal * taxRate).toFixed(2);
		discount = (subtotal * discountRate).toFixed(2);

		shipping = (subtotal > 0 ? shippingRate : 0).toFixed(2);
		total = parseFloat(subtotal) + parseFloat(tax) + parseFloat(shipping) - parseFloat(discount);
		total = total.toFixed(2)
	}
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Shopping Cart" pageTitle="Ecommerce" />

		<Row class="mb-3">
			<Col xl={8}>
			<Row class="align-items-center gy-3 mb-3">
				<div class="col-sm">
					<div>
						<h5 class="fs-14 mb-0">Your Cart (03 items)</h5>
					</div>
				</div>
				<div class="col-sm-auto">
					<Link href="/ecommerce/apps-ecommerce-products" class="link-primary text-decoration-underline">
					Continue Shopping
					</Link>
				</div>
			</Row>
			{#each ecommerceData.shoppingCart as cartItem}
			<Card class="product">
				<CardBody>
					<Row class="gy-3">
						<div class="col-sm-auto">
							<div class="avatar-lg bg-light rounded p-1">
								<img src={cartItem.img} alt="" class="img-fluid d-block" />
							</div>
						</div>
						<div class="col-sm">
							<h5 class="fs-14 text-truncate">
								<Link href="/ecommerce/apps-ecommerce-product-details" class="text-dark">
								{cartItem.name}
								</Link>
							</h5>
							<ul class="list-inline text-muted">
								<li class="list-inline-item">
									Color :{' '}
									<span class="fw-medium">
										{cartItem.color}
									</span>
								</li>
								<li class="list-inline-item">
									Size :{' '}
									<span class="fw-medium">{cartItem.size}</span>
								</li>
							</ul>

							<div class="input-step">
								<Button color="primary" on:click={()=> minusItem(cartItem)}>-</Button>
								<Input type="text" class="product-quantity" value={cartItem.data_attr}
									name="demo_vertical" readOnly />
								<Button color="primary" on:click={()=> plusItem(cartItem)}>+</Button>
							</div>
						</div>
						<div class="col-sm-auto">
							<div class="text-lg-end">
								<p class="text-muted mb-1">Item Price:</p>
								<h5 class="fs-14">
									$
									<span id="ticket_price" class="product-price">
										{cartItem.price}
									</span>
								</h5>
							</div>
						</div>
					</Row>
				</CardBody>

				<div class="card-footer">
					<div class="row align-items-center gy-3">
						<div class="col-sm">
							<div class="d-flex flex-wrap my-n1">
								<div>
									<Link href={null} class="d-block text-body p-1 px-2">
									<i class="ri-delete-bin-fill text-muted align-bottom me-1" />{' '}
									Remove
									</Link>
								</div>
								<div>
									<Link href={null} class="d-block text-body p-1 px-2">
									<i class="ri-star-fill text-muted align-bottom me-1" />{' '}
									Add Wishlist
									</Link>
								</div>
							</div>
						</div>
						<div class="col-sm-auto">
							<div class="d-flex align-items-center gap-2 text-muted">
								<div>Total :</div>
								<h5 class="fs-14 mb-0">
									$
									<span class="product-line-price">
										{' '}
										{cartItem.total}
									</span>
								</h5>
							</div>
						</div>
					</div>
				</div>
			</Card>
			{/each}
			<div class="text-end mb-4">
				<Link href="/ecommerce/apps-ecommerce-checkout" class="btn btn-primary btn-label right ms-auto">
				<i class="ri-arrow-right-line label-icon align-bottom fs-16 ms-2" />{' '}
				Checkout
				</Link>
			</div>
			</Col>
			<Col xl={4}>
			<div class="sticky-side-div">
				<Card>
					<CardHeader class="border-bottom-dashed">
						<h5 class="card-title mb-0">Order Summary</h5>
					</CardHeader>
					<CardHeader class="bg-light-subtle border-bottom-dashed">
						<div class="text-center">
							<h6 class="mb-2">
								Have a <span class="fw-semibold">promo</span> code ?
							</h6>
						</div>
						<div class="hstack gap-3 px-3 mx-n3">
							<input class="form-control me-auto" type="text" placeholder="Enter coupon code"
								aria-label="Add Promo Code here..." />
							<button type="button" class="btn btn-primary w-xs"> Apply </button>
						</div>
					</CardHeader>
					<CardBody class="pt-2">
						<div class="table-responsive">
							<table class="table table-borderless mb-0">
								<tbody>
									<tr>
										<td>Sub Total :</td>
										<td class="text-end" id="cart-subtotal"> $ {subtotal} </td>
									</tr>
									<tr>
										<td>
											Discount{' '}
											<span class="text-muted">(VELZON15)</span> :{' '}
										</td>
										<td class="text-end" id="cart-discount"> - $ {discount}</td>
									</tr>
									<tr>
										<td>Shipping Charge :</td>
										<td class="text-end" id="cart-shipping"> $ {shipping} </td>
									</tr>
									<tr>
										<td>Estimated Tax (12.5%) : </td>
										<td class="text-end" id="cart-tax"> $ {tax} </td>
									</tr>
									<tr class="table-active">
										<th>Total (USD) :</th>
										<td class="text-end">
											<span class="fw-semibold" id="cart-total"> $ {total} </span>
										</td>
									</tr>
								</tbody>
							</table>
						</div>
					</CardBody>
				</Card>

				<Alert color="primary" class="border-dashed">
					<div class="d-flex align-items-center">
						<lord-icon src="//cdn.lordicon.com/nkmsrxys.json" trigger="loop"
							colors="primary:#121331,secondary:#25a0e2" style="width:80px;height:80px">
						</lord-icon>
						<div class="ms-2">
							<h5 class="fs-14 text-primary fw-semibold">
								{' '}
								Buying for a loved one?
							</h5>
							<p class="text-black mb-1">
								Gift wrap and personalised message on card, <br />
								Only for <span class="fw-semibold">$9.99</span> USD
							</p>
							<button type="button" class="btn ps-0 btn-sm btn-link text-primary text-uppercase">
								Add Gift Wrap
							</button>
						</div>
					</div>
				</Alert>
			</div>
			</Col>
		</Row>
	</Container>
</div>