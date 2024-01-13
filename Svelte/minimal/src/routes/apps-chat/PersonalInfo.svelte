<script>
  import Link from "svelte-link";
  import {onMount} from "svelte";
  import {
    Button,
    Offcanvas,
    Dropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem,
  } from "sveltestrap";

  import data from "../../common/data/chat";
  import Attachements from "./attachement.svelte";

  export let currentuser, cuurentiseImg, show, onCloseClick;

  import img9 from '../../assets/images/small/img-9.jpg'
  import userdummyimg from '../../assets/images/users/user-dummy-img.jpg'

  onMount(() => {
    let btnfav = document.getElementById("favourite-btn");
    if(btnfav){
      btnfav.addEventListener("click",function(){
        if(btnfav.classList.contains("active")){
          btnfav.classList.remove("active");
        }else{
          btnfav.classList.add("active");

        }
      })
    }
  });

</script>

<Offcanvas
  isOpen={show}
  placement="end"
  class="offcanvas-end border-0 profile-details-canvas"
>
  <div class="profile-offcanvas p-0">
    <div class="team-cover">
      <img src={img9} alt="" class="img-fluid" />
    </div>
    <div class="p-1 pb-4 pt-0">
      <div class="team-settings">
        <div class="row g-0">
          <div class="col">
            <div class="btn nav-btn">
              <Button
                on:click={onCloseClick}
                color=""
                class="btn-close btn-close-white"
              />
            </div>
          </div>
          <div class="col-auto">
            <div class="user-chat-nav d-flex">
              <button type="button" class="btn nav-btn favourite-btn active" id="favourite-btn">
                <i class="ri-star-fill" />
              </button>

              <Dropdown>
                <DropdownToggle
                  class="btn nav-btn p-0 text-white"
                  color=""
                  tag="a"
                >
                  <i class="ri-more-2-fill" />
                </DropdownToggle>
                <DropdownMenu class="dropdown-menu-end">
                  <DropdownItem href={null}>
                    <i
                      class="ri-inbox-archive-line align-bottom text-muted me-2"
                    />
                    Archive
                  </DropdownItem>
                  <DropdownItem href={null}>
                    <i class="ri-mic-off-line align-bottom text-muted me-2" />
                    Muted
                  </DropdownItem>
                  <DropdownItem href={null}>
                    <i
                      class="ri-delete-bin-5-line align-bottom text-muted me-2"
                    />
                    Delete
                  </DropdownItem>
                </DropdownMenu>
              </Dropdown>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="p-3 text-center">
      {#if cuurentiseImg}
        <img
          src={cuurentiseImg}
          alt=""
          class="avatar-lg img-thumbnail rounded-circle mx-auto"
        />
      {:else}
        <img
          src={userdummyimg}
          alt=""
          class="avatar-lg img-thumbnail rounded-circle mx-auto"
        />
      {/if}

      <div class="mt-3">
        <h5 class="fs-16 mb-1">
          <Link href="{null}" class="link-primary username">
            {currentuser}
          </Link>
        </h5>
        <p class="text-muted">
          <i
            class="ri-checkbox-blank-circle-fill me-1 align-bottom text-success"
          />
          Online
        </p>
      </div>
      <div class="d-flex gap-3 justify-content-center">
        <button type="button" class="btn avatar-xs p-0">
          <span class="avatar-title rounded bg-light text-body">
            <i class="ri-question-answer-line" />
          </span>
        </button>

        <button type="button" class="btn avatar-xs p-0">
          <span class="avatar-title rounded bg-light text-body">
            <i class="ri-star-line" />
          </span>
        </button>

        <button type="button" class="btn avatar-xs p-0">
          <span class="avatar-title rounded bg-light text-body">
            <i class="ri-phone-line" />
          </span>
        </button>

        <Dropdown>
          <DropdownToggle class="btn avatar-xs p-0" color="" tag="a">
            <span class="avatar-title bg-light text-body rounded">
              <i class="ri-more-fill" />
            </span>
          </DropdownToggle>
          <DropdownMenu class="dropdown-menu-end">
            <DropdownItem href={null}>
              <i class="ri-inbox-archive-line align-bottom text-muted me-2" />
              Archive
            </DropdownItem>
            <DropdownItem href={null}>
              <i class="ri-mic-off-line align-bottom text-muted me-2" />
              Muted
            </DropdownItem>
            <DropdownItem href={null}>
              <i class="ri-delete-bin-5-line align-bottom text-muted me-2" />
              Delete
            </DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </div>
    </div>
    <div class="border-top border-top-dashed p-3">
      <h5 class="fs-15 mb-3">Personal Details</h5>
      <div class="mb-3">
        <p class="text-muted text-uppercase fw-medium fs-12 mb-1">Number</p>
        <h6>+(256) 2451 8974</h6>
      </div>
      <div class="mb-3">
        <p class="text-muted text-uppercase fw-medium fs-12 mb-1">Email</p>
        <h6>lisaparker@gmail.com</h6>
      </div>
      <div>
        <p class="text-muted text-uppercase fw-medium fs-12 mb-1">Location</p>
        <h6 class="mb-0">California, USA</h6>
      </div>
    </div>

    <div class="border-top border-top-dashed p-3">
      <h5 class="fs-15 mb-3">Attached Files</h5>

      <div class="vstack gap-2">
        {#each data.attachements as attachement}
          <Attachements {attachement} />
        {/each}

        <div class="text-center mt-2">
          <button type="button" class="btn btn-primary">
            Load more{" "}
            <i class="ri-arrow-right-fill align-bottom ms-1" />
          </button>
        </div>
      </div>
    </div>
  </div>
</Offcanvas>
