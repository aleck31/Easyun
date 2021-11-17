import React from 'react';
import {classnames} from '@@/tailwindcss-classnames';
import setting from '@/assets/images/settings.png';
import profile from '@/assets/images/userprofile.png';

export const CHeader = (): JSX.Element => {
	const container = classnames('bg-gray-600', 'text-white', 'text-3xl', 'h-16', 'flex', 'items-center');
	const content = classnames('ml-6','flex-none');
	return (
		<div className={container}>
			<span className={content}>Easyun</span>
			<div className={classnames('ml-40','flex-grow')}>
				<select defaultValue={'Home'} className={classnames('bg-gray-600')}>
					<option>Home</option>
					<option>Dashboard</option>
					<option>Event</option>
					<option>Account</option>
				</select>
			</div>
			<div className={classnames('float-right','flex-none','inline-flex')}>
				<span><img src={profile} alt="" className={classnames('w-12','h-12')}/></span>
				<span><img src={setting} alt="" className={classnames('w-12','h-12')}/></span>
				<span>admin</span>
				<span><img src={profile} alt="" className={classnames('w-12','h-12')}/></span>
			</div>
		</div>
	);
};
