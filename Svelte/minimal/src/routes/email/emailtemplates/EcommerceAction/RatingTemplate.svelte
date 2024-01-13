<script>
    import { Row, Col } from 'sveltestrap';
    import Link from 'svelte-link';
    //import Images
    import logo_dark from "../../../../assets/images/logo-dark.png";
    import img01 from "../../../../assets/images/products/img-1.png";
    import img02 from "../../../../assets/images/products/img-2.png";
    import img03 from "../../../../assets/images/products/img-3.png";
</script>
 <!-- svelte-ignore a11y-invalid-attribute -->

<Row>
    <Col lg={12}>
        <div class="justify-content-between d-flex align-items-center mt-3 mb-4">
            <h5 class="mb-0 pb-1 text-decoration-underline">Rating and Review Email Template</h5>
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
                                <td class="content-wrap" style="font-family: 'Roboto', sans-serif;box-sizing: border-box;color: #495057;font-size: 14px;vertical-align: top;margin: 0;border: 1px solid #e9ebec;border-radius: 7px;background-color: #fff;overflow: hidden;" valign="top">
                                    <meta itemprop="name" content="Confirm Email" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;" />
                                    <div style="padding: 20px;box-sizing: border-box; text-align: center; background-image: linear-gradient(to right, #25a0e2, #25a0e2);">
                                        <h6 style="font-family: 'Roboto', sans-serif;margin: 0; font-size: 15px;color: #fff;text-transform: uppercase;">FREE 1-2 day shipping on orders over $32</h6>
                                    </div>
                                    <div style="padding: 20px;box-sizing: border-box; text-align: center; border-bottom: 1px solid #e9ebec;">
                                        <img src={logo_dark} alt="" height="23">
                                    </div>
                                    <div style="padding: 20px;box-sizing: border-box; text-align: center;">
                                        <h5 style="font-family: 'Roboto', sans-serif;margin-bottom: 10px;font-weight: 500;">What did you think of your recent purchase?</h5>
                                        <div style="color: #f7b84b;font-size: 17px;">
                                            <i class="ri-star-fill"></i>
                                            <i class="ri-star-fill"></i>
                                            <i class="ri-star-fill"></i>
                                            <i class="ri-star-fill"></i>
                                            <i class="ri-star-fill"></i>
                                        </div>
                                        <p style="font-size: 14px;color: #98a6ad;border-bottom: 1px solid #e9ebec;padding-bottom: 18px;">We'd love to hear how you and your pet enjoyed these products. Please leave a reviews so we can share it with other pet parents just like you.</p>
                                    
                                        <table style="width:100%;font-family: 'Roboto', sans-serif;">
                                            <tbody>
                                                <tr style="text-align: left;">
                                                    <th style="padding: 5px;width: 110px;">
                                                        <img src={img03} alt="" height="80">
                                                    </th>
                                                    <th style="padding: 5px;">
                                                        <h6 style="font-family: 'Roboto', sans-serif; font-size: 14px; margin-bottom: 2px; font-weight: 500;">350 ml Glass Grocery Container</h6>
                                                        <p style="color: #878a99; font-weight: 400;margin-bottom: 5px;line-height: 1.5;font-size: 12px;">Category : Grocery</p>
                                                        <a href="javascript:void(0)" itemprop="url" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: .710rem;font-weight: 400; color: #FFF; text-decoration: none; text-align: center; cursor: pointer; display: inline-block; border-radius: .25rem; text-transform: capitalize; background-color: #0ab39c; margin: 0; border-color: #0ab39c; border-style: solid; border-width: 1px; padding: .25rem .5rem;" onMouseOver="this.style.background='#099885'" onMouseOut="this.style.background='#0ab39c'">Write a Review &#8594;</a>
                                                    </th>
                                                </tr>
                                                <tr style="text-align: left;">
                                                    <th style="padding: 5px;width: 110px;">
                                                        <img src={img02} alt="" height="80">
                                                    </th>
                                                    <th style="padding: 5px;">
                                                        <h6 style="font-family: 'Roboto', sans-serif; font-size: 14px; margin-bottom: 2px; font-weight: 500;">Urban Ladder Pashe Chair</h6>
                                                        <p style="color: #878a99; font-weight: 400;margin-bottom: 5px;line-height: 1.5;font-size: 12px;">Category : Furniture</p>
                                                        <a href="javascript:void(0)" itemprop="url" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: .710rem;font-weight: 400; color: #FFF; text-decoration: none; text-align: center; cursor: pointer; display: inline-block; border-radius: .25rem; text-transform: capitalize; background-color: #0ab39c; margin: 0; border-color: #0ab39c; border-style: solid; border-width: 1px; padding: .25rem .5rem;" onMouseOver="this.style.background='#099885'" onMouseOut="this.style.background='#0ab39c'">Write a Review &#8594;</a>
                                                    </th>
                                                </tr>
                                                <tr style="text-align: left;">
                                                    <th style="padding: 5px;width: 110px;">
                                                        <img src={img01} alt="" height="80">
                                                    </th>
                                                    <th style="padding: 5px;">
                                                        <h6 style="font-family: 'Roboto', sans-serif; font-size: 14px; margin-bottom: 2px; font-weight: 500;">Half Sleeve Round Neck T-Shirts</h6>
                                                        <p style="color: #878a99; font-weight: 400;margin-bottom: 5px;line-height: 1.5;font-size: 12px;">Category : Fashion</p>
                                                        <a href="javascript:void(0)" itemprop="url" style="font-family: 'Roboto', sans-serif; box-sizing: border-box; font-size: .710rem;font-weight: 400; color: #FFF; text-decoration: none; text-align: center; cursor: pointer; display: inline-block; border-radius: .25rem; text-transform: capitalize; background-color: #0ab39c; margin: 0; border-color: #0ab39c; border-style: solid; border-width: 1px; padding: .25rem .5rem;" onMouseOver="this.style.background='#099885'" onMouseOut="this.style.background='#0ab39c'">Write a Review &#8594;</a>
                                                    </th>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                    <div style="padding: 20px;box-sizing: border-box; text-align: center; background-color: rgba(240,101,72,.1);">
                                        <h6 style="font-family: 'Roboto', sans-serif;margin: 0; font-size: 15px;text-transform: uppercase;color: #f06548;">Call us 24/7 at 1-2345-678-9123</h6>
                                    </div>
                                    <div style="padding: 20px;box-sizing: border-box; text-align: center;">
                                        <p style="font-family: 'Roboto', sans-serif;margin-bottom: 0px;font-weight: 500;color: #98a6ad;">Review text is a text that contains reviews, ratings or reviews of a work such as a film, drama, or a book.</p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                        <div style="text-align: center; margin: 28px auto 0px auto;">
                            <p style="font-family: 'Roboto', sans-serif; font-size: 14px;color: #98a6ad; margin: 0px;">2022 Velzon. Design & Develop by Themesbrand</p>
                        </div>
                    </div>
                </td>
            </tr>
        </table>
    </Col>                       
</Row>