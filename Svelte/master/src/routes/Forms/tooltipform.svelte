<script>
    import {
        Row,
        Col,
        Card,
        CardBody,
        Label
    } from "sveltestrap";
    import PrismCode from '../../Components/Common/Prism.svelte'
    import PreviewCardHeader from '../../Components/Common/PreviewCardHeader.svelte';
    import { createForm } from "svelte-forms-lib";
    import * as yup from "yup";

const { form, errors, state, handleChange, handleSubmit } = createForm({
    initialValues: {
    fnm: "Mark",
    lnm: "Otto",
    unm:"",
    city: "",
    stateV: ""
    },
    validationSchema: yup.object().shape({
        fnm: yup.string().required("Please Enter Valid First Name"),
        lnm: yup.string().required("Please Enter Valid Last Name"),
        unm: yup.string().required("Please Enter User Name"),
        city: yup.string().required("Please Enter Your City"),
        stateV: yup.string().required("Please Enter Your State"),
    }),
    onSubmit: values => {
      alert(JSON.stringify(values));
    }
});

const code =`<form
    class="needs-validation was-validated"
    on:submit={handleSubmit}
>
    <Row>
    <Col md="4" class="position-relative">
        
        <Label htmlfor="validationTooltip01">
            First name
        </Label>
        <input
            type="text"
            class="form-control"
            id="validationTooltip01"
            placeholder="Mark"
            name="fnm"
            on:change={handleChange}
            on:blur={handleChange}
            bind:value={$form.fnm}
            required
        />
        {#if $errors.fnm}
        <div class="invalid-tooltip">{$errors.fnm}</div>
        {:else}
        <div class="valid-tooltip">Looks good!</div>
            {/if}
    </Col>
    <Col md="4" class="position-relative">
        
        <Label htmlfor="validationTooltip02">Last name</Label>
        <input
            type="text"
            class="form-control"
            id="validationTooltip02"
            placeholder="Otto"
            name="lnm"
            on:change={handleChange}
            on:blur={handleChange}
            bind:value={$form.lnm}
            required
        />
        {#if $errors.lnm}
            <div class="invalid-tooltip">{$errors.lnm}</div>
        {:else}
            <div class="valid-tooltip">Looks good!</div>
            {/if}
    </Col>
    <Col md="4" class="position-relative">
        
        <Label htmlfor="validationTooltipUsername">
            Username
        </Label>
        <div class="input-group">
            <div class="input-group-prepend">
            <span
                class="input-group-text"
                id="validationTooltipUsernamePrepend"
            >
                @
            </span>
            </div>
            <input
                type="text"
                class="form-control"
                name="unm"
                id="validationTooltipUsername"
                placeholder="Username"
                on:change={handleChange}
                on:blur={handleChange}
                bind:value={$form.unm}
                required
            />
            {#if $errors.unm}
            <div class="invalid-tooltip">{$errors.unm}</div>
            {:else}
            <div class="valid-tooltip">Looks good!</div>
            {/if}
        </div>
    </Col>
    <Col md="6" class="position-relative">
        
        <Label htmlfor="validationTooltip03">City</Label>
        <input
            type="text"
            class="form-control"
            name="city"
            id="validationTooltip03"
            placeholder="City"
            on:change={handleChange}
            on:blur={handleChange}
            bind:value={$form.city}
            required
        />
        {#if $errors.city}
            <div class="invalid-tooltip">{$errors.city}</div>
            {:else}
            <div class="valid-tooltip">Looks good!</div>
            {/if}
    </Col>
    <Col md="6" class="position-relative">
        
        <Label htmlfor="validationTooltip04">State</Label>
        <input
            type="text"
            name="stateV"
            class="form-control"
            id="validationTooltip04"
            placeholder="State"
            on:change={handleChange}
            on:blur={handleChange}
            bind:value={$form.stateV}
            required
        />
        {#if $errors.stateV}
        <div class="invalid-tooltip">{$errors.stateV}</div>
            {:else}
            <div class="valid-tooltip">Looks good!</div>
            {/if}
    </Col>
    </Row>
    <button class="btn btn-primary" type="submit">
    Submit form
    </button>
</form>`
</script>
<Row>
    <Col>
      <Card>
        <PreviewCardHeader title="Svelte Validation(Tooltips)" />
        <CardBody>
          <p class="text-muted">
            If your form layout allows it, you can swap the
            <code>.{"{valid|invalid-}"}feedback</code> classes for
            <code>.{"{valid|invalid-}"}-tooltip</code> classes to
            display validation feedback in a styled tooltip.
          </p>
          <div class="live-preview">
            <form
              class="needs-validation was-validated"
              on:submit={handleSubmit}
            >
              <Row>
                <Col md="4" class="position-relative">
                  
                    <Label htmlfor="validationTooltip01">
                      First name
                    </Label>
                    <input
                        type="text"
                        class="form-control"
                        id="validationTooltip01"
                        placeholder="Mark"
                        name="fnm"
                        on:change={handleChange}
                        on:blur={handleChange}
                        bind:value={$form.fnm}
                        required
                    />
                    {#if $errors.fnm}
                    <div class="invalid-tooltip">{$errors.fnm}</div>
                    {:else}
                    <div class="valid-tooltip">Looks good!</div>
                      {/if}
                </Col>
                <Col md="4" class="position-relative">
                  
                    <Label htmlfor="validationTooltip02">Last name</Label>
                    <input
                        type="text"
                        class="form-control"
                        id="validationTooltip02"
                        placeholder="Otto"
                        name="lnm"
                        on:change={handleChange}
                        on:blur={handleChange}
                        bind:value={$form.lnm}
                        required
                    />
                    {#if $errors.lnm}
                        <div class="invalid-tooltip">{$errors.lnm}</div>
                    {:else}
                        <div class="valid-tooltip">Looks good!</div>
                      {/if}
                </Col>
                <Col md="4" class="position-relative">
                 
                    <Label htmlfor="validationTooltipUsername">
                      Username
                    </Label>
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span
                          class="input-group-text"
                          id="validationTooltipUsernamePrepend"
                        >
                          @
                        </span>
                      </div>
                      <input
                            type="text"
                            class="form-control"
                            name="unm"
                            id="validationTooltipUsername"
                            placeholder="Username"
                            on:change={handleChange}
                            on:blur={handleChange}
                            bind:value={$form.unm}
                            required
                      />
                      {#if $errors.unm}
                      <div class="invalid-tooltip">{$errors.unm}</div>
                        {:else}
                        <div class="valid-tooltip">Looks good!</div>
                      {/if}
                    </div>
                </Col>
                <Col md="6" class="position-relative">
                 
                    <Label htmlfor="validationTooltip03">City</Label>
                    <input
                        type="text"
                        class="form-control"
                        name="city"
                        id="validationTooltip03"
                        placeholder="City"
                        on:change={handleChange}
                        on:blur={handleChange}
                        bind:value={$form.city}
                        required
                    />
                    {#if $errors.city}
                        <div class="invalid-tooltip">{$errors.city}</div>
                        {:else}
                        <div class="valid-tooltip">Looks good!</div>
                      {/if}
                </Col>
                <Col md="6" class="position-relative">
                  
                    <Label htmlfor="validationTooltip04">State</Label>
                    <input
                        type="text"
                        name="stateV"
                        class="form-control"
                        id="validationTooltip04"
                        placeholder="State"
                        on:change={handleChange}
                        on:blur={handleChange}
                        bind:value={$form.stateV}
                        required
                    />
                    {#if $errors.stateV}
                    <div class="invalid-tooltip">{$errors.stateV}</div>
                        {:else}
                        <div class="valid-tooltip">Looks good!</div>
                      {/if}
                </Col>
              </Row>
              <button class="btn btn-primary" type="submit">
                Submit form
              </button>
            </form>
          </div>
          <div class="d-none code-view">
            <PrismCode
                code={code}
                id="tooltipform"
            />
          </div>
        </CardBody>
      </Card>
    </Col>
  </Row>