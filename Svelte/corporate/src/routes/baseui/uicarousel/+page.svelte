<script>
import { Card, CardBody, Col, Container, Row, } from 'sveltestrap';
import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
import PreviewCardHeader from '../../../Components/Common/PreviewCardHeader.svelte';
import Slide from './slide.svelte'
import Slidewithcontrol from './Slidewithcontrol.svelte'
import Slidewithindicator from './Slidewithindicator.svelte'
import Slidewithcaption from './Slidewithcaption.svelte'
import Darkvariant from './Darkvariant.svelte'
import PrismCode from '../../../Components/Common/Prism.svelte'
import UiContent from "../../../Components/Common/UiContent.svelte";
// Slides Only

const slideOnlyCode =`<Carousel {items} bind:activeIndex>
<div class="carousel-inner">
    {#each items as item, index}
    <CarouselItem bind:activeIndex itemIndex={index}>
        <img src={item} class="d-block w-100" />
    </CarouselItem>
    {/each}
</div>
</Carousel>
`;

// With Controls
const withControlCode =`<Carousel {items} bind:activeIndex>
    <div class="carousel-inner">
      {#each items as item, index}
        <CarouselItem bind:activeIndex itemIndex={index}>
          <img src={item} class="d-block w-100" />
        </CarouselItem>
      {/each}
    </div>
  
    <CarouselControl direction="prev" bind:activeIndex {items} />
    <CarouselControl direction="next" bind:activeIndex {items} />
  </Carousel>
`;

// with Indicators
const withIndicatorCode =`<Carousel {items} bind:activeIndex>
    <CarouselIndicators bind:activeIndex {items} />

    <div class="carousel-inner">
        {#each items as item, index}
        <CarouselItem bind:activeIndex itemIndex={index}>
            <img src={item} class="d-block w-100" />
        </CarouselItem>
        {/each}
    </div>

<CarouselControl direction="prev" bind:activeIndex {items} />
<CarouselControl direction="next" bind:activeIndex {items} />
</Carousel>
`;

// with Captions
const withCaptionCode =`<Carousel {items} bind:activeIndex ride interval={2000}>
    <CarouselIndicators bind:activeIndex {items} />
  
    <div class="carousel-inner">
      {#each items as item, index}
        <CarouselItem bind:activeIndex itemIndex={index}>
          <img src={item.url} class="d-block w-100" alt={item.title} />
          <CarouselCaption
            captionHeader={item.title}
            captionText={item.subTitle}
          />
        </CarouselItem>
      {/each}
    </div>
  
    <CarouselControl direction="prev" bind:activeIndex {items} />
    <CarouselControl direction="next" bind:activeIndex {items} />
</Carousel>
`;

//with darkvariant
const darkvariant = `<Carousel dark {items} bind:activeIndex>
    <CarouselIndicators bind:activeIndex {items} />
  
    <div class="carousel-inner">
      {#each items as item, index}
        <CarouselItem bind:activeIndex itemIndex={index}>
          <img
            src={item.url}
            class="d-block w-100"
          
          />
          <CarouselCaption
            captionHeader={item.title}
            captionText={item.subTitle}
          />
        </CarouselItem>
      {/each}
    </div>
  
    <CarouselControl direction="prev" bind:activeIndex {items} />
    <CarouselControl direction="next" bind:activeIndex {items} />
</Carousel>`;
</script>
<UiContent />
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Carousel" pageTitle="Base UI" />
        <Row>
            <Col xl={6}>
                <Card>
                    <PreviewCardHeader title="Slides Only" />
                    <CardBody>                                    
                        <div class="live-preview">
                            <Slide />
                        </div>
                        <div class="d-none code-view">
                            <PrismCode
                                code={slideOnlyCode}
                                id="slideOnlyCode"
                            />
                        </div>
                    </CardBody>
                </Card>
            </Col>
            <Col xl={6}>
                <Card>
                    <PreviewCardHeader title="With Controls" />
                    <CardBody>                                    
                        <div class="live-preview">
                            <Slidewithcontrol />
                        </div>
                        <div class="d-none code-view">
                            <PrismCode
                                code={withControlCode}
                                id="withControlCode"
                            />
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>

        <Row>
            <Col xl={6}>
                <Card>
                    <PreviewCardHeader title="with Indicators" />

                    <CardBody>                                    
                        <div class="live-preview">
                            <Slidewithindicator />
                        </div>

                        <div class="d-none code-view">
                            <PrismCode
                                code={withIndicatorCode}
                                id="withIndicatorCode"
                            />
                        </div>

                    </CardBody>
                </Card>
            </Col>

            <Col xl={6}>
                <Card>
                    <PreviewCardHeader title="with Captions" />
                    <CardBody>                                    
                        <div class="live-preview" >
                            <Slidewithcaption />
                        </div>
                        <div class="d-none code-view">
                            <PrismCode
                                code={withCaptionCode}
                                id="withCaptionCode"
                            />
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>
        <Row>
            <Col xl={6}>
                <Card>
                    <PreviewCardHeader title="Crossfade Animation" />

                    <CardBody>                                    
                        <div class="live-preview">
                            <Slidewithindicator />
                        </div>

                        <div class="d-none code-view">
                            <PrismCode
                                code={withIndicatorCode}
                                id="withIndicatorCode"
                            />
                        </div>

                    </CardBody>
                </Card>
            </Col>

            <Col xl={6}>
                <Card>
                    <PreviewCardHeader title="Individual carousel-item Interval" />
                    <CardBody>                                    
                        <div class="live-preview" >
                            <Slidewithcaption />
                        </div>
                        <div class="d-none code-view">
                            <PrismCode
                                code={withCaptionCode}
                                id="withCaptionCode"
                            />
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>
        <Row>
            <Col xl={6}>
                <Card>
                    <PreviewCardHeader title="Disable Touch Swiping" />
                    <CardBody>                                    
                        <div class="live-preview" >
                            <Slidewithcaption />
                        </div>
                        <div class="d-none code-view">
                            <PrismCode
                                code={withCaptionCode}
                                id="withCaptionCode"
                            />
                        </div>
                    </CardBody>
                </Card>
            </Col>
            <Col xl={6}>
                <Card>
                    <PreviewCardHeader title="Dark variant" />
                    <CardBody>                                    
                        <div class="live-preview">
                            <Darkvariant />
                        </div>
                        <div class="d-none code-view">
                            <PrismCode
                                code={darkvariant}
                                id="darkvariant"
                            />
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>
        
    </Container>
</div>