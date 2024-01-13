<script>
    import { Row, Col } from 'sveltestrap';
    import Link from 'svelte-link';
</script>
 <!-- svelte-ignore a11y-invalid-attribute -->
<Row>
    <Col lg={12}>
        <div class="justify-content-between d-flex align-items-center mt-3 mb-4">
            <h5 class="mb-0 pb-1 text-decoration-underline">Invoice Action</h5>
        </div>
    </Col>

    <Col class="col-12">
        <table class="body-wrap" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; width: 100%; background-color: transparent; margin: 0;">
            <tr style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                <td style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;" valign="top"></td>
                <td class="container" width="600" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; display: block !important; max-width: 600px !important; clear: both !important; margin: 0 auto;" valign="top">
                    <div class="content" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; max-width: 600px; display: block; margin: 0 auto; padding: 20px;">
                        <table class="main" width="100%" cellpadding="0" cellspacing="0" itemprop="action" itemscope itemtype="http://schema.org/ConfirmAction" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; border-radius: 3px; margin: 0; border: none;">
                            <tr style="font-family: 'Roboto', sans-serif; font-size: 14px; margin: 0;">
                                <td class="content-wrap" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; color: #495057; font-size: 14px; vertical-align: top; margin: 0;padding: 30px; box-shadow: 0 3px 15px rgba(30,32,37,.06); ;border-radius: 7px; background-color: #fff;" valign="top">
                                    <meta itemprop="name" content="Confirm Email" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;" />
                                    <table width="100%" cellpadding="0" cellspacing="0" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                        <tr style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                            <td class="content-block" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 24px; vertical-align: top; margin: 0; padding: 0 0 10px; text-align: center;" valign="top">
                                                <h4 style="font-family: 'Roboto', sans-serif; margin-bottom: 10px; font-weight: 600;">Your order has been placed</h4>
                                            </td>
                                        </tr>
                                        <tr style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                            <td class="content-block" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 15px; vertical-align: top; margin: 0; padding: 0 0 12px;" valign="top">
                                                <h5 style="font-family: 'Roboto', sans-serif; margin-bottom: 3px;">Hey, Anna Adame</h5>
                                                <p style="font-family: 'Roboto', sans-serif; margin-bottom: 8px; color: #878a99;">Your order has been confirmed and will be shipping soon.</p>
                                            </td>
                                        </tr>
                                        <tr style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                            <td class="content-block" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 15px; vertical-align: top; margin: 0; padding: 0 0 18px;" valign="top">
                                                <table style="width:100%;">
                                                    <tbody>
                                                        <tr style="text-align: left;">
                                                            <th style="padding: 5px;">
                                                                <p style="color: #878a99; font-size: 13px; margin-bottom: 2px; font-weight: 400;">Order Number</p>
                                                                <span>VZ14524742541</span>
                                                            </th>
                                                            <th style="padding: 5px;">
                                                                <p style="color: #878a99; font-size: 13px; margin-bottom: 2px; font-weight: 400;">Order Date</p>
                                                                <span>05 April, 2022</span>
                                                            </th>
                                                            <th style="padding: 5px;">
                                                                <p style="color: #878a99; font-size: 13px; margin-bottom: 2px; font-weight: 400;">Payment Method</p>
                                                                <span>Viss - 4622</span>
                                                            </th>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                            <td class="content-block" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 15px; vertical-align: top; margin: 0; padding: 0 0 12px;" valign="top">
                                                <h6 style="font-family: 'Roboto', sans-serif; font-size: 15px; text-decoration-line: underline;margin-bottom: 15px;">Her'e what you ordered:</h6>
                                                <table style="width:100%;" cellspacing="0" cellpadding="0">
                                                    <thead style="text-align: left;">
                                                        <th style="padding: 8px;border-bottom: 1px solid #e9ebec;">Product Details</th>
                                                        <th style="padding: 8px;border-bottom: 1px solid #e9ebec;">Quantity</th>
                                                        <th style="padding: 8px;border-bottom: 1px solid #e9ebec;">Amount</th>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <td style="padding: 8px; font-size: 13px;">
                                                                <h6 style="margin-bottom: 2px; font-size: 14px;">Sweatshirt for Men (Pink)</h6>
                                                                <p style="margin-bottom: 2px; font-size: 13px; color: #878a99;">Graphic Print Men & Women Sweatshirt</p>
                                                            </td>
                                                            <td style="padding: 8px; font-size: 13px;">
                                                                02
                                                            </td>
                                                            <td style="padding: 8px; font-size: 13px;">
                                                                $239.98
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="padding: 8px; font-size: 13px;">
                                                                <h6 style="margin-bottom: 2px; font-size: 14px;">Noise NoiseFit Endure Smart Watch</h6>
                                                                <p style="margin-bottom: 2px; font-size: 13px; color: #878a99;">32.5mm (1.28 Inch) TFT Color Touch Display</p>
                                                            </td>
                                                            <td style="padding: 8px; font-size: 13px;">
                                                                01
                                                            </td>
                                                            <td style="padding: 8px; font-size: 13px;">
                                                                $94.99
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td colspan="2" style="padding: 8px; font-size: 13px; text-align: end;border-top: 1px solid #e9ebec;">
                                                                Subtotal
                                                            </td>
                                                            <th style="padding: 8px; font-size: 13px;border-top: 1px solid #e9ebec;">
                                                                $334.97
                                                            </th>
                                                        </tr>
                                                        <tr>
                                                            <td colspan="2" style="padding: 8px; font-size: 13px; text-align: end;">
                                                                Shipping Charge
                                                            </td>
                                                            <th style="padding: 8px; font-size: 13px;">
                                                                $9.50
                                                            </th>
                                                        </tr>
                                                        <tr>
                                                            <td colspan="2" style="padding: 8px; font-size: 13px; text-align: end;">
                                                                Taxs
                                                            </td>
                                                            <th style="padding: 8px; font-size: 13px;">
                                                                $15.26
                                                            </th>
                                                        </tr>
                                                        <tr>
                                                            <td colspan="2" style="padding: 8px; font-size: 13px; text-align: end;">
                                                                Discount
                                                            </td>
                                                            <th style="padding: 8px; font-size: 13px;">
                                                                $20.78
                                                            </th>
                                                        </tr>
                                                        <tr>
                                                            <td colspan="2" style="padding: 8px; font-size: 13px; text-align: end;border-top: 1px solid #e9ebec;">
                                                                Total Amount
                                                            </td>
                                                            <th style="padding: 8px; font-size: 13px;border-top: 1px solid #e9ebec;">
                                                                $338.95
                                                            </th>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                            <td class="content-block" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 15px; vertical-align: top; margin: 0; padding: 0 0 0px;" valign="top">
                                                <p style="font-family: 'Roboto', sans-serif; margin-bottom: 8px; color: #878a99;">Wl'll send you shipping confirmation when your item(s) are on the way! We appreciate your business, and hope you enjoy your purchase.</p>
                                                <h6 style="font-family: 'Roboto', sans-serif; font-size: 14px; margin-bottom: 0px; text-align: end;">Thank you!</h6>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>

                        <div style="margin-top: 32px; text-align: center;">
                            <a href="javascript:void(0)" itemprop="url" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: .8125rem; color: #FFF; text-decoration: none; font-weight: 400; text-align: center; cursor: pointer; display: inline-block; border-radius: .25rem; text-transform: capitalize; background-color: #405189; margin: 0; border-color: #405189; border-style: solid; border-width: 1px; padding: .5rem .9rem;">Download</a>
                            <a href="javascript:void(0)" itemprop="url" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: .8125rem; color: #FFF; text-decoration: none; font-weight: 400; text-align: center; cursor: pointer; display: inline-block; border-radius: .25rem; text-transform: capitalize; background-color: #0ab39c; margin: 0; border-color: #0ab39c; border-style: solid; border-width: 1px; padding: .5rem .9rem;">Back to Shop</a>
                        </div>
                        <div style="text-align: center; margin: 28px auto 0px auto;">
                            <p style="font-family: 'Roboto', sans-serif; font-size: 14px;color: #98a6ad; margin: 0px;">2022 Velzon. Design & Develop by Themesbrand</p>
                        </div>
                    </div>
                </td>
            </tr>
        </table>
    </Col>
</Row>