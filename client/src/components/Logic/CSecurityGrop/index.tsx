import React from 'react';
import {classnames, TTailwindString} from '@@/tailwindcss-classnames';
import {Icon} from '@iconify/react';

interface CSecurityGroupProps {
    classes?: TTailwindString;
}

const CSecurityGroup = (props: CSecurityGroupProps): JSX.Element => {
	return (
		<div className={classnames(props.classes, 'border', 'border-yellow-550', 'rounded', 'p-10', 'pt-5', 'mt-5')}>
			<div className={classnames('pb-10')}>
				<Icon className={classnames('inline-block', 'mr-2')} width="25" height="25" color='black'
					icon="ant-design:lock-outlined" fr={undefined}/>
                easy-sg-manager
			</div>
			<div>Enable Ping <input type='checkbox'/></div>
			<div>Enable SSH<input type='checkbox'/></div>
			<div className={classnames('pb-10')}>Enable RDP<input type='checkbox'/></div>

			<div>In Bound Port:</div>
			<div>TCP 660: 0.0.0.0/0</div>
		</div>
	);
};


export default CSecurityGroup;