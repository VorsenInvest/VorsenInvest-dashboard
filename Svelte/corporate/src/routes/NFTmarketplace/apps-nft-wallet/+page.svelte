<svelte:head>
  <title>Wallet Connect | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import { Card, CardBody, Col, Container, Row } from "sveltestrap";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import Link from "svelte-link";
    import data from '../../../common/data/NFTMarketplace'

    import metaMask from "../../../assets/images/nft/wallet/metamask.png";
</script>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Wallet Connect" pageTitle="NFT Marketplace" />
        <Row class="justify-content-center">
            <Col xl={5}>
                <div class="text-center mb-4">
                    <h4>Your current wallet</h4>
                    <p class="text-muted fs-13">WalletConnect is a convenient open source tool that enables a mobile wallet to easily connect to decentralized web applications, and interact with them from your phone.</p>
                </div>
            </Col>
        </Row>

        <Row class="justify-content-center mb-4">
            <Col lg={3}>
                <Card class="text-center">
                    <CardBody class="py-5 px-4">
                        <img src={metaMask} alt="" height="55" class="mb-3 pb-2" />
                        <h5>Metamask</h5>
                        <p class="text-muted pb-1">MetaMask is a software cryptocurrency wallet used to interact with the Ethereum blockchain.</p>
                        <Link href={null} class="btn btn-secondary">Change Wallet</Link>
                    </CardBody>
                </Card>
            </Col>
        </Row>

        <Row class="justify-content-center">
            <Col xl={5}>
                <div class="text-center mb-4">
                    <h4>Connect with one of our other available wallet providers.</h4>
                </div>
            </Col>
        </Row>

        <Row class="justify-content-center">
            {#each data.walletConnectData as item}
                <Col lg={3}>
                    <Card class="text-center">
                        <CardBody class="py-5 px-4">
                            <img src={item.img} alt="" height="55" class="mb-3 pb-2" />
                            <h5>{item.title}</h5>
                            <p class="text-muted pb-1">{item.textContent}</p>
                            <Link href={null} class="btn btn-soft-primary">Connect Wallet</Link>
                        </CardBody>
                    </Card>
                </Col>
            {/each}
        </Row>
    </Container>
</div>