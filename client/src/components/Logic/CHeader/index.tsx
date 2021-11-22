import React from 'react';
import { classnames } from '@@/tailwindcss-classnames';
import { Icon } from '@iconify/react';
import { Button, Menu, MenuItem } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const options = [
	'Home',
	'Dashboard',
	'Event',
	'Account',
];

export const CHeader = (): JSX.Element => {
	const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
	const [selectedIndex, setSelectedIndex] = React.useState(1);
	const open = Boolean(anchorEl);
	const handleClick = (event: React.MouseEvent<HTMLElement>) => {
		setAnchorEl(event.currentTarget);
	};

	const navigate = useNavigate();

	const handleMenuItemClick = (
		event: React.MouseEvent<HTMLElement>,
		index: number,
	) => {
		setSelectedIndex(index);
		setAnchorEl(null);
	};

	const handleClose = () => {
		setAnchorEl(null);
	};
	const container = classnames('bg-gray-600', 'text-white', 'text-3xl', 'h-16', 'flex', 'items-center');
	const content = classnames('ml-6', 'flex-none', 'cursor-pointer');
	return (
		<div className={container}>
			<span className={content} onClick={() => navigate('/home')}>Easyun</span>
			<div className={classnames('ml-40', 'flex-grow')}>
				<div>
					<Button
						id="basic-button"
						aria-controls="basic-menu"
						aria-haspopup="true"
						aria-expanded={open ? 'true' : undefined}
						onClick={handleClick}
					>
						<span className={classnames('text-white')}>{options[selectedIndex]}</span>
						<Icon className={'ml-5'} icon="iconoir:nav-arrow-down" color="#5c6f9a" width="25" height="25"
							  hFlip={true} fr={undefined}/>
					</Button>
					<Menu
						id="lock-menu"
						anchorEl={anchorEl}
						open={open}
						onClose={handleClose}
						MenuListProps={{
							'aria-labelledby': 'lock-button',
							role: 'listbox',
						}}
					>
						{options.map((option, index) => (
							<MenuItem
								key={option}
								selected={index === selectedIndex}
								onClick={(event) => handleMenuItemClick(event, index)}
							>
								{option}
							</MenuItem>
						))}
					</Menu>
				</div>
			</div>
			<div className={classnames('float-right', 'flex-none', 'inline-flex', 'items-center')}>
				<Icon id="free-trial"
					  className={classnames('cursor-pointer')} icon="fa:heartbeat" color="#9fbe8a" width="40"
					  height="40" fr={undefined}/>
				<Icon className={'mx-3'} icon="radix-icons:divider-vertical" color="#5c6f9a" width="30" height="30"
					  hFlip={true} fr={undefined}/>

				<span id="setting" className={classnames('cursor-pointer', 'inline-flex')}>
					<Icon className={classnames('ml-2', 'inline-block')} icon="ant-design:setting-filled"
						  color="#5c6f9a" width="30" height="30"
						  fr={undefined}/>
					<Icon className={'mr-2'} icon="iconoir:nav-arrow-down" color="#5c6f9a" width="25" height="25"
						  hFlip={true} fr={undefined}/>
				</span>

				<span id="username" className={'mx-5'} style={{color: '#5c6f9a'}}>admin</span>
				<span id="user" className={classnames('cursor-pointer', 'inline-flex')}>
					<Icon className={classnames('ml-2', 'inline-block')} icon="bi:person-fill" color="#5c6f9a"
						  width="30" height="30"
						  fr={undefined}/>
					<Icon className={classnames('mr-2')} icon="iconoir:nav-arrow-down" color="#5c6f9a" width="25"
						  height="25"
						  hFlip={true} fr={undefined}/>
				</span>

			</div>
		</div>
	);
};
