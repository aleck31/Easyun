import React from 'react';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import { classnames, TTailwindString } from '@@/tailwindcss-classnames';

const CUserCenter = (): JSX.Element => {
	return (
		<div>
			<br />
			<Box sx={{ width: '80%', bgcolor: 'background.paper', border: 1,borderColor:'grey.500',borderRadius:5, left: '100px'}}>
				<Box sx={{ my: 3, mx: 2 }}>profiles&contacts</Box>
				<Divider />
				<Box sx={{ m: 2 }}>
					<a href="http://www.baidu.com">my profile on aws</a>
				</Box>
			</Box>
			<br />
			<Box sx={{ width: '80%', bgcolor: 'background.paper', border: 1, borderColor:'grey.500',borderRadius:5, left: '100px'}}>
				<Box sx={{ my: 3, mx: 2 }}>SSH keys</Box>
				<Divider />
				<Box sx={{ m: 2 }}>
					<span>create new</span>
				</Box>
			</Box>
			<br />
			<Box sx={{ width: '80%', bgcolor: 'background.paper', border: 1, borderColor:'grey.500',borderRadius:5, left: '100px'}}> 
				<Box sx={{ my: 3, mx: 2 }}>API access keys</Box>
				<Divider />
				<Box sx={{ m: 2 }}>
					<a href="http://www.baidu.com">go to the IAM console</a>
				</Box>
			</Box>
			<br />
		</div>
	);
};

export default CUserCenter;
