<script>
    import { Card, CardBody, Col, Row } from 'sveltestrap';
</script>
<Row>
    <Col xs={12}>
        <h5 class="text-decoration-underline mb-3 mt-2 pb-3">Credit Card</h5>
    </Col>
</Row>  

<Row>
    <Col xxl={4}>
        <Card class="card-height-100">
            <div class="card-header">
                <h5 class="card-title mb-0">Credit Card - Custom</h5>
            </div>
            <CardBody>
                <div class="mx-auto" style="max-width: 350px">
                    <div class="text-bg-info bg-gradient p-4 rounded-3 mb-3">
                        <div class="d-flex">
                            <div class="flex-grow-1">
                                <i class="bx bx-chip h1 text-warning"></i>
                            </div>
                            <div class="flex-shrink-0">
                                <i class="bx bxl-visa display-2 mt-n3"></i>
                            </div>
                        </div>
                        <div class="card-number fs-20" id="card-num-elem">
                            XXXX XXXX XXXX XXXX
                        </div>

                        <Row class="mt-4">
                            <Col xs={4}>
                                <div>
                                    <div class="text-white-50">Card Holder</div>
                                    <div id="card-holder-elem" class="fw-medium fs-14">Full Name</div>
                                </div>
                            </Col>
                            <Col xs={4}>
                                <div class="expiry">
                                    <div class="text-white-50">Expires</div>
                                    <div class="fw-medium fs-14">
                                        <span id="expiry-month-elem">00</span>
                                        /
                                        <span id="expiry-year-elem">0000</span>
                                    </div>
                                </div>
                            </Col>
                            <Col xs={4}>
                                <div>
                                    <div class="text-white-50">CVC</div>
                                    <div id="cvc-elem" class="fw-medium fs-14">---</div>
                                </div>
                            </Col>
                        </Row>
                    </div>
                    
                </div>


                <form id="custom-card-form" autoComplete="off">
                    <div class="mb-3">
                        <label for="card-num-input" class="form-label">Card Number</label>
                        <input id="card-num-input" class="form-control" maxLength="19" placeholder="0000 0000 0000 0000" />
                    </div>

                    <div class="mb-3">
                        <label for="card-holder-input" class="form-label">Card Holder</label>
                        <input type="text" class="form-control" id="card-holder-input" placeholder="Enter holder name" />
                    </div>

                    <Row>
                        <div class="col-lg-4">
                            <div>
                                <label for="expiry-month-input" class="form-label">Expiry Month</label>
                                <select class="form-select" id="expiry-month-input">
                                    <option></option>
                                    <option value="01">01</option>
                                    <option value="02">02</option>
                                    <option value="03">03</option>
                                    <option value="04">04</option>
                                    <option value="05">05</option>
                                    <option value="06">06</option>
                                    <option value="07">07</option>
                                    <option value="08">08</option>
                                    <option value="09">09</option>
                                    <option value="10">10</option>
                                    <option value="11">11</option>
                                    <option value="12">12</option>
                                </select>
                            </div>
                        </div>
                        

                        <div class="col-lg-4">
                            <div>
                                <label for="expiry-year-input" class="form-label">Expiry Year</label>
                                <select class="form-select" id="expiry-year-input">
                                    <option></option>
                                    <option value="2020">2020</option>
                                    <option value="2021">2021</option>
                                    <option value="2022">2022</option>
                                    <option value="2023">2023</option>
                                    <option value="2024">2024</option>
                                    <option value="2025">2025</option>
                                    <option value="2026">2026</option>
                                    <option value="2027">2027</option>
                                    <option value="2028">2028</option>
                                    <option value="2029">2029</option>
                                    <option value="2030">2030</option>
                                </select>
                            </div>
                        </div>
                        

                        <div class="col-lg-4">
                            <div class="cvc">
                                <label for="cvc-input" class="form-label">CVC</label>
                                <input type="text" id="cvc-input" class="form-control" maxLength="3" />
                            </div>
                        </div>
                        
                    </Row>

                    <button class="btn btn-danger w-100 mt-3" type="submit">Pay Now</button>
                </form>
                
            </CardBody>
        </Card>
        
    </Col>
    
    <div class="col-xl-4">
        <div class="card">
            <div class="card-header">
                <h5 class="card-title mb-0">Credit Card - card js plugin</h5>
            </div>
            <div class="card-body">
                <div class="card-wrapper mb-3"></div>

                <div class="form-container active">
                    <form action="" id="card-form-elem" autoComplete="off">
                        <div class="mb-3">
                            <label for="card-number-input" class="form-label">Card Number</label>
                            <input class="form-control" placeholder="Card number" type="tel" id="card-number-input" />
                        </div>
                        <div class="mb-3">
                            <label for="card-name-input" class="form-label">Card Holder</label>
                            <input class="form-control" placeholder="Full name" type="text" id="card-name-input" />
                        </div>
                        <Row>
                            <Col sm={6}>
                                <div class="mb-3">
                                    <label for="card-expiry-input" class="form-label">Expiry</label>
                                    <input class="form-control" placeholder="MM/YY" type="tel" id="card-expiry-input" />
                                </div>
                            </Col>
                            <Col sm={6}>
                                <div class="mb-3">
                                    <label for="card-cvc-input" class="form-label">CVC</label>
                                    <input class="form-control" placeholder="CVC" type="number" id="card-cvc-input" />
                                </div>
                            </Col>
                        </Row>
                        <button class="btn btn-danger w-100" type="submit">Pay Now</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    
</Row>