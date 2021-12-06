// eslint-disable-next-line @typescript-eslint/no-var-requires
const Koa = require('koa');
// eslint-disable-next-line @typescript-eslint/no-var-requires
const bodyParser = require('koa-bodyparser');
// eslint-disable-next-line @typescript-eslint/no-var-requires
const Router = require('@koa/router');
// eslint-disable-next-line @typescript-eslint/no-var-requires
const fs = require('fs');

const app = new Koa();
const router = new Router();
app.use(bodyParser());

const JsonFilepath = './api.json';
router.post('/config', ctx => {
	const body = ctx.request.body;
	const data = JSON.stringify(body);
	fs.writeFileSync(JsonFilepath, data);
	ctx.status = 200;
	ctx.body = ctx.request.body;

});

router.get('/config', ctx => {
	const data = fs.readFileSync(JsonFilepath, 'utf8');
	const config = JSON.parse(data);
	console.log('host', config.host);
	ctx.status = 200;
	ctx.body = config;
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(8088);
console.log('server now on:', 8888);