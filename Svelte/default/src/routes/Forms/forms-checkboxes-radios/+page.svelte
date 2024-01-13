<script>
	import {
		Card,
		CardBody,
		Col,
		Container,
		Input,
		Label,
		Row,
	} from "sveltestrap";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";

	const Checkbox = `<Col lg={4} md={6}>
	<div>
		<p class="text-muted fw-medium">
			Default Checkbox
		</p>
		<p class="text-muted">
			Use <code>type="checkbox"</code>
			attribute to set a checkbox and add
			<code>checked</code> attribute to set
			a checkbox checked by default.
		</p>
		<div class="form-check mb-2">
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck1"
			/>
			<Label
				class="form-check-label"
				for="formCheck1"
				>Default checkbox</Label
			>
		</div>
		<div class="form-check">
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck2"
				checked
			/>
			/
			<Label
				class="form-check-label"
				for="formCheck2"
				>Checked checkbox</Label
			>
		</div>
	</div>
</Col>

<Col lg={4} md={6}>
	<div class="mt-4 mt-md-0">
		<p class="text-muted fw-medium">
			Disabled Checkbox
		</p>
		<p class="text-muted">
			Use <code>disabled</code> attribute
			to set a checkbox disabled and add
			<code>checked</code> attribute to set
			a checkbox checked by default.
		</p>
		<div>
			<div
				class="form-check form-check-right mb-2"
			>
				<input
					class="form-check-input"
					type="checkbox"
					value=""
					id="flexCheckDisabled"
					disabled
				/>
				<Label
					class="form-check-label"
					for="flexCheckDisabled"
				>
					Disabled checkbox
				</Label>
			</div>
		</div>
		<div>
			<div
				class="form-check form-check-right"
			>
				<input
					class="form-check-input"
					type="checkbox"
					value=""
					id="flexCheckCheckedDisabled"
					checked
					disabled
				/>
				<Label
					class="form-check-label"
					for="flexCheckCheckedDisabled"
				>
					Disabled checked checkbox
				</Label>
			</div>
		</div>
	</div>
</Col>

<Col lg={4} md={6}>
	<div class="mt-4 mt-md-0">
		<p class="text-muted fw-medium">
			Checkbox Right
		</p>
		<p class="text-muted">
			Use <code>form-check-right</code> class
			to form-check class to set a checkbox
			on the right side.
		</p>
		<div
			class="form-check form-check-right mb-2"
		>
			<input
				class="form-check-input"
				type="checkbox"
				name="formCheckboxRight"
				id="formCheckboxRight1"
			/>
			<Label
				class="form-check-label"
				for="formCheckboxRight1"
			>
				Form Radio Right
			</Label>
		</div>
		<div>
			<div
				class="form-check form-check-right"
			>
				<input
					class="form-check-input"
					type="checkbox"
					value=""
					id="flexCheckCheckedRightDisabled"
					checked
					disabled
				/>
				<Label
					class="form-check-label"
					for="flexCheckCheckedRightDisabled"
				>
					Disabled checked checkbox
				</Label>
			</div>
		</div>
	</div>
</Col>

<Col lg={6}>
	<div class="mt-3">
		<p class="text-muted fw-medium">
			Indeterminate
		</p>
		<div>
			<div class="form-check">
				<input
					class="form-check-input"
					type="checkbox"
					value=""
					id="defaultIndeterminateCheck"
				/>
				<Label
					class="form-check-label"
					for="defaultIndeterminateCheck"
				>
					Indeterminate checkbox
				</Label>
			</div>
		</div>
	</div>
</Col>
`;

	//Custom Checkbox

	const CustomCheckbox = `<Col md={6}>
<div>
	<p class="text-muted">
		Use <code>form-check-</code> class with
		below-mentioned color variation to set
		a color checkbox.
	</p>
	<div>
		<div class="form-check mb-3">
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck6"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck6"
			>
				Checkbox Primary
			</Label>
		</div>
		<div
			class="form-check form-check-secondary mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck7"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck7"
			>
				Checkbox Secondary
			</Label>
		</div>
		<div
			class="form-check form-check-success mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck8"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck8"
			>
				Checkbox Success
			</Label>
		</div>
		<div
			class="form-check form-check-warning mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck9"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck9"
			>
				Checkbox Warning
			</Label>
		</div>
		<div
			class="form-check form-check-danger mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck10"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck10"
			>
				Checkbox Danger
			</Label>
		</div>
		<div
			class="form-check form-check-info mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck11"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck11"
				>Checkbox Info</Label
			>
		</div>
		<div
			class="form-check form-check-dark"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck12"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck12"
				>Checkbox Dark</Label
			>
		</div>
	</div>
</div>
</Col>

<Col md={6}>
<div class="mt-4 mt-md-0">
	<p class="text-muted">
		Use <code>form-check-outline</code>
		class and <code>form-check-</code> class
		with below-mentioned color variation
		to set a color checkbox with outline.
	</p>

	<div>
		<div
			class="form-check form-check-outline form-check-primary mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck13"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck13"
			>
				Checkbox Outline Primary
			</Label>
		</div>
		<div
			class="form-check form-check-outline form-check-secondary mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck14"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck14"
			>
				Checkbox Outline Secondary
			</Label>
		</div>
		<div
			class="form-check form-check-outline form-check-success mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck15"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck15"
			>
				Checkbox Outline Success
			</Label>
		</div>
		<div
			class="form-check form-check-outline form-check-warning mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck16"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck16"
			>
				Checkbox Outline Warning
			</Label>
		</div>
		<div
			class="form-check form-check-outline form-check-danger mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck17"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck17"
			>
				Checkbox Outline Danger
			</Label>
		</div>
		<div
			class="form-check form-check-outline form-check-info mb-3"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck18"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck18"
			>
				Checkbox Outline Info
			</Label>
		</div>
		<div
			class="form-check form-check-outline form-check-dark"
		>
			<input
				class="form-check-input"
				type="checkbox"
				id="formCheck19"
				checked
			/>
			<Label
				class="form-check-label"
				for="formCheck19"
			>
				Checkbox Outline Dark
			</Label>
		</div>
	</div>
</div>
</Col>
`;

	const Radio = `<Col lg={4} md={6}>
<div>
	<p class="text-muted fw-medium">
		Default Radios
	</p>
	<p class="text-muted">
		Use <code>type="radio"</code>
		attribute to set a radio button and add
		<code>checked</code> attribute to set
		a radio checked by default.
	</p>
	<div class="form-check mb-2">
		<input
			class="form-check-input"
			type="radio"
			name="flexRadioDefault"
			id="flexRadioDefault1"
		/>
		<Label
			class="form-check-label"
			for="flexRadioDefault1"
		>
			Default radio
		</Label>
	</div>
	<div class="form-check">
		<input
			class="form-check-input"
			type="radio"
			name="flexRadioDefault"
			id="flexRadioDefault2"
			checked
		/>
		<Label
			class="form-check-label"
			for="flexRadioDefault2"
		>
			Default checked radio
		</Label>
	</div>
</div>
</Col>
<Col lg={4} md={6}>
<div class="mt-4 mt-md-0">
	<p class="text-muted fw-medium">
		Disabled Radios
	</p>
	<p class="text-muted">
		Use <code>disabled</code> attribute
		to set a radio button disabled and
		add
		<code>checked</code> attribute to set
		a radio checked by default.
	</p>
	<div class="form-check mb-2">
		<input
			class="form-check-input"
			type="radio"
			name="flexRadioDisabled"
			id="flexRadioDisabled"
			disabled
		/>
		<Label
			class="form-check-label"
			for="flexRadioDisabled"
		>
			Disabled radio
		</Label>
	</div>
	<div>
		<div class="form-check">
			<input
				class="form-check-input"
				type="radio"
				name="flexRadioDisabled"
				id="flexRadioCheckedDisabled"
				checked
				disabled
			/>
			<Label
				class="form-check-label"
				for="flexRadioCheckedDisabled"
			>
				Disabled checked radio
			</Label>
		</div>
	</div>
</div>
</Col>

<Col lg={4} md={6}>
<div class="mt-4 mt-md-0">
	<p class="text-muted fw-medium">
		Radio Right
	</p>
	<p class="text-muted">
		Use <code>form-check-right</code> class
		to form-check class to set a radio button
		on the right side.
	</p>
	<div
		class="form-check form-check-right mb-2"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradioRight"
			id="formradioRight1"
		/>
		<Label
			class="form-check-label"
			for="formradioRight1"
		>
			Form Radio Right
		</Label>
	</div>
	<div>
		<div
			class="form-check form-check-right"
		>
			<input
				class="form-check-input"
				type="radio"
				value=""
				name="formradioRight"
				id="flexCheckCheckedDisabled2"
				checked
				disabled
			/>
			<Label
				class="form-check-label"
				for="flexCheckCheckedDisabled2"
			>
				Disabled checked radio
			</Label>
		</div>
	</div>
</div>
</Col>
`;

	const CustomRadio = `<Col md={6}>
<div>
	<p class="text-muted">
		Use <code>form-check-</code> class with
		below-mentioned color variation to set
		a color radio.
	</p>

	<div
		class="form-check form-radio-primary mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor1"
			id="formradioRight5"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight5"
		>
			Radio Primary
		</Label>
	</div>

	<div
		class="form-check form-radio-secondary mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor2"
			id="formradioRight6"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight6"
		>
			Radio Secondary
		</Label>
	</div>

	<div
		class="form-check form-radio-success mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor3"
			id="formradioRight7"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight7"
		>
			Radio Success
		</Label>
	</div>

	<div
		class="form-check form-radio-warning mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor4"
			id="formradioRight8"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight8"
		>
			Radio Warning
		</Label>
	</div>

	<div
		class="form-check form-radio-danger mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor5"
			id="formradioRight9"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight9"
			>Radio Danger</Label
		>
	</div>

	<div
		class="form-check form-radio-info mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor6"
			id="formradioRight10"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight10"
			>Radio Info</Label
		>
	</div>

	<div class="form-check form-radio-dark">
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor7"
			id="formradioRight11"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight11"
			>Radio Dark</Label
		>
	</div>
</div>
</Col>

<Col md={6}>
<div class="mt-4 mt-md-0">
	<p class="text-muted">
		Use <code>form-check-outline</code>
		class and <code>form-check-</code> class
		with below-mentioned color variation
		to set a color radio with outline.
	</p>

	<div
		class="form-check form-radio-outline form-radio-primary mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor9"
			id="formradioRight13"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight13"
		>
			Radio Outline Primary
		</Label>
	</div>

	<div
		class="form-check form-radio-outline form-radio-secondary mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor10"
			id="formradioRight14"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight14"
		>
			Radio Outline Secondary
		</Label>
	</div>

	<div
		class="form-check form-radio-outline form-radio-success mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor11"
			id="formradioRight15"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight15"
		>
			Radio Outline Success
		</Label>
	</div>

	<div
		class="form-check form-radio-outline form-radio-warning mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor12"
			id="formradioRight16"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight16"
		>
			Radio Outline Warning
		</Label>
	</div>

	<div
		class="form-check form-radio-outline form-radio-danger mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor13"
			id="formradioRight17"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight17"
		>
			Radio Outline Danger
		</Label>
	</div>

	<div
		class="form-check form-radio-outline form-radio-info mb-3"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor14"
			id="formradioRight18"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight18"
		>
			Radio Outline Info
		</Label>
	</div>

	<div
		class="form-check form-radio-outline form-radio-dark"
	>
		<input
			class="form-check-input"
			type="radio"
			name="formradiocolor15"
			id="formradioRight19"
			checked
		/>
		<Label
			class="form-check-label"
			for="formradioRight19"
		>
			Radio Outline Dark
		</Label>
	</div>
</div>
</Col>
`;

	const Switches = `<Col lg={4} md={6}>
<div>
	<p class="text-muted fw-medium">
		Default Switches
	</p>
	<p class="text-muted">
		Use <code>form-switch</code> class
		to form-check class to set a switch
		and add
		<code>checked</code> attribute to set
		a switch checked by default.
	</p>
	<div
		class="form-check form-switch mb-2"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="flexSwitchCheckDefault"
		/>
		<Label
			class="form-check-label"
			for="flexSwitchCheckDefault"
			>Default switch input</Label
		>
	</div>

	<div class="form-check form-switch">
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="flexSwitchCheckChecked"
			checked
		/>
		<Label
			class="form-check-label"
			for="flexSwitchCheckChecked"
			>Checked switch input</Label
		>
	</div>
</div>
</Col>

<Col lg={4} md={6}>
<div class="mt-4 mt-md-0">
	<p class="text-muted fw-medium">
		Disabled Switches
	</p>
	<p class="text-muted">
		Use <code>disabled</code> attribute
		to set a radio button disabled and
		add
		<code>checked</code> attribute to set
		a switch checked by default.
	</p>
	<div
		class="form-check form-switch mb-2"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="flexSwitchCheckDisabled"
			disabled
		/>
		<Label
			class="form-check-label"
			for="flexSwitchCheckDisabled"
			>Switch input</Label
		>
	</div>

	<div class="form-check form-switch">
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="flexSwitchCheckCheckedDisabled1"
			checked
			disabled
		/>
		<Label
			class="form-check-label"
			for="flexSwitchCheckCheckedDisabled1"
			>Disabled checked switch input</Label
		>
	</div>
</div>
</Col>

<Col lg={4} md={6}>
<div class="mt-4 mt-md-0">
	<p class="text-muted fw-medium">
		Switch Right
	</p>
	<p class="text-muted">
		Use <code>form-check-right</code> class
		to form-check class to set a switch button
		on the right side.
	</p>
	<div>
		<div
			class="form-check form-switch form-check-right mb-2"
		>
			<input
				class="form-check-input"
				type="checkbox"
				role="switch"
				id="flexSwitchCheckRightDisabled"
				checked
			/>
			<Label
				class="form-check-label"
				for="flexSwitchCheckRightDisabled"
				>Switch Right input</Label
			>
		</div>
	</div>

	<div>
		<div
			class="form-check form-switch form-check-right"
		>
			<input
				class="form-check-input"
				type="checkbox"
				role="switch"
				id="flexSwitchCheckCheckedDisabled2"
				disabled
			/>
			<Label
				class="form-check-label"
				for="flexSwitchCheckCheckedDisabled2"
				>Disabled checked switch
				input</Label
			>
		</div>
	</div>
</div>
</Col>

<Col lg={4} md={6}>
<div class="mt-3">
	<p class="text-muted fw-medium">
		Switch sizes
	</p>
	<p class="text-muted">
		Use <code>form-switch-md</code>
		class to set a medium size switch button
		and
		<code>form-switch-lg</code> class to
		form-check class to set a large size
		switch button respectively. No such class
		is required for small size switch button.
	</p>

	<div
		class="form-check form-switch mb-3"
		dir="ltr"
	>
		<input
			type="checkbox"
			class="form-check-input"
			id="customSwitchsizesm"
			checked=""
		/>
		<Label
			class="form-check-label"
			for="customSwitchsizesm"
			>Small Size Switch</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-md mb-3"
		dir="ltr"
	>
		<input
			type="checkbox"
			class="form-check-input"
			id="customSwitchsizemd"
		/>
		<Label
			class="form-check-label"
			for="customSwitchsizemd"
			>Medium Size Switch</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-lg"
		dir="ltr"
	>
		<input
			type="checkbox"
			class="form-check-input"
			id="customSwitchsizelg"
			checked=""
		/>
		<Label
			class="form-check-label"
			for="customSwitchsizelg"
			>Large Size Switch</Label
		>
	</div>
</div>
</Col>
`;

	const SwitchColor = `<Col md={6}>
<div>
	<div
		class="form-check form-switch mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck1"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck1"
			>Switch Default</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-secondary mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck2"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck2"
			>Switch Secondary</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-success mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck3"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck3"
			>Switch Success</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-warning mb-2 mb-md-0"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck4"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck4"
			>Switch Warning</Label
		>
	</div>
</div>
</Col>

<Col md={6}>
<div>
	<div
		class="form-check form-switch form-switch-danger mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck5"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck5"
			>Switch Danger</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-info mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck6"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck6"
			>Switch Info</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-dark mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck7"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck7"
			>Switch Dark</Label
		>
	</div>
</div>
</Col>
    `;

	const CustomSwitches = `<Col md={6}>
<div>
	<div
		class="form-check form-switch form-switch-custom form-switch-primary mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck9"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck9"
			>Switch Primary</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-custom form-switch-secondary mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck10"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck10"
			>Switch Secondary</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-custom form-switch-success mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck11"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck11"
			>Switch Success</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-custom form-switch-warning mb-2 mb-md-0"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck12"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck12"
			>Switch Warning</Label
		>
	</div>
</div>
</Col>

<Col md={6}>
<div class="mt-4 mt-md-0">
	<div
		class="form-check form-switch form-switch-custom form-switch-danger mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck13"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck13"
			>Switch Danger</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-custom form-switch-info mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck14"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck14"
			>Switch Info</Label
		>
	</div>

	<div
		class="form-check form-switch form-switch-custom form-switch-dark mb-3"
	>
		<input
			class="form-check-input"
			type="checkbox"
			role="switch"
			id="SwitchCheck15"
			checked
		/>
		<Label
			class="form-check-label"
			for="SwitchCheck15"
			>Switch Dark</Label
		>
	</div>
</div>
</Col>
        `;

	const InlineCheckboxRadio = `<Col lg={4}>
<div class="mt-4 mt-lg-0">
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="checkbox"
			id="inlineCheckbox6"
			value="option1"
		/>
		<Label
			class="form-check-label"
			for="inlineCheckbox6">1</Label
		>
	</div>
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="checkbox"
			id="inlineCheckbox7"
			value="option2"
		/>
		<Label
			class="form-check-label"
			for="inlineCheckbox7">2</Label
		>
	</div>
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="checkbox"
			id="inlineCheckbox8"
			value="option3"
			disabled
		/>
		<Label
			class="form-check-label"
			for="inlineCheckbox8"
			>3 (disabled)</Label
		>
	</div>
</div>
</Col>

<Col lg={4}>
<div class="mt-4 mt-lg-0">
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="radio"
			name="inlineRadioOptions1"
			id="inlineRadio1"
			value="option1"
		/>
		<Label
			class="form-check-label"
			for="inlineRadio1">1</Label
		>
	</div>
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="radio"
			name="inlineRadioOptions2"
			id="inlineRadio2"
			value="option2"
		/>
		<Label
			class="form-check-label"
			for="inlineRadio2">2</Label
		>
	</div>
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="radio"
			name="inlineRadioOptions3"
			id="inlineRadio3"
			value="option3"
			disabled
		/>
		<Label
			class="form-check-label"
			for="inlineRadio3"
			>3 (disabled)</Label
		>
	</div>
</div>
</Col>

<Col lg={4}>
<div class="mt-4 mt-lg-0">
	<div
		class="form-check form-switch form-check-inline"
		dir="ltr"
	>
		<input
			type="checkbox"
			class="form-check-input"
			id="inlineswitch5"
		/>
		<Label
			class="form-check-label"
			for="inlineswitch5">1</Label
		>
	</div>
	<div
		class="form-check form-switch form-check-inline"
		dir="ltr"
	>
		<input
			type="checkbox"
			class="form-check-input"
			id="inlineswitch6"
		/>
		<Label
			class="form-check-label"
			for="inlineswitch6">2</Label
		>
	</div>
	<div
		class="form-check form-switch form-check-inline"
		dir="ltr"
	>
		<input
			type="checkbox"
			class="form-check-input"
			id="inlineswitchdisabled2"
			disabled
		/>
		<Label
			class="form-check-label"
			for="inlineswitchdisabled2"
			>2</Label
		>
	</div>
</div>
</Col>
`;

	const WithoutLabels = `<Col lg={4}>
<div class="mt-4 mt-lg-0">
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="checkbox"
			id="inlineCheckbox1"
			value="option1"
		/>
	</div>
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="checkbox"
			id="inlineCheckbox2"
			value="option2"
		/>
	</div>
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="checkbox"
			id="inlineCheckbox3"
			value="option3"
			disabled
		/>
	</div>
</div>
</Col>

<Col lg={4}>
<div class="mt-4 mt-lg-0">
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="radio"
			name="inlineRadioOptions"
			id="WithoutinlineRadio1"
			value="option1"
		/>
	</div>
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="radio"
			name="inlineRadioOptions"
			id="WithoutinlineRadio2"
			value="option2"
		/>
	</div>
	<div
		class="form-check form-check-inline"
	>
		<input
			class="form-check-input"
			type="radio"
			name="inlineRadioOptions"
			id="WithoutinlineRadio3"
			value="option3"
			disabled
		/>
	</div>
</div>
</Col>

<Col lg={4}>
<div class="mt-4 mt-lg-0">
	<div
		class="form-check form-switch form-check-inline"
		dir="ltr"
	>
		<input
			type="checkbox"
			class="form-check-input"
			id="inlineswitch"
		/>
	</div>
	<div
		class="form-check form-switch form-check-inline"
		dir="ltr"
	>
		<input
			type="checkbox"
			class="form-check-input"
			id="inlineswitch1"
		/>
	</div>
	<div
		class="form-check form-switch form-check-inline"
		dir="ltr"
	>
		<input
			type="checkbox"
			class="form-check-input"
			id="inlineswitchdisabled"
			disabled
		/>
	</div>
</div>
</Col>
`;

	//Radio Toggle Buttons
	const RadioToggleButtons = `<div class="hstack gap-2 flex-wrap">
<input
	type="radio"
	class="btn-check"
	name="options"
	id="option1"
	checked
/>
<Label class="btn btn-secondary" for="option1"
	>Checked</Label
>

<input
	type="radio"
	class="btn-check"
	name="options"
	id="option2"
/>
<Label class="btn btn-secondary" for="option2"
	>Radio</Label
>

<input
	type="radio"
	class="btn-check"
	name="options"
	id="option3"
	disabled
/>
<Label class="btn btn-secondary" for="option3"
	>Disabled</Label
>

<input
	type="radio"
	class="btn-check"
	name="options"
	id="option4"
/>
<Label class="btn btn-secondary" for="option4"
	>Radio</Label
>
</div>
`;

	//Outlined Styles
	const OutlinedStyles = `<div class="hstack gap-2 flex-wrap">
<input
	type="checkbox"
	class="btn-check"
	id="btn-check-outlined"
/>
<Label
	class="btn btn-outline-primary"
	for="btn-check-outlined"
	>Single toggle</Label
>

<input
	type="checkbox"
	class="btn-check"
	id="btn-check-2-outlined"
	checked
/>
<Label
	class="btn btn-outline-secondary"
	for="btn-check-2-outlined">Checked</Label
>

<input
	type="radio"
	class="btn-check"
	name="options-outlined"
	id="success-outlined"
	checked
/>
<Label
	class="btn btn-outline-success"
	for="success-outlined"
	>Checked success radio</Label
>

<input
	type="radio"
	class="btn-check"
	name="options-outlined"
	id="danger-outlined"
/>
<Label
	class="btn btn-outline-danger"
	for="danger-outlined">Danger radio</Label
>
</div>
`;
</script>

