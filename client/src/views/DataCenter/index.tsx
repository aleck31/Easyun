import React from 'react';
import {CHeader} from '@/components/Logic/CHeader';
import {CFooter} from '@/components/Logic/CFooter';
import {CSubnet} from '@/components/Logic/CSubnet';
import {classnames} from '@@/tailwindcss-classnames';
import CSecurityGroup from '@/components/Logic/CSecurityGrop';
import {CButton} from '@/components/Common/CButton';
import {Icon} from '@iconify/react';
import { useNavigate } from 'react-router-dom';

const DataCenter = (): JSX.Element => {
	const navigate = useNavigate();
	return (
		<div>
			<CHeader/>
			<div className={classnames('ml-5', 'mt-2')}>Easy DataCenter Networking</div>
			<div className={classnames('ml-24')}>Region:
				<Icon className={classnames('inline-block','mx-1')} icon="emojione-v1:flag-for-japan" color="gray" width="25" height="25" fr={undefined} />
                japan(ap-northeast-1)</div>
			<div className={classnames('ml-5')}>
				<span className={classnames('mr-2')}>IPv4 CIDR block:</span>
				<input className={classnames('border')} type="text"/>
			</div>
			<CSubnet index={1} isPublic={true} classes={classnames('w-96', 'inline-block')}/>
			<CSubnet index={2} isPublic={true} classes={classnames('w-96', 'inline-block')}/>
			<CSubnet index={1} isPublic={false} classes={classnames('w-96', 'inline-block')}/>
			<CSubnet index={2} isPublic={false} classes={classnames('w-96', 'inline-block')}/>


			<div className={classnames('ml-5', 'mt-10')}>Easyun DataCenter Security Group</div>
			<CSecurityGroup classes={classnames('mx-5', 'w-64', 'inline-block')}/>
			<CSecurityGroup classes={classnames('mx-5', 'w-64', 'inline-block')}/>
			<CSecurityGroup classes={classnames('mx-5', 'w-64', 'inline-block')}/>

			<div className={classnames('flex', 'justify-center', 'm-16')}>
				<CButton click={() => {
					navigate('/home');
				}} classes={classnames('bg-gray-400', 'text-white', 'rounded-2xl', 'w-32', 'h-9', 'mx-5')}>
					<Icon className={classnames('inline-block', 'mr-2')} icon="akar-icons:arrow-left" color="white"
						width="20" height="20" fr={undefined}/>
                    Back</CButton>
				<CButton click={() => {
					navigate('/resource');
				}} classes={classnames('bg-yellow-550', 'text-white', 'rounded-2xl', 'w-32', 'px-5')}>Create</CButton>
			</div>

			<CFooter/>
		</div>
	);
};


export default DataCenter;
