import * as React from 'react';
import { CHeader } from '@/components/Logic/CHeader';
import { CFooter } from '@/components/Logic/CFooter';
import { CButton } from '@/components/Common/CButton';
import { classnames } from '@@/tailwindcss-classnames';
import { Icon } from '@iconify/react';
import { useNavigate } from 'react-router-dom';

const StoragePage = (): JSX.Element => {
	const navigate = useNavigate();
	return (
		<div className={classnames('flex', 'flex-col', 'justify-center', 'items-center', 'm-10')}>
			<div className={classnames('text-3xl')}> Store your data on Cloud.</div>
			<div className={classnames('text-gray-700', 'my-2')}>
				{' '}
        Storage resource allow you to increase the amount of data storage availiable to your AWS
        Cloud resources.
			</div>
			<CButton
				click={() => {
					navigate('/resource/AddBucket');
				}}
				classes={classnames(
					'bg-yellow-550',
					'text-white',
					'rounded-3xl',
					'h-10',
					'w-32',
					'px-5',
					'my-5'
				)}
			>
        Add Bucket
			</CButton>
			<div className={classnames('text-blue-500')}>
				<a href="https://aws.amazon.com/cn/ec2" target="_blank" rel="noreferrer">
          Learn more about buckets
					<Icon
						className={classnames('inline-block', 'mx-1', 'text-blue-500')}
						icon="akar-icons:link-out"
						width="20"
						height="20"
						fr={undefined}
					/>
				</a>
			</div>
			<CButton
				click={() => {
					navigate('/resource/AddDisk');
				}}
				classes={classnames(
					'bg-yellow-550',
					'text-white',
					'rounded-3xl',
					'h-10',
					'w-32',
					'px-5',
					'my-5'
				)}
			>
        Add Disk
			</CButton>
			<div className={classnames('text-blue-500')}>
				<a href="https://aws.amazon.com/cn/ec2" target="_blank" rel="noreferrer">
          Learn more about Disk
					<Icon
						className={classnames('inline-block', 'mx-1', 'text-blue-500')}
						icon="akar-icons:link-out"
						width="20"
						height="20"
						fr={undefined}
					/>
				</a>
			</div>
		</div>
	);
};

export default StoragePage;