<svelte:head>
	<title
		>Checkboxes & Radio | Velzon - Svelte Admin & Dashboard Template</title
	>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Checkbox & Radio" pageTitle="Forms" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Checkbox" />
					<CardBody>
						<div class="live-preview">
							<Row>
								<Col lg={4} md={6}>
									<div>
										<p class="text-muted fw-medium">
											Default Checkbox
										</p>
										<p class="text-muted">
											Use <code>type="checkbox"</code>
											attribute to set a checkbox and add
											<code>checked</code> attribute to set
											a checkbox checked by default.
										</p>
										<div class="form-check mb-2">
											<input
												class="form-check-input"
												type="checkbox"
												id="formCheck1"
											/>
											<Label
												class="form-check-label"
												for="formCheck1"
												>Default checkbox</Label
											>
										</div>
										<div class="form-check">
											<input
												class="form-check-input"
												type="checkbox"
												id="formCheck2"
												checked
											/>
											<Label
												class="form-check-label"
												for="formCheck2"
												>Checked checkbox</Label
											>
										</div>
									</div>
								</Col>

								<Col lg={4} md={6}>
									<div class="mt-4 mt-md-0">
										<p class="text-muted fw-medium">
											Disabled Checkbox
										</p>
										<p class="text-muted">
											Use <code>disabled</code> attribute
											to set a checkbox disabled and add
											<code>checked</code> attribute to set
											a checkbox checked by default.
										</p>
										<div>
											<div class="form-check form-check-right mb-2"
											>
												<input
													class="form-check-input"
													type="checkbox"
													value=""
													id="flexCheckDisabled"
													disabled
												/>
												<Label
													class="form-check-label"
													for="flexCheckDisabled"
												>
													Disabled checkbox
												</Label>
											</div>
										</div>
										<div>
											<div class="form-check form-check-right"
											>
												<input
													class="form-check-input"
													type="checkbox"
													value=""
													id="flexCheckCheckedDisabled"
													checked
													disabled
												/>
												<Label
													class="form-check-label"
													for="flexCheckCheckedDisabled"
												>
													Disabled checked checkbox
												</Label>
											</div>
										</div>
									</div>
								</Col>

								<Col lg={4} md={6}>
									<div class="mt-4 mt-md-0">
										<p class="text-muted fw-medium">
											Checkbox Right
										</p>
										<p class="text-muted">
											Use <code>form-check-right</code> class
											to form-check class to set a checkbox
											on the right side.
										</p>
										<div class="form-check form-check-right mb-2"
										>
											<input
												class="form-check-input"
												type="checkbox"
												name="formCheckboxRight"
												id="formCheckboxRight1"
												checked
											/>
											<Label
												class="form-check-label"
												for="formCheckboxRight1"
											>
												Form Radio Right
											</Label>
										</div>
										<div>
											<div class="form-check form-check-right"
											>
												<input
													class="form-check-input"
													type="checkbox"
													value=""
													id="flexCheckCheckedRightDisabled"
													checked
													disabled
												/>
												<Label
													class="form-check-label"
													for="flexCheckCheckedRightDisabled"
												>
													Disabled checked checkbox
												</Label>
											</div>
										</div>
									</div>
								</Col>

								<Col lg={6}>
									<div class="mt-3">
										<p class="text-muted fw-medium">
											Indeterminate
										</p>
										<div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													value=""
													id="defaultIndeterminateCheck"
												/>
												<Label
													class="form-check-label"
													for="defaultIndeterminateCheck"
												>
													Indeterminate checkbox
												</Label>
											</div>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={Checkbox} id="formcheckbox"/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<div class="col-12">
				<Card>
					<PreviewCardHeader title="Custom Checkboxes" />
					<CardBody>
						<div class="live-preview">
							<Row>
								<Col md={6}>
									<div>
										<p class="text-muted">
											Use <code>form-check-</code> class with
											below-mentioned color variation to set
											a color checkbox.
										</p>
										<div>
											<div class="form-check mb-3">
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck6"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck6"
												>
													Checkbox Primary
												</Label>
											</div>
											<div class="form-check form-check-secondary mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck7"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck7"
												>
													Checkbox Secondary
												</Label>
											</div>
											<div class="form-check form-check-success mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck8"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck8"
												>
													Checkbox Success
												</Label>
											</div>
											<div class="form-check form-check-warning mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck9"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck9"
												>
													Checkbox Warning
												</Label>
											</div>
											<div class="form-check form-check-danger mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck10"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck10"
												>
													Checkbox Danger
												</Label>
											</div>
											<div class="form-check form-check-info mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck11"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck11"
													>Checkbox Info</Label
												>
											</div>
											<div class="form-check form-check-dark"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck12"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck12"
													>Checkbox Dark</Label
												>
											</div>
										</div>
									</div>
								</Col>

								<Col md={6}>
									<div class="mt-4 mt-md-0">
										<p class="text-muted">
											Use <code>form-check-outline</code>
											class and <code>form-check-</code> class
											with below-mentioned color variation
											to set a color checkbox with outline.
										</p>

										<div>
											<div class="form-check form-check-outline form-check-primary mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck13"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck13"
												>
													Checkbox Outline Primary
												</Label>
											</div>
											<div class="form-check form-check-outline form-check-secondary mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck14"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck14"
												>
													Checkbox Outline Secondary
												</Label>
											</div>
											<div class="form-check form-check-outline form-check-success mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck15"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck15"
												>
													Checkbox Outline Success
												</Label>
											</div>
											<div class="form-check form-check-outline form-check-warning mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck16"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck16"
												>
													Checkbox Outline Warning
												</Label>
											</div>
											<div class="form-check form-check-outline form-check-danger mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck17"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck17"
												>
													Checkbox Outline Danger
												</Label>
											</div>
											<div class="form-check form-check-outline form-check-info mb-3"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck18"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck18"
												>
													Checkbox Outline Info
												</Label>
											</div>
											<div class="form-check form-check-outline form-check-dark"
											>
												<input
													class="form-check-input"
													type="checkbox"
													id="formCheck19"
													checked
												/>
												<Label
													class="form-check-label"
													for="formCheck19"
												>
													Checkbox Outline Dark
												</Label>
											</div>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={CustomCheckbox} id="CustomCheckbox"/>
						</div>
					</CardBody>
				</Card>
			</div>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Radios" />
					<CardBody>
						<div class="live-preview">
							<Row>
								<Col lg={4} md={6}>
									<div>
										<p class="text-muted fw-medium">
											Default Radios
										</p>
										<p class="text-muted">
											Use <code>type="radio"</code>
											attribute to set a radio button and add
											<code>checked</code> attribute to set
											a radio checked by default.
										</p>
										<div class="form-check mb-2">
											<input
												class="form-check-input"
												type="radio"
												name="flexRadioDefault"
												id="flexRadioDefault1"
											/>
											<Label
												class="form-check-label"
												for="flexRadioDefault1"
											>
												Default radio
											</Label>
										</div>
										<div class="form-check">
											<input
												class="form-check-input"
												type="radio"
												name="flexRadioDefault"
												id="flexRadioDefault2"
												checked
											/>
											<Label
												class="form-check-label"
												for="flexRadioDefault2"
											>
												Default checked radio
											</Label>
										</div>
									</div>
								</Col>
								<Col lg={4} md={6}>
									<div class="mt-4 mt-md-0">
										<p class="text-muted fw-medium">
											Disabled Radios
										</p>
										<p class="text-muted">
											Use <code>disabled</code> attribute
											to set a radio button disabled and
											add
											<code>checked</code> attribute to set
											a radio checked by default.
										</p>
										<div class="form-check mb-2">
											<input
												class="form-check-input"
												type="radio"
												name="flexRadioDisabled"
												id="flexRadioDisabled"
												disabled
											/>
											<Label
												class="form-check-label"
												for="flexRadioDisabled"
											>
												Disabled radio
											</Label>
										</div>
										<div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="radio"
													name="flexRadioDisabled"
													id="flexRadioCheckedDisabled"
													checked
													disabled
												/>
												<Label
													class="form-check-label"
													for="flexRadioCheckedDisabled"
												>
													Disabled checked radio
												</Label>
											</div>
										</div>
									</div>
								</Col>

								<Col lg={4} md={6}>
									<div class="mt-4 mt-md-0">
										<p class="text-muted fw-medium">
											Radio Right
										</p>
										<p class="text-muted">
											Use <code>form-check-right</code> class
											to form-check class to set a radio button
											on the right side.
										</p>
										<div class="form-check form-check-right mb-2"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradioRight"
												id="formradioRight1"
											/>
											<Label
												class="form-check-label"
												for="formradioRight1"
											>
												Form Radio Right
											</Label>
										</div>
										<div>
											<div class="form-check form-check-right"
											>
												<input
													class="form-check-input"
													type="radio"
													value=""
													name="formradioRight"
													id="flexCheckCheckedDisabled2"
													checked
													disabled
												/>
												<Label
													class="form-check-label"
													for="flexCheckCheckedDisabled2"
												>
													Disabled checked radio
												</Label>
											</div>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={Radio} id="fromRadio"/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<div class="col-12">
				<Card>
					<PreviewCardHeader title="Custom Radio" />
					<CardBody>
						<div class="live-preview">
							<Row>
								<Col md={6}>
									<div>
										<p class="text-muted">
											Use <code>form-check-</code> class with
											below-mentioned color variation to set
											a color radio.
										</p>

										<div class="form-check form-radio-primary mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor1"
												id="formradioRight5"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight5"
											>
												Radio Primary
											</Label>
										</div>

										<div class="form-check form-radio-secondary mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor2"
												id="formradioRight6"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight6"
											>
												Radio Secondary
											</Label>
										</div>

										<div class="form-check form-radio-success mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor3"
												id="formradioRight7"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight7"
											>
												Radio Success
											</Label>
										</div>

										<div class="form-check form-radio-warning mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor4"
												id="formradioRight8"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight8"
											>
												Radio Warning
											</Label>
										</div>

										<div class="form-check form-radio-danger mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor5"
												id="formradioRight9"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight9"
												>Radio Danger</Label
											>
										</div>

										<div class="form-check form-radio-info mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor6"
												id="formradioRight10"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight10"
												>Radio Info</Label
											>
										</div>

										<div class="form-check form-radio-dark">
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor7"
												id="formradioRight11"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight11"
												>Radio Dark</Label
											>
										</div>
									</div>
								</Col>

								<Col md={6}>
									<div class="mt-4 mt-md-0">
										<p class="text-muted">
											Use <code>form-check-outline</code>
											class and <code>form-check-</code> class
											with below-mentioned color variation
											to set a color radio with outline.
										</p>

										<div class="form-check form-radio-outline form-radio-primary mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor9"
												id="formradioRight13"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight13"
											>
												Radio Outline Primary
											</Label>
										</div>

										<div class="form-check form-radio-outline form-radio-secondary mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor10"
												id="formradioRight14"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight14"
											>
												Radio Outline Secondary
											</Label>
										</div>

										<div class="form-check form-radio-outline form-radio-success mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor11"
												id="formradioRight15"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight15"
											>
												Radio Outline Success
											</Label>
										</div>

										<div class="form-check form-radio-outline form-radio-warning mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor12"
												id="formradioRight16"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight16"
											>
												Radio Outline Warning
											</Label>
										</div>

										<div class="form-check form-radio-outline form-radio-danger mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor13"
												id="formradioRight17"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight17"
											>
												Radio Outline Danger
											</Label>
										</div>

										<div class="form-check form-radio-outline form-radio-info mb-3"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor14"
												id="formradioRight18"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight18"
											>
												Radio Outline Info
											</Label>
										</div>

										<div class="form-check form-radio-outline form-radio-dark"
										>
											<input
												class="form-check-input"
												type="radio"
												name="formradiocolor15"
												id="formradioRight19"
												checked
											/>
											<Label
												class="form-check-label"
												for="formradioRight19"
											>
												Radio Outline Dark
											</Label>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={CustomRadio} id="CustomRadio" />
						</div>
					</CardBody>
				</Card>
			</div>
		</Row>

		<Row>
			<div class="col-12">
				<Card>
					<PreviewCardHeader title="Switches" />
					<CardBody>
						<div class="live-preview">
							<Row>
								<Col lg={4} md={6}>
									<div>
										<p class="text-muted fw-medium">
											Default Switches
										</p>
										<p class="text-muted">
											Use <code>form-switch</code> class
											to form-check class to set a switch
											and add
											<code>checked</code> attribute to set
											a switch checked by default.
										</p>
										<div class="form-check form-switch mb-2"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="flexSwitchCheckDefault"
											/>
											<Label
												class="form-check-label"
												for="flexSwitchCheckDefault"
												>Default switch input</Label
											>
										</div>

										<div class="form-check form-switch">
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="flexSwitchCheckChecked"
												checked
											/>
											<Label
												class="form-check-label"
												for="flexSwitchCheckChecked"
												>Checked switch input</Label
											>
										</div>
									</div>
								</Col>

								<Col lg={4} md={6}>
									<div class="mt-4 mt-md-0">
										<p class="text-muted fw-medium">
											Disabled Switches
										</p>
										<p class="text-muted">
											Use <code>disabled</code> attribute
											to set a radio button disabled and
											add
											<code>checked</code> attribute to set
											a switch checked by default.
										</p>
										<div class="form-check form-switch mb-2"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="flexSwitchCheckDisabled"
												disabled
											/>
											<Label
												class="form-check-label"
												for="flexSwitchCheckDisabled"
												>Switch input</Label
											>
										</div>

										<div class="form-check form-switch">
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="flexSwitchCheckCheckedDisabled1"
												checked
												disabled
											/>
											<Label
												class="form-check-label"
												for="flexSwitchCheckCheckedDisabled1"
												>Disabled checked switch input</Label
											>
										</div>
									</div>
								</Col>

								<Col lg={4} md={6}>
									<div class="mt-4 mt-md-0">
										<p class="text-muted fw-medium">
											Switch Right
										</p>
										<p class="text-muted">
											Use <code>form-check-right</code> class
											to form-check class to set a switch button
											on the right side.
										</p>
										<div>
											<div class="form-check form-switch form-check-right mb-2"
											>
												<input
													class="form-check-input"
													type="checkbox"
													role="switch"
													id="flexSwitchCheckRightDisabled"
													checked
												/>
												<Label
													class="form-check-label"
													for="flexSwitchCheckRightDisabled"
													>Switch Right input</Label
												>
											</div>
										</div>

										<div>
											<div class="form-check form-switch form-check-right"
											>
												<input
													class="form-check-input"
													type="checkbox"
													role="switch"
													id="flexSwitchCheckCheckedDisabled2"
													disabled
												/>
												<Label
													class="form-check-label"
													for="flexSwitchCheckCheckedDisabled2"
													>Disabled checked switch
													input</Label
												>
											</div>
										</div>
									</div>
								</Col>

								<Col lg={4} md={6}>
									<div class="mt-3">
										<p class="text-muted fw-medium">
											Switch sizes
										</p>
										<p class="text-muted">
											Use <code>form-switch-md</code>
											class to set a medium size switch button
											and
											<code>form-switch-lg</code> class to
											form-check class to set a large size
											switch button respectively. No such class
											is required for small size switch button.
										</p>

										<div class="form-check form-switch mb-3"
											dir="ltr"
										>
											<input
												type="checkbox"
												class="form-check-input"
												id="customSwitchsizesm"
												checked
											/>
											<Label
												class="form-check-label"
												for="customSwitchsizesm"
												>Small Size Switch</Label
											>
										</div>

										<div class="form-check form-switch form-switch-md mb-3"
											dir="ltr"
										>
											<input
												type="checkbox"
												class="form-check-input"
												id="customSwitchsizemd"
											/>
											<Label
												class="form-check-label"
												for="customSwitchsizemd"
												>Medium Size Switch</Label
											>
										</div>

										<div class="form-check form-switch form-switch-lg"
											dir="ltr"
										>
											<input
												type="checkbox"
												class="form-check-input"
												id="customSwitchsizelg"
												checked
											/>
											<Label
												class="form-check-label"
												for="customSwitchsizelg"
												>Large Size Switch</Label
											>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={Switches} id="fromSwitches" />
						</div>
					</CardBody>
				</Card>
			</div>
		</Row>
		<Row>
			<div class="col-12">
				<Card>
					<PreviewCardHeader title="Switches Color" />

					<div class="card-body">
						<p class="text-muted">
							Use <code>form-check-</code> class with below-mentioned
							color variation to set a color switch.
						</p>
						<div class="live-preview">
							<Row>
								<Col md={6}>
									<div>
										<div class="form-check form-switch mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck1"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck1"
												>Switch Default</Label
											>
										</div>

										<div class="form-check form-switch form-switch-secondary mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck2"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck2"
												>Switch Secondary</Label
											>
										</div>

										<div class="form-check form-switch form-switch-success mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck3"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck3"
												>Switch Success</Label
											>
										</div>

										<div class="form-check form-switch form-switch-warning mb-2 mb-md-0"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck4"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck4"
												>Switch Warning</Label
											>
										</div>
									</div>
								</Col>

								<Col md={6}>
									<div>
										<div class="form-check form-switch form-switch-danger mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck5"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck5"
												>Switch Danger</Label
											>
										</div>

										<div class="form-check form-switch form-switch-info mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck6"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck6"
												>Switch Info</Label
											>
										</div>

										<div class="form-check form-switch form-switch-dark mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck7"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck7"
												>Switch Dark</Label
											>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={SwitchColor} id="SwitchColor"/>
						</div>
					</div>
				</Card>
			</div>
		</Row>
		<Row>
			<div class="col-12">
				<Card>
					<PreviewCardHeader title="Custom Switches" />

					<CardBody>
						<p class="text-muted">
							Use <code>form-switch-custom</code> class &amp;
							<code>form-switch-</code> class with below-mentioned
							color variation to set a color radius.
						</p>
						<div class="live-preview">
							<Row>
								<Col md={6}>
									<div>
										<div class="form-check form-switch form-switch-custom form-switch-primary mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck9"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck9"
												>Switch Primary</Label
											>
										</div>

										<div class="form-check form-switch form-switch-custom form-switch-secondary mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck10"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck10"
												>Switch Secondary</Label
											>
										</div>

										<div class="form-check form-switch form-switch-custom form-switch-success mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck11"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck11"
												>Switch Success</Label
											>
										</div>

										<div class="form-check form-switch form-switch-custom form-switch-warning mb-2 mb-md-0"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck12"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck12"
												>Switch Warning</Label
											>
										</div>
									</div>
								</Col>

								<Col md={6}>
									<div class="mt-4 mt-md-0">
										<div class="form-check form-switch form-switch-custom form-switch-danger mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck13"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck13"
												>Switch Danger</Label
											>
										</div>

										<div class="form-check form-switch form-switch-custom form-switch-info mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck14"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck14"
												>Switch Info</Label
											>
										</div>

										<div class="form-check form-switch form-switch-custom form-switch-dark mb-3"
										>
											<input
												class="form-check-input"
												type="checkbox"
												role="switch"
												id="SwitchCheck15"
												checked
											/>
											<Label
												class="form-check-label"
												for="SwitchCheck15"
												>Switch Dark</Label
											>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={CustomSwitches} id="CustomSwitches"/>
						</div>
					</CardBody>
				</Card>
			</div>
		</Row>
		<Row>
			<Col xs={12}>
				<Card>
					<PreviewCardHeader title="Inline Checkbox & Radios" />

					<CardBody>
						<p class="text-muted">
							Use <code>form-check-inline</code> class to form-check
							class to set horizontally align checkboxes, radios, or
							switches.
						</p>
						<div class="live-preview">
							<Row>
								<Col lg={4}>
									<div class="mt-4 mt-lg-0">
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="checkbox"
												id="inlineCheckbox6"
												value="option1"
											/>
											<Label
												class="form-check-label"
												for="inlineCheckbox6">1</Label
											>
										</div>
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="checkbox"
												id="inlineCheckbox7"
												value="option2"
											/>
											<Label
												class="form-check-label"
												for="inlineCheckbox7">2</Label
											>
										</div>
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="checkbox"
												id="inlineCheckbox8"
												value="option3"
												disabled
											/>
											<Label
												class="form-check-label"
												for="inlineCheckbox8"
												>3 (disabled)</Label
											>
										</div>
									</div>
								</Col>

								<Col lg={4}>
									<div class="mt-4 mt-lg-0">
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="radio"
												name="inlineRadioOptions1"
												id="inlineRadio1"
												value="option1"
											/>
											<Label
												class="form-check-label"
												for="inlineRadio1">1</Label
											>
										</div>
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="radio"
												name="inlineRadioOptions2"
												id="inlineRadio2"
												value="option2"
											/>
											<Label
												class="form-check-label"
												for="inlineRadio2">2</Label
											>
										</div>
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="radio"
												name="inlineRadioOptions3"
												id="inlineRadio3"
												value="option3"
												disabled
											/>
											<Label
												class="form-check-label"
												for="inlineRadio3"
												>3 (disabled)</Label
											>
										</div>
									</div>
								</Col>

								<Col lg={4}>
									<div class="mt-4 mt-lg-0">
										<div class="form-check form-switch form-check-inline"
											dir="ltr"
										>
											<input
												type="checkbox"
												class="form-check-input"
												id="inlineswitch5"
											/>
											<Label
												class="form-check-label"
												for="inlineswitch5">1</Label
											>
										</div>
										<div class="form-check form-switch form-check-inline"
											dir="ltr"
										>
											<input
												type="checkbox"
												class="form-check-input"
												id="inlineswitch6"
											/>
											<Label
												class="form-check-label"
												for="inlineswitch6">2</Label
											>
										</div>
										<div class="form-check form-switch form-check-inline"
											dir="ltr"
										>
											<input
												type="checkbox"
												class="form-check-input"
												id="inlineswitchdisabled2"
												disabled
											/>
											<Label
												class="form-check-label"
												for="inlineswitchdisabled2"
												>2</Label
											>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={InlineCheckboxRadio} id="InlineCheckboxRadio"/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xs={12}>
				<Card>
					<PreviewCardHeader title="Without Labels" />
					<CardBody>
						<p class="text-muted">
							Omit the wrapping, <code>form-check</code> class for
							checkboxes, radios, or switches that have no label text.
							Remember to still provide some form of accessible name
							for assistive technologies (for instance, using aria-label).
						</p>
						<div class="live-preview">
							<Row>
								<Col lg={4}>
									<div class="mt-4 mt-lg-0">
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="checkbox"
												id="inlineCheckbox1"
												value="option1"
											/>
										</div>
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="checkbox"
												id="inlineCheckbox2"
												value="option2"
											/>
										</div>
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="checkbox"
												id="inlineCheckbox3"
												value="option3"
												disabled
											/>
										</div>
									</div>
								</Col>

								<Col lg={4}>
									<div class="mt-4 mt-lg-0">
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="radio"
												name="inlineRadioOptions"
												id="WithoutinlineRadio1"
												value="option1"
											/>
										</div>
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="radio"
												name="inlineRadioOptions"
												id="WithoutinlineRadio2"
												value="option2"
											/>
										</div>
										<div class="form-check form-check-inline"
										>
											<input
												class="form-check-input"
												type="radio"
												name="inlineRadioOptions"
												id="WithoutinlineRadio3"
												value="option3"
												disabled
											/>
										</div>
									</div>
								</Col>

								<Col lg={4}>
									<div class="mt-4 mt-lg-0">
										<div class="form-check form-switch form-check-inline"
											dir="ltr"
										>
											<input
												type="checkbox"
												class="form-check-input"
												id="inlineswitch"
											/>
										</div>
										<div class="form-check form-switch form-check-inline"
											dir="ltr"
										>
											<input
												type="checkbox"
												class="form-check-input"
												id="inlineswitch1"
											/>
										</div>
										<div class="form-check form-switch form-check-inline"
											dir="ltr"
										>
											<input
												type="checkbox"
												class="form-check-input"
												id="inlineswitchdisabled"
												disabled
											/>
										</div>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode code={WithoutLabels} id="WithoutLabels"/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col lg={6}>
				<Card>
					<PreviewCardHeader title="Radio Toggle Buttons" />
					<CardBody>
						<p class="text-muted">
							Create button-like checkboxes and radio buttons by
							using <code>btn</code> styles rather than
							form-check-label class on the &lt;label&gt;
							elements. These toggle buttons can further be
							grouped in a
							<a
								href="/getbootstrap.com/docs/5.1/components/button-group/"
								>button group</a> if needed.
						</p>
						<div class="live-preview">
							<div class="hstack gap-2 flex-wrap">
								<input
									type="radio"
									class="btn-check"
									name="options"
									id="option1"
									checked
								/>
								<Label class="btn btn-secondary" for="option1"
									>Checked</Label
								>

								<input
									type="radio"
									class="btn-check"
									name="options"
									id="option2"
								/>
								<Label class="btn btn-secondary" for="option2"
									>Radio</Label
								>

								<input
									type="radio"
									class="btn-check"
									name="options"
									id="option3"
									disabled
								/>
								<Label class="btn btn-secondary" for="option3"
									>Disabled</Label
								>

								<input
									type="radio"
									class="btn-check"
									name="options"
									id="option4"
								/>
								<Label class="btn btn-secondary" for="option4"
									>Radio</Label
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode code={RadioToggleButtons} id="RadioToggleButtons"/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<PreviewCardHeader title="Outlined Styles" />
					<CardBody>
						<p class="text-muted">
							Different variants of <code>btn</code> attribute, such
							as the various outlined styles, are supported.
						</p>
						<div class="live-preview">
							<div class="hstack gap-2 flex-wrap">
								<input
									type="checkbox"
									class="btn-check"
									id="btn-check-outlined"
								/>
								<Label
									class="btn btn-outline-primary"
									for="btn-check-outlined"
									>Single toggle</Label
								>

								<input
									type="checkbox"
									class="btn-check"
									id="btn-check-2-outlined"
									checked
								/>
								<Label
									class="btn btn-outline-secondary"
									for="btn-check-2-outlined">Checked</Label
								>

								<input
									type="radio"
									class="btn-check"
									name="options-outlined"
									id="success-outlined"
									checked
								/>
								<Label
									class="btn btn-outline-success"
									for="success-outlined"
									>Checked success radio</Label
								>

								<input
									type="radio"
									class="btn-check"
									name="options-outlined"
									id="danger-outlined"
								/>
								<Label
									class="btn btn-outline-danger"
									for="danger-outlined">Danger radio</Label
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode code={OutlinedStyles} id="OutlinedStyles"/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
