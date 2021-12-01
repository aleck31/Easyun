import api from '@/utils/api';
import {UserLogin} from '@/constant/apiConst';
import {Result} from '@/constant/result';

export default class userService {
	// xiaomo/xiaomo2019
	static async login<T>(username: string, password: string): Promise<Result<T>> {
		const result = await api.post(UserLogin, {
			username, password
		});
		return result.data as Result<T>;
	}
}
