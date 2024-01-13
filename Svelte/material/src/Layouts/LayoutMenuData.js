const Navdata = [
	{
		label: 'Menu',
		isHeader: true
	},
	{
		id: 'dashboard',
		label: 'Dashboards',
		icon: 'mdi mdi-speedometer',
		link: '/#',
		stateVariables: "isDashboard",
		subItems: [
			{
				id: 'analytics',
				label: 'Analytics',
				link: '/dashboard-analytics',
				parentId: 'dashboard'
			},
			{
				id: 'crm',
				label: 'CRM',
				link: '/dashboard-crm',
				parentId: 'dashboard'
			},
			{
				id: 'ecommerce',
				label: 'Ecommerce',
				link: '/dashboard',
				parentId: 'dashboard'
			},
			{
				id: 'crypto',
				label: 'Crypto',
				link: '/dashboard-crypto',
				parentId: 'dashboard'
			},
			{
				id: 'projects',
				label: 'Projects',
				link: '/dashboard-projects',
				parentId: 'dashboard'
			},
			{
				id: 'nft',
				label: 'NFT',
				link: '/dashboard-nft',
				parentId: 'dashboard',
				
			},
			{
				id: "job",
				label: "Job",
				link: "/dashboard-job",
				parentId: "dashboard",
				badgeColor: "success",
				badgeName: "New",
			},
		]
	},
	{
		id: 'apps',
		label: 'Apps',
		icon: 'mdi mdi-view-grid-plus-outline',
		link: '/#',
		stateVariables: "isApps",
		subItems: [
			{
				id: "calendar",
				label: "Calendar",
				link: "#",
				parentId: "apps",
				isChildItem: true,
				stateVariables: "isCalendar",
				childItems: [
					{
						id: "main-calendar",
						label: "Main Calendar",
						link: "/calendar",
						parentId: "apps"
					},
					{
						id: "month-calendar",
						label: "Month Grid",
						link: "/calendar/month-grid",
						parentId: "apps"
					}
				]
			},
			{
				id: 'chat',
				label: 'Chat',
				link: '/apps-chat',
				parentId: 'chat'
			},
			{
				id: "mailbox",
				label: "Email",
				link: "/#",
				parentId: "apps",
				isChildItem: true,
				stateVariables: "isEmail",
				childItems: [
					{
						id: "app-mailbox",
						label: "Mailbox",
						link: "/emailInbox/apps-mailbox",
						parentId: "apps"
					},
					{
						id: 'email-templates',
						label: "Email Templates",
						link: "/#",
						parentId: "apps",
						isChildItem: true,
						stateVariables: "isSubEmail",
						childItems: [
							{ id: "apps-email-basic", label: "Basic Action", link: "/email/emailtemplates/basicaction", parentId: "apps" },
							{ id: "apps-email-ecommerce", label: "Ecommerce Action", link: "/email/emailtemplates/ecommerceaction", parentId: "apps" },
						],
					},
				]
			},
			{
				id: 'appsecommerce',
				label: 'Ecommerce',
				link: '/#',
				isChildItem: true,
				stateVariables: "isEcommerce",
				childItems: [
					{ id: 'appsecommerceproducts', label: 'Product', link: '/ecommerce/apps-ecommerce-products' },
					{ id: 'appsproductdetails', label: 'Product Details', link: '/ecommerce/apps-ecommerce-product-details' },
					{ id: 'appsproductaddproduct', label: 'Create Product', link: '/ecommerce/apps-ecommerce-add-product' },
					{ id: 'appsproductorders', label: 'Orders', link: '/ecommerce/apps-ecommerce-orders' },
					{ id: 'apporderdetails', label: 'Order Details', link: '/ecommerce/apps-ecommerce-order-details' },
					{ id: 'ecommercecustomers', label: 'Customers', link: '/ecommerce/apps-ecommerce-customers' },
					{ id: 'ecommercecart', label: 'Shopping Cart', link: '/ecommerce/apps-ecommerce-cart' },
					{ id: 'ecommercecheckout', label: 'Checkout', link: '/ecommerce/apps-ecommerce-checkout' },
					{ id: 'ecommercesellers', label: 'Sellers', link: '/ecommerce/apps-ecommerce-sellers' },
					{ id: 'ecommercesellerdetails', label: 'Seller Details', link: '/ecommerce/apps-ecommerce-seller-details' }
				]
			},
			{
				id: 'appsprojects',
				label: 'Projects',
				link: '/#',
				isChildItem: true,
				stateVariables: "isProjects",
				childItems: [
					{ id: 'projectslist', label: 'List', link: '/projects/apps-projects-list' },
					{ id: 'projectsoverview', label: 'Overview', link: '/projects/apps-projects-overview' },
					{ id: 'projectscreate', label: 'Create Project', link: '/projects/apps-projects-create' }
				]
			},
			{
				id: 'tasks',
				label: 'Tasks',
				link: '/#',
				isChildItem: true,
				stateVariables: "isTasks",
				childItems: [
					{ id: 'tasks-kanban', label: 'Kanban Board', link: '/tasks/apps-tasks-kanban' },
					{ id: 'tasks-list-view', label: 'List View', link: '/tasks/apps-tasks-list-view' },
					{ id: 'tasks-details', label: 'Task Details', link: '/tasks/apps-tasks-details' }
				]
			},
			{
				id: 'appscrm',
				label: 'CRM',
				link: '/#',
				isChildItem: true,
				stateVariables: "isCRM",
				childItems: [
					{ id: 'crm-contacts', label: 'Contacts', link: '/crm/apps-crm-contacts' },
					{ id: 'crm-companies', label: 'Companies', link: '/crm/apps-crm-companies' },
					{ id: 'crm-deals', label: 'Deals', link: '/crm/apps-crm-deals' },
					{ id: 'crm-leads', label: 'Leads', link: '/crm/apps-crm-leads' }
				]
			},
			{
				id: 'appscrypto',
				label: 'Crypto',
				link: '/#',
				isChildItem: true,
				stateVariables: "isCrypto",
				childItems: [
					{ id: 'crypto-transactions', label: 'Transactions', link: '/crypto/transaction' },
					{ id: 'crypto-buy-sell', label: 'Buy & Sell', link: '/crypto/buysell' },
					{ id: 'crypto-orders', label: 'Orders', link: '/crypto/cryptoorder' },
					{ id: 'crypto-wallet', label: 'My Wallet', link: '/crypto/mywallet' },
					{ id: 'crypto-ico', label: 'ICO List', link: '/crypto/iconlist' },
					{ id: 'crypto-kyc', label: 'KYC Application', link: '/crypto/kycverification' }
				]
			},
			{
				id: 'invoices',
				label: 'Invoices',
				link: '/#',
				isChildItem: true,
				stateVariables: "isInvoices",
				childItems: [
					{ id: 'invoices-list', label: 'List View', link: '/invoices/apps-invoices-list' },
					{ id: 'invoices-details', label: 'Details', link: '/invoices/apps-invoices-details' },
					{ id: 'invoices-create', label: 'Create Invoice', link: '/invoices/apps-invoices-create' }
				]
			},
			{
				id: 'supportTickets',
				label: 'Support Tickets',
				link: '/#',
				isChildItem: true,
				stateVariables: "isSupportTickets",
				childItems: [
					{ id: 'tickets-list', label: 'List View', link: '/support/listview' },
					{ id: 'tickets-details', label: 'Ticket Details', link: '/support/ticketsdetails' }
				]
			},
			{
				id: "NFTMarketplace",
				label: "NFT Marketplace",
				link: "/#",
				isChildItem: true,
				parentId: "apps",
				
				stateVariables: "isNFTMarketplace",
				childItems: [
					{ id: "appnft-marketplace", label: "Marketplace", link: "/NFTmarketplace/apps-nft-marketplace" },
					{ id: "appnft-explore", label: "Explore Now", link: "/NFTmarketplace/apps-nft-explore" },
					{ id: "appnft-auction", label: "Live Auction", link: "/NFTmarketplace/apps-nft-auction" },
					{ id: "appnft-details", label: "Item Details", link: "/NFTmarketplace/apps-nft-item-details" },
					{ id: "appnft-collections", label: "Collections", link: "/NFTmarketplace/apps-nft-collections" },
					{ id: "appnft-creators", label: "Creators", link: "/NFTmarketplace/apps-nft-creators" },
					{ id: "appnft-ranking", label: "Ranking", link: "/NFTmarketplace/apps-nft-ranking" },
					{ id: "appnft-wallet", label: "Wallet Connect", link: "/NFTmarketplace/apps-nft-wallet" },
					{ id: "appnft-create", label: "Create NFT", link: "/NFTmarketplace/apps-nft-create" }
				]
			},
			{
				id: "filemanager",
				label: "File Manager",
				link: "/filemanager",
				parentId: "apps",
				
			},
			{
				id: "todo",
				label: "To Do",
				link: "/todo",
				parentId: "apps",				
			},
			{
				id: "job",
				label: "Jobs",
				link: "/#",
				parentId: "apps",
				badgeName: "New",
				badgeColor: "success",
				isChildItem: true,
				stateVariables: 'isJobs',
				childItems: [
				  {
					id: "job-statistics",
					label: "Statistics",
					link: "/Jobs/Statistics",
					parentId: "apps",
				  },
				  {
					id: 2,
					label: "Job Lists",
					link: "/#",
					parentId: "apps",
					isChildItem: true,
					stateVariables: 'isJobList',
					childItems: [
					  {
						id: 1,
						label: "List",
						link: "/Jobs/JobList/List",
						parentId: "apps",
					  },
					  {
						id: 2,
						label: "Grid",
						link: "/Jobs/JobList/Grid",
						parentId: "apps",
					  },
					  {
						id: 3,
						label: "Overview",
						link: "/Jobs/JobList/Overview",
						parentId: "apps",
					  },
					],
				  },
				  {
					id: 3,
					label: "Candidate Lists",
					link: "/#",
					parentId: "apps",
					isChildItem: true,
					stateVariables: 'isCandidateList',
					childItems: [
					  {
						id: 1,
						label: "List View",
						link: "/Jobs/CandidateList/ListView",
						parentId: "apps",
					  },
					  {
						id: 2,
						label: "Grid View",
						link: "/Jobs/CandidateList/GridView",
						parentId: "apps",
					  },
					],
				  },
				  {
					id: 4,
					label: "Application",
					link: "/Jobs/application",
					parentId: "apps",
				  },
				  {
					id: 5,
					label: "New Job",
					link: "/Jobs/newjob",
					parentId: "apps",
				  },
				  {
					id: 6,
					label: "Companies List",
					link: "/Jobs/companieslist",
					parentId: "apps",
				  },
				  {
					id: 7,
					label: "Job Categories",
					link: "/Jobs/jobcategories",
					parentId: "apps",
				  },
				],
			},
			{
				id: "apikey",
				label: "API Key",
				link: "/APIKey",
				parentId: "apps",
				badgeName: "New",
				badgeColor: "success"
			},
		]
	},
	{
		label: 'pages',
		isHeader: true
	},
	{
		id: 'authentication',
		label: 'Authentication',
		icon: 'ri-account-circle-line',
		link: '/#',
		stateVariables: "isAuth",
		subItems: [
			{
				id: 'signIn',
				label: 'Sign In',
				link: '/#',
				isChildItem: true,
				stateVariables: "isSignIn",
				childItems: [
					{ id: 'signin-basic', label: 'Basic', link: '/authenticationInner/login/auth-signin-basic' },
					{ id: 'signin-cover', label: 'Cover', link: '/authenticationInner/login/auth-signin-cover' }
				]
			},
			{
				id: 'signUp',
				label: 'Sign Up',
				link: '/#',
				isChildItem: true,
				stateVariables: "isSignUp",
				childItems: [
					{ id: 'signup-basic', label: 'Basic', link: '/authenticationInner/register/auth-signup-basic' },
					{ id: 'signup-cover', label: 'Cover', link: '/authenticationInner/register/auth-signup-cover' }
				]
			},
			{
				id: 'passwordReset',
				label: 'Password Reset',
				link: '/#',
				isChildItem: true,
				stateVariables: "isPasswordReset",
				childItems: [
					{ id: 'pass-reset-basic', label: 'Basic', link: '/authenticationInner/passwordreset/auth-pass-reset-basic' },
					{ id: 'pass-reset-cover', label: 'Cover', link: '/authenticationInner/passwordreset/auth-pass-reset-cover' }
				]
			},
			{
				id: "passwordCreate",
				label: "Password Create",
				link: "/#",
				isChildItem: true,
				parentId: "authentication",
				stateVariables: 'isPasswordCreate',
				childItems: [
					{ id: 1, label: "Basic", link: "/authenticationInner/passwordcreate/auth-pass-change-basic" },
					{ id: 2, label: "Cover", link: "/authenticationInner/passwordcreate/auth-pass-change-cover" },
				]
			},
			{
				id: 'lockScreen',
				label: 'Lock Screen',
				link: '/#',
				isChildItem: true,
				stateVariables: "isLockScreen",
				childItems: [
					{ id: 'lockscreen-basic', label: 'Basic', link: '/authenticationInner/lockscreen/auth-lockscreen-basic' },
					{ id: 'lockscreen-cover', label: 'Cover', link: '/authenticationInner/lockscreen/auth-lockscreen-cover' }
				]
			},
			{
				id: 'logout',
				label: 'Logout',
				link: '/#',
				isChildItem: true,
				stateVariables: "isLogout",
				childItems: [
					{ id: 'logout-basic', label: 'Basic', link: '/authenticationInner/logout/auth-logout-basic' },
					{ id: 'logout-cover', label: 'Cover', link: '/authenticationInner/logout/auth-logout-cover' }
				]
			},
			{
				id: 'successMessage',
				label: 'Success Message',
				link: '/#',
				isChildItem: true,
				stateVariables: "isSuccessMessage",
				childItems: [
					{ id: 'success-msg-basic', label: 'Basic', link: '/authenticationInner/successmessage/auth-success-msg-basic' },
					{ id: 'success-msg-cover', label: 'Cover', link: '/authenticationInner/successmessage/auth-success-msg-cover' }
				]
			},
			{
				id: 'twoStepVerification',
				label: 'Two Step Verification',
				link: '/#',
				isChildItem: true,
				stateVariables: "isVerification",
				childItems: [
					{ id: 'twostep-basic', label: 'Basic', link: '/authenticationInner/twostepverification/auth-twostep-basic' },
					{ id: 'twostep-cover', label: 'Cover', link: '/authenticationInner/twostepverification/auth-twostep-cover' }
				]
			},
			{
				id: 'errors',
				label: 'Errors',
				link: '/#',
				isChildItem: true,
				stateVariables: "isError",
				childItems: [
					{ id: '404-basic', label: '404 Basic', link: '/authenticationInner/errors/auth-404-basic' },
					{ id: '404-cover', label: '404 Cover', link: '/authenticationInner/errors/auth-404-cover' },
					{ id: '404-alt', label: '404 Alt', link: '/authenticationInner/errors/auth-404-alt' },
					{ id: 'auth-500', label: '500', link: '/authenticationInner/errors/auth-500' },
					{ id: 'auth-offline', label: 'Offline Page', link: '/authenticationInner/errors/auth-offline' }
				]
			}
		]
	},
	{
		id: 'pages',
		label: 'Pages',
		icon: 'mdi mdi-sticker-text-outline',
		link: '/#',
		stateVariables: "isPages",
		subItems: [
			{
				id: 'starter',
				label: 'Starter',
				link: '/pages/starter',
				parentId: 'pages'
			},
			{
				id: 'profile',
				label: 'Profile',
				link: '/#',
				isChildItem: true,
				stateVariables: "isProfile",
				childItems: [
					{ id: 'simplepage', label: 'Simple Page', link: '/pages/profile/simple' },
					{ id: 'profile-settings', label: 'Settings', link: '/pages/profile/settings' }
				]
			},
			{ id: 'team', label: 'Team', link: '/pages/team', parentId: 'pages' },
			{ id: 'timeline', label: 'Timeline', link: '/pages/timeline', parentId: 'pages' },
			{ id: 'faqs', label: 'FAQs', link: '/pages/faqs', parentId: 'pages' },
			{ id: 'pricing', label: 'Pricing', link: '/pages/pricing', parentId: 'pages' },
			{ id: 'gallery', label: 'Gallery', link: '/pages/gallery', parentId: 'pages' },
			{ id: 'maintenance', label: 'Maintenance', link: '/pages/pages-maintenance', parentId: 'pages' },
			{ id: 'comingSoon', label: 'Coming Soon', link: '/pages/pages-coming-soon', parentId: 'pages' },
			{ id: 'sitemap', label: 'Sitemap', link: '/pages/sitemap', parentId: 'pages' },
			{
				id: 'searchResults',
				label: 'Search Results',
				link: '/pages/searchresults',
				parentId: 'pages'
			},
			{ id: "PrivecyPolicy", label: "Privacy Policy", link: "/pages/privacypolicy", parentId: "pages",  badgeColor: "success",badgeName: "New", },
            { id: "TermsCondition", label: "Terms Condition", link: "/pages/termscondition", parentId: "pages", badgeColor: "success",badgeName: "New", },
		]
	},
	{
		id: "landing",
		label: "Landing",
		icon: "ri-rocket-line",
		link: "/#",
		stateVariables: 'isLanding',
		subItems: [
			{ id: "onePage", label: "One Page", link: "/landing/OnePage", parentId: "landing" },
			{ id: "nftLanding", label: "NFT Landing", link: "/landing/NFTLanding", parentId: "landing" },
			{ id: "jobLanding", label: "Job", link: "/landing/Job", parentId: "landing", badgeColor: "success",badgeName: "New" }
		],
	},
	{
		label: 'Components',
		isHeader: true
	},
	{
		id: 'baseUi',
		label: 'Base UI',
		icon: 'mdi mdi-cube-outline',
		link: '/#',
		stateVariables: "isBaseUi",
		subItems: [
			{ id: 'alerts', label: 'Alerts', link: '/baseui/uialerts', parentId: 'baseUi' },
			{ id: 'badges', label: 'Badges', link: '/baseui/uibadges', parentId: 'baseUi' },
			{ id: 'buttons', label: 'Buttons', link: '/baseui/uibuttons', parentId: 'baseUi' },
			{ id: 'colors', label: 'Colors', link: '/baseui/uicolors', parentId: 'baseUi' },
			{ id: 'cards', label: 'Cards', link: '/baseui/uicards', parentId: 'baseUi' },
			{ id: 'carousel', label: 'Carousel', link: '/baseui/uicarousel', parentId: 'baseUi' },
			{ id: 'dropdowns', label: 'Dropdowns', link: '/baseui/uidropdowns', parentId: 'baseUi' },
			{ id: 'grid', label: 'Grid', link: '/baseui/uigrid', parentId: 'baseUi' },
			{ id: 'images', label: 'Images', link: '/baseui/uiimages', parentId: 'baseUi' },
			{ id: 'tabs', label: 'Tabs', link: '/baseui/uitabs', parentId: 'baseUi' },
			{ id: 'accordions', label: 'Accordion & Collapse', link: '/baseui/uiaccordions', parentId: 'baseUi' },
			{ id: 'modals', label: 'Modals', link: '/baseui/uimodals', parentId: 'baseUi' },
			{ id: 'offcanvas', label: 'Offcanvas', link: '/baseui/uioffcanvas', parentId: 'baseUi' },
			{ id: 'placeholders', label: 'Placeholders', link: '/baseui/uiplaceholders', parentId: 'baseUi' },
			{ id: 'progress', label: 'Progress', link: '/baseui/uiprogress', parentId: 'baseUi' },
			{
				id: 'notifications',
				label: 'Notifications',
				link: '/baseui/uinotifications',
				parentId: 'baseUi'
			},
			{ id: 'media', label: 'Media', link: '/baseui/uimedia', parentId: 'baseUi' },
			{ id: 'embedvideo', label: 'Embed Video', link: '/baseui/uiembedvideo', parentId: 'baseUi' },
			{ id: 'typography', label: 'Typography', link: '/baseui/uitypography', parentId: 'baseUi' },
			{ id: 'lists', label: 'Lists', link: '/baseui/uilists', parentId: 'baseUi' },
			{ id: 'general', label: 'General', link: '/baseui/uigeneral', parentId: 'baseUi' },
			{ id: 'ribbons', label: 'Ribbons', link: '/baseui/uiribbons', parentId: 'baseUi' },
			{ id: 'utilities', label: 'Utilities', link: '/baseui/uiutilities', parentId: 'baseUi' }
		]
	},
	{
		id: 'advanceUi',
		label: 'Advance UI',
		icon: 'mdi mdi-layers-triple-outline',
		link: '/#',
		stateVariables: "isAdvanceUi",
		subItems: [
			{ id: 'scrollbar', label: 'Scrollbar', link: '/advanceUi/advance-ui-scrollbar', parentId: 'advanceUi' },
			{ id: 'animation', label: 'Animation', link: '/advanceUi/advance-ui-animation', parentId: 'advanceUi' },
			{
				id: 'swiperslider',
				label: 'Swiper Slider',
				link: '/advanceUi/advance-ui-swiper',
				parentId: 'advanceUi'
			},
			{ id: 'highlight', label: 'Highlight', link: '/advanceUi/advance-ui-highlight', parentId: 'advanceUi' }
		]
	},
	{
		id: 'widgets',
		label: 'Widgets',
		icon: 'mdi mdi-puzzle-outline',
		link: '/Widgets',
	},
	{
		id: 'forms',
		label: 'Forms',
		icon: 'mdi mdi-form-select',
		link: '/#',
		stateVariables: "isForms",
		subItems: [
			{ id: 'basicelements', label: 'Basic Elements', link: '/Forms/forms-elements', parentId: 'forms' },
			{ id: 'formselect', label: 'Form Select', link: '/Forms/forms-select', parentId: 'forms' },
			{
				id: 'checkboxsradios',
				label: 'Checkboxs & Radios',
				link: '/Forms/forms-checkboxes-radios',
				parentId: 'forms'
			},
			{ id: 'pickers', label: 'Pickers', link: '/Forms/forms-pickers', parentId: 'forms' },
			{ id: 'inputmasks', label: 'Input Masks', link: '/Forms/forms-masks', parentId: 'forms' },
			{ id: 'advanced', label: 'Advanced', link: '/Forms/forms-advanced', parentId: 'forms' },
			{ id: 'rangeslider', label: 'Range Slider', link: '/Forms/forms-range-sliders', parentId: 'forms' },
			{ id: 'validation', label: 'Validation', link: '/Forms/forms-validation', parentId: 'forms' },
			{ id: 'wizard', label: 'Wizard', link: '/Forms/forms-wizard', parentId: 'forms' },
			{ id: "editors", label: "Editors", link: "/Forms/form-editor", parentId: "forms" },
			{ id: 'fileuploads', label: 'File Uploads', link: '/Forms/forms-file-uploads', parentId: 'forms' },
			{ id: 'formlayouts', label: 'Form Layouts', link: '/Forms/forms-layouts', parentId: 'forms' }
		]
	},
	{
		id: 'tables',
		label: 'Tables',
		icon: 'mdi mdi-grid-large',
		link: '/#',
		stateVariables: "isTables",
		subItems: [
			{ id: 'basictables', label: 'Basic Tables', link: '/tables/basictables', parentId: 'tables' },
			{ id: 'gridjs', label: 'Grid Js', link: '/tables/gridjs', parentId: 'tables' },
			{ id: 'datatable', label: 'Datatables', link: '/tables/datatable', parentId: 'tables' },
		]
	},
	{
		id: 'charts',
		label: 'Charts',
		icon: 'mdi mdi-chart-donut',
		link: '/#',
		stateVariables: "isCharts",
		subItems: [
			{
				id: 'apexcharts',
				label: 'Apexcharts',
				link: '/#',
				isChildItem: true,
				stateVariables: "isApex",
				childItems: [
					{ id: 'lineCharts', label: 'Line', link: '/charts/apexCharts/lineCharts' },
					{ id: 'areaCharts', label: 'Area', link: '/charts/apexCharts/areaCharts' },
					{ id: 'columnCharts', label: 'Column', link: '/charts/apexCharts/columnCharts' },
					{ id: 'barCharts', label: 'Bar', link: '/charts/apexCharts/barCharts' },
					{ id: 'mixedCharts', label: 'Mixed', link: '/charts/apexCharts/mixedCharts' },
					{ id: 'timelineCharts', label: 'Timeline', link: '/charts/apexCharts/timelineCharts' },
					{ id: 'rangeareaCharts', label: 'Range Area', link: '/charts/apexCharts/rangeareaCharts' },
					{ id: 'funnelCharts', label: 'Funnel', link: '/charts/apexCharts/funnelCharts' },
					{ id: 'candlestickChart', label: 'Candlstick', link: '/charts/apexCharts/candlestickChart' },
					{ id: 'boxplotCharts', label: 'Boxplot', link: '/charts/apexCharts/boxplotCharts' },
					{ id: 'bubbleChart', label: 'Bubble', link: '/charts/apexCharts/bubbleChart' },
					{ id: 'scatterCharts', label: 'Scatter', link: '/charts/apexCharts/scatterCharts' },
					{ id: 'heatmapCharts', label: 'Heatmap', link: '/charts/apexCharts/heatmapCharts' },
					{ id: 'treemapCharts', label: 'Treemap', link: '/charts/apexCharts/treemapCharts' },
					{ id: 'pieCharts', label: 'Pie', link: '/charts/apexCharts/pieCharts' },
					{ id: 'radialbarCharts', label: 'Radialbar', link: '/charts/apexCharts/radialbarCharts' },
					{ id: 'radarCharts', label: 'Radar', link: '/charts/apexCharts/radarCharts' },
					{ id: 'polarCharts', label: 'Polar', link: '/charts/apexCharts/polarCharts' }
				]
			},
			{ id: 'chartjs', label: 'Chartjs', link: '/charts/chartsJs', parentId: 'charts' },
		]
	},
	{
		id: 'icons',
		label: 'Icons',
		icon: 'mdi mdi-android-studio',
		link: '/#',
		stateVariables: "isIcons",
		subItems: [
			{ id: 'remix', label: 'Remix', link: '/icons/RemixIcons', parentId: 'icons' },
			{ id: 'boxicons', label: 'Boxicons', link: '/icons/BoxIcons', parentId: 'icons' },
			{
				id: 'materialdesign',
				label: 'Material Design',
				link: '/icons/MaterialDesign',
				parentId: 'icons'
			},
			{ id: 'lineawesome', label: 'Line Awesome', link: '/icons/LineAwesomeIcons', parentId: 'icons' },
			{ id: 'feather', label: 'Feather', link: '/icons/FeatherIcons', parentId: 'icons' },
			{ id: "crypto", label: "Crypto SVG", link: "/icons/Cryptoicons", parentId: "icons" }
		]
	},
	{
		id: 'maps',
		label: 'Maps',
		icon: 'mdi mdi-map-marker-outline',
		link: '/#',
		stateVariables: "isMaps",
		subItems: [
			// { id: 'google', label: 'Google', link: '/maps', parentId: 'maps' }
			{ id: 'vector', label: 'Vector', link: '/maps/vectormap', parentId: 'maps' },
		]
	},
	{
		id: 'multilevel',
		label: 'Multi Level',
		icon: 'mdi mdi-share-variant-outline',
		link: '/#',
		stateVariables: "isMultiLevel",
		subItems: [
			{ id: 'level1.1', label: 'Level 1.1', link: '/#', parentId: 'multilevel' },
			{
				id: 'level1.2',
				label: 'Level 1.2',
				link: '/#',
				isChildItem: true,
				stateVariables: "isLevel1",
				childItems: [
					{ id: 1, label: 'Level 2.1', link: '/#' },
					{
						id: 'level2.2',
						label: 'Level 2.2',
						link: '/#',
						isChildItem: true,
						stateVariables: "isLevel2",
						childItems: [
							{ id: 1, label: 'Level 3.1', link: '/#' },
							{ id: 2, label: 'Level 3.2', link: '/#' }
						]
					}
				]
			}
		]
	}
];

const MOCK_DATA = {
	Navdata
}

export default MOCK_DATA;