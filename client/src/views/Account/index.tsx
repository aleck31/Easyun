import React from 'react';
import CUserCenter from '@/components/Logic/CUserCenter';
// import { useNavigate } from 'react-router-dom';
import {CHeader} from '@/components/Logic/CHeader';
import {CFooter} from '@/components/Logic/CFooter';

const Account = (): JSX.Element => {
	return(
		<div>
			<CHeader/>
			<CUserCenter/>
			<CFooter />
		</div>
	);};

export default Account;
