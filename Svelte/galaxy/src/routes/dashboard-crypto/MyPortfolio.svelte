<script>
import { DropdownItem, DropdownMenu, DropdownToggle, Dropdown } from 'sveltestrap';
import PortfolioCharts from './PortfolioCharts.svelte';
import btc from '../../assets/images/svg/crypto-icons/btc.svg'
import eth from '../../assets/images/svg/crypto-icons/eth.svg'
import ltc from '../../assets/images/svg/crypto-icons/ltc.svg'
import dash from '../../assets/images/svg/crypto-icons/dash.svg'
</script>
<div class="col-xxl-3">
    <div class="card card-height-100">
        <div class="card-header border-0 align-items-center d-flex">
            <h4 class="card-title mb-0 flex-grow-1">My Portfolio</h4>
            <div>
                <Dropdown>
                    <DropdownToggle tag="button" color="" class="btn btn-soft-primary btn-sm" >
                        <span class="text-uppercase">Btc<i class="mdi mdi-chevron-down align-middle ms-1"></i></span>
                    </DropdownToggle>
                    <DropdownMenu class="dropdown-menu dropdown-menu-end">
                        <DropdownItem>BTC</DropdownItem>
                        <DropdownItem>USD</DropdownItem>
                        <DropdownItem>Euro</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </div>
        </div>
        <div class="card-body">
            <div id="portfolio_donut_charts" class="apex-charts" dir="ltr">
                <PortfolioCharts dataColors={["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.65", "--vz-primary-rgb, 0.50"]} />
            </div>

            <ul class="list-group list-group-flush border-dashed mb-0 mt-3 pt-2">
                <li class="list-group-item px-0">
                    <div class="d-flex">
                        <div class="flex-shrink-0 avatar-xs">
                            <span class="avatar-title bg-light p-1 rounded-circle">
                                <img src={btc} class="img-fluid" alt="" />
                            </span>
                        </div>
                        <div class="flex-grow-1 ms-2">
                            <h6 class="mb-1">Bitcoin</h6>
                            <p class="fs-12 mb-0 text-muted"><i class="mdi mdi-circle fs-10 align-middle text-primary me-1"></i>BTC</p>
                        </div>
                        <div class="flex-shrink-0 text-end">
                            <h6 class="mb-1">BTC 0.00584875</h6>
                            <p class="text-success fs-12 mb-0">$19,405.12</p>
                        </div>
                    </div>
                </li>
                <li class="list-group-item px-0">
                    <div class="d-flex">
                        <div class="flex-shrink-0 avatar-xs">
                            <span class="avatar-title bg-light p-1 rounded-circle">
                                <img src={eth} class="img-fluid" alt="" />
                            </span>
                        </div>
                        <div class="flex-grow-1 ms-2">
                            <h6 class="mb-1">Ethereum</h6>
                            <p class="fs-12 mb-0 text-muted"><i class="mdi mdi-circle fs-10 align-middle text-info me-1"></i>ETH</p>
                        </div>
                        <div class="flex-shrink-0 text-end">
                            <h6 class="mb-1">ETH 2.25842108</h6>
                            <p class="text-danger fs-12 mb-0">$40552.18</p>
                        </div>
                    </div>
                </li>
                <li class="list-group-item px-0">
                    <div class="d-flex">
                        <div class="flex-shrink-0 avatar-xs">
                            <span class="avatar-title bg-light p-1 rounded-circle">
                                <img src={ltc} class="img-fluid" alt="" />
                            </span>
                        </div>
                        <div class="flex-grow-1 ms-2">
                            <h6 class="mb-1">Litecoin</h6>
                            <p class="fs-12 mb-0 text-muted"><i class="mdi mdi-circle fs-10 align-middle text-warning me-1"></i>LTC</p>
                        </div>
                        <div class="flex-shrink-0 text-end">
                            <h6 class="mb-1">LTC 10.58963217</h6>
                            <p class="text-success fs-12 mb-0">$15824.58</p>
                        </div>
                    </div>
                </li>
                <li class="list-group-item px-0 pb-0">
                    <div class="d-flex">
                        <div class="flex-shrink-0 avatar-xs">
                            <span class="avatar-title bg-light p-1 rounded-circle">
                                <img src={dash} class="img-fluid" alt="" />
                            </span>
                        </div>
                        <div class="flex-grow-1 ms-2">
                            <h6 class="mb-1">Dash</h6>
                            <p class="fs-12 mb-0 text-muted"><i class="mdi mdi-circle fs-10 align-middle text-success me-1"></i>DASH</p>
                        </div>
                        <div class="flex-shrink-0 text-end">
                            <h6 class="mb-1">DASH 204.28565885</h6>
                            <p class="text-success fs-12 mb-0">$30635.84</p>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>