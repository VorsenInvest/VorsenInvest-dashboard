<script>
    import {
    Carousel,
    CarouselCaption,
    CarouselControl,
    CarouselIndicators,
    CarouselItem
  } from 'sveltestrap';

    // Carousel images
    import img1 from "../../../assets/images/small/img-1.jpg";
    import img2 from "../../../assets/images/small/img-2.jpg";
    import img3 from "../../../assets/images/small/img-3.jpg";

  const items = [
    {
      url: img1,
      title: 'Slide 1',
      subTitle: 'Slide 1'
    },
    {
      url: img2,
      title: 'Slide 2',
      subTitle: 'Slide 2'
    },
    {
      url: img3,
      title: 'Slide 3',
      subTitle: 'Slide 3'
    }
  ];
  
  let activeIndex = 0;
</script>
<Carousel class="carousel-dark" dark {items} bind:activeIndex>
    <CarouselIndicators bind:activeIndex {items} />
  
    <div class="carousel-inner">
      {#each items as item, index}
        <CarouselItem bind:activeIndex itemIndex={index}>
          <img
            src={item.url}
            class="d-block w-100"
            alt={`${item} ${index + 1}`}
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
</Carousel>