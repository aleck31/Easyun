import * as React from 'react';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { CHeader } from '@/components/Logic/CHeader';
import { CFooter } from '@/components/Logic/CFooter';
import { CButton } from '@/components/Common/CButton';
import { classnames } from '@@/tailwindcss-classnames';
import { Icon } from '@iconify/react';
import { useNavigate } from 'react-router-dom';
import StoragePage from '@/views/Resource/Storage';

interface TabPanelProps {
	children?: React.ReactNode;
	index: number;
	value: number;
}

function TabPanel(props: TabPanelProps) {
	const {children, value, index, ...other} = props;

	return (
		<div
			role="tabpanel"
			hidden={value !== index}
			id={`simple-tabpanel-${index}`}
			aria-labelledby={`simple-tab-${index}`}
			{...other}
		>
			{value === index && (
				<Box sx={{p: 3}}>
					<Typography component={'span'}>{children}</Typography>
				</Box>
			)}
		</div>
	);
}

function a11yProps(index: number) {
	return {
		id: `simple-tab-${index}`,
		'aria-controls': `simple-tabpanel-${index}`,
	};
}

export const Resource = (): JSX.Element => {
	const [value, setValue] = React.useState(0);

	const navigate = useNavigate();

	const handleChange = (event: React.SyntheticEvent, newValue: number) => {
		setValue(newValue);
	};

	return (
		<div>
			<CHeader/>
			<Box sx={{width: '100%'}}>
				<Box sx={{borderBottom: 1, borderColor: 'divider'}}>
					<Tabs value={value} onChange={handleChange} aria-label="resource tab">
						<Tab label="Server" {...a11yProps(0)} />
						<Tab label="Storage" {...a11yProps(1)} />
						<Tab label="Database" {...a11yProps(2)} />
						<Tab label="Networking" {...a11yProps(3)} />
						<Tab label="Containers" {...a11yProps(4)} />
						<Tab label="Backups" {...a11yProps(5)} />
					</Tabs>
				</Box>
				<TabPanel value={value} index={0}>
					<div className={classnames('flex', 'flex-col', 'justify-center', 'items-center', 'm-10')}>
						<div className={classnames('text-3xl')}> You have no servers right now.</div>
						<div className={classnames('text-gray-700', 'my-2')}> Add a cloud server and get start with
							Easyun!
						</div>
						<CButton click={() => {
							navigate('/resource/addServer');
						}}
								 classes={classnames('bg-yellow-550', 'text-white', 'rounded-3xl', 'h-10', 'w-32', 'px-5', 'my-5')}>Add
							Server</CButton>
						<div className={classnames('text-blue-500')}>
							<a href="https://aws.amazon.com/cn/ec2" target="_blank" rel="noreferrer"> 
								Learn more about instance
								<Icon className={classnames('inline-block', 'mx-1', 'text-blue-500')}
									  icon="akar-icons:link-out" width="20" height="20" fr={undefined}/>
							</a>
						</div>
					</div>
				</TabPanel>
				<TabPanel value={value} index={1}>
					<StoragePage />
				</TabPanel>
				<TabPanel value={value} index={2}>
					Databases
				</TabPanel>
				<TabPanel value={value} index={3}>
					Networking
				</TabPanel>
				<TabPanel value={value} index={4}>
					Containers
				</TabPanel>
				<TabPanel value={value} index={5}>
					Backups
				</TabPanel>
			</Box>
			<CFooter/>
		</div>
	);
};


export default Resource;