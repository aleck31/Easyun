import React from 'react';
import { CHeader } from '@/components/Logic/CHeader';
import { CFooter } from '@/components/Logic/CFooter';
import { CSubnet } from '@/components/Logic/CSubnet';
import { classnames } from '@@/tailwindcss-classnames';

const DataCenter = (): JSX.Element => (
	<div>
		<CHeader/>
		<div className={classnames('ml-5')}>Easy DataCenter Networking</div>
		<CSubnet index={1} isPublic={true} classes={classnames('w-96', 'inline-block')}/>
		<CSubnet index={2} isPublic={true} classes={classnames('w-96', 'inline-block')}/>
		<CSubnet index={1} isPublic={false} classes={classnames('w-96', 'inline-block')}/>
		<CSubnet index={2} isPublic={false} classes={classnames('w-96', 'inline-block')}/>
		<CFooter/>
	</div>
);


export default DataCenter;
