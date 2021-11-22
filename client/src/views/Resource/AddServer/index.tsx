import React from 'react';
import { CHeader } from '@/components/Logic/CHeader';
import { CFooter } from '@/components/Logic/CFooter';
import { Icon } from '@iconify/react';
import { classnames } from '@@/tailwindcss-classnames';
import CPlatform from '@/components/Logic/CPlatform';

const AddServer = (): JSX.Element => {
	return (
		<div>
			<CHeader/>
			<div id="add-cloud-server-title" className={classnames('m-5')}>
				<Icon className={classnames('inline-block')} icon="fluent:add-circle-20-regular" width="30"
					  height="30" fr={undefined}/>
				<span>Add Cloud Server(EC2 Instance)</span>
			</div>

			<div id="identify-your-server-form">
				<div className={classnames('mx-5')}>Identify your server</div>
				<div className={classnames('mb-5', 'mt-2', 'mx-2')}>
					<input className={classnames('border', 'w-72', 'h-10', 'px-1', 'py-3', 'mx-3')} type="text"/>
					<span className={classnames('text-gray-500')}>x</span>
					<input min={1} max={99} defaultValue={'1'} maxLength={2}
						   className={classnames('border', 'w-14', 'py-1', 'px-2', 'h-10', 'mx-3')}
						   type="number"/>
				</div>
			</div>

			<div id="select-your-platform">
				<CPlatform/>
			</div>

			<div id="select-your-ami">

			</div>

			<CFooter/>
		</div>
	);
};


export default AddServer;