<script>
    import {
    Carousel,
    CarouselControl,
    CarouselIndicators,
    CarouselItem
  } from 'sveltestrap';

  // Carousel images
    import img1 from "../../../assets/images/small/img-1.jpg";
    import img2 from "../../../assets/images/small/img-2.jpg";
    import img3 from "../../../assets/images/small/img-3.jpg";

  const items = [
    img1,
    img2,
    img3
];
  let activeIndex = 0;
</script>
<Carousel {items} bind:activeIndex>
    <CarouselIndicators bind:activeIndex {items} />

    <div class="carousel-inner">
        {#each items as item, index}
        <CarouselItem bind:activeIndex itemIndex={index}>
            <img src={item} class="d-block w-100" alt={`${item} ${index + 1}`} />
        </CarouselItem>
        {/each}
    </div>

<CarouselControl direction="prev" bind:activeIndex {items} />
<CarouselControl direction="next" bind:activeIndex {items} />
</Carousel>