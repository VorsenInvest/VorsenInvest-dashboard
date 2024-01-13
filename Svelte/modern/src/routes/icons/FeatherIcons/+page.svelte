<svelte:head>
  <title>Feather Icons | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
    import { Card, CardBody, CardHeader, Col, Container, Row } from 'sveltestrap';
    import { ActivityIcon, AirplayIcon, AlertCircleIcon, AlertOctagonIcon, AlertTriangleIcon, AlignCenterIcon, AlignJustifyIcon, AlignLeftIcon, AlignRightIcon, AnchorIcon, ApertureIcon, ArchiveIcon, ArrowDownCircleIcon, ArrowDownLeftIcon, ArrowDownRightIcon, ArrowDownIcon, ArrowLeftCircleIcon, ArrowLeftIcon, ArrowRightCircleIcon, ArrowRightIcon, ArrowUpCircleIcon, ArrowUpLeftIcon, ArrowUpRightIcon, ArrowUpIcon, AtSignIcon, AwardIcon, BarChart2Icon, BarChartIcon, BatteryChargingIcon, BatteryIcon, BellOffIcon, BellIcon, BluetoothIcon, BoldIcon, BookOpenIcon, BookIcon, BookmarkIcon, BoxIcon, BriefcaseIcon, CalendarIcon, CameraOffIcon, CameraIcon, CastIcon, CheckCircleIcon, CheckSquareIcon, CheckIcon, ChevronDownIcon, ChevronLeftIcon, ChevronRightIcon, ChevronUpIcon, ChevronsDownIcon, ChevronsLeftIcon, ChevronsRightIcon, ChevronsUpIcon, ChromeIcon, CircleIcon, ClipboardIcon, ClockIcon, CloudDrizzleIcon, CloudLightningIcon, CloudOffIcon, CloudRainIcon, CloudSnowIcon, CloudIcon, CodeIcon, CodepenIcon, CodesandboxIcon, CoffeeIcon, ColumnsIcon, CommandIcon, CompassIcon, CopyIcon, CornerDownLeftIcon, CornerDownRightIcon, CornerLeftDownIcon, CornerLeftUpIcon, CornerRightDownIcon, CornerRightUpIcon, CornerUpLeftIcon, CornerUpRightIcon, CpuIcon, CreditCardIcon, CropIcon, CrosshairIcon, DatabaseIcon, DeleteIcon, DiscIcon, DivideCircleIcon, DivideSquareIcon, DivideIcon, DollarSignIcon, DownloadCloudIcon, DownloadIcon, DribbbleIcon, DropletIcon, Edit2Icon, Edit3Icon, EditIcon, ExternalLinkIcon, EyeOffIcon, EyeIcon, FacebookIcon, FastForwardIcon, FeatherIcon, FigmaIcon, FileMinusIcon, FilePlusIcon, FileTextIcon, FileIcon, FilmIcon, FilterIcon, FlagIcon, FolderMinusIcon, FolderPlusIcon, FolderIcon, FramerIcon, FrownIcon, GiftIcon, GitBranchIcon, GitCommitIcon, GitMergeIcon, GitPullRequestIcon, GithubIcon, GitlabIcon, GlobeIcon, GridIcon, HardDriveIcon, HashIcon, HeadphonesIcon, HeartIcon, HelpCircleIcon, HexagonIcon, HomeIcon, ImageIcon, InboxIcon, InfoIcon, InstagramIcon, ItalicIcon, KeyIcon, LayersIcon, LayoutIcon, LifeBuoyIcon, Link2Icon, LinkIcon, LinkedinIcon, ListIcon, LoaderIcon, LockIcon, LogInIcon, LogOutIcon, MailIcon, MapPinIcon, MapIcon, Maximize2Icon, MaximizeIcon, MehIcon, MenuIcon, MessageCircleIcon, MessageSquareIcon, MicOffIcon, MicIcon, Minimize2Icon, MinimizeIcon, MinusCircleIcon, MinusSquareIcon, MinusIcon, MonitorIcon, MoonIcon, MoreHorizontalIcon, MoreVerticalIcon, MousePointerIcon, MoveIcon, MusicIcon, Navigation2Icon, NavigationIcon, OctagonIcon, PackageIcon, PaperclipIcon, PauseCircleIcon, PauseIcon, PenToolIcon, PercentIcon, PhoneCallIcon, PhoneForwardedIcon, PhoneIncomingIcon, PhoneMissedIcon, PhoneOffIcon, PhoneOutgoingIcon, PhoneIcon, PieChartIcon, PlayCircleIcon, PlayIcon, PlusCircleIcon, PlusSquareIcon, PlusIcon, PocketIcon, PowerIcon, PrinterIcon, RadioIcon, RefreshCcwIcon, RefreshCwIcon, RepeatIcon, RewindIcon, RotateCcwIcon, RotateCwIcon, RssIcon, SaveIcon, ScissorsIcon, SearchIcon, SendIcon, ServerIcon, SettingsIcon, Share2Icon, ShareIcon, ShieldOffIcon, ShieldIcon, ShoppingBagIcon, ShoppingCartIcon, ShuffleIcon, SidebarIcon, SkipBackIcon, SkipForwardIcon, SlackIcon, SlashIcon, SlidersIcon, SmartphoneIcon, SmileIcon, SpeakerIcon, SquareIcon, StarIcon, StopCircleIcon, SunIcon, SunriseIcon, SunsetIcon, TabletIcon, TagIcon, TargetIcon, TerminalIcon, ThermometerIcon, ThumbsDownIcon, ThumbsUpIcon, ToggleLeftIcon, ToggleRightIcon, ToolIcon, Trash2Icon, TrashIcon, TrelloIcon, TrendingDownIcon, TrendingUpIcon, TriangleIcon, TruckIcon, TvIcon, TwitchIcon, TwitterIcon, TypeIcon, UmbrellaIcon, UnderlineIcon, UnlockIcon, UploadCloudIcon, UploadIcon, UserCheckIcon, UserMinusIcon, UserPlusIcon, UserXIcon, UserIcon, UsersIcon, VideoOffIcon, VideoIcon, VoicemailIcon, Volume1Icon, Volume2Icon, VolumeXIcon, VolumeIcon, WatchIcon, WifiOffIcon, WifiIcon, WindIcon, XCircleIcon, XOctagonIcon, XSquareIcon, XIcon, YoutubeIcon, ZapOffIcon, ZapIcon, ZoomInIcon, ZoomOutIcon } from "svelte-feather-icons";
