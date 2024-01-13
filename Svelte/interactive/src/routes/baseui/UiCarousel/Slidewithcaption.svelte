<script>
      import {
    Carousel,
    CarouselControl,
    CarouselIndicators,
    CarouselItem,
    CarouselCaption
  } from 'sveltestrap';

    // Carousel images
    import img7 from "../../../assets/images/small/img-7.jpg";
    import img2 from "../../../assets/images/small/img-2.jpg";
    import img9 from "../../../assets/images/small/img-9.jpg";

  const items = [
    {
      url: img7,
      title: 'Slide 1',
      subTitle: 'Slide 1'
    },
    {
      url: img2,
      title: 'Slide 2',
      subTitle: 'Slide 2'
    },
    {
      url: img9,
      title: 'Slide 3',
      subTitle: 'Slide 3'
    }
  ];
  let activeIndex = 0;
</script>
<Carousel {items} bind:activeIndex ride interval={2000}>
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