import axios, {Response} from 'redaxios';

export default class userService {
	// xiaomo/xiaomo2019
	static async login<T>(username: string, password: string): Promise<Response<T>> {
		return axios.post('api/v1.0/user/token', {
			username, password
		});
	}
}