</script>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Feather" pageTitle="Icons" />
        <Row>
            <div class="col-12">
                <Card>
                    <CardHeader>
                        <h4 class="card-title">Examples</h4>
                        <p class="text-muted mb-0">Use <code>&lt;ActivityIcon /&gt;</code> class.</p>
                    </CardHeader>
                    <CardBody class="pt-0">
                        <Row class="icon-demo-content">
                            <Col xl={3} lg={4} sm={6}>
                                <ActivityIcon />ActivityIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon></AirplayIcon>AirplayIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlertCircleIcon></AlertCircleIcon>AlertCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlertOctagonIcon></AlertOctagonIcon>AlertOctagonIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlertTriangleIcon></AlertTriangleIcon>AlertTriangleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlignCenterIcon></AlignCenterIcon>AlignCenterIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlignJustifyIcon></AlignJustifyIcon>AlignJustifyIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlignLeftIcon></AlignLeftIcon>AlignLeftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlignRightIcon></AlignRightIcon>AlignRightIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AnchorIcon></AnchorIcon>AnchorIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ApertureIcon></ApertureIcon>ApertureIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArchiveIcon></ArchiveIcon>ArchiveIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowDownCircleIcon></ArrowDownCircleIcon>ArrowDownCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowDownLeftIcon></ArrowDownLeftIcon>ArrowDownLeftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowDownRightIcon></ArrowDownRightIcon>ArrowDownRightIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowDownIcon></ArrowDownIcon>ArrowDownIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowLeftCircleIcon></ArrowLeftCircleIcon>ArrowLeftCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowLeftIcon></ArrowLeftIcon>ArrowLeftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowRightCircleIcon></ArrowRightCircleIcon>ArrowRightCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowRightIcon></ArrowRightIcon>ArrowRightIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowUpCircleIcon></ArrowUpCircleIcon>ArrowUpCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowUpLeftIcon></ArrowUpLeftIcon>ArrowUpLeftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowUpRightIcon></ArrowUpRightIcon>ArrowUpRightIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArrowUpIcon></ArrowUpIcon>ArrowUpIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AtSignIcon></AtSignIcon>AtSignIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AwardIcon></AwardIcon>AwardIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BarChart2Icon></BarChart2Icon>BarChart2Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BarChartIcon></BarChartIcon>BarChartIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BatteryChargingIcon></BatteryChargingIcon>BatteryChargingIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BatteryIcon></BatteryIcon>BatteryIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BellOffIcon></BellOffIcon>BellOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BellIcon></BellIcon>BellIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BluetoothIcon></BluetoothIcon>BluetoothIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BoldIcon></BoldIcon>BoldIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BookOpenIcon></BookOpenIcon>BookOpenIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BookIcon></BookIcon>BookIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BookmarkIcon></BookmarkIcon>BookmarkIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BoxIcon></BoxIcon>BoxIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <BriefcaseIcon></BriefcaseIcon>BriefcaseIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CalendarIcon></CalendarIcon>CalendarIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CameraOffIcon></CameraOffIcon>CameraOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CameraIcon></CameraIcon>CameraIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CastIcon></CastIcon>CastIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CheckCircleIcon></CheckCircleIcon>CheckCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CheckSquareIcon></CheckSquareIcon>CheckSquareIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CheckIcon></CheckIcon>CheckIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ChevronDownIcon></ChevronDownIcon>ChevronDownIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ChevronLeftIcon></ChevronLeftIcon>ChevronLeftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ChevronRightIcon></ChevronRightIcon>ChevronRightIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ChevronUpIcon></ChevronUpIcon>ChevronUpIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ChevronsDownIcon></ChevronsDownIcon>ChevronsDownIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ChevronsLeftIcon></ChevronsLeftIcon>ChevronsLeftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ChevronsRightIcon></ChevronsRightIcon>ChevronsRightIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ChevronsUpIcon></ChevronsUpIcon>ChevronsUpIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ChromeIcon></ChromeIcon>ChromeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CircleIcon></CircleIcon>CircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ClipboardIcon></ClipboardIcon>ClipboardIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ClockIcon></ClockIcon>ClockIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CloudDrizzleIcon></CloudDrizzleIcon>CloudDrizzleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CloudLightningIcon></CloudLightningIcon>CloudLightningIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CloudOffIcon></CloudOffIcon>CloudOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CloudRainIcon></CloudRainIcon>CloudRainIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CloudSnowIcon></CloudSnowIcon>CloudSnowIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CloudIcon></CloudIcon>CloudIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CodeIcon></CodeIcon>CodeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CodepenIcon></CodepenIcon>CodepenIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CodesandboxIcon></CodesandboxIcon>CodesandboxIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CoffeeIcon></CoffeeIcon>CoffeeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ColumnsIcon></ColumnsIcon>ColumnsIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CommandIcon></CommandIcon>CommandIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CompassIcon></CompassIcon>CompassIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CopyIcon></CopyIcon>CopyIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CornerDownLeftIcon></CornerDownLeftIcon>CornerDownLeftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CornerDownRightIcon></CornerDownRightIcon>CornerDownRightIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CornerLeftDownIcon></CornerLeftDownIcon>CornerLeftDownIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CornerLeftUpIcon></CornerLeftUpIcon>CornerLeftUpIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CornerRightDownIcon></CornerRightDownIcon>CornerRightDownIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CornerRightUpIcon></CornerRightUpIcon>CornerRightUpIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CornerUpLeftIcon></CornerUpLeftIcon>CornerUpLeftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CornerUpRightIcon></CornerUpRightIcon>CornerUpRightIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CpuIcon></CpuIcon>CpuIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CreditCardIcon></CreditCardIcon>CreditCardIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CropIcon></CropIcon>CropIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <CrosshairIcon></CrosshairIcon>CrosshairIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DatabaseIcon></DatabaseIcon>DatabaseIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DeleteIcon></DeleteIcon>DeleteIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DiscIcon></DiscIcon>DiscIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DivideCircleIcon></DivideCircleIcon>DivideCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DivideSquareIcon></DivideSquareIcon>DivideSquareIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DivideIcon></DivideIcon>DivideIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DollarSignIcon></DollarSignIcon>DollarSignIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DownloadCloudIcon></DownloadCloudIcon>DownloadCloudIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DownloadIcon></DownloadIcon>DownloadIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DribbbleIcon></DribbbleIcon>DribbbleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <DropletIcon></DropletIcon>DropletIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Edit2Icon></Edit2Icon>Edit2Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Edit3Icon></Edit3Icon>Edit3Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <EditIcon></EditIcon>EditIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ExternalLinkIcon></ExternalLinkIcon>ExternalLinkIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <EyeOffIcon></EyeOffIcon>EyeOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <EyeIcon></EyeIcon>EyeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FacebookIcon></FacebookIcon>FacebookIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FastForwardIcon></FastForwardIcon>FastForwardIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FeatherIcon></FeatherIcon>FeatherIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FigmaIcon></FigmaIcon>FigmaIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FileMinusIcon></FileMinusIcon>FileMinusIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FilePlusIcon></FilePlusIcon>FilePlusIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FileTextIcon></FileTextIcon>FileTextIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FileIcon></FileIcon>FileIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FilmIcon></FilmIcon>FilmIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FilterIcon></FilterIcon>FilterIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FlagIcon></FlagIcon>FlagIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FolderMinusIcon></FolderMinusIcon>FolderMinusIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FolderPlusIcon></FolderPlusIcon>FolderPlusIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FolderIcon></FolderIcon>FolderIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FramerIcon></FramerIcon>FramerIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <FrownIcon></FrownIcon>FrownIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <GiftIcon></GiftIcon>GiftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <GitBranchIcon></GitBranchIcon>GitBranchIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <GitCommitIcon></GitCommitIcon>GitCommitIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <GitMergeIcon></GitMergeIcon>GitMergeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <GitPullRequestIcon></GitPullRequestIcon>GitPullRequestIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <GithubIcon></GithubIcon>GithubIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <GitlabIcon></GitlabIcon>GitlabIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <GlobeIcon></GlobeIcon>GlobeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <GridIcon></GridIcon>GridIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <HardDriveIcon></HardDriveIcon>HardDriveIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <HashIcon></HashIcon>HashIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <HeadphonesIcon></HeadphonesIcon>HeadphonesIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <HeartIcon></HeartIcon>HeartIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <HelpCircleIcon></HelpCircleIcon>HelpCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <HexagonIcon></HexagonIcon>HexagonIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <HomeIcon></HomeIcon>HomeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ImageIcon></ImageIcon>ImageIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <InboxIcon></InboxIcon>InboxIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <InfoIcon></InfoIcon>InfoIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <InstagramIcon></InstagramIcon>InstagramIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ItalicIcon></ItalicIcon>ItalicIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <KeyIcon></KeyIcon>KeyIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <LayersIcon></LayersIcon>LayersIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <LayoutIcon></LayoutIcon>LayoutIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <LifeBuoyIcon></LifeBuoyIcon>LifeBuoyIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Link2Icon></Link2Icon>Link2Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <LinkIcon></LinkIcon>LinkIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <LinkedinIcon></LinkedinIcon>LinkedinIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ListIcon></ListIcon>ListIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <LoaderIcon></LoaderIcon>LoaderIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <LockIcon></LockIcon>LockIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <LogInIcon></LogInIcon>LogInIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <LogOutIcon></LogOutIcon>LogOutIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MailIcon></MailIcon>MailIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MapPinIcon></MapPinIcon>MapPinIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MapIcon></MapIcon>MapIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Maximize2Icon></Maximize2Icon>Maximize2Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MaximizeIcon></MaximizeIcon>MaximizeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MehIcon></MehIcon>MehIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MenuIcon></MenuIcon>MenuIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MessageCircleIcon></MessageCircleIcon>MessageCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MessageSquareIcon></MessageSquareIcon>MessageSquareIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MicOffIcon></MicOffIcon>MicOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MicIcon></MicIcon>MicIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Minimize2Icon></Minimize2Icon>Minimize2Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MinimizeIcon></MinimizeIcon>MinimizeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MinusCircleIcon></MinusCircleIcon>MinusCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MinusSquareIcon></MinusSquareIcon>MinusSquareIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MinusIcon></MinusIcon>MinusIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MonitorIcon></MonitorIcon>MonitorIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MoonIcon></MoonIcon>MoonIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MoreHorizontalIcon></MoreHorizontalIcon>MoreHorizontalIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MoreVerticalIcon></MoreVerticalIcon>MoreVerticalIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MousePointerIcon></MousePointerIcon>MousePointerIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MoveIcon></MoveIcon>MoveIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <MusicIcon></MusicIcon>MusicIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Navigation2Icon></Navigation2Icon>Navigation2Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <NavigationIcon></NavigationIcon>NavigationIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <OctagonIcon></OctagonIcon>OctagonIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PackageIcon></PackageIcon>PackageIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PaperclipIcon></PaperclipIcon>PaperclipIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PauseCircleIcon></PauseCircleIcon>PauseCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PauseIcon></PauseIcon>PauseIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PenToolIcon></PenToolIcon>PenToolIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PercentIcon></PercentIcon>PercentIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PhoneCallIcon></PhoneCallIcon>PhoneCallIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PhoneForwardedIcon></PhoneForwardedIcon>PhoneForwardedIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PhoneIncomingIcon></PhoneIncomingIcon>PhoneIncomingIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PhoneMissedIcon></PhoneMissedIcon>PhoneMissedIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PhoneOffIcon></PhoneOffIcon>PhoneOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PhoneOutgoingIcon></PhoneOutgoingIcon>PhoneOutgoingIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PhoneIcon></PhoneIcon>PhoneIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PieChartIcon></PieChartIcon>PieChartIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PlayCircleIcon></PlayCircleIcon>PlayCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PlayIcon></PlayIcon>PlayIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PlusCircleIcon></PlusCircleIcon>PlusCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PlusSquareIcon></PlusSquareIcon>PlusSquareIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PlusIcon></PlusIcon>PlusIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PocketIcon></PocketIcon>PocketIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PowerIcon></PowerIcon>PowerIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <PrinterIcon></PrinterIcon>PrinterIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <RadioIcon></RadioIcon>RadioIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <RefreshCcwIcon></RefreshCcwIcon>RefreshCcwIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <RefreshCwIcon></RefreshCwIcon>RefreshCwIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <RepeatIcon></RepeatIcon>RepeatIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <RewindIcon></RewindIcon>RewindIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <RotateCcwIcon></RotateCcwIcon>RotateCcwIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <RotateCwIcon></RotateCwIcon>RotateCwIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <RssIcon></RssIcon>RssIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SaveIcon></SaveIcon>SaveIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ScissorsIcon></ScissorsIcon>ScissorsIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SearchIcon></SearchIcon>SearchIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SendIcon></SendIcon>SendIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ServerIcon></ServerIcon>ServerIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SettingsIcon></SettingsIcon>SettingsIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Share2Icon></Share2Icon>Share2Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ShareIcon></ShareIcon>ShareIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ShieldOffIcon></ShieldOffIcon>ShieldOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ShieldIcon></ShieldIcon>ShieldIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ShoppingBagIcon></ShoppingBagIcon>ShoppingBagIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ShoppingCartIcon></ShoppingCartIcon>ShoppingCartIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ShuffleIcon></ShuffleIcon>ShuffleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SidebarIcon></SidebarIcon>SidebarIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SkipBackIcon></SkipBackIcon>SkipBackIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SkipForwardIcon></SkipForwardIcon>SkipForwardIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SlackIcon></SlackIcon>SlackIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SlashIcon></SlashIcon>SlashIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SlidersIcon></SlidersIcon>SlidersIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SmartphoneIcon></SmartphoneIcon>SmartphoneIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SmileIcon></SmileIcon>SmileIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SpeakerIcon></SpeakerIcon>SpeakerIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SquareIcon></SquareIcon>SquareIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <StarIcon></StarIcon>StarIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <StopCircleIcon></StopCircleIcon>StopCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SunIcon></SunIcon>SunIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SunriseIcon></SunriseIcon>SunriseIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <SunsetIcon></SunsetIcon>SunsetIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TabletIcon></TabletIcon>TabletIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TagIcon></TagIcon>TagIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TargetIcon></TargetIcon>TargetIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TerminalIcon></TerminalIcon>TerminalIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ThermometerIcon></ThermometerIcon>ThermometerIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ThumbsDownIcon></ThumbsDownIcon>ThumbsDownIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ThumbsUpIcon></ThumbsUpIcon>ThumbsUpIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ToggleLeftIcon></ToggleLeftIcon>ToggleLeftIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ToggleRightIcon></ToggleRightIcon>ToggleRightIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ToolIcon></ToolIcon>ToolIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Trash2Icon></Trash2Icon>Trash2Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TrashIcon></TrashIcon>TrashIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TrelloIcon></TrelloIcon>TrelloIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TrendingDownIcon></TrendingDownIcon>TrendingDownIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TrendingUpIcon></TrendingUpIcon>TrendingUpIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TriangleIcon></TriangleIcon>TriangleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TruckIcon></TruckIcon>TruckIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TvIcon></TvIcon>TvIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TwitchIcon></TwitchIcon>TwitchIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TwitterIcon></TwitterIcon>TwitterIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <TypeIcon></TypeIcon>TypeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UmbrellaIcon></UmbrellaIcon>UmbrellaIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UnderlineIcon></UnderlineIcon>UnderlineIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UnlockIcon></UnlockIcon>UnlockIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UploadCloudIcon></UploadCloudIcon>UploadCloudIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UploadIcon></UploadIcon>UploadIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UserCheckIcon></UserCheckIcon>UserCheckIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UserMinusIcon></UserMinusIcon>UserMinusIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UserPlusIcon></UserPlusIcon>UserPlusIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UserXIcon></UserXIcon>UserXIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UserIcon></UserIcon>UserIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <UsersIcon></UsersIcon>UsersIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <VideoOffIcon></VideoOffIcon>VideoOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <VideoIcon></VideoIcon>VideoIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <VoicemailIcon></VoicemailIcon>VoicemailIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Volume1Icon></Volume1Icon>Volume1Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <Volume2Icon></Volume2Icon>Volume2Icon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <VolumeXIcon></VolumeXIcon>VolumeXIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <VolumeIcon></VolumeIcon>VolumeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <WatchIcon></WatchIcon>WatchIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <WifiOffIcon></WifiOffIcon>WifiOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <WifiIcon></WifiIcon>WifiIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <WindIcon></WindIcon>WindIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <XCircleIcon></XCircleIcon>XCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <XOctagonIcon></XOctagonIcon>XOctagonIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <XSquareIcon></XSquareIcon>XSquareIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <XIcon></XIcon>XIcon,
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <YoutubeIcon></YoutubeIcon>YoutubeIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ZapOffIcon></ZapOffIcon>ZapOffIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ZapIcon></ZapIcon>ZapIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ZoomInIcon></ZoomInIcon>ZoomInIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ZoomOutIcon></ZoomOutIcon>ZoomOutIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon></AirplayIcon>AirplayIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon></AirplayIcon>AirplayIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon></AirplayIcon>AirplayIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon></AirplayIcon>AirplayIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon></AirplayIcon>AirplayIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon></AirplayIcon>AirplayIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon></AirplayIcon>AirplayIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlertCircleIcon></AlertCircleIcon>AlertCircleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlertOctagonIcon></AlertOctagonIcon>AlertOctagonIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AlertTriangleIcon></AlertTriangleIcon>AlertTriangleIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <AnchorIcon></AnchorIcon>AnchorIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ApertureIcon></ApertureIcon>ApertureIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ArchiveIcon></ArchiveIcon>ArchiveIcon
                            </Col>
                            <Col xl={3} lg={4} sm={6}>
                                <ClockIcon></ClockIcon>ClockIcon
                            </Col>
                        </Row>
                        <!-- end row -->
                    </CardBody>
                    <!-- end card-body -->
                </Card>
                <!-- end card -->
            </div>
            <!-- end col -->
        </Row>
        <!-- end row -->

        <Row>
            <div class="col-12">
                <Card>
                    <CardHeader>
                        <h4 class="card-title">Sizes</h4>
                        <p class="text-muted mb-0">
                            Use
                            <code>&lt;AirplayIcon class="icon-**"&gt;</code>. Available sizes
                            <code>xs, sm,md,lg,xl,xxl</code>
                        </p>
                    </CardHeader>
                    <CardBody class="pt-0">
                        <Row class="icon-demo-content">
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon size="24"></AirplayIcon>AirplayIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon size="1x"></AirplayIcon>AirplayIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon size="1.5x"></AirplayIcon>AirplayIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon size="2x"></AirplayIcon>AirplayIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon size="3x"></AirplayIcon>AirplayIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon size="4x"></AirplayIcon>AirplayIcon
                            </Col>
                        </Row>
                        <!-- emd row -->
                    </CardBody>
                    <!-- end card-body -->
                </Card>
                <!-- end card -->
            </div>
            <!-- end col -->
        </Row>
        <!-- end row -->

        <Row>
            <div class="col-12">
                <Card>
                    <CardHeader>
                        <h4 class="card-title">Two Tones Color Icons</h4>
                        <p class="text-muted mb-0">
                            Use
                            <code>&lt;AirplayIcon class="icon-dual-**"&gt;</code>.
                        </p>
                    </CardHeader>
                    <CardBody class="pt-0">
                        <Row class="icon-demo-content">
                            <Col xl={3} lg={4} sm={6}>
                                <AirplayIcon class="icon-dual"></AirplayIcon>AirplayIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <AlertCircleIcon class="icon-dual-primary"></AlertCircleIcon>AlertCircleIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <AlertOctagonIcon class="icon-dual-success"></AlertOctagonIcon>AlertOctagonIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <AlertTriangleIcon class="icon-dual-info"></AlertTriangleIcon>AlertTriangleIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <AnchorIcon class="icon-dual-warning"></AnchorIcon>AnchorIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <ApertureIcon class="icon-dual-danger"></ApertureIcon>ApertureIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <ArchiveIcon class="icon-dual-dark"></ArchiveIcon>ArchiveIcon
                            </Col>

                            <Col xl={3} lg={4} sm={6}>
                                <ClockIcon class="icon-dual-secondary"></ClockIcon>ClockIcon
                            </Col>
                        </Row>
                        <!-- emd row -->
                    </CardBody>
                    <!-- end card-body -->
                </Card>
                <!-- end card -->
            </div>
            <!-- end col -->
        </Row>
    </Container>
</div>