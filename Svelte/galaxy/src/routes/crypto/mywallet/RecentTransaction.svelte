<script>
    import { Card, CardBody, CardHeader } from "sveltestrap";
    import btc from '../../../assets/images/svg/crypto-icons/btc.svg'
    import ltc from '../../../assets/images/svg/crypto-icons/ltc.svg'
    import xmr from '../../../assets/images/svg/crypto-icons/xmr.svg'
    import fil from '../../../assets/images/svg/crypto-icons/fil.svg'
    import dot from '../../../assets/images/svg/crypto-icons/dot.svg'
</script>

<Card>
    <CardHeader>
        <h5 class="card-title mb-0">Recent Transaction</h5>
    </CardHeader>
    <CardBody>
        <div class="d-flex mb-3">
            <div class="flex-shrink-0">
                <img
                    src={btc}
                    alt=""
                    class="avatar-xxs"
                />
            </div>
            <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Bitcoin (BTC)</h6>
                <p class="text-muted mb-0">Today</p>
            </div>
            <div>
                <h6 class="text-danger mb-0">- $422.89</h6>
            </div>
        </div>
        <div class="d-flex mb-3">
            <div class="flex-shrink-0">
                <img
                    src={ltc}
                    alt=""
                    class="avatar-xxs"
                />
            </div>
            <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Litecoin (LTC)</h6>
                <p class="text-muted mb-0">Yesterday</p>
            </div>
            <div>
                <h6 class="text-success mb-0">+ $784.20</h6>
            </div>
        </div>
        <div class="d-flex mb-3">
            <div class="flex-shrink-0">
                <img
                    src={xmr}
                    alt=""
                    class="avatar-xxs"
                />
            </div>
            <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Monero (XMR)</h6>
                <p class="text-muted mb-0">01 Jan, 2022</p>
            </div>
            <div>
                <h6 class="text-danger mb-0">- $356.74</h6>
            </div>
        </div>
        <div class="d-flex mb-3">
            <div class="flex-shrink-0">
                <img
                    src={fil}
                    alt=""
                    class="avatar-xxs"
                />
            </div>
            <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Filecoin (FIL)</h6>
                <p class="text-muted mb-0">30 Dec, 2021</p>
            </div>
            <div>
                <h6 class="text-success mb-0">+ $1,247.00</h6>
            </div>
        </div>
        <div class="d-flex mb-3">
            <div class="flex-shrink-0">
                <img
                    src={dot}
                    alt=""
                    class="avatar-xxs"
                />
            </div>
            <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Polkadot (DOT)</h6>
                <p class="text-muted mb-0">27 Dec, 2021</p>
            </div>
            <div>
                <h6 class="text-success btn mb-0">+ $7,365.80</h6>
            </div>
        </div>
        <div>
            <a href="/crypto/transaction/apps-crypto-transactions" class="btn btn-soft-primary w-100"
                >View All Transactions <i
                    class="ri-arrow-right-line align-bottom"
                /></a
            >
        </div>
    </CardBody>
</Card>
