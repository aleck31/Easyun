import React from 'react';
import {classnames, TTailwindString} from '@@/tailwindcss-classnames';
import {Icon} from '@iconify/react';

interface Props {
    index: number;
    isPublic: boolean;
    classes?: TTailwindString;
}

export const CSubnet = (props: Props): JSX.Element => {
	const title = props.isPublic ? 'Public subnet ' + props.index : 'Private subnet ' + props.index;
	let classes = props.classes;
	if (props.isPublic) {
		classes = classnames(classes, 'bg-green-50');
	} else {
		classes = classnames(classes, 'bg-yellow-50');
	}
	return (
		<div className={classnames(classes, 'mx-3', 'my-2')}>
			{
				props.isPublic ? <Icon className={classnames('relative', 'float-right', 'text-transparent')}
					width="25" height="25"
					icon="ant-design:lock-outlined" fr={undefined}/> :
					<Icon className={classnames('relative', 'top-0', 'right-0', 'float-right')}
						icon="ant-design:lock-outlined"
						width="25" height="25"
						fr={undefined}/>
			}
			<div>
				<div color="text.secondary">
					{title}
				</div>
				<div className="grid grid-cols-5 gap-4">
					<div className="col-span-2">ipv4 CIDR Block</div>
					<div className="col-span-3">
						<input className={classnames('h-6', 'border', 'w-40')}/>
					</div>
				</div>
				<div className="grid grid-cols-5 gap-4">
					<div className="col-span-2">Availability Zone</div>
					<div className="col-span-3">
						<select className={classnames('h-6')} defaultValue={1}>
							<option value={1}>saba5198fa-rtb</option>
							<option value={2}>saba5198fa-rtb</option>
							<option value={3}>saba5198fa-rtb</option>
						</select>
					</div>
				</div>
				<div className="grid grid-cols-5 gap-4">
					<div className="col-span-2">Gateway</div>
					<div className="col-span-3">
						<select className={'h-6'} defaultValue={1}>
							<option value={1}>saba5198fa-rtb</option>
							<option value={2}>saba5198fa-rtb</option>
							<option value={3}>saba5198fa-rtb</option>
						</select></div>
				</div>
				<div className="grid grid-cols-5 gap-4">
					<div className="col-span-2">Route Table</div>
					<div className="col-span-3">
						<select className={'h-6'} defaultValue={1}>
							<option value={1}>saba5198fa-rtb</option>
							<option value={2}>saba5198fa-rtb</option>
							<option value={3}>saba5198fa-rtb</option>
						</select>
					</div>
				</div>

			</div>
		</div>
	);
};
